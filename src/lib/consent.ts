export type ConsentStatus = 'accepted_all' | 'rejected_all' | 'custom';

export type ConsentPreferences = {
	necessary: true;
	functional: boolean;
	analytics: boolean;
	marketing: boolean;
};

export type ConsentState = ConsentPreferences & {
	status: ConsentStatus;
	updatedAt: string;
	version: number;
};

export type ConsentCategory = keyof ConsentPreferences;

export const CONSENT_STORAGE_KEY = 'hds_cookie_consent_v1';
export const CONSENT_VERSION = 1;

const DEFAULT_PREFERENCES: ConsentPreferences = {
	necessary: true,
	functional: false,
	analytics: false,
	marketing: false
};

function isBrowser(): boolean {
	return typeof window !== 'undefined';
}

function isValidConsentShape(value: unknown): value is ConsentState {
	if (!value || typeof value !== 'object') return false;

	const candidate = value as Partial<ConsentState>;
	return (
		candidate.necessary === true &&
		typeof candidate.functional === 'boolean' &&
		typeof candidate.analytics === 'boolean' &&
		typeof candidate.marketing === 'boolean' &&
		typeof candidate.updatedAt === 'string' &&
		(candidate.status === 'accepted_all' ||
			candidate.status === 'rejected_all' ||
			candidate.status === 'custom')
	);
}

export function readStoredConsent(): ConsentState | null {
	if (!isBrowser()) return null;

	try {
		const raw = window.localStorage.getItem(CONSENT_STORAGE_KEY);
		if (!raw) return null;

		const parsed = JSON.parse(raw) as unknown;
		if (!isValidConsentShape(parsed)) return null;

		return {
			...parsed,
			version: CONSENT_VERSION
		};
	} catch {
		return null;
	}
}

function dispatchConsentUpdate(consent: ConsentState): void {
	window.__cookieConsentState = consent;
	window.dispatchEvent(
		new CustomEvent<ConsentState>('cookie-consent-updated', { detail: consent })
	);
	if (typeof window.__updateConsent === 'function') {
		window.__updateConsent(consent);
	}
}

function persistAndApply(consent: ConsentState): ConsentState {
	if (!isBrowser()) return consent;

	try {
		window.localStorage.setItem(CONSENT_STORAGE_KEY, JSON.stringify(consent));
	} catch {
		// Ignore storage errors (private mode / blocked storage)
	}

	dispatchConsentUpdate(consent);
	return consent;
}

export function initConsentFromStorage(): ConsentState | null {
	const consent = readStoredConsent();
	if (!consent || !isBrowser()) return consent;

	dispatchConsentUpdate(consent);
	return consent;
}

export function acceptAllConsent(): ConsentState {
	return persistAndApply({
		...DEFAULT_PREFERENCES,
		functional: true,
		analytics: true,
		marketing: true,
		status: 'accepted_all',
		updatedAt: new Date().toISOString(),
		version: CONSENT_VERSION
	});
}

export function rejectAllConsent(): ConsentState {
	return persistAndApply({
		...DEFAULT_PREFERENCES,
		status: 'rejected_all',
		updatedAt: new Date().toISOString(),
		version: CONSENT_VERSION
	});
}

export function saveCustomConsent(preferences: {
	functional: boolean;
	analytics: boolean;
	marketing: boolean;
}): ConsentState {
	return persistAndApply({
		necessary: true,
		functional: preferences.functional,
		analytics: preferences.analytics,
		marketing: preferences.marketing,
		status: 'custom',
		updatedAt: new Date().toISOString(),
		version: CONSENT_VERSION
	});
}

export function hasConsentCategory(category: ConsentCategory): boolean {
	if (category === 'necessary') return true;
	if (!isBrowser()) return false;

	const activeConsent = window.__cookieConsentState ?? readStoredConsent();
	if (!activeConsent) return false;

	return Boolean(activeConsent[category]);
}
