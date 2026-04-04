<script lang="ts">
	import { t, locale } from '$lib/i18n';
	import { Leaf, Recycle, Sun, Droplet } from 'lucide-svelte';

	const copy = $derived(
		$locale === 'ru'
			? {
					subtitle: 'В гармонии с окружающей средой',
					title: 'Экологичность',
					philosophyTitle: 'Мы уважаем горы и заботимся о будущем.',
					philosophyText:
						'Мы считаем себя хранителями драгоценной и хрупкой территории. Поэтому каждый день применяем практики, снижающие воздействие на среду и поддерживающие местную экономику.',
					items: [
						{
							title: 'Чистая энергия',
							text: 'Солнечные панели для нагрева воды и светодиодное освещение с низким энергопотреблением.'
						},
						{
							title: 'Без пластика',
							text: 'Мы отказались от одноразовой пластиковой упаковки в пользу дозаторов и стеклянных бутылок.'
						},
						{
							title: 'Родниковая вода',
							text: 'Мы ценим чистейшую воду источников Торньона, фильтруем ее и подаем к столу.'
						},
						{
							title: 'Местные и органические продукты',
							text: 'Мы отдаем приоритет производителям долины, чтобы сократить выбросы, связанные с транспортировкой.'
						}
					]
				}
			: {
					subtitle: "In Armonia con l'Ambiente",
					title: 'Sostenibilita',
					philosophyTitle: 'Rispettiamo la montagna, curiamo il futuro.',
					philosophyText:
						"Siamo custodi di un territorio prezioso e fragile. Per questo motivo adottiamo quotidianamente pratiche sostenibili che riducono il nostro impatto ambientale e promuovono l'economia locale.",
					items: [
						{
							title: 'Energia Pulita',
							text: 'Pannelli solari per la produzione di acqua calda e illuminazione LED a basso consumo.'
						},
						{
							title: 'Zero Plastica',
							text: 'Abbiamo eliminato le monoporzioni di plastica in favore di dispenser e bottiglie di vetro.'
						},
						{
							title: 'Acqua di Fonte',
							text: "Valorizziamo l'acqua purissima delle sorgenti di Torgnon, filtrata e servita al tavolo."
						},
						{
							title: 'Km 0 & Biologico',
							text: 'Privilegiamo i produttori della valle per ridurre le emissioni legate ai trasporti.'
						}
					]
				}
	);
</script>

<svelte:head>
	<title>{copy.title} | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
	<div class="absolute inset-0">
		<img
			src="https://images.unsplash.com/photo-1518173946687-a4c8892bbd9f?q=80&w=2000&auto=format&fit=crop"
			class="ken-burns h-full w-full object-cover opacity-80"
			alt="Sustainability at Hotel du Soleil"
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
		<Leaf class="mx-auto mb-10 h-10 w-10 text-alpine-gold" />
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

<section
	class="mx-auto grid max-w-7xl grid-cols-1 gap-8 bg-alpine-bg px-6 pb-32 md:grid-cols-2 lg:grid-cols-4"
>
	<div class="fade-up-element border border-alpine-border bg-white p-8 text-center shadow-sm">
		<Sun class="mx-auto mb-6 h-8 w-8 text-alpine-gold" />
		<h4 class="mb-4 font-serif text-xl italic">{copy.items[0].title}</h4>
		<p class="text-xs leading-relaxed font-light text-alpine-muted">{copy.items[0].text}</p>
	</div>
	<div class="fade-up-element border border-alpine-border bg-white p-8 text-center shadow-sm">
		<Recycle class="mx-auto mb-6 h-8 w-8 text-alpine-gold" />
		<h4 class="mb-4 font-serif text-xl italic">{copy.items[1].title}</h4>
		<p class="text-xs leading-relaxed font-light text-alpine-muted">{copy.items[1].text}</p>
	</div>
	<div class="fade-up-element border border-alpine-border bg-white p-8 text-center shadow-sm">
		<Droplet class="mx-auto mb-6 h-8 w-8 text-alpine-gold" />
		<h4 class="mb-4 font-serif text-xl italic">{copy.items[2].title}</h4>
		<p class="text-xs leading-relaxed font-light text-alpine-muted">{copy.items[2].text}</p>
	</div>
	<div class="fade-up-element border border-alpine-border bg-white p-8 text-center shadow-sm">
		<Leaf class="mx-auto mb-6 h-8 w-8 text-alpine-gold" />
		<h4 class="mb-4 font-serif text-xl italic">{copy.items[3].title}</h4>
		<p class="text-xs leading-relaxed font-light text-alpine-muted">{copy.items[3].text}</p>
	</div>
</section>
