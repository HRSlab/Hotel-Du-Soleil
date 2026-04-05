import fs from 'node:fs';
import path from 'node:path';
import { v2 as cloudinary } from 'cloudinary';

const ROOT_DIR = process.cwd();
const ENV_PATH = path.join(ROOT_DIR, '.env');
const STATIC_IMGS_DIR = path.join(ROOT_DIR, 'static', 'imgs');
const OUTPUT_PATH = path.join(ROOT_DIR, 'src', 'lib', 'generated', 'cloudinary-manifest.json');

function loadEnvFile(filePath) {
	if (!fs.existsSync(filePath)) {
		return;
	}

	const raw = fs.readFileSync(filePath, 'utf8');
	for (const line of raw.split(/\r?\n/)) {
		const trimmed = line.trim();

		if (!trimmed || trimmed.startsWith('#')) {
			continue;
		}

		const separatorIndex = trimmed.indexOf('=');
		if (separatorIndex === -1) {
			continue;
		}

		const key = trimmed.slice(0, separatorIndex).trim();
		let value = trimmed.slice(separatorIndex + 1).trim();

		if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
			value = value.slice(1, -1);
		}

		if (!(key in process.env)) {
			process.env[key] = value;
		}
	}
}

function normalizeStem(value) {
	return value
		.toLowerCase()
		.replace(/\.[^.]+$/, '')
		.replace(/_[a-z0-9]{6}$/i, '')
		.replace(/[^a-z0-9]+/g, '-')
		.replace(/^-+|-+$/g, '');
}

function walkFiles(directory, prefix = '') {
	return fs.readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
		if (entry.name.startsWith('.')) {
			return [];
		}

		const nextPrefix = prefix ? `${prefix}/${entry.name}` : entry.name;
		const nextPath = path.join(directory, entry.name);

		return entry.isDirectory() ? walkFiles(nextPath, nextPrefix) : [nextPrefix];
	});
}

async function fetchAllResources(resourceType) {
	const resources = [];
	let nextCursor;

	do {
		const response = await cloudinary.api.resources({
			type: 'upload',
			resource_type: resourceType,
			max_results: 500,
			next_cursor: nextCursor
		});

		resources.push(...response.resources);
		nextCursor = response.next_cursor;
	} while (nextCursor);

	return resources;
}

function chooseBestMatch(localPath, matches) {
	if (matches.length === 1) {
		return matches[0];
	}

	const exactBasename = path.basename(localPath, path.extname(localPath)).toLowerCase();
	const exactMatch = matches.find((candidate) => {
		const candidateStem = candidate.publicId.replace(/_[a-z0-9]{6}$/i, '').toLowerCase();
		return candidateStem === exactBasename;
	});

	return exactMatch ?? matches[0];
}

loadEnvFile(ENV_PATH);

const cloudName = process.env.PUBLIC_CLOUDINARY_CLOUD_NAME;
const apiKey = process.env.PUBLIC_CLOUDINARY_API_KEY;
const apiSecret = process.env.CLOUDINARY_API_SECRET;

if (!cloudName || !apiKey || !apiSecret) {
	throw new Error('Missing Cloudinary credentials in .env.');
}

cloudinary.config({
	cloud_name: cloudName,
	api_key: apiKey,
	api_secret: apiSecret,
	secure: true
});

const [imageResources, videoResources] = await Promise.all([
	fetchAllResources('image'),
	fetchAllResources('video')
]);

const allResources = [...imageResources, ...videoResources].map((resource) => ({
	publicId: resource.public_id,
	resourceType: resource.resource_type,
	format: resource.format,
	version: resource.version,
	secureUrl: resource.secure_url,
	normalizedStem: normalizeStem(resource.public_id)
}));

const resourceBuckets = new Map();
for (const resource of allResources) {
	const bucket = resourceBuckets.get(resource.normalizedStem) ?? [];
	bucket.push(resource);
	resourceBuckets.set(resource.normalizedStem, bucket);
}

const localFiles = walkFiles(STATIC_IMGS_DIR);
const manifest = {};
const misses = [];

for (const localFile of localFiles) {
	const key = normalizeStem(path.basename(localFile));
	const bucket = resourceBuckets.get(key) ?? [];

	if (bucket.length === 0) {
		misses.push(`/imgs/${localFile}`);
		continue;
	}

	const match = chooseBestMatch(localFile, bucket);
	manifest[`/imgs/${localFile}`] = {
		publicId: match.publicId,
		resourceType: match.resourceType,
		version: match.version,
		format: match.format,
		secureUrl: match.secureUrl
	};
	}

fs.mkdirSync(path.dirname(OUTPUT_PATH), { recursive: true });
fs.writeFileSync(OUTPUT_PATH, `${JSON.stringify(manifest, null, 2)}\n`);

const summary = {
	localAssets: localFiles.length,
	cloudinaryAssets: allResources.length,
	mappedAssets: Object.keys(manifest).length,
	missedAssets: misses.length,
	misses: misses.slice(0, 50)
};

console.log(JSON.stringify(summary, null, 2));