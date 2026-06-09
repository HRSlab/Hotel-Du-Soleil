# Architecture

## Overview

Hotel Du Soleil is a **content/marketing website** for an alpine hotel. It is a
SvelteKit application that is mostly static (pages are pre-rendered/SSR'd marketing
content) with a few dynamic touches: a server-rendered weather page, client-side
internationalization, analytics, and deep-links into an external booking engine.

There is **no application database and no custom backend API**. All "data" is either:

- hard-coded in TypeScript modules (e.g. room definitions in [`src/lib/rooms.ts`](../src/lib/rooms.ts)),
- stored as translation JSON under [`src/lib/i18n/locales`](../src/lib/i18n/locales), or
- fetched from third-party services at request/render time (Open-Meteo, Cloudinary, the Slope booking engine, Canary chat, Google Analytics).

## Tech stack

| Layer          | Technology                                                                                                                                         |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Framework      | [SvelteKit](https://svelte.dev/docs/kit) `^2.50`                                                                                                   |
| UI library     | [Svelte 5](https://svelte.dev/docs/svelte) `^5.51` (uses **runes**: `$state`, `$props`, `$derived`, `$effect`, `$bindable`)                        |
| Styling        | [Tailwind CSS 4](https://tailwindcss.com/docs) via `@tailwindcss/vite`, with a custom theme in [`src/routes/layout.css`](../src/routes/layout.css) |
| Build tool     | [Vite 7](https://vite.dev)                                                                                                                         |
| Language       | TypeScript 5 (strict)                                                                                                                              |
| Deploy adapter | `@sveltejs/adapter-auto` (Netlify in production)                                                                                                   |
| Icons          | [`lucide-svelte`](https://lucide.dev)                                                                                                              |
| Animation      | [GSAP](https://gsap.com), `svelte-motion`, native Svelte transitions, CSS + `IntersectionObserver`                                                 |
| Carousels      | [Swiper](https://swiperjs.com) and custom carousel components                                                                                      |
| Media CDN      | [Cloudinary](https://cloudinary.com)                                                                                                               |
| Utilities      | `clsx` + `tailwind-merge` (the `cn()` helper found in several components)                                                                          |

## Rendering model

- **File-based routing.** Everything under [`src/routes`](../src/routes) maps to a URL.
  `+page.svelte` files are pages, `+layout.svelte` wraps all pages, `+page.server.ts`
  runs server-side loaders, and `+server.ts` files are endpoints. See [Routes & pages](./routes.md).
- **Adapter-auto.** The build target is detected automatically; in production it
  builds for **Netlify** (see [`netlify.toml`](../netlify.toml) and [Deployment](./deployment.md)).
- **Runes mode** is enabled for project code (not `node_modules`) in
  [`svelte.config.js`](../svelte.config.js).

## Request / render lifecycle

1. **Server hook** — [`src/hooks.server.ts`](../src/hooks.server.ts) runs on every
   request. It redirects "hidden" sections (`/posizione`, `/sport`, `/sport/*`) to
   `/` with a `307`, so those pages exist in the repo but are not publicly reachable.
2. **HTML shell** — [`src/app.html`](../src/app.html) is the document template. It
   sets up async Google Fonts (Cormorant Garamond + Inter), bootstraps **Google
   Analytics with Consent Mode defaulting to denied**, and injects the SvelteKit head/body.
3. **Root layout** — [`src/routes/+layout.svelte`](../src/routes/+layout.svelte)
   wraps every page with the `Navbar`, `Footer`, `CookieBanner`, `PromoCarousel`,
   `CloudinaryRuntime`, and `SecurityGuard`. It also:
   - initializes cookie consent,
   - injects the **Canary** chat widget,
   - wires up analytics (page views, scroll-depth, contact/outbound/booking click tracking),
   - sets `<html lang>`/`dir` from the active locale,
   - runs an `IntersectionObserver` to add `is-visible` for scroll-reveal animations.
4. **Page** — the matched `+page.svelte` renders its content, pulling copy from the
   i18n store and assets from `/imgs/...` (optionally rewritten to Cloudinary).

## Cross-cutting concerns

| Concern        | Where it lives                                                                      | Doc                                               |
| -------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------- |
| Translations   | `src/lib/i18n/*`                                                                    | [i18n](./internationalization.md)                 |
| Booking links  | `src/lib/config/booking.ts`                                                         | [Booking](./booking.md)                           |
| Media delivery | `src/lib/cloudinary.ts`, `src/lib/server/cloudinary.ts`, `CloudinaryRuntime.svelte` | [Cloudinary](./cloudinary.md)                     |
| Analytics      | `src/lib/analytics.ts`, `+layout.svelte`, `app.html`                                | [Analytics & consent](./analytics-and-consent.md) |
| Consent        | `src/lib/consent.ts`, `CookieBanner.svelte`                                         | [Analytics & consent](./analytics-and-consent.md) |
| Weather        | `src/routes/meteo/*`, `*WeatherWidget.svelte`                                       | [Weather](./weather.md)                           |
| SEO            | `src/routes/sitemap.xml/+server.ts`, per-page `<svelte:head>`                       | [Routes](./routes.md)                             |

## Data-flow diagram (text)

```
Browser request
   │
   ▼
hooks.server.ts ──(hidden path?)──▶ 307 redirect to /
   │ no
   ▼
app.html (fonts, GA consent=denied default)
   │
   ▼
+layout.svelte ──▶ Navbar / Footer / CookieBanner / PromoCarousel
   │                 + analytics listeners + Canary chat + Cloudinary rewrite
   ▼
+page.svelte ──▶ i18n store ($t)  ──▶ locale JSON
              ──▶ /imgs/... assets ──▶ (optional) Cloudinary CDN
              ──▶ booking buttons   ──▶ getBookingEngineUrl() ──▶ Slope.it
              ──▶ weather widgets   ──▶ Open-Meteo / wttr.in
```
