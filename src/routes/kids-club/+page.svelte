<script lang="ts">
	import { t, locale } from '$lib/i18n';
	import { Baby, Palette, Puzzle } from 'lucide-svelte';

	const copy = $derived(
		$locale === 'ru'
			? {
					cards: [
						{
							title: 'Творческие мастерские',
							text: 'От рисования до создания маленьких горных сувениров: мы развиваем воображение, моторику и любознательность детей.'
						},
						{
							title: 'Игры и испытания',
							text: 'Большой выбор настольных игр и групповых занятий помогает детям общаться, играть и веселиться в безопасной обстановке.'
						},
						{
							title: 'Услуги няни',
							text: 'По запросу мы организуем индивидуальный babysitting, адаптированный к ритму и потребностям каждой семьи.'
						}
					]
				}
			: {
					cards: [
						{
							title: 'Laboratori Creativi',
							text: 'Dalla pittura alla creazione di piccoli ricordi montani, stimoliamo la manualita e la fantasia dei bambini.'
						},
						{
							title: 'Giochi & Sfide',
							text: "Un'ampia selezione di giochi da tavolo e attivita di gruppo per socializzare e divertirsi in sicurezza."
						},
						{
							title: 'Baby Sitting',
							text: 'Su richiesta, offriamo un servizio di baby sitting personalizzato per le esigenze di ogni famiglia.'
						}
					]
				}
	);
</script>

<svelte:head>
	<title>{$t('kids_club.title')} | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
	<div class="absolute inset-0">
		<img
			src="/imgs/Winter_Park.jpeg"
			class="ken-burns h-full w-full object-cover opacity-80"
			alt="Kids Club"
		/>
		<div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/40 to-alpine-bg"></div>
	</div>

	<div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
		<span
			class="fade-up-element mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs"
		>
			{$t('kids_club.subtitle')}
		</span>
		<h1 class="fade-up-element font-serif text-5xl leading-tight font-light text-white md:text-7xl">
			{$t('kids_club.title')}
		</h1>
	</div>
</header>

<section class="bg-alpine-bg px-6 py-20 lg:py-32">
	<div class="fade-up-element mx-auto max-w-3xl text-center">
		<Baby class="mx-auto mb-10 h-10 w-10 text-alpine-gold" />
		<h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
			{$t('kids_club.title')}
		</h3>
		<p
			class="mx-auto mt-12 max-w-xl border-t border-alpine-border pt-12 text-sm leading-relaxed font-light text-alpine-muted md:text-base"
		>
			{$t('kids_club.description')}
		</p>
	</div>
</section>

<section
	class="mx-auto grid max-w-7xl grid-cols-1 gap-12 bg-alpine-bg px-6 pb-20 text-center md:grid-cols-3 lg:pb-32"
>
	<div class="fade-up-element border border-alpine-border bg-white p-8 shadow-sm">
		<Palette class="mx-auto mb-6 h-8 w-8 text-alpine-gold" />
		<h4 class="mb-4 font-serif text-2xl text-alpine-text">{copy.cards[0].title}</h4>
		<p class="text-xs leading-relaxed font-light text-alpine-muted">
			{copy.cards[0].text}
		</p>
	</div>
	<div class="fade-up-element border border-alpine-border bg-white p-8 shadow-sm">
		<Puzzle class="mx-auto mb-6 h-8 w-8 text-alpine-gold" />
		<h4 class="mb-4 font-serif text-2xl text-alpine-text">{copy.cards[1].title}</h4>
		<p class="text-xs leading-relaxed font-light text-alpine-muted">
			{copy.cards[1].text}
		</p>
	</div>
	<div class="fade-up-element border border-alpine-border bg-white p-8 shadow-sm">
		<Baby class="mx-auto mb-6 h-8 w-8 text-alpine-gold" />
		<h4 class="mb-4 font-serif text-2xl text-alpine-text">{copy.cards[2].title}</h4>
		<p class="text-xs leading-relaxed font-light text-alpine-muted">
			{copy.cards[2].text}
		</p>
	</div>
</section>
