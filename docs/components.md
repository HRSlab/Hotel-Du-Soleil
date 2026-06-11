# Components

Reusable components live in [`src/lib/components`](../src/lib/components) and are
imported with the `$lib` alias, e.g.:

```svelte
import Navbar from '$lib/components/Navbar.svelte';
```

All components use **Svelte 5 runes** (`$props`, `$state`, `$derived`, `$bindable`).
Several use a `cn()` helper (`twMerge(clsx(...))`) to compose Tailwind classes.

## Layout & navigation

### `Navbar.svelte`

Top navigation with a mega-menu, language switcher (driven by `locale`/`locales`
from i18n, with `langLabels` for display names), and a "book" entry point that opens
the `BookingDrawer`. Uses the `clickOutside` action to close menus.

### `Footer.svelte`

Site footer. Pure presentational; pulls all copy from the i18n store (`$t('footer.*')`).

### `CookieBanner.svelte`

Renders only while consent is unset (`$cookieConsent === null`). Calls
`setCookieConsent('accepted' | 'rejected')` from [`src/lib/consent.ts`](../src/lib/consent.ts)
and links to `/cookie-policy`. See [Analytics & consent](./analytics-and-consent.md).

### `CloudinaryRuntime.svelte`

Invisible runtime hook mounted in the root layout. When Cloudinary delivery is
enabled, it rewrites `img[src]`, `source[src]`, and `poster` attributes to Cloudinary
URLs (and observes DOM mutations to catch dynamically added nodes). See [Cloudinary](./cloudinary.md).

### `SecurityGuard.svelte`

Mounts global listeners that disable right-click, copy/cut, drag, and common
DevTools/print keyboard shortcuts — a light content-protection measure for the
hotel's imagery. (Note: this is a deterrent only, not real security.)

## Booking

### `BookingBar.svelte`

Horizontal booking widget (used on the home page). Local `$state` for `arrival`,
`departure`, `adults`, `children`; opens the `Calendar` and a guests dropdown;
builds the booking URL with `getBookingEngineUrl('booking_bar')`.

### `BookingDrawer.svelte`

Slide-in booking panel (opened from the navbar). Prop: `isOpen` (`$bindable`,
default `false`). Shows date/guest selectors plus direct contact actions
(phone/WhatsApp/email). Builds the booking URL via `getBookingEngineUrl`.

### `RoomBookingWidget.svelte`

Compact booking widget used on room pages. Same pattern as `BookingBar`, with
`getBookingEngineUrl('room_booking_widget')`.

### `Calendar.svelte`

Reusable date-range picker. Props: `arrival` (`$bindable`), `departure`
(`$bindable`), `onSelect` callback. Localizes month/day names from the active
`locale` via a `localeMap` (e.g. `it` → `it-IT`). Disables past dates.

## Carousels & galleries

### `RoomCarousel.svelte`

Cycles through the rooms defined in [`src/lib/rooms.ts`](../src/lib/rooms.ts),
showing image, name, price, and details with prev/next controls.

### `OffersCarousel.svelte`

Carousel of offer cards (title, tag, description, image, `href` to the offer page).
The offer list is defined inline in the component.

### `PromoCarousel.svelte`

Marquee-style promo strip rendered globally in the layout. Each promo links to a
booking-engine promotion via the helpers in
[`src/lib/config/booking.ts`](../src/lib/config/booking.ts) (RESTART, Torgnon Hiking,
Forte di Bard, Aosta Romana).

### `ImageCarousel.svelte`

Generic image carousel. Props: `images: { src, alt }[]`, `aspectRatio`
(default `aspect-[4/5]`), `autoPlay` (default `false`), `autoPlayInterval`
(default `5000` ms). Uses Svelte `fade` transitions and arrow controls.

### `HorizontalScrollJack.svelte`

Scroll-jacking horizontal gallery with lerp-smoothed scrolling and parallax layers.
Prop: `images: { src, alt }[]`.

### `HorizontalScrollJackGSAP.svelte`

A simpler responsive grid variant of the gallery (despite the name, the committed
version renders a CSS grid of lazy-loaded images). Prop: `images: { src, alt }[]`.

## Weather

### `HomeWeatherWidget.svelte`

Compact current-conditions widget for the home page. Fetches `https://wttr.in/Torgnon?format=j1`
on mount and renders temperature/wind/snow with Lucide icons.

### `WeatherWidget.svelte`

Richer weather widget (temp, feels-like, wind, visibility, precipitation, snow) with
an `iconFromCode` mapping. See [Weather](./weather.md).

## Forms

### `OfferLeadForm.svelte`

Lead-capture block shown on offer pages. Props: `title`, `subtitle`, and optional
`notesPlaceholder`, `submitLabel`, `successTitle`, `successText`. Surfaces direct
booking contacts (phone `+39 379 335 7713`, email `booking@hotel-du-soleil.it`).

## Component → feature map

| Component                                                                       | Primary doc                                           |
| ------------------------------------------------------------------------------- | ----------------------------------------------------- |
| `BookingBar`, `BookingDrawer`, `RoomBookingWidget`, `Calendar`, `PromoCarousel` | [Booking](./booking.md)                               |
| `CloudinaryRuntime`                                                             | [Cloudinary](./cloudinary.md)                         |
| `CookieBanner`                                                                  | [Analytics & consent](./analytics-and-consent.md)     |
| `HomeWeatherWidget`, `WeatherWidget`                                            | [Weather](./weather.md)                               |
| `Navbar`                                                                        | [i18n](./internationalization.md) (language switcher) |
