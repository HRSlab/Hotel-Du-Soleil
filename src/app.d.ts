// See https://svelte.dev/docs/kit/types#app.d.ts
// for information about these interfaces
declare global {
	type CookieConsentState = {
		necessary: true;
		functional: boolean;
		analytics: boolean;
		marketing: boolean;
		status: 'accepted_all' | 'rejected_all' | 'custom';
		updatedAt: string;
		version: number;
	};

	interface Window {
		dataLayer: unknown[];
		gtag?: (...args: unknown[]) => void;
		__cookieConsentState?: CookieConsentState;
		__updateConsent?: (consent: CookieConsentState) => void;
		__gaLoaded?: boolean;
	}

	namespace App {
		// interface Error {}
		// interface Locals {}
		// interface PageData {}
		// interface PageState {}
		// interface Platform {}
	}
}

export {};
