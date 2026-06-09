# Routes & pages

Routing is **file-based** under [`src/routes`](../src/routes). Page URLs use
Italian slugs (the site's primary language is Italian). This page lists every route,
notes which ones are intentionally hidden, and documents the SEO endpoints.

## Layouts & shell

- [`+layout.svelte`](../src/routes/+layout.svelte) — global wrapper applied to all
  pages (navbar, footer, cookie banner, promo carousel, analytics, chat widget,
  scroll-reveal observer). See [Architecture](./architecture.md).
- [`layout.css`](../src/routes/layout.css) — Tailwind theme + global CSS, imported
  by the layout.

## Page routes

| URL                        | File                                           | Notes                                                                                                                                         |
| -------------------------- | ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `/`                        | `+page.svelte`                                 | Home: hero (image + optional Cloudinary video), booking bar, weather, room & offer carousels.                                                 |
| `/camere`                  | `camere/+page.svelte`                          | Rooms overview.                                                                                                                               |
| `/camere/[slug]`           | `camere/[slug]/+page.svelte`                   | Room detail; `slug` matches a key in [`src/lib/rooms.ts`](../src/lib/rooms.ts) (`matrimoniale`, `tripla`, `quadrupla_standard`, `familiare`). |
| `/ristorante`              | `ristorante/+page.svelte`                      | Restaurant landing.                                                                                                                           |
| `/ristorante/menu`         | `ristorante/menu/+page.svelte`                 | Menu.                                                                                                                                         |
| `/ristorante/cantina`      | `ristorante/cantina/+page.svelte`              | Wine cellar / wine list.                                                                                                                      |
| `/ristorante/lounge-bar`   | `ristorante/lounge-bar/+page.svelte`           | Lounge bar.                                                                                                                                   |
| `/wellness`                | `wellness/+page.svelte`                        | Wellness landing.                                                                                                                             |
| `/wellness/spa`            | `wellness/spa/+page.svelte`                    | Spa.                                                                                                                                          |
| `/wellness/private-spa`    | `wellness/private-spa/+page.svelte`            | Private spa.                                                                                                                                  |
| `/wellness/massaggi`       | `wellness/massaggi/+page.svelte`               | Massages.                                                                                                                                     |
| `/wellness/trattamenti`    | `wellness/trattamenti/+page.svelte`            | Treatments.                                                                                                                                   |
| `/esperienze`              | `esperienze/+page.svelte`                      | Experiences landing.                                                                                                                          |
| `/esperienze/ciaspolate`   | `esperienze/ciaspolate/+page.svelte`           | Snowshoeing.                                                                                                                                  |
| `/esperienze/degustazione` | `esperienze/degustazione/+page.svelte`         | Tasting.                                                                                                                                      |
| `/esperienze/guide`        | `esperienze/guide/+page.svelte`                | Guided activities.                                                                                                                            |
| `/esperienze/yoga`         | `esperienze/yoga/+page.svelte`                 | Yoga.                                                                                                                                         |
| `/struttura`               | `struttura/+page.svelte`                       | The property/facility.                                                                                                                        |
| `/storia`                  | `storia/+page.svelte`                          | History.                                                                                                                                      |
| `/sostenibilita`           | `sostenibilita/+page.svelte`                   | Sustainability.                                                                                                                               |
| `/eventi`                  | `eventi/+page.svelte`                          | Events.                                                                                                                                       |
| `/kids-club`               | `kids-club/+page.svelte`                       | Kids club.                                                                                                                                    |
| `/meteo`                   | `meteo/+page.svelte` + `meteo/+page.server.ts` | Weather — server-loaded from Open-Meteo. See [Weather](./weather.md).                                                                         |
| `/offerte`                 | `offerte/+page.svelte`                         | Offers index. See per-offer rows below.                                                                                                       |
| `/policy`                  | `policy/+page.svelte`                          | Privacy/website policy.                                                                                                                       |
| `/cookie-policy`           | `cookie-policy/+page.svelte`                   | Cookie policy.                                                                                                                                |
| `/termini`                 | `termini/+page.svelte`                         | Terms & conditions.                                                                                                                           |

### Offers (`/offerte/*`)

Each promotion is its own page. Several deep-link into the booking engine via the
promotion-URL helpers in [`src/lib/config/booking.ts`](../src/lib/config/booking.ts)
(see [Booking](./booking.md)).

| URL                                       | File                                                  |
| ----------------------------------------- | ----------------------------------------------------- |
| `/offerte/restart`                        | `offerte/restart/+page.svelte`                        |
| `/offerte/torgnon-hiking-adventure`       | `offerte/torgnon-hiking-adventure/+page.svelte`       |
| `/offerte/forte-di-bard-gourmet-escape`   | `offerte/forte-di-bard-gourmet-escape/+page.svelte`   |
| `/offerte/aosta-romana-castello-di-fenis` | `offerte/aosta-romana-castello-di-fenis/+page.svelte` |
| `/offerte/workation-alpino`               | `offerte/workation-alpino/+page.svelte`               |
| `/offerte/family-base-camp`               | `offerte/family-base-camp/+page.svelte`               |
| `/offerte/family-mountain-camp`           | `offerte/family-mountain-camp/+page.svelte`           |
| `/offerte/summit-taste`                   | `offerte/summit-taste/+page.svelte`                   |
| `/offerte/wheels-relax`                   | `offerte/wheels-relax/+page.svelte`                   |
| `/offerte/orizzonti-silenzio`             | `offerte/orizzonti-silenzio/+page.svelte`             |

## Hidden routes (redirected)

[`src/hooks.server.ts`](../src/hooks.server.ts) intercepts requests and issues a
`307` redirect to `/` for these paths, so the pages exist in the repo but are not
publicly reachable:

- `/posizione`
- `/sport` and any `/sport/*` (`/sport/bike`, `/sport/sci`, `/sport/trekking`, `/sport/noleggio`)

```ts
function isHiddenSectionPath(pathname: string): boolean {
	return pathname === '/posizione' || pathname === '/sport' || pathname.startsWith('/sport/');
}
```

To re-enable a section, remove its path from `isHiddenSectionPath` (and, for SEO,
add it back to the sitemap below).

## SEO endpoints

- **`/sitemap.xml`** — [`sitemap.xml/+server.ts`](../src/routes/sitemap.xml/+server.ts)
  returns an XML sitemap built from a hard-coded `routes` array against
  `https://www.hotel-du-soleil.it`. It sets `lastmod` to today's date and uses
  `priority` 1.0 for `/`, 0.9 for `/offerte`, and 0.8 for the rest.
  > Note: the array currently includes `/posizione` and `/sport` even though those
  > are redirected by the server hook — keep them in sync when changing visibility.
- **Per-page metadata** — pages set `<title>`, `<meta name="description">`, and
  keywords inside `<svelte:head>` (see the home page for an example).

## Adding a page

1. Create `src/routes/<slug>/+page.svelte`.
2. Pull copy from the i18n store (`$t('...')`) and add the keys to each locale file
   under `src/lib/i18n/locales` (see [i18n](./internationalization.md)).
3. Add the URL to the sitemap `routes` array.
4. If the page should be reachable, make sure it isn't matched by `isHiddenSectionPath`.
