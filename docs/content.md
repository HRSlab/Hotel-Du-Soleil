# Content management

Most page copy is translatable text in the i18n JSON files (see
[Internationalization](./internationalization.md)). This page covers the **structured
content** that lives in code and the tooling used to author certain pages.

## Room catalog — `src/lib/rooms.ts`

[`src/lib/rooms.ts`](../src/lib/rooms.ts) exports the room data consumed by the rooms
pages (`/camere`, `/camere/[slug]`) and `RoomCarousel`.

- `commonAmenities: string[]` — amenities shared by all rooms (TV, Wi-Fi, ski box,
  parking, half-board, etc.), spread into each room's `amenities`.
- `rooms: Record<string, Room>` — keyed by slug. Current keys:
  `matrimoniale`, `tripla`, `quadrupla_standard`, `familiare`.

Each room has:

```ts
{
  name: string;          // display name
  slug: string;          // matches the [slug] route param
  description: string;   // long description (may contain \n paragraphs)
  price: string;         // e.g. 'da €120 / notte'
  size: string;          // e.g. '18-20 mq'
  occupancy: string;     // e.g. '2 ospiti'
  bedType: string;
  highlight: string;
  image: string;         // hero/card image path under /imgs/...
  amenities: string[];
  gallery: string[];     // image paths
}
```

> The `rooms` value is typed `Record<string, any>` — when adding fields, prefer
> tightening this to a proper `Room` interface.

### Adding or editing a room

1. Add/edit an entry in `rooms` (the key is the URL slug).
2. Point `image`/`gallery` at files in `static/imgs/...` (and re-run
   `npm run optimize-images` / `npm run cloudinary:sync` if needed).
3. The `/camere/[slug]` page resolves content by slug automatically.

## Offers / promotions

Offer **pages** live under `src/routes/offerte/<slug>/+page.svelte` and their
booking deep-links/IDs live in [`src/lib/config/booking.ts`](../src/lib/config/booking.ts).
The featured lists shown in `OffersCarousel` and `PromoCarousel` are defined inline
in those components. See [Booking](./booking.md) for the full add-an-offer checklist.

## Backlog — `to-do.md`

[`to-do.md`](../to-do.md) is a free-form content/feature backlog (e.g. translations
still needed, images/content to add for various sections, legal pages). It is not
wired into any tooling — it's a human checklist.

## Content-generation scripts (`scripts/*.py`)

Several Python scripts were used to generate or patch specific experience/wellness
pages programmatically:

| Script                                         | Target                   |
| ---------------------------------------------- | ------------------------ |
| `fix_ciaspolate.py`                            | `/esperienze/ciaspolate` |
| `fix_yoga.py`, `fix_yoga2.py`, `write_yoga.py` | `/esperienze/yoga`       |
| `write_guide.py`                               | `/esperienze/guide`      |
| `write_massaggi.py`                            | `/wellness/massaggi`     |

These are **one-off authoring helpers**, run manually with Python (not part of the
npm build). They write Svelte page content. Treat them as historical/utility scripts;
day-to-day edits are made directly in the `.svelte` files and the i18n JSON.

## Asset conventions

- Public images/videos go in `static/imgs/...` and are referenced as `/imgs/...`.
- Prefer **WebP** (run `npm run optimize-images` to convert).
- When using Cloudinary delivery, keep the manifest in sync
  (`npm run cloudinary:sync`). See [Cloudinary](./cloudinary.md).
