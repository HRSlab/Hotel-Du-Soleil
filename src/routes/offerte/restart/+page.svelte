<script lang="ts">
	import { t } from '$lib/i18n';
	import { RESTART_PROMOTION_ID, getPromotionUrl } from '$lib/config/booking';

	const restartPromoUrl = getPromotionUrl(RESTART_PROMOTION_ID, 'restart_offer_page');
</script>

<svelte:head>
	<title>{$t('restart_page.head_title')}</title>
	<meta name="description" content={$t('restart_page.meta_description')} />
</svelte:head>

<header class="relative h-[88vh] w-full overflow-hidden bg-[#1a1a1a]">
	<div class="absolute inset-0">
		<img
			src="https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=2200&auto=format&fit=crop"
			alt={$t('restart_page.hero_alt')}
			class="h-full w-full object-cover opacity-55"
		/>
		<div class="absolute inset-0 bg-linear-to-b from-black/85 via-black/30 to-alpine-bg"></div>
	</div>

	<div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-28 text-center">
		<span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase">
			{$t('restart_page.hero_tag')}
		</span>
		<h1 class="font-serif text-5xl leading-tight font-light text-white md:text-8xl">
			{$t('restart_page.hero_title_line1')}
			<span class="mt-2 block text-3xl italic md:text-5xl"
				>{$t('restart_page.hero_title_line2')}</span
			>
		</h1>
		<p class="mt-6 max-w-2xl text-sm font-light text-white/60 md:text-base">
			{$t('restart_page.hero_intro')}
		</p>
	</div>
</header>

<section class="bg-alpine-bg px-6 py-24 lg:py-32">
	<div class="mx-auto grid max-w-7xl grid-cols-1 items-center gap-14 lg:grid-cols-2 lg:gap-24">
		<div>
			<div class="mb-10 h-20 w-px bg-alpine-border"></div>
			<h2 class="font-serif text-4xl leading-tight text-alpine-text md:text-6xl">
				{$t('restart_page.essence_title')}
			</h2>
			<p class="mt-6 text-sm leading-relaxed font-light text-alpine-muted md:text-base">
				{$t('restart_page.essence_p1')}
			</p>
			<p class="mt-4 text-sm leading-relaxed font-light text-alpine-muted md:text-base">
				{$t('restart_page.essence_p2')}
			</p>

			<div class="mt-10 border border-alpine-border bg-white p-8">
				<span class="text-[10px] font-bold tracking-[0.22em] text-alpine-muted uppercase"
					>{$t('restart_page.offer_tag')}</span
				>
				<p class="mt-4 text-sm leading-relaxed font-light text-alpine-muted">
					{$t('restart_page.offer_intro')}
				</p>
				<div class="mt-4 flex flex-wrap items-end gap-x-3 gap-y-1">
					<span class="font-serif text-5xl text-alpine-text">EUR 94,00</span>
					<span class="pb-2 text-sm font-light text-alpine-muted"
						>{$t('restart_page.offer_price_unit')}</span
					>
				</div>
				<ul class="mt-4 space-y-2 text-sm leading-relaxed text-alpine-muted">
					<li class="text-alpine-text">• {$t('restart_page.offer_saving')}</li>
				</ul>
			</div>
		</div>

		<div>
			<div class="grid grid-cols-1 gap-6">
				<article class="border border-alpine-border bg-white p-7">
					<span class="text-[10px] font-bold tracking-[0.2em] text-alpine-gold uppercase">01</span>
					<h3 class="mt-3 font-serif text-3xl text-alpine-text">{$t('restart_page.exp1_title')}</h3>
					<p class="mt-3 text-sm leading-relaxed font-light text-alpine-muted">
						{$t('restart_page.exp1_text')}
					</p>
				</article>

				<article class="border border-alpine-gold/40 bg-alpine-text p-7 text-white">
					<span class="text-[10px] font-bold tracking-[0.2em] text-alpine-gold uppercase">02</span>
					<h3 class="mt-3 font-serif text-3xl">{$t('restart_page.exp2_title')}</h3>
					<p class="mt-3 text-sm leading-relaxed font-light text-white/75">
						{$t('restart_page.exp2_text')}
					</p>
				</article>

				<article class="border border-alpine-border bg-white p-7">
					<span class="text-[10px] font-bold tracking-[0.2em] text-alpine-gold uppercase">03</span>
					<h3 class="mt-3 font-serif text-3xl text-alpine-text">{$t('restart_page.exp3_title')}</h3>
					<p class="mt-3 text-sm leading-relaxed font-light text-alpine-muted">
						{$t('restart_page.exp3_text')}
					</p>
				</article>
			</div>
		</div>
	</div>
</section>

<section class="bg-white px-6 pb-24">
	<div class="mx-auto max-w-7xl text-center">
		<a
			href={restartPromoUrl}
			target="_blank"
			rel="noopener noreferrer"
			class="inline-flex items-center justify-center bg-alpine-text px-10 py-4 text-[11px] font-bold tracking-[0.2em] text-white uppercase transition-colors hover:bg-alpine-gold"
		>
			{$t('restart_page.cta')}
		</a>
	</div>
</section>
