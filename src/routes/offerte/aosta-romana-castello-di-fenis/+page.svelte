<script lang="ts">
	import { t } from '$lib/i18n';
	import OfferLeadForm from '$lib/components/OfferLeadForm.svelte';
	import { getAostaRomanaPromotionUrl } from '$lib/config/booking';

	const canonicalUrl = 'https://www.hotel-du-soleil.it/offerte/aosta-romana-castello-di-fenis';
	const bookingUrl = getAostaRomanaPromotionUrl('aosta_romana_offer_page');
</script>

<svelte:head>
	<title>{$t('aosta_romana_offer_page.head_title')}</title>
	<meta name="description" content={$t('aosta_romana_offer_page.meta_description')} />
	<link rel="canonical" href={canonicalUrl} />
	<meta property="og:title" content={$t('aosta_romana_offer_page.head_title')} />
	<meta property="og:description" content={$t('aosta_romana_offer_page.og_description')} />
	<meta property="og:type" content="website" />
	<meta property="og:url" content={canonicalUrl} />
	<meta name="twitter:card" content="summary_large_image" />
	<script type="application/ld+json">
{JSON.stringify({
	'@context': 'https://schema.org',
	'@type': 'Offer',
	name: $t('aosta_romana_offer_page.schema_name'),
	description: $t('aosta_romana_offer_page.schema_description'),
	price: '580.00',
	priceCurrency: 'EUR',
	availability: 'https://schema.org/InStock',
	url: canonicalUrl,
	itemOffered: {
		'@type': 'Trip',
		name: $t('aosta_romana_offer_page.schema_name'),
		itinerary: [
			$t('aosta_romana_offer_page.day1_schema'),
			$t('aosta_romana_offer_page.day2_schema'),
			$t('aosta_romana_offer_page.day3_schema'),
			$t('aosta_romana_offer_page.day4_schema')
		]
	}
})}
	</script>
</svelte:head>

<header class="relative h-[82vh] w-full overflow-hidden bg-[#1a1a1a]">
	<div class="absolute inset-0">
		<img
			src="https://www.villageparadis.it/immagini/arco-d-augusto-aosta-romana-villageparadis-agriturismo_ea.jpg"
			alt={$t('aosta_romana_offer_page.hero_alt')}
			class="h-full w-full object-cover opacity-55"
		/>
		<div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/35 to-alpine-bg"></div>
	</div>

	<div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
		<span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase"
			>{$t('aosta_romana_offer_page.hero_tag')}</span
		>
		<h1 class="font-serif text-5xl leading-tight font-light text-white md:text-7xl">
			{$t('aosta_romana_offer_page.hero_title')}
		</h1>
		<p class="mt-6 max-w-2xl text-sm font-light text-white/65 md:text-base">
			{$t('aosta_romana_offer_page.hero_intro')}
		</p>
	</div>
</header>

<section class="bg-alpine-bg px-6 py-24">
	<div class="mx-auto grid max-w-7xl grid-cols-1 gap-12 lg:grid-cols-2">
		<div>
			<h2 class="font-serif text-4xl text-alpine-text md:text-5xl">
				{$t('aosta_romana_offer_page.section_title')}
			</h2>
			<p class="mt-6 text-sm leading-relaxed font-light text-alpine-muted md:text-base">
				{$t('aosta_romana_offer_page.section_text')}
			</p>
			<div class="mt-10 border border-alpine-border bg-white p-8">
				<span class="text-[10px] font-bold tracking-[0.2em] text-alpine-muted uppercase"
					>{$t('aosta_romana_offer_page.price_label')}</span
				>
				<p class="mt-3 font-serif text-5xl text-alpine-text">EUR 580,00</p>
				<p class="text-sm text-alpine-muted">{$t('aosta_romana_offer_page.price_guests')}</p>
				<p class="mt-2 text-sm text-alpine-muted">{$t('aosta_romana_offer_page.price_unit')}</p>
			</div>
		</div>

		<div class="space-y-4">
			<article class="border border-alpine-border bg-white p-6">
				<h3 class="font-serif text-3xl text-alpine-text">
					{$t('aosta_romana_offer_page.highlights_title')}
				</h3>
				<ul class="mt-4 space-y-3 text-sm font-light text-alpine-muted">
					<li>{$t('aosta_romana_offer_page.highlight_1')}</li>
					<li>{$t('aosta_romana_offer_page.highlight_2')}</li>
					<li>{$t('aosta_romana_offer_page.highlight_3')}</li>
					<li>{$t('aosta_romana_offer_page.highlight_4')}</li>
				</ul>
			</article>
			<article class="border border-alpine-border bg-white p-6">
				<h3 class="font-serif text-3xl text-alpine-text">
					{$t('aosta_romana_offer_page.includes_title')}
				</h3>
				<p class="mt-3 text-sm font-light text-alpine-muted">
					{$t('aosta_romana_offer_page.includes_text')}
				</p>
				<p class="mt-3 text-sm font-light text-alpine-muted">
					{$t('aosta_romana_offer_page.includes_note')}
				</p>
			</article>
		</div>
	</div>
