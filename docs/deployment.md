# Deployment

The site is built with SvelteKit's **`adapter-auto`** and deployed to **Netlify**.

## Build

```sh
npm run build      # vite build → produces the deployable output
npm run preview    # serve the build locally to sanity-check
```

`adapter-auto` (configured in [`svelte.config.js`](../svelte.config.js)) detects the
host at build time and selects the appropriate adapter — Netlify in production. If you
ever pin to a single host, replace it with the host-specific adapter (e.g.
`@sveltejs/adapter-netlify`).

## Netlify configuration

[`netlify.toml`](../netlify.toml):

```toml
[build]
  command = "npm run build"
  publish = "build"

[[redirects]]
  from = "https://hotel-du-soleil.it/*"
  to = "https://www.hotel-du-soleil.it/:splat"
  status = 301
  force = true

[[redirects]]
  from = "https://hoteldusoleil.netlify.app/*"
  to = "https://www.hotel-du-soleil.it/:splat"
  status = 301
  force = true
```

- **Build command:** `npm run build`; **publish dir:** `build`.
- **Canonical host redirects:** the apex domain (`hotel-du-soleil.it`) and the
  `*.netlify.app` URL are 301-redirected to `https://www.hotel-du-soleil.it`. The
  `www` host is the canonical one (also used in the sitemap and host redirects).

## Environment variables in production

If Cloudinary delivery is used in production, set the `PUBLIC_CLOUDINARY_*` and
`CLOUDINARY_API_SECRET` variables in the Netlify site settings (Build & deploy →
Environment). Without them the site serves local `/imgs/...` assets. See
[Cloudinary](./cloudinary.md) and [Development](./development.md).

## SEO / canonical URLs

- The canonical origin is `https://www.hotel-du-soleil.it`.
- `/sitemap.xml` is generated dynamically from the route list in
  [`src/routes/sitemap.xml/+server.ts`](../src/routes/sitemap.xml/+server.ts).
- Keep the sitemap, the host redirects, and the hidden-section logic in
  [`src/hooks.server.ts`](../src/hooks.server.ts) consistent when changing which
  pages are public.

## Pre-deploy checklist

```sh
npm run format    # apply Prettier
npm run lint      # prettier --check + eslint
npm run check     # svelte-check type-check
npm run build     # ensure a clean production build
```
