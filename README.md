# Hotel Du Soleil

[![Netlify Status](https://api.netlify.com/api/v1/badges/5d207c32-b7e7-4626-8aea-6246d1de6347/deploy-status)](https://app.netlify.com/projects/preeminent-marigold-40ba4d/deploys)

Marketing website for **Hotel Du Soleil**, an alpine hotel in **Torgnon, Valle
d'Aosta** ([www.hotel-du-soleil.it](https://www.hotel-du-soleil.it)).

Built with **SvelteKit 2 · Svelte 5 (runes) · Tailwind CSS 4 · TypeScript**, with
multilingual content, Cloudinary media delivery, a Slope.it booking-engine
integration, Google Analytics (Consent Mode), and a live weather page for the resort.

## Quick start

```sh
npm install          # also runs `svelte-kit sync`
cp .env.example .env # optional: Cloudinary config (site works without it)
npm run dev          # start the dev server (add `-- --open` to open a browser)
```

Build & preview a production bundle:

```sh
npm run build
npm run preview
```

## Scripts

| Script                    | Purpose                                               |
| ------------------------- | ----------------------------------------------------- |
| `npm run dev`             | Dev server with HMR.                                  |
| `npm run build`           | Production build.                                     |
| `npm run preview`         | Serve the production build.                           |
| `npm run check`           | Type-check (`svelte-check`).                          |
| `npm run lint`            | `prettier --check` + `eslint`.                        |
| `npm run format`          | Auto-format with Prettier.                            |
| `npm run cloudinary:sync` | Rebuild the Cloudinary asset manifest (needs `.env`). |
| `npm run optimize-images` | Convert `static/imgs` images to WebP.                 |

> No pre-commit hooks are configured — run `npm run format`, `npm run lint`, and
> `npm run check` manually before committing.

## Project layout

```
src/
├── app.html            # Document shell (fonts, GA bootstrap)
├── hooks.server.ts     # Redirects hidden sections (/sport, /posizione) to /
├── routes/             # File-based pages, layouts, endpoints
└── lib/
    ├── components/      # Reusable Svelte components
    ├── i18n/            # Custom translation store + locale JSON
    ├── config/booking.ts  # Booking engine + promotion URLs
    ├── cloudinary.ts / server/cloudinary.ts  # Media delivery
    ├── analytics.ts / consent.ts             # GA4 + cookie consent
    └── rooms.ts         # Room catalog data
static/imgs/            # Public images (served at /imgs/...)
scripts/                # Image optimization, Cloudinary sync, content helpers
```

## Documentation

Full documentation lives in [`docs/`](./docs/README.md):

- [Architecture](./docs/architecture.md)
- [Project structure](./docs/project-structure.md)
- [Development guide](./docs/development.md)
- [Routes & pages](./docs/routes.md)
- [Components](./docs/components.md)
- [Internationalization (i18n)](./docs/internationalization.md)
- [Booking integration](./docs/booking.md)
- [Cloudinary media pipeline](./docs/cloudinary.md)
- [Analytics & cookie consent](./docs/analytics-and-consent.md)
- [Weather feature](./docs/weather.md)
- [Configuration reference](./docs/configuration.md)
- [Content management](./docs/content.md)
- [Deployment](./docs/deployment.md)

## Tech stack

SvelteKit · Svelte 5 · Tailwind CSS 4 · Vite 7 · TypeScript 5 · Cloudinary ·
GSAP / svelte-motion / Swiper · Lucide icons · deployed on Netlify (`adapter-auto`).
