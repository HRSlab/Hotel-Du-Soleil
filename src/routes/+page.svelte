<script lang="ts">
	import { t } from '$lib/i18n';
	import BookingBar from '$lib/components/BookingBar.svelte';
	import WeatherWidget from '$lib/components/WeatherWidget.svelte';
	import RoomCarousel from '$lib/components/RoomCarousel.svelte';
	import { Map, Utensils, ShieldCheck, ArrowRight } from 'lucide-svelte';
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
		<div class="absolute inset-0 bg-gradient-to-b from-black/80 via-black/40 to-alpine-bg"></div>
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
			Crediamo nel lusso dell'essenziale, nel calore umano e nel valore del tempo rallentato.
		</h3>
		<p
			class="mx-auto mb-12 max-w-xl text-sm leading-relaxed font-light text-alpine-muted md:text-base"
		>
			L'Hotel du Soleil è il tuo Base Camp a 1.500 metri di quota. Abbiamo eliminato il superfluo
			per lasciare spazio a ciò che conta davvero: il legno naturale, il sapore autentico della
			cucina alpina e la maestosità della natura appena fuori dalla porta.
		</p>
		<a
			href="/storia"
			class="border-b border-alpine-text pb-1 text-[11px] font-bold tracking-[0.2em] text-alpine-text uppercase transition-colors hover:border-alpine-gold hover:text-alpine-gold"
		>
			Scopri la nostra storia
		</a>
	</div>
</section>

<!-- LE CAMERE (Grid Editoriale) -->
<section class="mx-auto max-w-7xl px-6 py-24">
	<div
		class="fade-up-element mb-16 flex flex-col items-end justify-between border-b border-alpine-border pb-6 md:flex-row"
	>
		<h2 class="font-serif text-4xl text-alpine-text md:text-5xl">Spazi di Riposo</h2>
		<p class="mt-4 text-xs tracking-widest text-alpine-muted uppercase md:mt-0">
			Sostanza & Comfort
		</p>
	</div>

	<RoomCarousel />
</section>

<!-- ESPERIENZA ALPINA -->
<section class="mt-10 border-t border-alpine-border bg-white py-32">
	<div class="mx-auto max-w-7xl px-6">
		<div class="fade-up-element mb-24 text-center">
			<h2 class="mb-6 font-serif text-4xl text-alpine-text">L'Esperienza Alpina</h2>
			<p class="mx-auto max-w-xl text-sm font-light text-alpine-muted">
				La nostra promessa è un'ospitalità pratica e calda. Dimenticate lo stress logistico e
				lasciatevi viziare dai sapori veri della nostra valle.
			</p>
		</div>

		<div class="grid grid-cols-1 gap-16 px-4 md:grid-cols-3">
			<div class="fade-up-element flex flex-col items-center text-center">
				<Map class="mb-6 h-8 w-8 stroke-[1.5px] text-alpine-gold" />
				<h4 class="mb-4 text-xs font-bold tracking-[0.2em] text-alpine-text uppercase">
					Accesso Diretto
				</h4>
				<p class="text-sm leading-relaxed font-light text-alpine-muted">
					A soli 20 metri dagli impianti di risalita e dai principali sentieri. La montagna inizia
					letteralmente dalla nostra porta.
				</p>
			</div>

			<div class="fade-up-element flex flex-col items-center text-center">
				<Utensils class="mb-6 h-8 w-8 stroke-[1.5px] text-alpine-gold" />
				<h4 class="mb-4 text-xs font-bold tracking-[0.2em] text-alpine-text uppercase">
					Ristorazione Vera
				</h4>
				<p class="text-sm leading-relaxed font-light text-alpine-muted">
					La mezza pensione offre menù che rispettano la tradizione valdostana. Materie prime
					eccellenti, ricette tramandate con cura.
				</p>
			</div>

			<div class="fade-up-element flex flex-col items-center text-center">
				<ShieldCheck class="mb-6 h-8 w-8 stroke-[1.5px] text-alpine-gold" />
				<h4 class="mb-4 text-xs font-bold tracking-[0.2em] text-alpine-text uppercase">
					Comfort Logistico
				</h4>
				<p class="text-sm leading-relaxed font-light text-alpine-muted">
					Garage coperto riservato, wifi nelle aree comuni e un caldo salotto con camino dove
					rilassarsi a fine giornata.
				</p>
			</div>
		</div>
	</div>
</section>
