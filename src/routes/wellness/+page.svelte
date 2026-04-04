<script lang="ts">
	import { t, locale } from '$lib/i18n';

	const copy = $derived(
		$locale === 'ru'
			? { philosophy: 'Тепло дерева и очищающий пар.' }
			: { philosophy: 'Il calore del legno, il vapore purificante.' }
	);
</script>

<svelte:head>
	<title>{$t('wellness.main_title')} | Hotel du Soleil</title>
</svelte:head>

<div class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
	<div class="absolute inset-0">
		<img
			src="https://images.unsplash.com/photo-1544161515-4af6b1d46bdc?q=80&w=1000&auto=format&fit=crop"
			alt="Alpine Wellness"
			class="ken-burns h-full w-full object-cover opacity-70"
		/>
		<div class="absolute inset-0 bg-linear-to-b from-black/40 via-transparent to-alpine-bg"></div>
	</div>
	<div
		class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pt-20 pb-24 text-center"
	>
		<span
			class="fade-up-element mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs"
		>
			{$t('wellness.main_subtitle')}
		</span>
		<h1
			class="fade-up-element font-serif text-5xl font-light tracking-tight text-white md:text-7xl"
		>
			{$t('wellness.main_title')}
		</h1>
	</div>
</div>

<div class="min-h-screen bg-alpine-bg px-6 py-24">
	<div class="mx-auto max-w-4xl">
		<div class="fade-up-element mb-16 text-center">
			<p class="text-xl leading-relaxed font-light text-alpine-text md:text-2xl">
				{$t('wellness.philosophy_title') || copy.philosophy}
			</p>
		</div>

		<div class="fade-up-element mt-20 grid grid-cols-1 gap-12 md:grid-cols-2">
			<div class="border border-alpine-border bg-white p-12 shadow-sm">
				<h3 class="mb-6 font-serif text-3xl text-alpine-text">
					{$t('wellness.trattamenti.title')}
				</h3>
				<p class="leading-relaxed font-light text-alpine-muted">
					{$t('wellness.trattamenti.subtitle')}
				</p>
			</div>
			<div class="border border-alpine-border bg-white p-12 shadow-sm">
				<h3 class="mb-6 font-serif text-3xl text-alpine-text">{$t('wellness.massaggi.title')}</h3>
				<p class="leading-relaxed font-light text-alpine-muted">
					{$t('wellness.massaggi.subtitle')}
				</p>
			</div>
		</div>
	</div>
</div>
