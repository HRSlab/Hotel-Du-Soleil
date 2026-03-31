<script lang="ts">
	import { t } from '$lib/i18n';

	import BookingBar from '$lib/components/BookingBar.svelte';
	import WeatherWidget from '$lib/components/WeatherWidget.svelte';
	import RoomCarousel from '$lib/components/RoomCarousel.svelte';
	import { Map, Utensils, ShieldCheck } from 'lucide-svelte';
</script>

<svelte:head>
	<title>Chalet du Soleil | Modern Alpine Retreat</title>
</svelte:head>

<!-- HERO SECTION -->
<header class="relative h-screen w-full overflow-hidden bg-[#1a1a1a]">
	<div class="absolute inset-0">
		<img
			src="/imgs/exterior-snow-back-2026.webp"
			alt="Chalet du Soleil hero background"
			class="h-full w-full object-cover md:hidden"
		/>
		<video
			autoplay
			loop
			muted
			playsinline
			preload="metadata"
			poster="/imgs/deer-dish-hero.webp"
			class="absolute inset-0 hidden h-full w-full object-cover opacity-100 md:block"
		>
			<source src="/imgs/fontina-dop-hero.mp4" type="video/mp4" />
		</video>
		<div class="absolute inset-0 bg-black/40"></div>
		<div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/40 to-alpine-bg"></div>
	</div>

	<div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-32 text-center">
		<div class="fade-up-element">
			<span
				class="mb-6 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs"
			>
				{$t('hero.subtitle')}
			</span>
			<h2
				class="mb-10 font-serif text-5xl leading-tight font-light text-white md:text-7xl lg:text-8xl"
			>
				<!-- eslint-disable-next-line svelte/no-at-html-tags -->
				{@html $t('hero.title')}
			</h2>
		</div>
	</div>
</header>

<!-- BOOKING BAR -->
<BookingBar />

<!-- WEATHER & INFO -->
<div class="mx-auto flex max-w-7xl justify-center px-6 py-12">
	<WeatherWidget />
</div>

<!-- FILOSOFIA -->
<section class="bg-alpine-bg px-6 py-20 lg:py-32">
	<div class="fade-up-element mx-auto max-w-3xl text-center">
		<div class="deco-line mb-12"></div>
		<h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-5xl">
			{$t('home.philosophy_title')}
		</h3>
		<p
			class="mx-auto mb-12 max-w-xl text-sm leading-relaxed font-light text-alpine-muted md:text-base"
		>
			{$t('home.philosophy_text')}
		</p>
		<a
			href="/struttura"
			class="border-b border-alpine-text pb-1 text-[11px] font-bold tracking-[0.2em] text-alpine-text uppercase transition-colors hover:border-alpine-gold hover:text-alpine-gold"
		>
			{$t('home.philosophy_cta')}
		</a>
	</div>
</section>

<!-- LE CAMERE (Grid Editoriale) -->
<section class="mx-auto max-w-7xl px-6 py-24">
	<div
		class="fade-up-element mb-16 flex flex-col items-end justify-between border-b border-alpine-border pb-6 md:flex-row"
	>
		<h2 class="font-serif text-4xl text-alpine-text md:text-5xl">{$t('home.rooms_title')}</h2>
		<p class="mt-4 text-xs font-bold tracking-widest text-alpine-muted uppercase md:mt-0">
			{$t('home.rooms_subtitle')}
		</p>
	</div>

	<RoomCarousel />
</section>

