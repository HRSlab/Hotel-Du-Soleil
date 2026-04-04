<script lang="ts">
	import { locale } from '$lib/i18n';
	import { Sparkles, UtensilsCrossed } from 'lucide-svelte';

	const copy = $derived(
		$locale === 'ru'
			? {
					title: 'Дегустационное меню',
					heroTitle: 'Альпийская алхимия',
					intro: 'Путешествие по вершинам, лесам и горным потокам в 7 актах.',
					acts: [
						{
							label: 'Акт I',
							title: 'Амюз-буш: воздушная Fontina и хрустящий картофель',
							subtitle: 'Суть территории в одном дыхании.',
							text: 'Невесомое облако Fontina DOP с высокогорных пастбищ на тончайшем хрустящем чипсе из картофеля Торньона. Мгновенный контраст между воздушностью и земной хрустящей текстурой.'
						},
						{
							label: 'Акт II',
							title: 'Закуска: маринованная альпийская форель',
							subtitle: 'Свежесть ледниковых потоков.',
							text: 'Филе форели сухого посола с хвойной цедрой, поданное с холодным кремом из сладкого лука-порея и кубиками зеленого яблока из долины для яркой кислотности.'
						},
						{
							label: 'Акт III',
							title: 'Первое блюдо: открытый равиоло с картофелем и ореховым маслом',
							subtitle: 'Деконструкция памяти.',
							text: 'Полупрозрачный лист яичной пасты покрывает легкую картофельную пену. Блюдо завершается за столом золотой нитью шалфейного beurre noisette и стружкой летнего черного трюфеля.'
						},
						{
							label: 'Акт IV',
							title: 'Фирменное блюдо: современная Torgnolette',
							subtitle: 'Наше посвящение деревне.',
							text: 'Классическая Torgnolette из картофеля, лука-порея и Fontina переосмыслена в разных текстурах картофеля, с текучей сердцевиной из сыра и редукцией из томленого порея.'
						},
						{
							label: 'Акт V',
							title: 'Основное блюдо: филе оленя с редукцией',
							subtitle: 'Король подлеска.',
							text: 'Обжаренное филе с кедровым ароматом, лактоферментированной черникой и копченым картофельным шелком, поданное под клошем с дымом и редукцией красного вина.'
						},
						{
							label: 'Акт VI',
							title: 'Пре-десерт: гранита из альпийских трав',
							subtitle: 'Дыхание ледников.',
							text: 'Бальзамический интермеццо на основе тимьяна, перечной мяты и лимона, чтобы перезапустить чувства перед финальной сладостью.'
						},
						{
							label: 'Акт VII',
							title: 'Десерт: молоко, мед и фундук',
							subtitle: 'Белая гора.',
							text: 'Легкий мусс из горного молока, мед из рододендрона и земля из обжаренного пьемонтского фундука вызывают в памяти чистоту снега на наших вершинах.'
						}
					]
				}
			: {
					title: 'Menu Degustazione',
					heroTitle: 'Alchimia Alpina',
					intro: 'Un viaggio tra vette, boschi e torrenti in 7 atti.',
					acts: [
						{
							label: 'Atto I',
							title: 'Amuse-bouche: Aria di Fontina e Patata Croccante',
							subtitle: "L'essenza del territorio in un soffio.",
							text: "Una nuvola impalpabile di Fontina DOP d'alpeggio, ottenuta tramite lecitina e sferificazione, adagiata su una cialda sottilissima di patata di Torgnon fritta in olio di vinaccioli. Un contrasto immediato tra l'evanescenza dell'aria e la croccantezza della terra."
						},
						{
							label: 'Atto II',
							title: 'Antipasto: Trota Alpina Marinata',
							subtitle: 'Freschezza dai torrenti glaciali.',
							text: "Filetto di trota salmonata marinato a secco con sale bilanciato e scorza di pino. Servito con una vellutata fredda di porri dolci di Cervere e brunoise di mela verde della Valle, per un'esplosione di acidita che pulisce il palato."
						},
						{
							label: 'Atto III',
							title: 'Primo: Raviolo Aperto di Patate e Burro Nocciola',
							subtitle: 'La decostruzione della memoria.',
							text: "Un velo di pasta all'uovo trasparente che ricopre una spuma leggera di patate Kennebec. Il piatto e ultimato al tavolo con un filo d'oro di burro nocciola infuso alla salvia e una grattugiata di tartufo nero estivo o polvere di funghi porcini."
						},
						{
							label: 'Atto IV',
							title: 'Piatto Firma: Torgnolette Contemporanea',
							subtitle: 'Il nostro omaggio al villaggio.',
							text: 'La classica Torgnolette (patate, porri e fontina) viene reinventata: diverse consistenze di patata (fondente, in spuma e soffiata) si fondono con un cuore di fontina fluida e una riduzione di porri brasati al burro chiarificato. Un cuore antico, una forma moderna.'
						},
						{
							label: 'Atto V',
							title: 'Secondo: Filetto di Cervo con Riduzione',
							subtitle: 'Il Re del Sottobosco.',
							text: "Filetto scottato al Cirmolo, mirtilli latto-fermentati e seta di patata affumicata. La nostra opera d'arte stellata, servita sotto cloche di fumo con una riduzione di vino rosso."
						},
						{
							label: 'Atto VI',
							title: 'Pre-Dessert: Granita alle Erbe Alpine',
							subtitle: 'Il respiro dei ghiacciai.',
							text: 'Un intermezzo balsamico a base di timo serpillo, menta piperita e limoni di Sorrento, per resettare i sensi e prepararsi alla dolcezza finale.'
						},
						{
							label: 'Atto VII',
							title: 'Dessert: Latte, Miele e Nocciole',
							subtitle: 'Bianco Montagna.',
							text: 'Una mousse leggera di latte di montagna, un nido di miele di rododendro e terra di nocciole piemontesi tostate. Un dessert monocromatico che richiama la purezza della neve sulle nostre vette.'
						}
					]
				}
	);
