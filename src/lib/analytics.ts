type EventParams = Record<string, string | number | boolean | null | undefined>;

function isBrowser(): boolean {
	return typeof window !== 'undefined';
}

export function trackEvent(eventName: string, params: EventParams = {}): void {
	if (!isBrowser() || typeof window.gtag !== 'function') return;
	window.gtag('event', eventName, params);
}

export function trackPageView(path: string, title: string): void {
	if (!isBrowser() || typeof window.gtag !== 'function') return;
	window.gtag('event', 'page_view', {
		page_path: path,
		page_title: title,
		page_location: window.location.href
	});
}

export function isBookingUrl(url: URL): boolean {
	return /booking\.slope\.it$/i.test(url.hostname);
}

export function classifyContactHref(
	rawHref: string
): 'phone' | 'email' | 'whatsapp' | 'other' | null {
	const href = rawHref.trim().toLowerCase();
	if (!href) return null;
	if (href.startsWith('tel:')) return 'phone';
	if (href.startsWith('mailto:')) return 'email';
	if (href.includes('wa.me') || href.includes('whatsapp')) return 'whatsapp';
	return null;
}
