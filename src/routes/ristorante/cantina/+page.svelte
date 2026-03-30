<script lang="ts">
	import { Wine, Grape, GlassWater, Coffee } from 'lucide-svelte';

	// Strutturiamo i dati dei vini per un rendering pulito e per facilitare future traduzioni (i18n)
	const menuVini = [
		{
			titolo: "Bollicine d'Alta Quota",
			sottotitolo: 'Metodo Classico & Spumanti',
			icona: Wine,
			vini: [
				{
					nome: 'Cuvée Skyway Monte Bianco - Pas Dosè',
					desc: '100% Priè Blanc • Dègorgement 36 mesi',
					prezzo: '110 €'
				},
				{
					nome: 'Spumante Metodo Classico - Pas Dosè',
					desc: '100% Priè Blanc • Morgex e La Salle • Dègorgement 24 mesi',
					prezzo: '32 €'
				}
			]
		},
		{
			titolo: 'I Bianchi',
			sottotitolo: 'Freschezza e Mineralità Alpina',
			icona: Grape,
			vini: [
				{
					nome: "Petite Arvine DOC 'Fleur'",
					desc: '100% Petite Arvine • 9 mesi sui lieviti',
					prezzo: '34 €'
				},
				{
					nome: 'Pinot Gris DOC - Lo Triolet',
					desc: '100% Pinot Gris • Marco Martin • Fermentazione in acciaio',
					prezzo: '45 €'
				},
				{
					nome: "Chardonnay DOC 'Revei'",
					desc: '100% Chardonnay • 12 mesi in botti di rovere francese',
					prezzo: '34 €'
				}
			]
		},
		{
			titolo: 'I Rossi',
			sottotitolo: 'Corpo, Tradizione e Carattere',
			icona: GlassWater,
			vini: [
				{
					nome: "Enfer d'Arvier DOC",
					desc: 'Petit Rouge, Pinot Noir, Gamay • Danilo Thomain',
					prezzo: '38 €'
				},
				{
					nome: 'Fumin DOC',
					desc: '100% Fumin • Affinamento in legno grande e piccolo',
					prezzo: '34 €'
				},
				{
					nome: 'Torrette Supérieur DOC',
					desc: '85% Petit Rouge, 15% Fumin • Barrique di rovere x 12 mesi',
					prezzo: '38 €'
				},
				{ nome: 'Syrah DOC', desc: '90% Syrah, 10% Fumin • Affinamento in acciaio', prezzo: '38 €' }
			]
		}
	];

	const spiriti = [
		{ nome: 'Gin Acqueverdi (La Valdôtaine)', prezzo: '12 €' },
		{ nome: 'Amaro Ebo Lebo (Ottoz)', prezzo: '5 €' },
		{ nome: 'Grappa Monovitigno Blanc de Morgex', prezzo: '4 €' },
		{ nome: 'Grappa Chaudelune (La Valdôtaine)', prezzo: '7 €' }
	];
</script>

<svelte:head>
	<title>La Cantina | Chalet Du Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
	<img
		src="https://images.unsplash.com/photo-1506377247377-2a5b3b417ebb?q=80&w=2000&auto=format&fit=crop"
		class="ken-burns h-full w-full object-cover opacity-70"
		alt="Wine Cellar"
	/>
	<div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/40 to-alpine-bg"></div>
	<div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
		<h1 class="fade-up-element font-serif text-5xl leading-tight font-light text-white md:text-7xl">
			La Cantina
		</h1>
	</div>
</header>

<section class="bg-alpine-bg px-6 py-32">
	<div class="fade-up-element mx-auto max-w-3xl text-center">
		<Wine class="mx-auto mb-10 h-10 w-10 text-alpine-gold" />
		<h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
			Viticoltura eroica d'alta quota.
		</h3>
		<p
			class="mt-12 border-t border-alpine-border pt-12 text-sm leading-relaxed font-light text-alpine-muted md:text-base"
		>
			Selezioniamo con cura e passione le migliori e più esclusive etichette valdostane per
			valorizzare una terra complessa e fiera. I nostri maîtres vi guideranno in un viaggio
			enologico unico, pensato per esaltare ogni sfumatura culinaria.
		</p>
	</div>
</section>

<section class="bg-alpine-bg px-6 pb-32">
	<div class="mx-auto max-w-4xl">
		{#each menuVini as sezione}
			<div class="fade-up-element mb-24">
				<div class="mb-16 text-center">
					<svelte:component this={sezione.icona} class="mx-auto mb-4 h-6 w-6 text-alpine-gold" />
					<h2 class="font-serif text-3xl text-alpine-text md:text-4xl">{sezione.titolo}</h2>
					<p class="mt-3 text-[10px] tracking-widest text-alpine-muted uppercase">
						{sezione.sottotitolo}
					</p>
				</div>

				<div class="space-y-10">
					{#each sezione.vini as vino}
						<div class="group">
							<div
								class="mb-2 flex items-baseline justify-between font-serif text-xl text-alpine-text md:text-2xl"
							>
								<span class="pr-4">{vino.nome}</span>
								<div class="menu-leader"></div>
								<span class="pl-4 text-alpine-gold transition-colors group-hover:text-alpine-text"
									>{vino.prezzo}</span
								>
							</div>
							<p class="text-xs font-light tracking-wider text-alpine-muted uppercase">
								{vino.desc}
							</p>
						</div>
					{/each}
				</div>
			</div>
		{/each}

		<div class="fade-up-element mt-32 border border-alpine-border bg-white p-10 shadow-sm md:p-16">
			<Coffee class="mx-auto mb-6 h-6 w-6 text-alpine-gold" />
			<h3 class="mb-10 text-center font-serif text-2xl text-alpine-text">Spiriti e Fine Pasto</h3>
			<div class="grid grid-cols-1 gap-x-16 gap-y-6 md:grid-cols-2">
				{#each spiriti as spirito}
					<div
						class="group flex cursor-default justify-between border-b border-alpine-border pb-3 text-sm text-alpine-text"
					>
						<span class="font-medium transition-colors group-hover:text-alpine-gold"
							>{spirito.nome}</span
						>
						<span class="text-alpine-gold">{spirito.prezzo}</span>
					</div>
				{/each}
			</div>
		</div>
	</div>
</section>

<style>
	/* Svelte scopes CSS automatically, keeping things perfectly clean */
	.menu-leader {
		grow: 1;
		border-bottom: 1px dotted #d6d3cd;
		position: relative;
		top: -6px;
		opacity: 0.6;
		transition: opacity 0.3s ease;
	}

	.group:hover .menu-leader {
		opacity: 1;
		border-bottom: 1px dotted #b89872; /* Changes to alpine-gold on hover */
	}
</style>