<!-- EDITORIAL SECTIONS (Restaurant, Wellness, Activities) -->
<section class="bg-white py-24 lg:py-48">
	<div class="mx-auto max-w-7xl space-y-32 px-6 lg:space-y-64">
		<!-- Part 1: Ristorante -->
		<div class="grid grid-cols-1 items-center gap-12 lg:grid-cols-2 lg:gap-24">
			<div class="fade-up-element order-2 lg:order-1">
				<div class="relative aspect-4/5 overflow-hidden rounded-sm shadow-2xl lg:aspect-square">
					<img
						src="/imgs/deer-dish-hero.webp"
						alt="Ristorante Chalet du Soleil"
						class="h-full w-full object-cover transition-transform duration-700 hover:scale-105"
					/>
				</div>
			</div>
			<div class="fade-up-element order-1 lg:order-2">
				<span
					class="mb-4 block text-[10px] font-bold tracking-[0.3em] text-alpine-gold uppercase md:text-xs"
				>
					{#if $t('nav.restaurant')}
						{$t('nav.restaurant')}
					{/if}
				</span>
				<h2 class="mb-8 font-serif text-4xl text-alpine-text lg:text-6xl">
					{$t('home.restaurant_section_title')}
				</h2>
				<p class="mb-10 max-w-lg text-sm leading-relaxed font-light text-alpine-muted lg:text-lg">
					{$t('home.restaurant_section_text')}
				</p>
				<a
					href="/ristorante"
					class="inline-block border-b border-alpine-text pb-1 text-[11px] font-bold tracking-[0.2em] text-alpine-text uppercase transition-colors hover:border-alpine-gold hover:text-alpine-gold"
				>
					Scopri la cucina
				</a>
			</div>
		</div>

		<!-- Part 2: Wellness -->
		<div class="grid grid-cols-1 items-center gap-12 lg:grid-cols-2 lg:gap-24">
			<div class="fade-up-element lg:pr-12">
				<span
					class="mb-4 block text-[10px] font-bold tracking-[0.3em] text-alpine-gold uppercase md:text-xs"
				>
					{#if $t('nav.wellness')}
						{$t('nav.wellness')}
					{/if}
				</span>
				<h2 class="mb-8 font-serif text-4xl text-alpine-text lg:text-6xl">
					{$t('home.wellness_section_title')}
				</h2>
				<p class="mb-10 max-w-lg text-sm leading-relaxed font-light text-alpine-muted lg:text-lg">
					{$t('home.wellness_section_text')}
				</p>
				<a
					href="/wellness"
					class="inline-block border-b border-alpine-text pb-1 text-[11px] font-bold tracking-[0.2em] text-alpine-text uppercase transition-colors hover:border-alpine-gold hover:text-alpine-gold"
				>
					Ritrova il tempo
				</a>
			</div>
			<div class="fade-up-element">
				<div class="relative aspect-4/5 overflow-hidden rounded-sm shadow-2xl lg:aspect-square">
					<img
						src="/imgs/jacuzzi-spa-hds-2026.webp"
						alt="Wellness & Spa"
						class="h-full w-full object-cover transition-transform duration-700 hover:scale-105"
					/>
				</div>
			</div>
		</div>

		<!-- Part 3: Activities -->
		<div class="grid grid-cols-1 items-center gap-12 lg:grid-cols-2 lg:gap-24">
			<div class="fade-up-element order-2 lg:order-1">
				<div class="relative aspect-4/5 overflow-hidden rounded-sm shadow-2xl lg:aspect-square">
					<img
						src="/imgs/ski-ome-activities.webp"
						alt="Attività Outdoor"
						class="h-full w-full object-cover transition-transform duration-700 hover:scale-105"
					/>
				</div>
			</div>
			<div class="fade-up-element order-1 lg:order-2">
				<span
					class="mb-4 block text-[10px] font-bold tracking-[0.3em] text-alpine-gold uppercase md:text-xs"
				>
					{#if $t('nav.sport')}
						{$t('nav.sport')}
					{/if}
				</span>
				<h2 class="mb-8 font-serif text-4xl text-alpine-text lg:text-6xl">
					{$t('home.sport_section_title')}
				</h2>
				<p class="mb-10 max-w-lg text-sm leading-relaxed font-light text-alpine-muted lg:text-lg">
					{$t('home.sport_section_text')}
				</p>
				<a
					href="/sport"
					class="inline-block border-b border-alpine-text pb-1 text-[11px] font-bold tracking-[0.2em] text-alpine-text uppercase transition-colors hover:border-alpine-gold hover:text-alpine-gold"
				>
					Vivi l'Alpe
				</a>
			</div>
		</div>
	</div>
</section>

<!-- ESPERIENZA ALPINA -->
<section class="mt-10 border-t border-alpine-border bg-white py-20 lg:py-32">
	<div class="mx-auto max-w-7xl px-6">
		<div class="fade-up-element mb-24 text-center">
			<h2 class="mb-6 font-serif text-4xl text-alpine-text">{$t('home.experience_title')}</h2>
			<p class="mx-auto max-w-xl text-sm leading-relaxed font-light text-alpine-muted">
				{$t('home.experience_text')}
			</p>
		</div>

		<div class="grid grid-cols-1 gap-16 px-4 md:grid-cols-3">
			<div class="fade-up-element flex flex-col items-center text-center">
				<Map class="mb-6 h-8 w-8 stroke-[1.5px] text-alpine-gold" />
				<h4 class="mb-4 text-xs font-bold tracking-[0.2em] text-alpine-text uppercase">
					{$t('home.feature_access_title')}
				</h4>
				<p class="text-sm leading-relaxed font-light text-alpine-muted">
					{$t('home.feature_access_text')}
				</p>
			</div>

			<div class="fade-up-element flex flex-col items-center text-center">
				<Utensils class="mb-6 h-8 w-8 stroke-[1.5px] text-alpine-gold" />
				<h4 class="mb-4 text-xs font-bold tracking-[0.2em] text-alpine-text uppercase">
					{$t('home.feature_food_title')}
				</h4>
				<p class="text-sm leading-relaxed font-light text-alpine-muted">
					{$t('home.feature_food_text')}
				</p>
			</div>

			<div class="fade-up-element flex flex-col items-center text-center">
				<ShieldCheck class="mb-6 h-8 w-8 stroke-[1.5px] text-alpine-gold" />
				<h4 class="mb-4 text-xs font-bold tracking-[0.2em] text-alpine-text uppercase">
					{$t('home.feature_comfort_title')}
				</h4>
				<p class="text-sm leading-relaxed font-light text-alpine-muted">
					{$t('home.feature_comfort_text')}
				</p>
			</div>
		</div>
	</div>
</section>
