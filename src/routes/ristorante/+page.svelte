<script lang="ts">
	import { t } from '$lib/i18n';
	import { Coffee, UtensilsCrossed, Wine, Flame, Gamepad2, Sun } from 'lucide-svelte';
</script>

<svelte:head>
	<title>Ristorante | Chalet du Soleil Torgnon</title>
</svelte:head>

<!-- HERO SECTION -->
<header class="relative h-screen w-full overflow-hidden bg-[#1a1a1a]">
	<div class="absolute inset-0">
		<img
			src="/imgs/deer-dish-hero.webp"
			alt="Ristorante Chalet du Soleil"
			class="ken-burns h-full w-full object-cover opacity-80"
		/>
		<div class="absolute inset-0 bg-black/40"></div>
		<div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/40 to-alpine-bg"></div>
	</div>

	<div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-32 text-center">
		<div class="fade-up-element">
			<span
				class="mb-6 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs"
			>
				{$t('ristorante.hero_label')}
			</span>
			<h1 class="mb-10 font-serif text-5xl leading-tight font-light text-white md:text-7xl">
				{$t('ristorante.hero_title')}
			</h1>
		</div>
	</div>
</header>

<!-- FILOSOFIA -->
<section class="bg-alpine-bg px-6 py-32">
	<div class="fade-up-element mx-auto max-w-3xl text-center">
		<div class="deco-line mb-12"></div>
		<h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-5xl">
			{$t('ristorante.philosophy_title')}
		</h3>
		<p class="mx-auto max-w-xl text-sm leading-relaxed font-light text-alpine-muted md:text-base">
			{$t('ristorante.philosophy_text')}
		</p>
	</div>
</section>

<!-- HIGHLIGHTS / SECTIONS -->
<section class="mx-auto max-w-7xl border-t border-alpine-border px-6 py-24">
	<div class="grid grid-cols-1 gap-16 md:grid-cols-3">
		<!-- Colazione -->
		<div class="fade-up-element group flex flex-col items-center text-center">
			<div
				class="relative mb-8 flex h-24 w-24 items-center justify-center overflow-hidden rounded-full border border-alpine-border bg-white"
			>
				<Coffee
					class="z-10 h-8 w-8 text-alpine-gold transition-transform duration-500 group-hover:scale-110"
					strokeWidth="1.5"
				/>
			</div>
			<h4 class="mb-4 font-serif text-2xl text-alpine-text">{$t('ristorante.breakfast_title')}</h4>
			<p class="text-sm leading-relaxed font-light text-alpine-muted">
				{$t('ristorante.breakfast_text')}
			</p>
		</div>

		<!-- Cena -->
		<div class="fade-up-element group mt-12 flex flex-col items-center text-center md:mt-0">
			<div
				class="relative mb-8 flex h-24 w-24 items-center justify-center overflow-hidden rounded-full border border-alpine-border bg-white"
			>
				<UtensilsCrossed
					class="z-10 h-8 w-8 text-alpine-gold transition-transform duration-500 group-hover:scale-110"
					strokeWidth="1.5"
				/>
			</div>
			<h4 class="mb-4 font-serif text-2xl text-alpine-text">{$t('ristorante.dinner_title')}</h4>
			<p class="text-sm leading-relaxed font-light text-alpine-muted">
				{$t('ristorante.dinner_text')}
			</p>
		</div>

		<!-- Lounge Bar -->
		<div class="fade-up-element group flex flex-col items-center text-center">
			<div
				class="relative mb-8 flex h-24 w-24 items-center justify-center overflow-hidden rounded-full border border-alpine-border bg-white"
			>
				<Wine
					class="z-10 h-8 w-8 text-alpine-gold transition-transform duration-500 group-hover:scale-110"
					strokeWidth="1.5"
				/>
			</div>
			<h4 class="mb-4 font-serif text-2xl text-alpine-text">{$t('ristorante.lounge_title')}</h4>
			<p class="text-sm leading-relaxed font-light text-alpine-muted">
				{$t('ristorante.lounge_text')}
			</p>
		</div>


	</div>
</section>

