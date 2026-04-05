import { CLOUDINARY_API_SECRET } from '$env/static/private';
import { PUBLIC_CLOUDINARY_API_KEY, PUBLIC_CLOUDINARY_CLOUD_NAME } from '$env/static/public';
import { v2 as cloudinary } from 'cloudinary';

export const hasCloudinaryServerConfig = Boolean(
	PUBLIC_CLOUDINARY_CLOUD_NAME && PUBLIC_CLOUDINARY_API_KEY && CLOUDINARY_API_SECRET
);

if (hasCloudinaryServerConfig) {
	cloudinary.config({
		cloud_name: PUBLIC_CLOUDINARY_CLOUD_NAME,
		api_key: PUBLIC_CLOUDINARY_API_KEY,
		api_secret: CLOUDINARY_API_SECRET,
		secure: true
	});
}

export { cloudinary };

export function assertCloudinaryServerConfig(): void {
	if (!hasCloudinaryServerConfig) {
		throw new Error(
			'Cloudinary server config is incomplete. Set PUBLIC_CLOUDINARY_CLOUD_NAME, PUBLIC_CLOUDINARY_API_KEY, and CLOUDINARY_API_SECRET.'
		);
	}
}

export function signCloudinaryParams(params: Record<string, string | number | undefined>): string {
	assertCloudinaryServerConfig();

	const filteredParams = Object.fromEntries(
		Object.entries(params).filter((entry): entry is [string, string | number] => entry[1] !== undefined)
	);

	return cloudinary.utils.api_sign_request(filteredParams, CLOUDINARY_API_SECRET);
}