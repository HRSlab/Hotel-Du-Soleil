# Hotel Du Soleil — Documentation

This folder contains the full technical documentation for the **Hotel Du Soleil**
website (`www.hotel-du-soleil.it`), a multilingual marketing site for an alpine
hotel in Torgnon, Valle d'Aosta, built with **SvelteKit 2 + Svelte 5 + Tailwind CSS 4**.

## Contents

| Document                                                 | Description                                                                                                 |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| [Architecture](./architecture.md)                        | High-level overview of the tech stack, rendering model, request lifecycle, and how the pieces fit together. |
| [Project structure](./project-structure.md)              | Annotated directory and file map of the repository.                                                         |
| [Development guide](./development.md)                    | Local setup, environment variables, npm scripts, linting/formatting, and common workflows.                  |
| [Routes & pages](./routes.md)                            | Complete map of the file-based routes, the section-hiding redirect logic, and SEO endpoints.                |
| [Components](./components.md)                            | Catalog of the reusable Svelte components in `src/lib/components`, with their props and responsibilities.   |
| [Internationalization (i18n)](./internationalization.md) | The custom translation store, supported locales, RTL handling, and how to add/edit translations.            |
| [Booking integration](./booking.md)                      | How the Slope.it booking engine and promotion deep-links are wired, including UTM tracking.                 |
| [Cloudinary media pipeline](./cloudinary.md)             | Image/video delivery, the runtime rewrite hook, and the manifest sync script.                               |
| [Analytics & cookie consent](./analytics-and-consent.md) | Google Analytics 4 (Consent Mode v2), the cookie banner, and the custom event taxonomy.                     |
| [Weather feature](./weather.md)                          | The `/meteo` page (Open-Meteo) and the home/section weather widgets.                                        |
| [Configuration reference](./configuration.md)            | Every config file (`svelte.config.js`, `vite.config.ts`, `tsconfig.json`, ESLint, Prettier, Netlify).       |
| [Content management](./content.md)                       | Where page content lives: room data, offers, the to-do backlog, and the content-generation scripts.         |
| [Deployment](./deployment.md)                            | How the site is built and deployed (Netlify + `adapter-auto`).                                              |

## Quick links

- **Production site:** https://www.hotel-du-soleil.it
- **Booking engine:** https://booking.slope.it
- **Framework docs:** [SvelteKit](https://svelte.dev/docs/kit), [Svelte 5 runes](https://svelte.dev/docs/svelte/what-are-runes), [Tailwind CSS 4](https://tailwindcss.com/docs)

> New to the codebase? Start with [Architecture](./architecture.md), then skim
> [Project structure](./project-structure.md) and the [Development guide](./development.md).