<!-- IMAGE GRID -->
<section class="bg-white py-24">
	<div class="mx-auto grid max-w-7xl grid-cols-1 gap-8 px-6 md:grid-cols-2">
		<div class="group aspect-4/5 overflow-hidden">
			<img
				src="/imgs/deer-dish-hds.webp"
				alt="Cucina Alpina"
				class="h-full w-full object-cover transition-transform duration-1000 group-hover:scale-105"
			/>
		</div>
		<div class="flex flex-col gap-8">
			<div class="group aspect-video overflow-hidden">
				<img
					src="/imgs/amuse-hds-bouche.webp"
					alt="Vini Valdostani"
					class="h-full w-full object-cover transition-transform duration-1000 group-hover:scale-105"
				/>
			</div>
			<div
				class="relative flex flex-1 flex-col items-start justify-center overflow-hidden border border-alpine-border bg-alpine-bg p-12"
			>
				<span class="mb-4 block text-[10px] font-bold tracking-[0.2em] text-alpine-muted uppercase"
				>{$t('ristorante.behind_label')}</span
			>
				<h4 class="relative z-10 mb-6 font-serif text-3xl text-alpine-text">{$t('ristorante.km0_title')}</h4>
				<p class="relative z-10 text-sm leading-relaxed font-light text-alpine-muted">
					{$t('ristorante.km0_text')}
				</p>
				<div class="pointer-events-none absolute -right-12 -bottom-12 opacity-5">
					<UtensilsCrossed class="h-64 w-64 text-alpine-text" />
				</div>
			</div>
		</div>
	</div>
</section>

<!-- LOUNGE & CAMINO -->
<section class="border-t border-alpine-border bg-alpine-bg px-6 py-32">
	<div class="fade-up-element mx-auto max-w-3xl text-center">
		<Flame class="mx-auto mb-10 h-10 w-10 text-alpine-gold" />
		<h2 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-5xl">
			{$t('ristorante.warmth_title')}
		</h2>
		<p class="text-sm leading-relaxed font-light text-alpine-muted md:text-base">
			{$t('ristorante.warmth_text')}
		</p>
	</div>
</section>

<section class="mx-auto max-w-7xl space-y-32 bg-alpine-bg px-6 pb-32">
	<!-- Svago -->
	<div class="fade-up-element flex flex-col items-center gap-12 md:flex-row lg:gap-20">
		<div class="group relative w-full overflow-hidden bg-alpine-border md:w-1/2">
			<img
				src="/imgs/bar-and-lounge/bar-pooltable.webp"
				alt="Sala Biliardo"
				class="img-elegant aspect-4/3 h-full w-full object-cover"
			/>
		</div>
		<div class="w-full md:w-1/2">
			<Gamepad2 class="mb-6 h-8 w-8 text-alpine-gold" />
			<h3 class="mb-4 font-serif text-4xl text-alpine-text">{$t('ristorante.games_title')}</h3>
			<p class="mb-6 text-[10px] font-bold tracking-widest text-alpine-muted uppercase">
				{$t('ristorante.games_subtitle')}
			</p>
			<p class="text-sm leading-relaxed font-light text-alpine-muted">
				{$t('ristorante.games_text')}
			</p>
		</div>
	</div>

	<!-- Aperitivo -->
	<div class="fade-up-element flex flex-col items-center gap-12 md:flex-row-reverse lg:gap-20">
		<div class="group relative w-full overflow-hidden bg-alpine-border md:w-1/2">
			<img
				src="/imgs/bar-and-lounge/aperitivo-garden.webp"
				alt="Aperitivo all'aperto"
				class="img-elegant aspect-4/3 h-full w-full object-cover"
			/>
		</div>
		<div class="w-full md:w-1/2">
			<Sun class="mb-6 h-8 w-8 text-alpine-gold" />
			<h3 class="mb-4 font-serif text-4xl text-alpine-text">{$t('ristorante.aperitivo_title')}</h3>
			<p class="mb-6 text-[10px] font-bold tracking-widest text-alpine-muted uppercase">
				{$t('ristorante.aperitivo_subtitle')}
			</p>
			<p class="text-sm leading-relaxed font-light text-alpine-muted">
				{$t('ristorante.aperitivo_text')}
			</p>
		</div>
	</div>

	<!-- Colazione al camino -->
	<div class="fade-up-element flex flex-col items-center gap-12 md:flex-row lg:gap-20">
		<div class="group relative w-full overflow-hidden bg-alpine-border md:w-1/2">
			<img
				src="/imgs/bar-and-lounge/fireplace-bar.webp"
				alt="Colazione accanto al camino"
				class="img-elegant aspect-4/3 h-full w-full object-cover"
			/>
		</div>
		<div class="w-full md:w-1/2">
			<Flame class="mb-6 h-8 w-8 text-alpine-gold" />
			<h3 class="mb-4 font-serif text-4xl text-alpine-text">{$t('ristorante.morning_title')}</h3>
			<p class="mb-6 text-[10px] font-bold tracking-widest text-alpine-muted uppercase">
				{$t('ristorante.morning_subtitle')}
			</p>
			<p class="text-sm leading-relaxed font-light text-alpine-muted">
				{$t('ristorante.morning_text')}
			</p>
		</div>
	</div>
</section>
