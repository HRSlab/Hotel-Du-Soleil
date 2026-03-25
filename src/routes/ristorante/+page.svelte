<script lang="ts">
	import { t } from '$lib/i18n';
	import { Coffee, UtensilsCrossed, Wine } from 'lucide-svelte';
</script>

<svelte:head>
	<title>Ristorante | Hotel du Soleil Torgnon</title>
</svelte:head>

<!-- HERO SECTION -->
<header class="relative h-screen w-full overflow-hidden bg-[#1a1a1a]">
	<div class="absolute inset-0">
		<img
			src="/imgs/deer-dish-hero.webp"
			alt="Ristorante Hotel du Soleil"
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
				Sapori Autentici
			</span>
			<h1 class="mb-10 font-serif text-5xl leading-tight font-light text-white md:text-7xl">
				Il Ristorante
			</h1>
		</div>
	</div>
</header>

<!-- FILOSOFIA -->
<section class="bg-alpine-bg px-6 py-32">
	<div class="fade-up-element mx-auto max-w-3xl text-center">
		<div class="deco-line mb-12"></div>
		<h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-5xl">
			La tradizione valdostana incontra la freschezza degli ingredienti di montagna.
		</h3>
		<p class="mx-auto max-w-xl text-sm leading-relaxed font-light text-alpine-muted md:text-base">
			La nostra cucina è un omaggio sincero al territorio. Privilegiamo le materie prime a
			chilometro zero, selezionando personalmente i migliori formaggi degli alpeggi locali, le carni
			del territorio e le erbe spontanee per offrirvi un'esperienza gastronomica genuina e
			indimenticabile.
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
			<h4 class="mb-4 font-serif text-2xl text-alpine-text">Il Risveglio</h4>
			<p class="text-sm leading-relaxed font-light text-alpine-muted">
				Il buongiorno inizia con il profumo del burro di montagna e delle torte fatte in casa. Il
				nostro buffet offre un'ampia selezione di dolce e salato: Fontina DOP, salumi tipici, yogurt
				locali, cereali e confetture artigianali.
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
			<h4 class="mb-4 font-serif text-2xl text-alpine-text">La Cena</h4>
			<p class="text-sm leading-relaxed font-light text-alpine-muted">
				Ogni sera il nostro chef propone un menù curato che spazia dalle ricette classiche come la
				Valpellinentze o la polenta concia, a piatti internazionali, sempre accompagnati da un ricco
				buffet di verdure e sfiziosità.
			</p>
		</div>

		<!-- Cantina -->
		<div class="fade-up-element group mt-12 flex flex-col items-center text-center md:mt-0">
			<div
				class="relative mb-8 flex h-24 w-24 items-center justify-center overflow-hidden rounded-full border border-alpine-border bg-white"
			>
				<Wine
					class="z-10 h-8 w-8 text-alpine-gold transition-transform duration-500 group-hover:scale-110"
					strokeWidth="1.5"
				/>
			</div>
			<h4 class="mb-4 font-serif text-2xl text-alpine-text">La Cantina</h4>
			<p class="text-sm leading-relaxed font-light text-alpine-muted">
				Una selezione attenta delle migliori etichette valdostane per esaltare ogni piatto. I nostri
				maîtres saranno felici di consigliarvi gli abbinamenti perfetti per esplorare l'eccellenza
				vitivinicola eroica della nostra regione.
			</p>
		</div>
	</div>
</section>

<!-- IMAGE GRID -->
<section class="bg-white py-24">
	<div class="mx-auto grid max-w-7xl grid-cols-1 gap-8 px-6 md:grid-cols-2">
		<div class="group aspect-4/5 overflow-hidden">
			<img
				src="imgs/deer_dish_hds.webp"
				alt="Cucina Alpina"
				class="h-full w-full object-cover transition-transform duration-1000 group-hover:scale-105"
			/>
		</div>
		<div class="flex flex-col gap-8">
			<div class="group aspect-video overflow-hidden">
				<img
					src="imgs/amuse_hds_bouche.webp"
					alt="Vini Valdostani"
					class="h-full w-full object-cover transition-transform duration-1000 group-hover:scale-105"
				/>
			</div>
			<div
				class="relative flex flex-1 flex-col items-start justify-center overflow-hidden border border-alpine-border bg-alpine-bg p-12"
			>
				<span class="mb-4 block text-[10px] font-bold tracking-[0.2em] text-alpine-muted uppercase"
					>Dietro le Quinte</span
				>
				<h4 class="relative z-10 mb-6 font-serif text-3xl text-alpine-text">Prodotti a KM Zero</h4>
				<p class="relative z-10 text-sm leading-relaxed font-light text-alpine-muted">
					La nostra Fontina arriva direttamente dagli alpeggi circostanti, e molte verdure dal
					nostro orto di famiglia. Una scelta di qualità e sostenibilità.
				</p>
				<div class="pointer-events-none absolute -right-12 -bottom-12 opacity-5">
					<UtensilsCrossed class="h-64 w-64 text-alpine-text" />
				</div>
			</div>
		</div>
	</div>
</section>
