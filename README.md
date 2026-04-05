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
CLOUDINARY_API_SECRET=
```

- `PUBLIC_CLOUDINARY_CLOUD_NAME` is required for delivery URLs.
- `PUBLIC_CLOUDINARY_API_KEY` and `PUBLIC_CLOUDINARY_UPLOAD_PRESET` are required for unsigned browser uploads.
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
