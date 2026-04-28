<script lang="ts">
	import { t } from '$lib/i18n';

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
			tag: 'RICONNESSIONE',
			title: 'RESTART',
			description:
				'Pacchetto benessere e connessione con la natura tra sauna, yoga e sentieri silenziosi.',
			image:
				'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=1600&auto=format&fit=crop'
		},
		{
			href: '/offerte/torgnon-hiking-adventure',
			tag: 'PACCHETTO AVVENTURA',
			title: 'TORGNON HIKING & ADVENTURE',
			description:
				'4 giorni tra trekking, Petit Monde, Adventure Park e giro panoramico in e-bike.',
			image:
				'https://images.unsplash.com/photo-1551632811-561732d1e306?q=80&w=1600&auto=format&fit=crop'
		},
		{
			href: '/offerte/forte-di-bard-gourmet-escape',
			tag: 'HERITAGE & TASTE',
			title: 'FORTE DI BARD & GOURMET ESCAPE',
			description:
				'3 notti tra Forte di Bard, degustazione locale, hiking signature day ed e-bike panoramica.',
			image: 'https://www.lovevda.it/immagini/DisplayImage/33914'
		},
		{
			href: '/offerte/aosta-romana-castello-di-fenis',
			tag: 'ROMAN HERITAGE & CASTLE',
			title: 'AOSTA ROMANA & CASTELLO DI FÉNIS',
			description:
				'3 notti tra il cuore romano di Aosta, Porta Praetoria, Castello di Fénis e base montana a Torgnon.',
			image:
				'https://www.villageparadis.it/immagini/arco-d-augusto-aosta-romana-villageparadis-agriturismo_ea.jpg'
		}
	];
</script>

<section class="w-full bg-alpine-bg px-6 pt-0 pb-20">
	<div class="mx-auto max-w-7xl">
		<div class="mb-12 text-center">
			<h2 class="font-serif text-4xl text-alpine-text md:text-5xl">Offerte e Pacchetti</h2>
			<p class="mt-4 text-sm leading-relaxed font-light text-alpine-muted md:text-base">
				Esperienze curate per ogni momento dell'anno. Scopri le nostre proposte esclusive tra
				montagna, cultura e benessere.
			</p>
		</div>

		<!-- Grid Layout -->
		<div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-4">
			{#each offers as offer (offer.href)}
				<article
					class="group border border-alpine-border bg-white transition-all duration-500 hover:-translate-y-1 hover:border-alpine-gold hover:shadow-2xl"
				>
					<a href={offer.href} class="block">
						<div class="aspect-16/10 overflow-hidden">
							<img
								src={offer.image}
								alt={offer.title}
								class="img-elegant h-full w-full object-cover transition-transform duration-700 group-hover:scale-105"
								loading="lazy"
							/>
						</div>
						<div class="p-6">
							<span class="text-[9px] font-bold tracking-[0.22em] text-alpine-gold uppercase">
								{offer.tag}
							</span>
							<h3 class="mt-2 font-serif text-lg text-alpine-text">
								{offer.title}
							</h3>
							<p class="mt-2 text-xs leading-relaxed font-light text-alpine-muted">
								{offer.description}
							</p>
							<span
								class="mt-4 inline-flex border-b border-alpine-text pb-1 text-[10px] font-bold tracking-[0.2em] text-alpine-text uppercase transition-colors group-hover:border-alpine-gold group-hover:text-alpine-gold"
							>
								{$t('offers_page.card_cta')}
							</span>
						</div>
					</a>
				</article>
			{/each}
		</div>
	</div>
</section>
