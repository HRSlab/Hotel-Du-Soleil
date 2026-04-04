<script lang="ts">
	import { locale } from '$lib/i18n';
	import { Coffee, Flame, Gamepad2, Sun, Croissant } from 'lucide-svelte';

	const copy = $derived(
		$locale === 'ru'
			? {
					title: 'Лаунж и камин',
					introTitle: 'Верните себе тепло.',
					introText:
						'Сердце Hotel du Soleil. Наш большой центральный камин из кирпича и меди создан для того, чтобы замедлить время. Согрейтесь у огня с горячим шоколадом или авторским дистиллятом после дня на свежем воздухе.',
					sections: [
						{
							title: 'Отдых и общение',
							label: 'Бильярд и настольный футбол',
							text: 'Лаунж-зона подходит для всей семьи. Играйте в бильярд или настольный футбол в просторной непринужденной атмосфере, пока на фоне потрескивает камин.'
						},
						{
							title: 'Аперитив на солнце',
							label: 'Коктейли и отдых в саду',
							text: 'В теплые дни бар выходит на улицу. Наслаждайтесь яркими освежающими коктейлями на шезлонгах в саду с видом на традиционную архитектуру Валле-д’Аоста из дерева и камня.'
						},
						{
							title: 'Сладкое пробуждение',
							label: 'Завтрак у огня',
							text: 'Начните день в аромате дерева и тепле очага. Просторные рустикальные столы ждут вас для момента чистой энергии перед прогулками по Тоньону.'
						}
					]
				}
			: {
					title: 'Lounge & Camino',
					introTitle: 'Ritrova il tepore.',
					introText:
						"Il cuore pulsante dell'Hotel du Soleil. Il nostro grande camino centrale in mattoni e rame e il luogo ideale dove fermare il tempo. Lasciatevi avvolgere dal crepitio del fuoco con una cioccolata calda alpina o un distillato artigianale dopo una giornata trascorsa all'aria aperta.",
					sections: [
						{
							title: 'Svago e Convivialita',
							label: 'Biliardo & Calcio Balilla',
							text: 'La nostra area lounge e pensata per il relax di tutta la famiglia. Sfidatevi in una partita a biliardo o a calcio balilla in un ambiente informale e spazioso, sempre accompagnati dal calore del camino sullo sfondo.'
						},
						{
							title: 'Aperitivo al Sole',
							label: 'Cocktail & Relax in Giardino',
							text: "Nelle giornate piu miti, il nostro bar si estende verso l'esterno. Godetevi i nostri cocktail colorati e rinfrescanti comodamente sdraiati sui lettini del nostro giardino, con la vista inconfondibile della tradizionale architettura valdostana in pietra e legno."
						},
						{
							title: 'Il Dolce Risveglio',
							label: 'Colazione accanto al fuoco',
							text: 'Iniziate la giornata circondati dal profumo del legno e dal calore del focolare. I nostri ampi tavoli rustici vi accolgono per un momento di pura energia prima di esplorare le meraviglie di Torgnon.'
						}
					]
				}
	);
</script>

<svelte:head>
	<title>{copy.title} | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
	<img
		src="/imgs/bar-and-lounge/fireplace-bar.webp"
		class="ken-burns h-full w-full object-cover opacity-80"
		alt="Il grande camino centrale"
	/>
	<div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/40 to-alpine-bg"></div>
	<div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
		<h1 class="fade-up-element font-serif text-5xl leading-tight font-light text-white md:text-7xl">
			{copy.title}
		</h1>
	</div>
</header>

<section class="bg-alpine-bg px-6 py-24">
	<div class="fade-up-element mx-auto max-w-3xl text-center">
		<Flame class="mx-auto mb-10 h-10 w-10 text-alpine-gold" />
		<h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
			{copy.introTitle}
		</h3>
		<p
			class="mt-12 border-t border-alpine-border pt-12 text-sm leading-relaxed font-light text-alpine-muted md:text-base"
		>
			{copy.introText}
		</p>
	</div>
</section>

<section class="mx-auto max-w-7xl space-y-32 bg-alpine-bg px-6 pb-32">
	<div class="fade-up-element flex flex-col items-center gap-12 md:flex-row lg:gap-20">
		<div class="group relative w-full overflow-hidden bg-alpine-border md:w-1/2">
			<img
				src="/imgs/bar-and-lounge/bar-pooltable.webp"
				alt="Sala Biliardo"
				class="img-elegant aspect-4/3 h-full w-full object-cover"
			/>
		</div>
		<div class="w-full md:w-1/2">
			<Gamepad2 class="mb-6 h-8 w-8 text-alpine-gold" />
			<h2 class="mb-4 font-serif text-4xl text-alpine-text">{copy.sections[0].title}</h2>
			<p class="mb-6 text-[10px] font-bold tracking-widest text-alpine-muted uppercase">
				{copy.sections[0].label}
			</p>
			<p class="mb-8 text-sm leading-relaxed font-light text-alpine-muted">
				{copy.sections[0].text}
			</p>
		</div>
	</div>

	<div class="fade-up-element flex flex-col items-center gap-12 md:flex-row-reverse lg:gap-20">
		<div class="group relative w-full overflow-hidden bg-alpine-border md:w-1/2">
			<img
				src="/imgs/bar-and-lounge/aperitivo-garden.webp"
				alt="Aperitivo all'aperto"
				class="img-elegant aspect-4/3 h-full w-full object-cover"
			/>
		</div>
		<div class="w-full md:w-1/2">
			<Sun class="mb-6 h-8 w-8 text-alpine-gold" />
			<h2 class="mb-4 font-serif text-4xl text-alpine-text">{copy.sections[1].title}</h2>
			<p class="mb-6 text-[10px] font-bold tracking-widest text-alpine-muted uppercase">
				{copy.sections[1].label}
			</p>
			<p class="mb-8 text-sm leading-relaxed font-light text-alpine-muted">
				{copy.sections[1].text}
			</p>
		</div>
	</div>

	<div class="fade-up-element flex flex-col items-center gap-12 md:flex-row lg:gap-20">
		<div class="group relative w-full overflow-hidden bg-alpine-border md:w-1/2">
			<img
				src="/imgs/bar-and-lounge/fireplace-bar.webp"
				alt="Tavoli per colazione"
				class="img-elegant aspect-4/3 h-full w-full object-cover"
			/>
		</div>
		<div class="w-full md:w-1/2">
			<Croissant class="mb-6 h-8 w-8 text-alpine-gold" />
			<h2 class="mb-4 font-serif text-4xl text-alpine-text">{copy.sections[2].title}</h2>
			<p class="mb-6 text-[10px] font-bold tracking-widest text-alpine-muted uppercase">
				{copy.sections[2].label}
			</p>
			<p class="mb-8 text-sm leading-relaxed font-light text-alpine-muted">
				{copy.sections[2].text}
			</p>
		</div>
	</div>
</section>
