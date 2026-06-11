# Project structure

Annotated map of the repository. Generated/ignored folders (`node_modules`,
`.svelte-kit`, `build`) are omitted.

```
Hotel-Du-Soleil/
├── README.md                 # Project overview + quick start (links to docs/)
├── docs/                     # ← this documentation
├── to-do.md                  # Content/feature backlog (see docs/content.md)
├── package.json              # Scripts and dependencies
├── package-lock.json
├── svelte.config.js          # SvelteKit + adapter-auto config (runes enabled)
├── vite.config.ts            # Vite plugins (Tailwind + SvelteKit)
├── tsconfig.json             # TypeScript (strict, extends generated config)
├── eslint.config.js          # Flat ESLint config (JS/TS/Svelte + Prettier)
├── .prettierrc               # Prettier (tabs, single quotes, Svelte+Tailwind plugins)
├── .prettierignore
├── .npmrc                    # engine-strict=true
├── .env.example              # Template for Cloudinary env vars
├── netlify.toml              # Build command, publish dir, host redirects
├── index.html.bak            # Legacy static HTML (pre-SvelteKit) — not used by the app
├── .vscode/                  # Editor settings
├── scripts/                  # Build/content tooling (see below)
├── static/                   # Static assets served at site root (images, robots, etc.)
└── src/
    ├── app.html              # HTML document shell (fonts, GA bootstrap)
    ├── app.d.ts              # Ambient TS types (Window.gtag/dataLayer, App namespace)
    ├── hooks.server.ts       # Server hook: redirects hidden sections to /
    ├── routes/               # File-based routes (pages, layouts, endpoints)
    └── lib/                  # Reusable code, importable via the `$lib` alias
```

## `src/lib`

```
src/lib/
├── index.ts                  # Barrel: re-exports ./cloudinary
├── rooms.ts                  # Room catalog data (names, prices, galleries, amenities)
├── analytics.ts              # GA4 event helpers + URL classification
├── consent.ts                # Cookie-consent store + Google Consent Mode updates
├── cloudinary.ts             # Browser-safe Cloudinary URL building + manifest lookup
├── assets/                   # In-bundle assets (favicon)
├── config/
│   └── booking.ts            # Booking engine URL + promotion deep-link helpers
├── generated/
│   └── cloudinary-manifest.json   # Local-path → Cloudinary public-id map (generated)
├── i18n/
│   ├── index.ts              # Locale store, `t` translator, `dir`, locales list
│   └── locales/              # it, en, ru, fr, de, es, ar, zh JSON files
├── server/
│   └── cloudinary.ts         # Server-only signed Cloudinary operations (uses secret)
├── utils/
│   └── clickOutside.ts       # Svelte action for outside-click detection
└── components/               # Reusable UI components (see docs/components.md)
```

## `src/routes`

See [Routes & pages](./routes.md) for the full URL map. Top level:

```
src/routes/
├── +layout.svelte            # Global shell (navbar, footer, analytics, etc.)
├── +page.svelte              # Home page
├── layout.css                # Tailwind theme + global styles
├── camere/                   # Rooms (list + [slug] detail)
├── ristorante/               # Restaurant (+ cantina, lounge-bar, menu)
├── wellness/                 # Wellness (+ spa, private-spa, massaggi, trattamenti)
├── sport/                    # Sport (+ bike, sci, trekking, noleggio) — HIDDEN via hook
├── esperienze/               # Experiences (+ ciaspolate, degustazione, guide, yoga)
├── offerte/                  # Offers/promotions (one folder per package)
├── eventi/ , kids-club/ , storia/ , struttura/ , sostenibilita/
├── posizione/                # Location — HIDDEN via hook
├── meteo/                    # Weather page (+page.server.ts loads Open-Meteo)
├── policy/ , cookie-policy/ , termini/   # Legal pages
└── sitemap.xml/+server.ts    # Dynamic sitemap endpoint
```

## `scripts/`

| Script                                                                                                     | Run via                   | Purpose                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------- | ------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `optimize-images.js`                                                                                       | `npm run optimize-images` | Convert images under `static/imgs` to WebP using `sharp`.                                                                   |
| `sync-cloudinary-manifest.mjs`                                                                             | `npm run cloudinary:sync` | Match local `static/imgs` files to Cloudinary resources and write `src/lib/generated/cloudinary-manifest.json`.             |
| `fix_ciaspolate.py`, `fix_yoga.py`, `fix_yoga2.py`, `write_guide.py`, `write_massaggi.py`, `write_yoga.py` | run manually with Python  | One-off content-authoring helpers used to generate/patch specific experience pages. See [Content management](./content.md). |

## Notable non-source files

- **`index.html.bak`** — a large legacy single-file HTML version of the site kept
  for reference. It is **not** part of the SvelteKit build.
- **`static/`** — anything here is served from the site root (e.g. `static/imgs/foo.webp`
  → `/imgs/foo.webp`). It is excluded from Prettier (see `.prettierignore`).
