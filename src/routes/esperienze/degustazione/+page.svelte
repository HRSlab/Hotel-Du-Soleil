<script lang="ts">
    import { locale } from '$lib/i18n';
    import { Utensils, GlassWater, MapPin } from 'lucide-svelte';

    const copy = $derived($locale === 'ru'
        ? {
            title: 'Fontina DOP',
            heroLabel: 'Гастрономическое впечатление',
            introTitle: 'Самое чистое выражение горного молока.',
            introText: 'Fontina, произведенная на альпийских пастбищах Торньона, это настоящее произведение искусства. Мы знакомим гостей с секретами сыроделия и очарованием пещер выдержки, высеченных в скале.',
            sectionTitle: 'На альпийском пастбище',
            sectionText: 'Летом мы организуем утренние экскурсии к местным сыроварням, где можно увидеть дойку и процесс изготовления сыра. Вкус только что сделанного сыра остается в памяти надолго.',
            winePairing: 'Винные сочетания',
            km0: 'Настоящий zero km'
        }
        : {
            title: 'Fontina DOP',
            heroLabel: 'Esperienza Gastronomica',
            introTitle: "L'espressione piu pura del latte di montagna.",
            introText: 'La Fontina prodotta negli alpeggi di Torgnon e un\'opera d\'arte. Vi portiamo a scoprire i segreti della lavorazione e il fascino delle grotte di stagionatura scavate nella roccia.',
            sectionTitle: 'In Alpeggio',
            sectionText: 'Durante i mesi estivi organizziamo escursioni mattutine verso le malghe locali dove potrete assistere alla munta e alla caseificazione. Il sapore del formaggio appena fatto e un\'emozione che rimarra impressa nei vostri sensi.',
            winePairing: 'Abbinamenti Vini',
            km0: 'Km 0 REALE'
        });
</script>

<svelte:head>
    <title>{copy.title} | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div class="absolute inset-0">
        <img src="https://images.unsplash.com/photo-1485962391905-fb1ae13c3453?q=80&w=2000&auto=format&fit=crop" class="ken-burns h-full w-full object-cover opacity-80" alt="Degustazione Fontina DOP" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/40 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            {copy.heroLabel}
        </span>
        <h1 class="font-serif text-5xl md:text-7xl leading-tight font-light text-white fade-up-element">
            {copy.title}
        </h1>
    </div>
</header>

<section class="bg-alpine-bg px-6 py-24">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <Utensils class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            {copy.introTitle}
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            {copy.introText}
        </p>
    </div>
</section>

<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element overflow-hidden bg-alpine-border">
        <img src="https://images.unsplash.com/photo-1452195125355-903496c21e64?q=80&w=1500&auto=format&fit=crop" alt="Cheese Cellar" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90">
    </div>
    <div class="fade-up-element">
        <h2 class="font-serif text-4xl text-alpine-text mb-6 italic">{copy.sectionTitle}</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            {copy.sectionText}
        </p>
        <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
            <div class="flex items-center gap-3">
                 <GlassWater class="w-5 h-5 text-alpine-gold" />
                 <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{copy.winePairing}</span>
            </div>
            <div class="flex items-center gap-3">
                 <MapPin class="w-5 h-5 text-alpine-gold" />
                 <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{copy.km0}</span>
            </div>
        </div>
    </div>
</section>
