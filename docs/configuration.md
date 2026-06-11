# Configuration reference

Every configuration file in the repo and what it controls.

## `package.json`

Defines the project name (`hotel-du-soleil`), `"type": "module"` (ESM), the npm
scripts (see [Development](./development.md)), and dependencies. Notable runtime deps:
`cloudinary`, `gsap`, `swiper`, `three`/`@types/three`, `lucide-svelte`,
`svelte-motion`, `clsx`, `tailwind-merge`.

## `svelte.config.js`

```js
import adapter from '@sveltejs/adapter-auto';
const config = {
	kit: { adapter: adapter() },
	vitePlugin: {
		dynamicCompileOptions: ({ filename }) =>
			filename.includes('node_modules') ? undefined : { runes: true }
	}
};
```

- **`adapter-auto`** detects the deploy target at build time (Netlify in production).
  If you settle on a single host, you can swap in a specific adapter.
- **Runes mode** is forced on for project code (not `node_modules`), which is why
  components use `$state`/`$props`/etc.

## `vite.config.ts`

```ts
export default defineConfig({ plugins: [tailwindcss(), sveltekit()] });
```

Tailwind CSS 4 is wired in via the `@tailwindcss/vite` plugin (no separate
`tailwind.config.js`/PostCSS file — Tailwind 4 is configured in CSS).

## `tsconfig.json`

Extends the generated `./.svelte-kit/tsconfig.json` and enables: `strict`,
`allowJs` + `checkJs`, `esModuleInterop`, `forceConsistentCasingInFileNames`,
`resolveJsonModule`, `skipLibCheck`, `sourceMap`, `moduleResolution: bundler`, and
`rewriteRelativeImportExtensions`. Path aliases (other than `$lib`) are managed by
SvelteKit.

## `eslint.config.js`

Flat config composing: `includeIgnoreFile('.gitignore')`, `js.configs.recommended`,
`typescript-eslint` recommended, `eslint-plugin-svelte` recommended, and
`eslint-config-prettier` (+ the Svelte Prettier compat). Custom rules:

- `no-undef: 'off'` (recommended for TS projects).
- `svelte/no-navigation-without-resolve: 'off'`.

The Svelte block sets up the TS parser with `projectService` and the project's
`svelteConfig` for `.svelte`/`.svelte.ts`/`.svelte.js` files.

## `.prettierrc` / `.prettierignore`

Prettier options: **tabs**, single quotes, no trailing commas, 100-char width,
plugins `prettier-plugin-svelte` + `prettier-plugin-tailwindcss`, with
`tailwindStylesheet: ./src/routes/layout.css` so class sorting knows the theme.
`.prettierignore` excludes lockfiles and `static/`.

## `.npmrc`

```
engine-strict=true
```

Enforces the declared Node/npm engine constraints during install.

## Tailwind theme — `src/routes/layout.css`

Tailwind 4 is configured **in CSS** here (imported by the root layout). This is where
the alpine color palette (`alpine-text`, `alpine-gold`, `alpine-bg`, `alpine-border`,
`alpine-muted`, etc.), fonts, and global styles/animations are defined. The custom
`is-visible` / `fade-up-element` classes used for scroll-reveal animations live here.

## `netlify.toml`

```toml
[build]
  command = "npm run build"
  publish = "build"
[[redirects]]   # apex → www
[[redirects]]   # netlify.app → www
```

See [Deployment](./deployment.md).

## Environment variables (`.env`)

Cloudinary-only; templated in `.env.example`. The app runs without them (falls back
to local assets). Full reference in [Cloudinary](./cloudinary.md). `.env`/`.env.*`
are git-ignored except `.env.example` and `.env.test`.

## `app.html` (not a config file, but global setup)

Sets the document `lang`/`dir`, async-loads Google Fonts (Cormorant Garamond +
Inter), and bootstraps Google Analytics with Consent Mode (defaults denied). See
[Analytics & consent](./analytics-and-consent.md).
