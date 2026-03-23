<script lang="ts">
	import { t } from '$lib/i18n';

	import BookingBar from '$lib/components/BookingBar.svelte';
	import WeatherWidget from '$lib/components/WeatherWidget.svelte';
	import RoomCarousel from '$lib/components/RoomCarousel.svelte';
	import { Map, Utensils, ShieldCheck } from 'lucide-svelte';
</script>

<svelte:head>
	<title>Hotel du Soleil | Modern Alpine Retreat</title>
</svelte:head>

<!-- HERO SECTION -->
<header class="relative h-screen w-full overflow-hidden bg-[#1a1a1a]">
	<div class="absolute inset-0">
		<video autoplay loop muted playsinline class="h-full w-full object-cover opacity-100">
			<source src="/imgs/bg_video_hero.webm" type="video/webm" />
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
<section class="bg-alpine-bg px-6 py-32">
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
			href={"/storia"}
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
		<p class="mt-4 text-xs tracking-widest text-alpine-muted uppercase md:mt-0 font-bold">
			{$t('home.rooms_subtitle')}
		</p>
	</div>

	<RoomCarousel />
</section>

<!-- ESPERIENZA ALPINA -->
<section class="mt-10 border-t border-alpine-border bg-white py-32">
	<div class="mx-auto max-w-7xl px-6">
		<div class="fade-up-element mb-24 text-center">
			<h2 class="mb-6 font-serif text-4xl text-alpine-text">{$t('home.experience_title')}</h2>
			<p class="mx-auto max-w-xl text-sm font-light text-alpine-muted leading-relaxed">
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
