# Analytics & cookie consent

The site uses **Google Analytics 4** (measurement ID `G-GGKFG688CK`) with **Google
Consent Mode v2**, gated behind an explicit cookie banner. Analytics events only fire
after the visitor accepts cookies.

## Pieces

| File                                                                                  | Role                                                                                                                              |
| ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| [`src/app.html`](../src/app.html)                                                     | Loads `gtag.js`, sets Consent Mode **defaults to denied**, and configures GA with `send_page_view: false` + `anonymize_ip: true`. |
| [`src/lib/consent.ts`](../src/lib/consent.ts)                                         | Consent store + `localStorage` persistence + Google consent updates.                                                              |
| [`src/lib/components/CookieBanner.svelte`](../src/lib/components/CookieBanner.svelte) | The accept/reject UI.                                                                                                             |
| [`src/lib/analytics.ts`](../src/lib/analytics.ts)                                     | Consent-aware event helpers + URL classifiers.                                                                                    |
| [`src/routes/+layout.svelte`](../src/routes/+layout.svelte)                           | Initializes consent and wires up page-view, scroll-depth, and click tracking.                                                     |

## Consent flow

1. **Default denied.** `app.html` calls `gtag('consent', 'default', { analytics_storage: 'denied', ad_*: 'denied', ... })` before anything else, and configures GA with `send_page_view: false` so nothing is sent automatically.
2. **Initialize on load.** The layout calls `initializeCookieConsent()` (from `consent.ts`) on mount, which reads `localStorage['hds_cookie_consent']`:
   - `'accepted'` → store set to accepted, Google consent updated to `analytics_storage: 'granted'`.
   - `'rejected'` → store rejected, consent stays denied.
   - unset → the `CookieBanner` is shown (`$cookieConsent === null`).
3. **User choice.** `setCookieConsent('accepted' | 'rejected')` persists the choice and calls `updateGoogleConsent(...)`. Ads-related signals are always denied; only `analytics_storage` toggles.
4. **Reset.** `resetCookieConsent()` clears the stored choice (re-shows the banner) — useful from a cookie-policy "manage preferences" control.

```ts
// consent.ts (storage key + states)
const STORAGE_KEY = 'hds_cookie_consent';
export type CookieConsent = 'accepted' | 'rejected' | null;
export function hasAnalyticsConsent(): boolean {
	return isBrowser() && localStorage.getItem(STORAGE_KEY) === 'accepted';
}
```

## Event tracking

[`src/lib/analytics.ts`](../src/lib/analytics.ts) exposes helpers that **no-op unless
consent is granted** and `window.gtag` exists:

| Helper                       | Emits                                                 | When                                                           |
| ---------------------------- | ----------------------------------------------------- | -------------------------------------------------------------- |
| `trackPageView(path, title)` | `page_view`                                           | On every client-side navigation (from the layout's `$effect`). |
| `trackEvent(name, params)`   | custom event                                          | Used by the tracking listeners below.                          |
| `isBookingUrl(url)`          | —                                                     | True for `booking.slope.it` links.                             |
| `classifyContactHref(href)`  | `'phone' \| 'email' \| 'whatsapp' \| 'other' \| null` | Classifies `tel:`/`mailto:`/WhatsApp links.                    |

The root layout installs a capturing document click listener and a scroll listener
that emit:

| Event              | Trigger                                   | Key params                                 |
| ------------------ | ----------------------------------------- | ------------------------------------------ |
| `page_view`        | route change                              | `page_path`, `page_title`, `page_location` |
| `scroll_depth`     | reaching 25/50/75/90% of the page         | `percent_scrolled`, `page_path`            |
| `contact_click`    | clicking a `tel:`/`mailto:`/WhatsApp link | `contact_type`, `link_url`, `page_path`    |
| `begin_checkout`   | clicking a link to the booking engine     | `currency: 'EUR'`, `link_url`, `page_path` |
| `select_promotion` | clicking a link to `/offerte/<slug>`      | `promotion_id`, `page_path`                |
| `outbound_click`   | clicking any cross-origin link            | `link_url`, `link_domain`, `page_path`     |

Scroll milestones are tracked per page (the set is cleared on navigation).

## Third-party widget

The layout also injects the **Canary** chat widget (`hotel-du-soleil-torgnon83`)
on mount. It is loaded from Canary's CDN and themed to the site's gold/charcoal palette.

## Adding a new tracked event

1. Add a `trackEvent('your_event', { ... })` call where the interaction happens (or
   extend the layout's central click listener for global behaviors).
2. Remember it will only fire when the user has accepted cookies — test by accepting
   in the banner first.
