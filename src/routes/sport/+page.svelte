<script lang="ts">
	import { t, locale } from '$lib/i18n';
	import { Snowflake, Bike, Mountain, Wind, Map, Compass, ChevronDown, Check } from 'lucide-svelte';
	import { Motion } from 'svelte-motion';

	// Varianti per le animazioni di orchestrazione (stagger)
	// Questo crea l'effetto "rivelazione a cascata" tipico dei siti premiati
	const containerVariants = {
		hidden: { opacity: 0 },
		visible: {
			opacity: 1,
			transition: {
				staggerChildren: 0.2 // Ritardo tra un elemento figlio e l'altro
			}
		}
	};

	const itemVariants = {
		hidden: { y: 60, opacity: 0 },
		visible: {
			y: 0,
			opacity: 1,
			transition: {
				duration: 1.1,
				ease: [0.22, 1, 0.36, 1] // Quintic ease-out per un movimento organico
			}
		}
	};

	// Effetto Parallasse per l'Hero Image
	let scrollY = $state(0);

	const copy = $derived(
		$locale === 'ru'
			? {
					sciLabel: 'Курорт ski-in / ski-out',
					sciServices: [
						'Прямой доступ к подъемникам',
						'Лыжная комната и подогрев ботинок',
						'Ски-пасс на ресепшене'
					],
					bikeLabel: 'E-Bike и треккинг',
					bikeServices: [
						'Прокат E-Bike у партнеров',
						'Безопасная bike room с зоной мойки',
						'Карты и GPX-треки'
					],
					servicesTitle: 'Сервисы для спортсменов',
					servicesSubtitle: 'Все необходимое в одном месте',
					serviceCards: [
						{
							title: 'Ski Room & Dry',
							text: 'Индивидуальные шкафчики и система сушки и подогрева ботинок, чтобы снаряжение всегда было готово.'
						},
						{
							title: 'Партнерские гиды',
							text: 'Мы сотрудничаем с лучшими местными гидами для зимнего freeride и летних восхождений.'
						},
						{
							title: 'Спортивный завтрак',
							text: 'Усиленный утренний буфет с белками и углеводами для активного дня в горах.'
						}
					]
				}
			: {
					sciLabel: 'Ski-in / Ski-out Resort',
					sciServices: [
						'Accesso diretto agli impianti',
						'Ski Room e Deposito Scarponi Riscaldato',
						'Skipass in Reception'
					],
					bikeLabel: 'E-Bike & Trekking',
					bikeServices: [
						'Noleggio E-Bike convenzionato',
						'Bike Room sicura con area lavaggio',
						'Mappe e sentieri GPX'
					],
					servicesTitle: 'Servizi per lo Sportivo',
					servicesSubtitle: 'Tutto cio che ti serve, in un solo posto',
					serviceCards: [
						{
							title: 'Ski Room & Dry',
							text: 'Armadietti privati e sistema di asciugatura e riscaldamento per scarponi, sempre pronti.'
						},
						{
							title: 'Guide Partner',
							text: 'Collaboriamo con le migliori guide locali per freeride invernale e scalate estive.'
						},
						{
							title: 'Colazione Bio',
							text: 'Buffet mattutino rinforzato con proteine e carboidrati studiati per chi fa sport.'
						}
					]
				}
	);
</script>

<svelte:window bind:scrollY />

