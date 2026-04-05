# sv

Everything you need to build a Svelte project, powered by [`sv`](https://github.com/sveltejs/cli).

## Creating a project

If you're seeing this, you've probably already done this step. Congrats!

```sh
# create a new project
npx sv create my-app
```

To recreate this project with the same configuration:

```sh
# recreate this project
npx sv@0.12.8 create --template minimal --types ts --add tailwindcss="plugins:none" prettier eslint --install npm ./
```

## Developing

Once you've created a project and installed dependencies with `npm install` (or `pnpm install` or `yarn`), start a development server:

```sh
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

## Building

To create a production version of your app:

```sh
npm run build
```

You can preview the production build with `npm run preview`.

> To deploy your app, you may need to install an [adapter](https://svelte.dev/docs/kit/adapters) for your target environment.

## Cloudinary

Cloudinary is wired into the SvelteKit app with public env vars for browser-safe delivery and a server-only helper for signed operations.

### Environment variables

Copy the values you need into `.env`:

```env
PUBLIC_CLOUDINARY_CLOUD_NAME=
PUBLIC_CLOUDINARY_API_KEY=
PUBLIC_CLOUDINARY_UPLOAD_PRESET=
PUBLIC_CLOUDINARY_ENABLE_DELIVERY=false
PUBLIC_CLOUDINARY_BASE_FOLDER=hotel-du-soleil
CLOUDINARY_API_SECRET=
```

- `PUBLIC_CLOUDINARY_CLOUD_NAME` is required for delivery URLs.
- `PUBLIC_CLOUDINARY_API_KEY` and `PUBLIC_CLOUDINARY_UPLOAD_PRESET` are required for unsigned browser uploads.
- `PUBLIC_CLOUDINARY_ENABLE_DELIVERY=true` turns on automatic rewriting of local `/imgs/...` paths to Cloudinary delivery URLs.
- `PUBLIC_CLOUDINARY_BASE_FOLDER` defines the folder prefix used when local assets are mapped to Cloudinary public IDs.
- `CLOUDINARY_API_SECRET` is server-only and must never be sent to the client.

### Browser usage

Use `$lib` exports from `src/lib/cloudinary.ts` to build delivery URLs or upload forms:

```ts
import { getCloudinaryDeliveryUrl, resolveCloudinaryUrl } from '$lib';

const heroUrl = getCloudinaryDeliveryUrl('hotel-du-soleil/home/hero', 'image', {
	width: 1600,
	height: 900,
	crop: 'fill',
	quality: 'auto',
	format: 'auto'
});

const src = resolveCloudinaryUrl({
	publicId: 'hotel-du-soleil/rooms/matrimoniale-hero',
	fallbackSrc: '/imgs/Rooms/matrimoniale-superior-hero-1.webp'
});
```

### Server usage

Use `src/lib/server/cloudinary.ts` for signed uploads or admin-style operations:

```ts
import { cloudinary, signCloudinaryParams } from '$lib/server/cloudinary';

const signature = signCloudinaryParams({
	folder: 'hotel-du-soleil/uploads',
	timestamp: Math.floor(Date.now() / 1000)
});

const result = await cloudinary.uploader.upload('/absolute/path/to/file.webp');
```

Existing image paths in the app were left unchanged. To migrate page assets to Cloudinary delivery, provide the public IDs or the folder naming convention used in your Cloudinary account.

### Automatic local asset mapping

The app now includes a global runtime hook in `src/lib/components/CloudinaryRuntime.svelte`.

- When `PUBLIC_CLOUDINARY_ENABLE_DELIVERY=false`, the site keeps using the current local `/imgs/...` files.
- When `PUBLIC_CLOUDINARY_ENABLE_DELIVERY=true`, local image, video source, and poster URLs are rewritten to Cloudinary on the client.
- The default mapping turns `/imgs/Rooms/matrimoniale-superior-hero-1.webp` into `hotel-du-soleil/imgs/Rooms/matrimoniale-superior-hero-1`.

That means you can upload assets later using the same relative path structure under your Cloudinary base folder, then switch delivery on without editing every page.
