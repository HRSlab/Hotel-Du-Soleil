import type { RequestHandler } from '@sveltejs/kit';

const SITE_URL = 'https://www.hotel-du-soleil.it';

const routes = [
	'/',
	'/camere',
	'/ristorante',
	'/wellness',
	'/sport',
	'/esperienze',
	'/offerte',
	'/offerte/restart',
	'/offerte/torgnon-hiking-adventure',
	'/offerte/forte-di-bard-gourmet-escape',
	'/offerte/aosta-romana-castello-di-fenis',
	'/offerte/workation-alpino',
	'/offerte/family-base-camp',
	'/offerte/family-mountain-camp',
	'/offerte/summit-taste',
	'/offerte/wheels-relax',
	'/offerte/orizzonti-silenzio',
	'/struttura',
	'/posizione',
	'/sostenibilita',
	'/storia',
	'/meteo',
	'/eventi',
	'/kids-club',
	'/policy',
	'/cookie-policy',
	'/termini'
];

export const GET: RequestHandler = async () => {
	const lastmod = new Date().toISOString().split('T')[0];
	const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${routes
	.map(
		(path) => `  <url>
    <loc>${SITE_URL}${path}</loc>
    <lastmod>${lastmod}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>${path === '/' ? '1.0' : path === '/offerte' ? '0.9' : '0.8'}</priority>
  </url>`
	)
	.join('\n')}
</urlset>`;

	return new Response(xml, {
		headers: {
			'Content-Type': 'application/xml; charset=utf-8',
			'Cache-Control': 'max-age=0, s-maxage=3600'
		}
	});
};
