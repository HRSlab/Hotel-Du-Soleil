export const BOOKING_ENGINE_URL = 'https://booking.slope.it/140f49cb-e4f4-40e9-b494-25cfa4618e56';
export const RESTART_PROMOTION_ID = '0a5f7d69-f3a1-4589-a5da-6815eec23058';
export const TORGNON_HIKING_ADVENTURE_PROMOTION_ID = 'fe4b48f6-c950-4fa6-9d0c-4fe8bfaf6fb8';
export const FORTE_BARD_GOURMET_ESCAPE_PROMOTION_ID = 'e0b96979-bc8d-4f54-a304-0a489635299f';

export function getBookingEngineUrl(source?: string): string {
	if (!source) return BOOKING_ENGINE_URL;

	const url = new URL(BOOKING_ENGINE_URL);
	url.searchParams.set('utm_source', 'hotel_du_soleil_website');
	url.searchParams.set('utm_medium', 'referral');
	url.searchParams.set('utm_campaign', source);

	return url.toString();
}

export function getPromotionUrl(promotionId: string, source?: string): string {
	const promotionPath = `/promotions/${promotionId}`;
	const base = source ? getBookingEngineUrl(source) : BOOKING_ENGINE_URL;
	const url = new URL(base);
	url.pathname = `${url.pathname.replace(/\/$/, '')}${promotionPath}`;
	return url.toString();
}

export function getRestartPromotionUrl(source?: string): string {
	return getPromotionUrl(RESTART_PROMOTION_ID, source);
}

export function getTorgnonHikingAdventurePromotionUrl(source?: string): string {
	return getPromotionUrl(TORGNON_HIKING_ADVENTURE_PROMOTION_ID, source);
}

export function getForteBardGourmetEscapePromotionUrl(source?: string): string {
	return getPromotionUrl(FORTE_BARD_GOURMET_ESCAPE_PROMOTION_ID, source);
}

export const AOSTA_ROMANA_CASTELLO_DI_FENIS_PROMOTION_ID = '2e92557f-9516-40eb-8ff6-175a663445d8';

export function getAostaRomanaPromotionUrl(source?: string): string {
	if (!AOSTA_ROMANA_CASTELLO_DI_FENIS_PROMOTION_ID) return getBookingEngineUrl(source);
	return getPromotionUrl(AOSTA_ROMANA_CASTELLO_DI_FENIS_PROMOTION_ID, source);
}
