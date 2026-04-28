<script lang="ts">
	import {
		getRestartPromotionUrl,
		getTorgnonHikingAdventurePromotionUrl,
		getForteBardGourmetEscapePromotionUrl,
		getAostaRomanaPromotionUrl
	} from '$lib/config/booking';

	interface Promo {
		title: string;
		price: string;
		url: string;
	}

	const promos: Promo[] = [
		{
			title: 'RESTART',
			price: 'EUR 520',
			url: getRestartPromotionUrl('promo_marquee_restart')
		},
		{
			title: 'TORGNON HIKING & ADVENTURE',
			price: 'EUR 520',
			url: getTorgnonHikingAdventurePromotionUrl('promo_marquee_torgnon')
		},
		{
			title: 'FORTE DI BARD & GOURMET ESCAPE',
			price: 'EUR 540',
			url: getForteBardGourmetEscapePromotionUrl('promo_marquee_forte')
		},
		{
			title: 'AOSTA ROMANA & CASTELLO DI FENIS',
			price: 'EUR 580',
			url: getAostaRomanaPromotionUrl('promo_marquee_aosta')
		}
	];

	const marqueeItems = [...promos, ...promos];
</script>

<div
	class="fixed inset-x-0 top-0 z-60 h-10 border-b border-alpine-text/20 bg-alpine-gold text-alpine-text"
	role="region"
	aria-label="Promotional marquee"
>
	<div class="marquee-track-wrap h-full overflow-hidden">
		<div class="marquee-track flex h-full w-max items-center whitespace-nowrap">
			{#each marqueeItems as promo, index (index)}
				<a
					href={promo.url}
					target="_blank"
					rel="noopener noreferrer"
					class="promo-pill mx-2 inline-flex h-6 items-center gap-2 rounded-sm border border-alpine-text/25 px-3 text-[10px] tracking-[0.14em] uppercase transition-colors hover:bg-alpine-text hover:text-white"
				>
					<span class="font-semibold">{promo.title}</span>
					<span class="text-alpine-text/70">•</span>
					<span class="font-bold">{promo.price}</span>
				</a>
			{/each}
		</div>
	</div>
</div>

<style>
	.marquee-track {
		animation: promo-marquee 30s linear infinite;
	}

	.marquee-track-wrap:hover .marquee-track {
		animation-play-state: paused;
	}

	@keyframes promo-marquee {
		0% {
			transform: translateX(0);
		}
		100% {
			transform: translateX(-50%);
		}
	}

	@media (prefers-reduced-motion: reduce) {
		.marquee-track {
			animation: none;
		}
	}
</style>