</script>

<svelte:head>
	<title>{copy.title} | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[50vh] w-full overflow-hidden bg-[#1a1a1a]">
	<img
		src="/imgs/deer_dish_hero.webp"
		class="ken-burns h-full w-full object-cover opacity-60"
		alt="Cucina Alpina"
	/>
	<div class="absolute inset-0 bg-linear-to-b from-black/80 to-alpine-bg"></div>
	<div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-16 text-center">
		<span
			class="fade-up-element mb-4 block text-[10px] font-bold tracking-[0.4em] text-white/80 uppercase"
			>{copy.title}</span
		>
		<h1 class="fade-up-element font-serif text-5xl leading-tight font-light text-white md:text-7xl">
			{copy.heroTitle}
		</h1>
	</div>
</header>

<main class="min-h-screen bg-alpine-bg pb-32">
	<div class="fade-up-element mx-auto max-w-4xl px-6 pt-12 text-center">
		<Sparkles class="mx-auto mb-8 h-8 w-8 text-alpine-gold" />
		<p class="mb-6 font-serif text-2xl text-alpine-text italic">{copy.intro}</p>
		<div class="deco-line mx-auto mb-16"></div>

		<div class="space-y-16 border-t border-alpine-border pt-16 text-left">
			{#each copy.acts as act, index (act.label)}
				<div class="group relative border-t border-alpine-border/30 pt-16 text-center">
					{#if index === 0}
						<div class="hidden"></div>
					{/if}
					{#if index === 3}
						<UtensilsCrossed
							class="absolute -top-6 left-1/2 h-12 w-12 -translate-x-1/2 bg-alpine-bg px-2 text-alpine-border/50"
						/>
					{/if}
					<span
						class="mb-3 block text-[10px] font-bold tracking-[0.2em] text-alpine-gold uppercase {index ===
						3
							? 'mt-4'
							: ''}">{act.label}</span
					>
					<h3 class="font-serif {index === 3 ? 'text-3xl' : 'text-2xl'} mb-2 text-alpine-text">
						{act.title}
					</h3>
					<p class="mb-6 text-xs font-light tracking-widest text-alpine-muted uppercase">
						{act.subtitle}
					</p>
					<p
						class="text-sm {index === 3
							? 'font-medium text-alpine-text'
							: 'font-light text-alpine-muted'} mx-auto max-w-2xl leading-relaxed {index === 6
							? 'mt-4'
							: ''}"
					>
						{act.text}
					</p>
				</div>
			{/each}
		</div>
	</div>
</main>
