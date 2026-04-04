<script lang="ts">
	import { t, locale } from '$lib/i18n';
	import { Heart } from 'lucide-svelte';

	const copy = $derived(
		$locale === 'ru'
			? {
					intro:
						'Профессиональные массажи для восстановления, расслабления и снятия мышечного напряжения после активного дня в горах.'
				}
			: { intro: 'Massaggi professionali per ogni esigenza.' }
	);
</script>

<svelte:head>
	<title>{$t('wellness.massaggi.title')} | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
	<div class="absolute inset-0">
		<img
			src="https://images.unsplash.com/photo-1544161515-4af6b1d46bdc?q=80&w=2000&auto=format&fit=crop"
			class="ken-burns h-full w-full object-cover opacity-70"
			alt="Massaggi"
		/>
		<div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/20 to-alpine-bg"></div>
	</div>
	<div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
		<span
			class="fade-up-element mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs"
		>
			{$t('wellness.massaggi.subtitle')}
		</span>
		<h1 class="fade-up-element font-serif text-5xl leading-tight font-light text-white md:text-7xl">
			{$t('wellness.massaggi.title')}
		</h1>
	</div>
</header>

<section class="bg-alpine-bg px-6 py-24">
	<div class="fade-up-element mx-auto max-w-3xl text-center">
		<Heart class="mx-auto mb-10 h-10 w-10 text-alpine-gold" />
		<h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
			{$t('wellness.massaggi.subtitle')}
		</h3>
		<p
			class="mx-auto mt-12 max-w-xl border-t border-alpine-border pt-12 text-sm leading-relaxed font-light text-alpine-muted md:text-base"
		>
			{$t('wellness.massaggi.p1') || copy.intro}
		</p>
	</div>
</section>
