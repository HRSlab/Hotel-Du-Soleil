import {
	PUBLIC_CLOUDINARY_API_KEY,
	PUBLIC_CLOUDINARY_CLOUD_NAME,
	PUBLIC_CLOUDINARY_UPLOAD_PRESET
} from '$env/static/public';

export type CloudinaryResourceType = 'image' | 'video' | 'raw';

export type CloudinaryTransformationOptions = {
	width?: number | string;
	height?: number | string;
	crop?: string;
	quality?: number | string;
	format?: string;
	fetchFormat?: string;
	gravity?: string;
	effect?: string;
	dpr?: number | string;
	aspectRatio?: string;
	radius?: number | string;
	startOffset?: number | string;
	endOffset?: number | string;
	background?: string;
	zoom?: number | string;
	custom?: string[];
};

export type CloudinaryDeliverySource = {
	publicId?: string;
	fallbackSrc?: string;
	resourceType?: CloudinaryResourceType;
	type?: string;
	version?: string | number;
};

export const cloudinaryConfig = {
	cloudName: PUBLIC_CLOUDINARY_CLOUD_NAME,
	apiKey: PUBLIC_CLOUDINARY_API_KEY,
	uploadPreset: PUBLIC_CLOUDINARY_UPLOAD_PRESET
} as const;

export const hasCloudinaryDelivery = Boolean(cloudinaryConfig.cloudName);

export const hasCloudinaryUnsignedUpload = Boolean(
	cloudinaryConfig.cloudName && cloudinaryConfig.apiKey && cloudinaryConfig.uploadPreset
);

function buildTransformationSegment(options: CloudinaryTransformationOptions = {}): string {
	const segments = [
		options.width ? `w_${options.width}` : undefined,
		options.height ? `h_${options.height}` : undefined,
		options.crop ? `c_${options.crop}` : undefined,
		options.quality ? `q_${options.quality}` : undefined,
		options.format ? `f_${options.format}` : undefined,
		options.fetchFormat ? `fl_${options.fetchFormat}` : undefined,
		options.gravity ? `g_${options.gravity}` : undefined,
		options.effect ? `e_${options.effect}` : undefined,
		options.dpr ? `dpr_${options.dpr}` : undefined,
		options.aspectRatio ? `ar_${options.aspectRatio}` : undefined,
		options.radius ? `r_${options.radius}` : undefined,
		options.startOffset ? `so_${options.startOffset}` : undefined,
		options.endOffset ? `eo_${options.endOffset}` : undefined,
		options.background ? `b_${options.background}` : undefined,
		options.zoom ? `z_${options.zoom}` : undefined,
		...(options.custom ?? [])
	].filter(Boolean);

	return segments.join(',');
}

function encodePublicId(publicId: string): string {
	return publicId
		.split('/')
		.filter(Boolean)
		.map((segment) => encodeURIComponent(segment))
		.join('/');
}

export function getCloudinaryDeliveryUrl(
	publicId: string,
	resourceType: CloudinaryResourceType = 'image',
	options: CloudinaryTransformationOptions = {},
	config: Pick<CloudinaryDeliverySource, 'type' | 'version'> = {}
): string {
	if (!cloudinaryConfig.cloudName) {
		throw new Error('Cloudinary delivery is not configured. Set PUBLIC_CLOUDINARY_CLOUD_NAME.');
	}

	const assetType = config.type ?? 'upload';
	const transformationSegment = buildTransformationSegment(options);
	const versionSegment = config.version ? `v${config.version}/` : '';
	const path = encodePublicId(publicId);

	return [
		'https://res.cloudinary.com',
		cloudinaryConfig.cloudName,
		resourceType,
		assetType,
		transformationSegment ? `${transformationSegment}/` : '',
		`${versionSegment}${path}`
	].join('/');
}

export function resolveCloudinaryUrl(
	source: string | CloudinaryDeliverySource,
	options: CloudinaryTransformationOptions = {}
): string {
	if (typeof source === 'string') {
		if (/^https?:\/\//.test(source) || source.startsWith('/')) {
			return source;
		}

		if (!hasCloudinaryDelivery) {
			return source;
		}

		return getCloudinaryDeliveryUrl(source, 'image', options);
	}

	if (source.publicId && hasCloudinaryDelivery) {
		return getCloudinaryDeliveryUrl(source.publicId, source.resourceType ?? 'image', options, {
			type: source.type,
			version: source.version
		});
	}

	if (source.fallbackSrc) {
		return source.fallbackSrc;
	}

	throw new Error('No Cloudinary publicId or fallbackSrc was provided.');
}

export function getUnsignedCloudinaryUploadUrl(resourceType: Exclude<CloudinaryResourceType, 'raw'> = 'image'): string {
	if (!hasCloudinaryUnsignedUpload) {
		throw new Error(
			'Unsigned uploads are not configured. Set PUBLIC_CLOUDINARY_API_KEY and PUBLIC_CLOUDINARY_UPLOAD_PRESET.'
		);
	}

	return `https://api.cloudinary.com/v1_1/${cloudinaryConfig.cloudName}/${resourceType}/upload`;
}

export function getUnsignedCloudinaryUploadFields(extraFields: Record<string, string> = {}): Record<string, string> {
	if (!hasCloudinaryUnsignedUpload) {
		throw new Error(
			'Unsigned uploads are not configured. Set PUBLIC_CLOUDINARY_API_KEY and PUBLIC_CLOUDINARY_UPLOAD_PRESET.'
		);
	}

	return {
		upload_preset: cloudinaryConfig.uploadPreset,
		api_key: cloudinaryConfig.apiKey,
		...extraFields
	};
}