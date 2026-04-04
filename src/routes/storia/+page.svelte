<script lang="ts">
	import { locale } from '$lib/i18n';
	import { History, Heart } from 'lucide-svelte';

	const copy = $derived(
		$locale === 'ru'
			? {
					title: 'История',
					subtitle: 'Память места',
					philosophyTitle: 'История гостеприимства, рожденная в горах.',
					philosophyText:
						'Hotel du Soleil вырос вместе с Торньоном, сохранив семейный дух и спокойный ритм настоящего альпийского отдыха. Каждое поколение добавляло заботу, не теряя связи с местной традицией.',
					rootsTitle: 'Наши корни',
					rootsLabel: 'С 1980 года',
					rootsText:
						'Отель возник как искренний семейный проект: дать гостям теплый, простой и надежный дом у склонов. Сегодня эта идея остается прежней: подлинное гостеприимство, внимание к деталям и тесная связь с природой Валле-д’Аоста.'
				}
			: {
					title: 'Storia',
					subtitle: 'La Memoria di un Luogo',
					philosophyTitle: 'Una storia di ospitalita nata tra le montagne.',
					philosophyText:
						"L'Hotel du Soleil e cresciuto insieme a Torgnon, mantenendo vivo lo spirito familiare e il ritmo lento di una vera vacanza alpina. Ogni generazione ha aggiunto cura senza perdere il legame con la tradizione locale.",
					rootsTitle: 'Le Nostre Radici',
					rootsLabel: 'Dal 1980',
					rootsText:
						"L'hotel nasce come progetto di famiglia: offrire agli ospiti una casa calda, semplice e affidabile a pochi passi dalle piste. Ancora oggi questa visione resta la stessa: ospitalita autentica, attenzione ai dettagli e un rapporto diretto con la natura valdostana."
				}
	);
</script>

<svelte:head>
	<title>{copy.title} | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
	<div class="absolute inset-0">
		<img
			src="https://images.unsplash.com/photo-1554034483-04fda0d3507b?q=80&w=2000&auto=format&fit=crop"
			class="ken-burns h-full w-full object-cover opacity-80 grayscale"
			alt="History of Hotel du Soleil"
		/>
		<div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/40 to-alpine-bg"></div>
	</div>

	<div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
		<span
			class="fade-up-element mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs"
		>
			{copy.subtitle}
		</span>
		<h1 class="fade-up-element font-serif text-5xl leading-tight font-light text-white md:text-7xl">
			{copy.title}
		</h1>
	</div>
</header>

<section class="bg-alpine-bg px-6 py-24">
	<div class="fade-up-element mx-auto max-w-3xl text-center">
		<History class="mx-auto mb-10 h-10 w-10 text-alpine-gold" />
		<h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
			{copy.philosophyTitle}
		</h3>
		<p
			class="mx-auto mt-12 max-w-xl border-t border-alpine-border pt-12 text-sm leading-relaxed font-light text-alpine-muted md:text-base"
		>
			{copy.philosophyText}
		</p>
	</div>
</section>

<section class="mx-auto max-w-7xl space-y-32 bg-alpine-bg px-6 pb-32">
	<div class="fade-up-element flex flex-col items-center gap-12 md:flex-row">
		<div class="group relative w-full cursor-default overflow-hidden bg-alpine-border md:w-1/2">
			<img
				src="https://images.unsplash.com/photo-1544984243-ec57ea16fe75?q=80&w=1500&auto=format&fit=crop"
				alt="Old Look of Torgnon"
				class="img-elegant aspect-4/3 h-full w-full object-cover grayscale transition-all duration-700 hover:grayscale-0"
			/>
		</div>
		<div class="w-full md:w-1/2">
			<Heart class="mb-6 h-8 w-8 stroke-[1.5px] text-alpine-gold" />
			<h2 class="mb-4 font-serif text-4xl text-alpine-text">{copy.rootsTitle}</h2>
			<p class="mb-6 text-[10px] font-bold tracking-widest text-alpine-muted uppercase">
				{copy.rootsLabel}
			</p>
			<p class="mb-8 text-sm leading-relaxed font-light text-alpine-muted">
				{copy.rootsText}
			</p>
		</div>
	</div>
</section>
