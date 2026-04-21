export const BOOKING_ENGINE_URL = 'https://booking.slope.it/140f49cb-e4f4-40e9-b494-25cfa4618e56';
export const RESTART_PROMOTION_ID = '0a5f7d69-f3a1-4589-a5da-6815eec23058';

export function getBookingEngineUrl(source?: string): string {
	if (!source) return BOOKING_ENGINE_URL;

	const url = new URL(BOOKING_ENGINE_URL);
	url.searchParams.set('utm_source', 'hotel_du_soleil_website');
	url.searchParams.set('utm_medium', 'referral');
	url.searchParams.set('utm_campaign', source);

	return url.toString();
}

export function getRestartPromotionUrl(source?: string): string {
	const promotionPath = `/promotions/${RESTART_PROMOTION_ID}`;
	const base = source ? getBookingEngineUrl(source) : BOOKING_ENGINE_URL;
	const url = new URL(base);
	url.pathname = `${url.pathname.replace(/\/$/, '')}${promotionPath}`;
	return url.toString();
}