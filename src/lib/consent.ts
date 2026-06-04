import { writable } from 'svelte/store';

export type CookieConsent = 'accepted' | 'rejected' | null;

const STORAGE_KEY = 'hds_cookie_consent';

export const cookieConsent = writable<CookieConsent>(null);

function isBrowser(): boolean {
	return typeof window !== 'undefined';
}

function updateGoogleConsent(mode: Exclude<CookieConsent, null>): void {
	if (!isBrowser() || typeof window.gtag !== 'function') return;

	const analyticsGranted = mode === 'accepted' ? 'granted' : 'denied';

	window.gtag('consent', 'update', {
		analytics_storage: analyticsGranted,
		ad_storage: 'denied',
		ad_user_data: 'denied',
		ad_personalization: 'denied',
		functionality_storage: 'granted',
		security_storage: 'granted'
	});
}

export function initializeCookieConsent(): void {
	if (!isBrowser()) return;

	const stored = window.localStorage.getItem(STORAGE_KEY);
	if (stored === 'accepted' || stored === 'rejected') {
		cookieConsent.set(stored);
		updateGoogleConsent(stored);
		return;
	}

	cookieConsent.set(null);
}

export function setCookieConsent(mode: Exclude<CookieConsent, null>): void {
	if (!isBrowser()) return;

	window.localStorage.setItem(STORAGE_KEY, mode);
	cookieConsent.set(mode);
	updateGoogleConsent(mode);
}

export function hasAnalyticsConsent(): boolean {
	if (!isBrowser()) return false;
	return window.localStorage.getItem(STORAGE_KEY) === 'accepted';
}
