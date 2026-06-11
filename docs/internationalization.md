# Internationalization (i18n)

The site uses a small **custom translation system** built on Svelte stores — there
is no external i18n library. It lives in [`src/lib/i18n`](../src/lib/i18n).

## How it works

[`src/lib/i18n/index.ts`](../src/lib/i18n/index.ts) imports one JSON file per
language and exposes:

| Export    | Type               | Description                                                                  |
| --------- | ------------------ | ---------------------------------------------------------------------------- |
| `locale`  | `writable<string>` | The active language code. Defaults to `'it'`.                                |
| `t`       | `derived` store    | A translator: `$t('section.key')` returns the string for the current locale. |
| `dir`     | `derived` store    | Text direction — `'rtl'` for Arabic, otherwise `'ltr'`.                      |
| `locales` | `string[]`         | The list of locales offered in the UI.                                       |

Usage in a component:

```svelte
<script lang="ts">
	import { t, locale, locales } from '$lib/i18n';
</script>

<h1>{$t('home.hero.title')}</h1>
<button onclick={() => locale.set('en')}>EN</button>
```

### Lookup & fallback

`t` splits the key on `.` and walks the nested JSON object. If a key is missing in
the active locale (and the active locale isn't Italian), it **falls back to Italian
(`it`)**. If still missing, it returns `undefined`.

```ts
export const t = derived(locale, ($locale) => (key: string) => {
	const keys = key.split('.');
	let value = translations[$locale];
	for (const k of keys) value = value?.[k];
	if (value === undefined && $locale !== 'it') {
		value = translations['it'];
		for (const k of keys) value = value?.[k];
	}
	return value;
});
```

Because values may be `undefined`, some pages render translated HTML with
`{@html $t('...')}` (e.g. the hero title) — keep translation values trusted/static.

### Direction (RTL)

The root layout reacts to `dir` and sets `document.documentElement.dir`:

```ts
// +layout.svelte
$effect(() => {
	document.documentElement.lang = $locale;
	document.documentElement.dir = $dir; // 'rtl' for ar
});
```

## Locales

Translation files live in [`src/lib/i18n/locales`](../src/lib/i18n/locales):

| Code | File      | Notes                                      |
| ---- | --------- | ------------------------------------------ |
| `it` | `it.json` | **Default & fallback** language (Italian). |
| `en` | `en.json` | English.                                   |
| `ru` | `ru.json` | Russian.                                   |
| `fr` | `fr.json` | French.                                    |
| `de` | `de.json` | German.                                    |
| `es` | `es.json` | Spanish.                                   |
| `ar` | `ar.json` | Arabic (renders RTL).                      |
| `zh` | `zh.json` | Chinese.                                   |

> **Important:** all eight files are imported and available to `t`, but the UI's
> active language list is currently limited by `export const locales = ['it', 'en', 'ru'];`
> in `index.ts`. The `Navbar` builds its switcher from `locales`, so only those three
> are user-selectable by default even though more translation files exist. To expose
> another language, add its code to the `locales` array.

## Key namespaces

Each locale JSON is organized into top-level sections, including:

```
common, nav, megamenu, hero, booking, home, footer,
rooms, rooms_data, rooms_amenities, rooms_specs,
ristorante, wellness, sport, experiences, struttura, posizione,
sostenibilita, meteo, eventi, kids_club,
offers_page, promo, restart_page, torgnon_offer_page,
aosta_romana_offer_page, forte_bard_offer_page, offer_lead_form,
degustazione_page, ciaspolate_page, yoga_page, guide_page, massaggi_page,
policy, cookie_policy, cookie_banner, termini
```

## Editing / adding translations

- **Edit copy:** find the key under the relevant section in `it.json` (and the other
  locale files) and update the value.
- **Add a new key:** add it to **every** locale file you support — at minimum `it.json`
  (the fallback). Missing keys silently fall back to Italian, then to `undefined`.
- **Add a new language:**
  1. Create `src/lib/i18n/locales/<code>.json`.
  2. Import it in `index.ts` and add it to the `translations` map.
  3. Add `<code>` to the `locales` array to show it in the switcher.
  4. If it's an RTL language, extend the `dir` logic accordingly.
  5. Add a display label in `Navbar.svelte`'s `langLabels`.