<svelte:head>
	<title>{$t('sport.main_title')} | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[85vh] w-full overflow-hidden bg-[#1a1a1a]">
	<div
		class="absolute inset-0 scale-110"
		style="transform: translateY({scrollY * 0.3}px) scale(1.1);"
	>
		<img
			src="/imgs/ski-sport-hero.webp"
			alt="Alpine Sport"
			class="ken-burns h-full w-full object-cover opacity-70"
		/>
		<div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/20 to-alpine-bg"></div>
	</div>

	<div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-32 text-center">
		<Motion initial="hidden" animate="visible" variants={containerVariants}>
			<div>
				<Motion variants={itemVariants}>
					<span
						class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs"
					>
						{$t('sport.main_subtitle')}
					</span>
				</Motion>
				<Motion variants={itemVariants}>
					<h1
						class="mb-16 font-serif text-5xl leading-none font-light tracking-tight text-white md:text-8xl"
					>
						{$t('sport.main_title')}
					</h1>
				</Motion>
				<Motion variants={itemVariants}>
					<div class="flex w-full justify-center">
						<ChevronDown class="h-10 w-10 animate-bounce text-alpine-gold" strokeWidth={1} />
					</div>
				</Motion>
			</div>
		</Motion>
	</div>
</header>

<!-- @ts-ignore -->
<Motion
	initial="hidden"
	whileInView="visible"
	viewport={{ once: true, amount: 0.3 }}
	variants={itemVariants}
>
	<section class="border-b border-alpine-border bg-alpine-bg px-6 py-32">
		<div class="mx-auto max-w-3xl text-center">
			<Compass class="mx-auto mb-12 h-12 w-12 text-alpine-gold" strokeWidth={1} />
			<h3
				class="mx-auto mb-12 max-w-xl font-serif text-3xl leading-snug text-alpine-text md:text-5xl lg:text-6xl"
			>
				{$t('sport.philosophy_title')}
			</h3>
			<p
				class="mx-auto mt-16 max-w-2xl border-t border-alpine-border pt-16 text-sm leading-relaxed font-light text-alpine-muted md:text-lg"
			>
				{$t('sport.philosophy_text')}
			</p>
		</div>
	</section>
</Motion>

<section class="mx-auto max-w-360 space-y-32 bg-alpine-bg px-6 pt-32 pb-32">
	<!-- @ts-ignore -->
	<Motion
		initial="hidden"
		whileInView="visible"
		viewport={{ once: true, amount: 0.3 }}
		variants={itemVariants}
	>
		<div class="flex flex-col items-center gap-16 md:flex-row lg:gap-24">
			<div
				class="group relative w-full cursor-default overflow-hidden bg-alpine-border shadow-xl md:w-3/5"
			>
				<img
					src="https://www.lovevda.it/immagini/DisplayImage/61122?width=1920&guid=74950a9e-1379-467a-8149-9b31b6ae6ff1"
					alt="Sci a Torgnon"
					class="img-elegant aspect-16/10 h-full w-full object-cover"
				/>
				<div
					class="absolute inset-0 bg-black/10 opacity-0 transition-opacity group-hover:opacity-100"
				></div>
			</div>
			<div class="w-full p-4 md:w-2/5 lg:p-10">
				<Snowflake class="mb-8 h-10 w-10 stroke-1 text-alpine-gold" />
				<h2 class="mb-6 font-serif text-4xl text-alpine-text lg:text-5xl">
					{$t('sport.sci.title')}
				</h2>
				<p class="mb-8 text-[11px] font-bold tracking-widest text-alpine-muted uppercase">
					{copy.sciLabel}
				</p>
				<p class="mb-12 max-w-md text-sm leading-relaxed font-light text-alpine-muted md:text-base">
					{$t('sport.sci.subtitle')}
				</p>
				<!-- @ts-ignore -->
				<Motion
					initial="hidden"
					whileInView="visible"
					viewport={{ once: true, amount: 0.8 }}
					variants={containerVariants}
				>
					<ul class="mb-12 space-y-5 text-sm font-medium text-alpine-text">
						{#each copy.sciServices as service (service)}
							<Motion variants={itemVariants}>
								<li class="flex items-center gap-4 border-b border-alpine-border pb-4">
									<div
										class="flex h-6 w-6 items-center justify-center rounded-full bg-alpine-gold/10"
									>
										<Check class="h-4 w-4 text-alpine-gold" strokeWidth={3} />
									</div>
									{service}
								</li>
							</Motion>
						{/each}
					</ul>
				</Motion>
			</div>
		</div>
	</Motion>

	<!-- @ts-ignore -->
	<Motion
		initial="hidden"
		whileInView="visible"
		viewport={{ once: true, amount: 0.3 }}
		variants={itemVariants}
	>
		<div class="flex flex-col items-center gap-16 md:flex-row-reverse lg:gap-24">
			<div
				class="group relative w-full cursor-default overflow-hidden bg-alpine-border shadow-xl md:w-3/5"
			>
				<img
					src="/imgs/mtb-torgnon-1.webp"
					alt="Mountain Bike"
					class="img-elegant aspect-16/10 h-full w-full object-cover"
				/>
				<div
					class="absolute inset-0 bg-black/10 opacity-0 transition-opacity group-hover:opacity-100"
				></div>
			</div>
			<div class="w-full p-4 md:w-2/5 lg:p-10">
				<Bike class="mb-8 h-10 w-10 stroke-1 text-alpine-gold" />
				<h2 class="mb-6 font-serif text-4xl text-alpine-text lg:text-5xl">
					{$t('sport.bike.title')}
				</h2>
				<p class="mb-8 text-[11px] font-bold tracking-widest text-alpine-muted uppercase">
					{copy.bikeLabel}
				</p>
				<p class="mb-12 max-w-md text-sm leading-relaxed font-light text-alpine-muted md:text-base">
					{$t('sport.bike.subtitle')}
				</p>
				<!-- @ts-ignore -->
				<Motion
					initial="hidden"
					whileInView="visible"
					viewport={{ once: true, amount: 0.8 }}
					variants={containerVariants}
				>
					<ul class="mb-12 space-y-5 text-sm font-medium text-alpine-text">
						{#each copy.bikeServices as service (service)}
							<Motion variants={itemVariants}>
								<li class="flex items-center gap-4 border-b border-alpine-border pb-4">
									<div
										class="flex h-6 w-6 items-center justify-center rounded-full bg-alpine-gold/10"
									>
										<Check class="h-4 w-4 text-alpine-gold" strokeWidth={3} />
									</div>
									{service}
								</li>
							</Motion>
						{/each}
					</ul>
				</Motion>
			</div>
		</div>
	</Motion>
</section>

<section class="border-t border-alpine-border bg-white px-6 py-32">
	<div class="mx-auto max-w-screen-2xl">
		<!-- @ts-ignore -->
		<Motion
			initial="hidden"
			whileInView="visible"
			viewport={{ once: true, amount: 0.3 }}
			variants={itemVariants}
		>
			<div class="mx-auto mb-24 max-w-xl text-center">
				<h2 class="mb-5 font-serif text-4xl leading-tight text-alpine-text md:text-5xl">
					{copy.servicesTitle}
				</h2>
				<p class="text-[11px] font-bold tracking-widest text-alpine-muted uppercase">
					{copy.servicesSubtitle}
				</p>
			</div>
		</Motion>

		<!-- @ts-ignore -->
		<Motion
			initial="hidden"
			whileInView="visible"
			viewport={{ once: true, amount: 0.1 }}
			variants={containerVariants}
		>
			<div class="grid grid-cols-1 gap-8 md:grid-cols-3 lg:gap-12">
				{#each [{ icon: Wind, ...copy.serviceCards[0] }, { icon: Map, ...copy.serviceCards[1] }, { icon: Mountain, ...copy.serviceCards[2] }] as { icon: Icon, title, text } (title)}
					<Motion variants={itemVariants}>
						<div
							class="flex flex-col items-center border border-alpine-border bg-white p-12 text-center transition-all duration-500 hover:border-alpine-gold hover:shadow-2xl md:p-16"
						>
							<Icon class="mb-8 h-8 w-8 stroke-1 text-alpine-gold" />
							<h4 class="mb-6 font-serif text-3xl text-alpine-text">{title}</h4>
							<p
								class="mx-auto max-w-xs text-xs leading-relaxed font-light text-alpine-muted lg:text-sm"
							>
								{text}
							</p>
						</div>
					</Motion>
				{/each}
			</div>
		</Motion>
	</div>
</section>
