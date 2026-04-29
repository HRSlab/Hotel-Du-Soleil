<script lang="ts">
	import { fade, fly } from 'svelte/transition';
	import { ArrowLeft, ArrowRight } from 'lucide-svelte';

	interface Offer {
		href: string;
		tag: string;
		title: string;
		description: string;
		image: string;
	}

	const offers: Offer[] = [
		{
			href: '/offerte/restart',
			tag: 'Riconnessione',
			title: 'RESTART',
			description:
				'Pacchetto benessere e connessione con la natura tra sauna, yoga e sentieri silenziosi.',
			image:
				'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=1920&auto=format&fit=crop'
		},
		{
			href: '/offerte/torgnon-hiking-adventure',
			tag: 'Avventura',
			title: 'TORGNON HIKING & ADVENTURE',
			description:
				'4 giorni tra trekking, Petit Monde, Adventure Park e giro panoramico in e-bike.',
			image:
				'https://images.unsplash.com/photo-1551632811-561732d1e306?q=80&w=1920&auto=format&fit=crop'
		},
		{
			href: '/offerte/forte-di-bard-gourmet-escape',
			tag: 'Heritage & Taste',
			title: 'FORTE DI BARD & GOURMET ESCAPE',
			description:
				'3 notti tra Forte di Bard, degustazione locale, hiking signature day ed e-bike panoramica.',
			image:
				'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?q=80&w=1920&auto=format&fit=crop'
		},
		{
			href: '/offerte/aosta-romana-castello-di-fenis',
			tag: 'Roman Heritage & Castle',
			title: 'AOSTA ROMANA & CASTELLO DI FÉNIS',
			description:
				'3 notti tra il cuore romano di Aosta, Porta Praetoria, Castello di Fénis e base montana a Torgnon.',
			image:
				'https://commons.wikimedia.org/wiki/Special:FilePath/Teatro_romano_aosta_verso_l%27alto.JPG'
		}
	];

	let currentIndex = $state(0);
	let direction = $state<'next' | 'prev'>('next');

	function next() {
		direction = 'next';
		currentIndex = (currentIndex + 1) % offers.length;
	}

	function prev() {
		direction = 'prev';
		currentIndex = (currentIndex - 1 + offers.length) % offers.length;
	}

	function goTo(i: number) {
		direction = i > currentIndex ? 'next' : 'prev';
		currentIndex = i;
	}

	const current = $derived(offers[currentIndex]);
	const xIn = $derived(direction === 'next' ? 40 : -40);
</script>

<section class="relative w-full overflow-hidden bg-[#0e0e0e]">
	<!-- Section header -->
	<div class="relative z-10 flex items-end justify-between px-8 pt-14 pb-10 md:px-16">
		<div>
			<span class="mb-3 block text-[10px] font-bold tracking-[0.4em] text-alpine-gold uppercase">
				Offerte & Pacchetti
			</span>
			<h2 class="font-serif text-4xl font-light text-white md:text-5xl">Esperienze su misura</h2>
		</div>
		<a
			href="/offerte"
			class="hidden border-b border-white/40 pb-1 text-[11px] font-bold tracking-[0.2em] text-white/70 uppercase transition-colors hover:border-alpine-gold hover:text-alpine-gold md:inline-block"
		>
			Tutte le offerte
		</a>
	</div>

	<!-- Slide area -->
	<div class="relative aspect-video max-h-[75vh] w-full overflow-hidden md:aspect-21/9">
		{#key currentIndex}
			<!-- Background image -->
			<div in:fade={{ duration: 700 }} out:fade={{ duration: 400 }} class="absolute inset-0">
				<img
					src={current.image}
					alt={current.title}
					class="h-full w-full object-cover"
					loading="lazy"
				/>
				<div
					class="absolute inset-0 bg-linear-to-r from-black/75 via-black/30 to-transparent"
				></div>
				<div
					class="absolute inset-0 bg-linear-to-t from-black/60 via-transparent to-transparent"
				></div>
			</div>

			<!-- Text content -->
			<div
				in:fly={{ x: xIn, duration: 700, delay: 120 }}
				class="absolute bottom-0 left-0 z-10 max-w-xl px-8 pb-12 md:px-16 md:pb-16"
			>
				<span class="mb-4 block text-[10px] font-bold tracking-[0.3em] text-alpine-gold uppercase">
					{current.tag}
				</span>
				<h3 class="mb-4 font-serif text-3xl leading-tight font-light text-white md:text-5xl">
					{current.title}
				</h3>
				<p class="mb-8 max-w-sm text-sm leading-relaxed font-light text-white/70">
					{current.description}
				</p>
				<a
					href={current.href}
					class="inline-flex items-center gap-3 border border-white/30 px-6 py-3 text-[11px] font-bold tracking-[0.2em] text-white uppercase transition-all duration-300 hover:border-alpine-gold hover:bg-alpine-gold hover:text-alpine-text"
				>
					Scopri il pacchetto
					<ArrowRight class="h-3 w-3" />
				</a>
			</div>
		{/key}

		<!-- Prev / Next buttons -->
		<div class="absolute right-6 bottom-12 z-20 flex items-center gap-3 md:right-12 md:bottom-16">
			<button
				onclick={prev}
				aria-label="Offerta precedente"
				class="flex h-12 w-12 items-center justify-center border border-white/30 text-white transition-all duration-300 hover:border-alpine-gold hover:bg-alpine-gold hover:text-alpine-text"
			>
				<ArrowLeft class="h-4 w-4" />
			</button>
			<button
				onclick={next}
				aria-label="Offerta successiva"
				class="flex h-12 w-12 items-center justify-center border border-white/30 text-white transition-all duration-300 hover:border-alpine-gold hover:bg-alpine-gold hover:text-alpine-text"
			>
				<ArrowRight class="h-4 w-4" />
			</button>
		</div>

		<!-- Counter -->
		<div
			class="absolute top-6 right-8 z-20 text-[10px] font-bold tracking-[0.3em] text-white/50 md:right-12"
		>
			{String(currentIndex + 1).padStart(2, '0')} / {String(offers.length).padStart(2, '0')}
		</div>
	</div>

	<!-- Dot navigation -->
	<div class="flex items-center justify-center gap-2 py-6">
		{#each offers as _, i}
			<button
				onclick={() => goTo(i)}
				aria-label={`Offerta ${i + 1}`}
				class="h-0.5 transition-all duration-400 {i === currentIndex
					? 'w-8 bg-alpine-gold'
					: 'w-3 bg-white/25 hover:bg-white/50'}"
			></button>
		{/each}
	</div>

	<!-- Mobile CTA -->
	<div class="px-8 pb-10 text-center md:hidden">
		<a
			href="/offerte"
			class="inline-block border-b border-white/40 pb-1 text-[11px] font-bold tracking-[0.2em] text-white/70 uppercase"
		>
			Tutte le offerte
		</a>
	</div>
</section>