</section>

<section class="bg-white px-6 py-20">
	<div class="mx-auto max-w-7xl">
		<div class="mb-10 border-b border-alpine-border pb-6">
			<h2 class="font-serif text-4xl text-alpine-text md:text-5xl">
				{$t('aosta_romana_offer_page.itinerary_title')}
			</h2>
		</div>

		<div class="grid grid-cols-1 gap-6 lg:grid-cols-2">
			<article class="border border-alpine-border bg-alpine-bg p-7">
				<span class="text-[10px] font-bold tracking-[0.2em] text-alpine-gold uppercase"
					>{$t('aosta_romana_offer_page.day1_label')}</span
				>
				<h3 class="mt-3 font-serif text-3xl text-alpine-text">
					{$t('aosta_romana_offer_page.day1_title')}
				</h3>
				<p class="mt-3 text-sm font-light text-alpine-muted">
					{$t('aosta_romana_offer_page.day1_text')}
				</p>
			</article>

			<article class="border border-alpine-border bg-white p-7">
				<span class="text-[10px] font-bold tracking-[0.2em] text-alpine-gold uppercase"
					>{$t('aosta_romana_offer_page.day2_label')}</span
				>
				<h3 class="mt-3 font-serif text-3xl text-alpine-text">
					{$t('aosta_romana_offer_page.day2_title')}
				</h3>
				<p class="mt-3 text-sm font-light text-alpine-muted">
					{$t('aosta_romana_offer_page.day2_text')}
				</p>
			</article>

			<article class="border border-alpine-border bg-white p-7">
				<span class="text-[10px] font-bold tracking-[0.2em] text-alpine-gold uppercase"
					>{$t('aosta_romana_offer_page.day3_label')}</span
				>
				<h3 class="mt-3 font-serif text-3xl text-alpine-text">
					{$t('aosta_romana_offer_page.day3_title')}
				</h3>
				<p class="mt-3 text-sm font-light text-alpine-muted">
					{$t('aosta_romana_offer_page.day3_text')}
				</p>
			</article>

			<article class="border border-alpine-border bg-alpine-text p-7 text-white">
				<span class="text-[10px] font-bold tracking-[0.2em] text-alpine-gold uppercase"
					>{$t('aosta_romana_offer_page.day4_label')}</span
				>
				<h3 class="mt-3 font-serif text-3xl">{$t('aosta_romana_offer_page.day4_title')}</h3>
				<p class="mt-3 text-sm font-light text-white/75">
					{$t('aosta_romana_offer_page.day4_text')}
				</p>
			</article>
		</div>
	</div>
</section>

<section class="bg-white px-6 pb-24">
	<div class="mx-auto max-w-7xl text-center">
		<a
			href={bookingUrl}
			target="_blank"
			rel="noopener noreferrer"
			class="inline-flex items-center justify-center bg-alpine-text px-10 py-4 text-[11px] font-bold tracking-[0.2em] text-white uppercase transition-colors hover:bg-alpine-gold"
		>
			{$t('aosta_romana_offer_page.booking_cta')}
		</a>
		<p class="mt-4 text-sm font-light text-alpine-muted">
			{$t('aosta_romana_offer_page.booking_caption')}
		</p>
	</div>
</section>

<OfferLeadForm
	title={$t('aosta_romana_offer_page.form_title')}
	subtitle={$t('aosta_romana_offer_page.form_subtitle')}
	notesPlaceholder={$t('aosta_romana_offer_page.form_notes')}
	successText={$t('aosta_romana_offer_page.form_success')}
/>
