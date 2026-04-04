<script lang="ts">
	import { t, locale } from '$lib/i18n';
	import { Users, Tv, GlassWater, Maximize } from 'lucide-svelte';

	const copy = $derived(
		$locale === 'ru'
			? {
					cards: [
						{
							title: 'Технологии',
							text: 'Залы для встреч оснащены проекторами, быстрым Wi-Fi и современными аудиосистемами.'
						},
						{
							title: 'Гибкость',
							text: 'Модульные пространства подходят как для небольших советов директоров, так и для корпоративных team building мероприятий.'
						},
						{
							title: 'Кейтеринг',
							text: 'Coffee break, легкий обед или торжественный ужин готовятся из лучших местных продуктов.'
						}
					]
				}
			: {
					cards: [
						{
							title: 'Tecnologia',
							text: 'Sale meeting dotate di proiettori, connessione Wi-Fi ad alta velocita e sistemi audio moderni.'
						},
						{
							title: 'Flessibilita',
							text: 'Spazi modulabili adatti a piccoli meeting board o eventi di team building aziendali.'
						},
						{
							title: 'Catering',
							text: 'Coffee break, light lunch o cene di gala preparati con i migliori ingredienti del territorio.'
						}
					]
				}
	);
</script>

<svelte:head>
	<title>{$t('eventi.title')} | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
	<div class="absolute inset-0">
		<img
			src="/imgs/Meeting_Room.webp"
			class="ken-burns h-full w-full object-cover opacity-80"
			alt="Meetings and Events"
		/>
		<div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/40 to-alpine-bg"></div>
	</div>

	<div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
		<span
			class="fade-up-element mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs"
		>
			{$t('eventi.subtitle')}
		</span>
		<h1 class="fade-up-element font-serif text-5xl leading-tight font-light text-white md:text-7xl">
			{$t('eventi.title')}
		</h1>
	</div>
</header>

<section class="bg-alpine-bg px-6 py-20 lg:py-32">
	<div class="fade-up-element mx-auto max-w-3xl text-center">
		<Users class="mx-auto mb-10 h-10 w-10 text-alpine-gold" />
		<h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
			{$t('eventi.title')}
		</h3>
		<p
			class="mx-auto mt-12 max-w-xl border-t border-alpine-border pt-12 text-sm leading-relaxed font-light text-alpine-muted md:text-base"
		>
			{$t('eventi.description')}
		</p>
	</div>
</section>

<section
	class="mx-auto grid max-w-7xl grid-cols-1 gap-12 bg-alpine-bg px-6 pb-20 text-center md:grid-cols-3 lg:pb-32"
>
	<div class="fade-up-element border border-alpine-border bg-white p-8 shadow-sm">
		<Tv class="mx-auto mb-6 h-8 w-8 text-alpine-gold" />
		<h4 class="mb-4 font-serif text-2xl text-alpine-text">{copy.cards[0].title}</h4>
		<p class="text-xs leading-relaxed font-light text-alpine-muted">
			{copy.cards[0].text}
		</p>
	</div>
	<div class="fade-up-element border border-alpine-border bg-white p-8 shadow-sm">
		<Maximize class="mx-auto mb-6 h-8 w-8 text-alpine-gold" />
		<h4 class="mb-4 font-serif text-2xl text-alpine-text">{copy.cards[1].title}</h4>
		<p class="text-xs leading-relaxed font-light text-alpine-muted">
			{copy.cards[1].text}
		</p>
	</div>
	<div class="fade-up-element border border-alpine-border bg-white p-8 shadow-sm">
		<GlassWater class="mx-auto mb-6 h-8 w-8 text-alpine-gold" />
		<h4 class="mb-4 font-serif text-2xl text-alpine-text">{copy.cards[2].title}</h4>
		<p class="text-xs leading-relaxed font-light text-alpine-muted">
			{copy.cards[2].text}
		</p>
	</div>
</section>
