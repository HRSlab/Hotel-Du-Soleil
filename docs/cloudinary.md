# Cloudinary media pipeline

Images and videos can be served either from the local `static/imgs/` folder or from
**Cloudinary** (a media CDN with on-the-fly transformations). The integration is
designed to be **opt-in and non-breaking**: with no configuration the site keeps using
local assets, and any unmapped asset falls back to its local file.

## Pieces

| File                                                                                            | Role                                                                                                        |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| [`src/lib/cloudinary.ts`](../src/lib/cloudinary.ts)                                             | Browser-safe URL building, config flags, manifest lookup, unsigned-upload helpers. Re-exported from `$lib`. |
| [`src/lib/server/cloudinary.ts`](../src/lib/server/cloudinary.ts)                               | Server-only signed operations (uses the API secret).                                                        |
| [`src/lib/components/CloudinaryRuntime.svelte`](../src/lib/components/CloudinaryRuntime.svelte) | Runtime DOM hook that rewrites `/imgs/...` URLs to Cloudinary when enabled.                                 |
| [`src/lib/generated/cloudinary-manifest.json`](../src/lib/generated/cloudinary-manifest.json)   | Generated map of local paths → Cloudinary `{ publicId, resourceType, version, ... }`.                       |
| [`scripts/sync-cloudinary-manifest.mjs`](../scripts/sync-cloudinary-manifest.mjs)               | Builds the manifest from your Cloudinary account.                                                           |

## Environment variables

Set these in `.env` (template in `.env.example`):

| Variable                            | Scope           | Meaning                                                                                 |
| ----------------------------------- | --------------- | --------------------------------------------------------------------------------------- |
| `PUBLIC_CLOUDINARY_CLOUD_NAME`      | public          | Required for any delivery URL.                                                          |
| `PUBLIC_CLOUDINARY_API_KEY`         | public          | Required for unsigned browser uploads.                                                  |
| `PUBLIC_CLOUDINARY_UPLOAD_PRESET`   | public          | Required for unsigned browser uploads.                                                  |
| `PUBLIC_CLOUDINARY_ENABLE_DELIVERY` | public          | `'true'` turns on automatic rewriting of local `/imgs/...` paths. Default `false`.      |
| `PUBLIC_CLOUDINARY_BASE_FOLDER`     | public          | Folder prefix used when mapping local assets to public IDs (default `hotel-du-soleil`). |
| `CLOUDINARY_API_SECRET`             | **server-only** | Used for signed uploads/admin operations. Never sent to the client.                     |

Derived config flags exposed by `cloudinary.ts`:

- `hasCloudinaryDelivery` — a cloud name is set.
- `isCloudinaryDeliveryEnabled` — cloud name set **and** delivery flag `true`.
- `hasCloudinaryUnsignedUpload` — cloud name + API key + upload preset are set.

## Building delivery URLs

```ts
import { getCloudinaryDeliveryUrl, resolveCloudinaryUrl } from '$lib';

// Explicit public ID + transformations
const heroUrl = getCloudinaryDeliveryUrl('hotel-du-soleil/home/hero', 'image', {
	width: 1600,
	height: 900,
	crop: 'fill',
	quality: 'auto',
	format: 'auto'
});

// Resolve a value that might be a local path, a remote URL, a public ID, or an object
const src = resolveCloudinaryUrl({
	publicId: 'hotel-du-soleil/rooms/matrimoniale-hero',
	fallbackSrc: '/imgs/Rooms/matrimoniale-superior-hero-1.webp'
});
```

`getCloudinaryDeliveryUrl(publicId, resourceType, options, config)` assembles
`https://res.cloudinary.com/<cloud>/<type>/upload/<transforms>/v<version>/<publicId>`.
The supported transformation options map to Cloudinary's URL params (e.g. `width` →
`w_`, `crop` → `c_`, `quality` → `q_`, `gravity` → `g_`, plus `custom: string[]` for
raw segments).

### `resolveCloudinaryUrl` resolution order

1. A full `http(s)://` string → returned unchanged.
2. A `/...` path → only rewritten if delivery is enabled **and** it's a `/imgs/...`
   asset present in the manifest; otherwise the local path is returned.
3. A bare string (treated as a public ID) → a delivery URL if a cloud name is set.
4. An object with `publicId` → a delivery URL (or `fallbackSrc` when delivery is off).
5. Otherwise `fallbackSrc`, or throws if neither is available.

## Automatic runtime rewriting

[`CloudinaryRuntime.svelte`](../src/lib/components/CloudinaryRuntime.svelte) is
mounted globally in the root layout. When `PUBLIC_CLOUDINARY_ENABLE_DELIVERY=true`,
it walks the DOM and rewrites `img[src]`, `source[src]`, and `poster` attributes
through `resolveCloudinaryUrl`, and uses a `MutationObserver` to handle nodes added
later. This means existing pages keep using `/imgs/...` markup unchanged — delivery
is swapped in transparently. Assets not in the manifest fall back to the local file.

## Manifest sync workflow

After uploading new files to Cloudinary, regenerate the manifest so the runtime can
map local paths to real public IDs/versions:

```sh
npm run cloudinary:sync
```

[`scripts/sync-cloudinary-manifest.mjs`](../scripts/sync-cloudinary-manifest.mjs):

1. Loads Cloudinary credentials from `.env` (throws if missing).
2. Fetches **all** image and video resources from your Cloudinary account.
3. Walks `static/imgs/**` and matches each local file to a resource by a
   "normalized stem" (lowercased, extension and trailing `_xxxxxx` hash removed,
   non-alphanumerics collapsed to `-`).
4. Writes `src/lib/generated/cloudinary-manifest.json` and prints a summary
   (counts of local assets, cloud assets, mapped, and missed).

## Uploads

- **Server (signed):** use [`src/lib/server/cloudinary.ts`](../src/lib/server/cloudinary.ts).
  It configures the SDK only when full server config is present, and exposes
  `cloudinary`, `assertCloudinaryServerConfig()`, and `signCloudinaryParams()`.
- **Browser (unsigned):** `getUnsignedCloudinaryUploadUrl()` and
  `getUnsignedCloudinaryUploadFields()` from `cloudinary.ts` build a direct upload
  endpoint + form fields using the public API key and upload preset.

## Local image optimization (separate from Cloudinary)

`npm run optimize-images` runs [`scripts/optimize-images.js`](../scripts/optimize-images.js),
which converts non-WebP images under `static/imgs` to WebP (quality 80) with `sharp`,
skipping files that are already WebP or up to date. This is independent of Cloudinary
and is about shrinking the locally-committed assets.
