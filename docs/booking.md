# Booking integration

The site does not process bookings itself. All "Book now" actions deep-link into an
external booking engine hosted by **Slope.it**. The URLs and promotion IDs are
centralized in [`src/lib/config/booking.ts`](../src/lib/config/booking.ts).

## Booking engine URL

```ts
export const BOOKING_ENGINE_URL = 'https://booking.slope.it/140f49cb-e4f4-40e9-b494-25cfa4618e56';

export function getBookingEngineUrl(source?: string): string {
	if (!source) return BOOKING_ENGINE_URL;
	const url = new URL(BOOKING_ENGINE_URL);
	url.searchParams.set('utm_source', 'hotel_du_soleil_website');
	url.searchParams.set('utm_medium', 'referral');
	url.searchParams.set('utm_campaign', source);
	return url.toString();
}
```

- Call `getBookingEngineUrl()` with **no argument** for a bare link.
- Pass a `source` string to attach **UTM parameters** for campaign attribution. The
  `source` becomes `utm_campaign`. Existing call sites use sources like
  `booking_bar`, `room_booking_widget`, and `promo_marquee_restart`.

## Promotion deep-links

Promotions point at a `/promotions/<id>` path on the booking engine. `getPromotionUrl`
composes that path while preserving any UTM params:

```ts
export function getPromotionUrl(promotionId: string, source?: string): string {
	const promotionPath = `/promotions/${promotionId}`;
	const base = source ? getBookingEngineUrl(source) : BOOKING_ENGINE_URL;
	const url = new URL(base);
	url.pathname = `${url.pathname.replace(/\/$/, '')}${promotionPath}`;
	return url.toString();
}
```

### Defined promotions

| Helper                                           | Promotion ID constant                         | Offer page                                |
| ------------------------------------------------ | --------------------------------------------- | ----------------------------------------- |
| `getRestartPromotionUrl(source?)`                | `RESTART_PROMOTION_ID`                        | `/offerte/restart`                        |
| `getTorgnonHikingAdventurePromotionUrl(source?)` | `TORGNON_HIKING_ADVENTURE_PROMOTION_ID`       | `/offerte/torgnon-hiking-adventure`       |
| `getForteBardGourmetEscapePromotionUrl(source?)` | `FORTE_BARD_GOURMET_ESCAPE_PROMOTION_ID`      | `/offerte/forte-di-bard-gourmet-escape`   |
| `getAostaRomanaPromotionUrl(source?)`            | `AOSTA_ROMANA_CASTELLO_DI_FENIS_PROMOTION_ID` | `/offerte/aosta-romana-castello-di-fenis` |

`getAostaRomanaPromotionUrl` falls back to the bare booking URL if its promotion ID
is empty — a useful pattern when adding a new promotion before its ID is known.

## Where booking links are used

| Component                  | Source tag                        |
| -------------------------- | --------------------------------- |
| `BookingBar.svelte`        | `booking_bar`                     |
| `RoomBookingWidget.svelte` | `room_booking_widget`             |
| `BookingDrawer.svelte`     | via `getBookingEngineUrl`         |
| `PromoCarousel.svelte`     | `promo_marquee_*` (per promotion) |

The booking widgets (`BookingBar`, `RoomBookingWidget`, `BookingDrawer`) collect
arrival/departure dates and guest counts locally via the shared `Calendar` component,
then hand off to the engine URL. Direct contact options (phone/WhatsApp/email) are
also offered in `BookingDrawer` and `OfferLeadForm`.

## Analytics tie-in

Clicks that navigate to `booking.slope.it` are detected by `isBookingUrl()` in
[`src/lib/analytics.ts`](../src/lib/analytics.ts) and tracked as a GA `begin_checkout`
event; links to `/offerte/<slug>` fire `select_promotion`. See
[Analytics & consent](./analytics-and-consent.md).

## Adding a new promotion

1. Add the promotion ID constant and a `getXyzPromotionUrl()` helper to
   `src/lib/config/booking.ts`.
2. Create the offer page under `src/routes/offerte/<slug>/+page.svelte`.
3. Link the page/CTA to the new helper, passing a descriptive `source`.
4. Add the offer to `OffersCarousel` / `PromoCarousel` if it should be featured.
5. Add the route to the sitemap (`src/routes/sitemap.xml/+server.ts`).
