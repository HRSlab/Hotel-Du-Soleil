# Development guide

## Prerequisites

- **Node.js** (project developed with Node 22; `package.json` uses ESM/`"type": "module"`).
  `.npmrc` sets `engine-strict=true`, so an incompatible Node version will fail install.
- **npm** (a `package-lock.json` is committed; prefer `npm`).

## Install

```sh
npm install
```

This also runs the `prepare` script (`svelte-kit sync`) to generate `.svelte-kit`
types. If you ever see missing `$types`/`$env` types, re-run:

```sh
npm run prepare
```

## Environment variables

Copy the example file and fill in the values you need:

```sh
cp .env.example .env
```

`.env.example` contains the Cloudinary configuration:

```env
PUBLIC_CLOUDINARY_CLOUD_NAME=
PUBLIC_CLOUDINARY_API_KEY=
PUBLIC_CLOUDINARY_UPLOAD_PRESET=
PUBLIC_CLOUDINARY_ENABLE_DELIVERY=false
PUBLIC_CLOUDINARY_BASE_FOLDER=hotel-du-soleil
CLOUDINARY_API_SECRET=
```

- The site runs **fine without any of these** — when Cloudinary is not configured
  the app simply serves local `/imgs/...` files.
- `PUBLIC_*` vars are exposed to the browser; `CLOUDINARY_API_SECRET` is server-only.
- See [Cloudinary media pipeline](./cloudinary.md) for the full meaning of each var.

`.env` and `.env.*` are git-ignored (except `.env.example`/`.env.test`).

## Run the dev server

```sh
npm run dev
# or open a browser automatically:
npm run dev -- --open
```

Vite serves the app (default `http://localhost:5173`).

## npm scripts

| Script            | Command                                     | What it does                                                        |
| ----------------- | ------------------------------------------- | ------------------------------------------------------------------- |
| `dev`             | `vite dev`                                  | Start the dev server with HMR.                                      |
| `build`           | `vite build`                                | Production build.                                                   |
| `preview`         | `vite preview`                              | Serve the production build locally.                                 |
| `prepare`         | `svelte-kit sync`                           | Generate SvelteKit types (runs on install).                         |
| `check`           | `svelte-kit sync && svelte-check`           | Type-check `.svelte`/`.ts` against `tsconfig.json`.                 |
| `check:watch`     | same, `--watch`                             | Continuous type-checking.                                           |
| `lint`            | `prettier --check . && eslint .`            | Verify formatting + lint.                                           |
| `format`          | `prettier --write .`                        | Auto-format the codebase.                                           |
| `cloudinary:sync` | `node scripts/sync-cloudinary-manifest.mjs` | Rebuild the Cloudinary manifest (needs Cloudinary creds in `.env`). |
| `optimize-images` | `node scripts/optimize-images.js`           | Convert `static/imgs` files to WebP.                                |

## Lint & format

The repo uses **Prettier** (formatting) and **ESLint flat config** (linting), and
the `lint` script runs both. Before committing:

```sh
npm run format   # apply formatting
npm run lint     # verify formatting + lint rules
npm run check    # type-check
```

Formatting conventions (from `.prettierrc`): **tabs**, single quotes, no trailing
commas, 100-char print width, with the Svelte and Tailwind Prettier plugins.

> There are **no pre-commit hooks** configured in this repo (no Husky / no
> `.pre-commit-config.yaml`), so run the checks above manually.

## TypeScript

`tsconfig.json` extends the generated `.svelte-kit/tsconfig.json` and enables
`strict`, `checkJs`/`allowJs`, and `resolveJsonModule`. Use the `$lib` alias for
library imports (e.g. `import { t } from '$lib/i18n'`).

## Building & previewing

```sh
npm run build
npm run preview
```

Production deployment is handled by Netlify — see [Deployment](./deployment.md).
