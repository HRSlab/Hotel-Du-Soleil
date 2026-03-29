<script lang="ts">
    import { t } from '$lib/i18n';
    import { Heart, Clock, Droplets, Flame, Leaf, ArrowRight, ShieldCheck, Star, Hand, Sparkles, Waves } from 'lucide-svelte';

    let scrollY = $state(0);
</script>

<svelte:window bind:scrollY />

<svelte:head>
    <title>{$t('wellness.massaggi.title')} | Hotel du Soleil</title>
    <meta name="description" content="Massaggi sportivi e decontratturanti nell'area wellness dell'Hotel du Soleil a Torgnon. Recupero muscolare dopo una giornata in montagna, mani esperte e oli essenziali alpini." />
</svelte:head>

<!-- ═══════════════════ HERO ═══════════════════ -->
<header class="relative h-[85vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div
        class="absolute inset-0 scale-110"
        style="transform: translateY({scrollY * 0.25}px) scale(1.1);"
    >
        <img src="https://images.unsplash.com/photo-1544161515-4af6b1d46bdc?q=80&w=2000&auto=format&fit=crop" class="h-full w-full object-cover opacity-55" alt="Massaggio sportivo" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/30 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-28 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            {$t('wellness.massaggi.subtitle')}
        </span>
        <h1 class="font-serif text-5xl md:text-8xl leading-tight font-light text-white fade-up-element">
            {$t('wellness.massaggi.title')}
        </h1>
        <p class="mt-6 text-white/50 text-sm font-light max-w-md fade-up-element">
            Il recupero perfetto dopo una giornata in montagna
        </p>
    </div>
</header>

<!-- ═══════════════════ INTRO ═══════════════════ -->
<section class="bg-alpine-bg px-6 py-28">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <Heart class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            Le mani che conoscono la fatica della montagna.
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            Dopo ore sugli sci, sui sentieri o in bicicletta, il corpo ha bisogno di cure esperte. 
            I nostri massaggiatori professionisti conoscono le esigenze degli sportivi 
            e utilizzano tecniche specifiche per sciogliere tensioni, 
            accelerare il recupero e restituirvi l'energia per il giorno dopo.
        </p>
    </div>
</section>

<!-- ═══════════════════ LA FILOSOFIA ═══════════════════ -->
<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
        <img src="https://images.unsplash.com/photo-1600334129128-685c5582fd35?q=80&w=1500&auto=format&fit=crop" alt="Ambiente massaggi wellness" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
    </div>

    <div class="fade-up-element">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">La Nostra Filosofia</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">Sport & Benessere,<br/>Un Legame Naturale</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            Non offriamo un menu generico di trattamenti. Ogni massaggio è pensato 
            per chi vive la montagna attivamente: sciatori, escursionisti, ciclisti, arrampicatori. 
            I nostri terapisti valutano le vostre esigenze specifiche prima di ogni seduta.
        </p>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
            Utilizziamo oli essenziali locali — arnica montana, pino cembro, ginepro alpino — 
            che uniscono il profumo della montagna alle proprietà antinfiammatorie 
            e decontratturanti della tradizione erboristica valdostana.
        </p>
        <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
            <div class="flex items-center gap-3">
                <Leaf class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Oli alpini naturali</span>
            </div>
            <div class="flex items-center gap-3">
                <ShieldCheck class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Terapisti certificati</span>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ STATS ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-20 px-6">
    <div class="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-12 text-center">
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">6</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Tipologie di massaggio</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">50'</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Durata media</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">2</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Cabine private</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">7/7</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Giorni su prenotazione</p>
        </div>
    </div>
</section>

<!-- ═══════════════════ I MASSAGGI ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">I Nostri Massaggi</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">Ogni trattamento, un'esperienza su misura</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12">
            <!-- Decontratturante -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Flame class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">Il Più Richiesto</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Decontratturante Sportivo</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">50 minuti · €85</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        Massaggio profondo mirato sulle zone di maggiore tensione muscolare. 
                        Ideale dopo una giornata intensa sugli sci o sul bike. 
                        Manovre decise su gambe, schiena e spalle per sciogliere contratture 
                        e favorire il recupero.
                    </p>
                    <div class="pt-6 border-t border-alpine-border">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">Ideale per</p>
                        <p class="text-xs text-alpine-text mt-2 font-light">Sciatori · Ciclisti · Escursionisti</p>
                    </div>
                </div>
            </div>

            <!-- Hot Stone -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Sparkles class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">Calore & Relax</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Hot Stone Alpino</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">60 minuti · €95</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        Pietre vulcaniche calde posizionate lungo i meridiani del corpo, 
                        combinate con manovre lente e avvolgenti. Il calore penetra in profondità, 
                        sciogliendo le tensioni accumulate dal freddo e dall'attività fisica.
                    </p>
                    <div class="pt-6 border-t border-alpine-border">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">Ideale per</p>
                        <p class="text-xs text-alpine-text mt-2 font-light">Chi soffre il freddo · Tensioni croniche</p>
                    </div>
                </div>
            </div>

            <!-- Arnica -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Leaf class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">Tradizione Alpina</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Rituale all'Arnica Montana</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">50 minuti · €90</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        Olio di arnica montana raccolto negli alpeggi valdostani, con proprietà 
                        antinfiammatorie e lenitive riconosciute da secoli. 
                        Massaggio medio-profondo su tutto il corpo, 
                        perfetto per lenire dolori muscolari e piccoli traumi sportivi.
                    </p>
                    <div class="pt-6 border-t border-alpine-border">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">Ideale per</p>
                        <p class="text-xs text-alpine-text mt-2 font-light">Dolori muscolari · Post-infortunio</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Seconda riga -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12 mt-8 lg:mt-12">
            <!-- Rilassante -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Waves class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">Relax Totale</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Rilassante Totale</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">50 minuti · €80</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        Manovre lente e avvolgenti con olio di pino cembro. 
                        Non è un massaggio sportivo — è un rituale di puro relax. 
                        Pensato per chi vuole staccare completamente e lasciarsi andare 
                        al profumo del bosco alpino.
                    </p>
                    <div class="pt-6 border-t border-alpine-border">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">Ideale per</p>
                        <p class="text-xs text-alpine-text mt-2 font-light">Stress · Insonnia · Relax profondo</p>
                    </div>
                </div>
            </div>

            <!-- Gambe -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Hand class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">Mirato</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Defaticante Gambe</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">30 minuti · €55</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        Trattamento specifico per gambe pesanti e affaticate. 
                        Manovre drenanti e decontratturanti concentrate su polpacci, 
                        quadricipiti e piedi. Il formato breve lo rende perfetto 
                        come rituale quotidiano après-ski.
                    </p>
                    <div class="pt-6 border-t border-alpine-border">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">Ideale per</p>
                        <p class="text-xs text-alpine-text mt-2 font-light">Après-ski · Gambe pesanti · Recupero rapido</p>
                    </div>
                </div>
            </div>

            <!-- Coppia -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Heart class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">Romantico</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Massaggio in Coppia</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">50 minuti · €160 (per 2)</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        Due cabine comunicanti, due terapisti sincronizzati, 
                        un momento di relax condiviso. Scegliete ognuno il tipo di massaggio 
                        che preferite e godetevi l'esperienza fianco a fianco. 
                        Include tisana alpina al termine.
                    </p>
                    <div class="pt-6 border-t border-alpine-border">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">Ideale per</p>
                        <p class="text-xs text-alpine-text mt-2 font-light">Coppie · Anniversari · Occasioni speciali</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ L'ESPERIENZA ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
        <div class="fade-up-element">
            <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">Il Rituale</span>
            <h2 class="font-serif text-4xl text-alpine-text mb-6">Ogni Massaggio<br/>È un'Esperienza Completa</h2>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
                Non iniziamo mai direttamente con il trattamento. 
                Ogni seduta prevede un breve colloquio per capire le vostre esigenze, 
                le zone di tensione e l'intensità desiderata. 
                Al termine, una tisana calda alle erbe alpine e qualche minuto 
                di riposo nella zona relax completano l'esperienza.
            </p>
            <div class="space-y-6">
                <div class="flex items-start gap-4">
                    <div class="w-8 h-8 rounded-full border border-alpine-gold flex items-center justify-center shrink-0 mt-0.5">
                        <span class="text-xs font-serif text-alpine-gold">1</span>
                    </div>
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">Accoglienza</p>
                        <p class="text-xs text-alpine-muted font-light">Tisana di benvenuto e colloquio con il terapista</p>
                    </div>
                </div>
                <div class="flex items-start gap-4">
                    <div class="w-8 h-8 rounded-full border border-alpine-gold flex items-center justify-center shrink-0 mt-0.5">
                        <span class="text-xs font-serif text-alpine-gold">2</span>
                    </div>
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">Il Trattamento</p>
                        <p class="text-xs text-alpine-muted font-light">30-60 minuti di massaggio personalizzato</p>
                    </div>
                </div>
                <div class="flex items-start gap-4">
                    <div class="w-8 h-8 rounded-full border border-alpine-gold flex items-center justify-center shrink-0 mt-0.5">
                        <span class="text-xs font-serif text-alpine-gold">3</span>
                    </div>
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">Riposo</p>
                        <p class="text-xs text-alpine-muted font-light">Zona relax con tisana calda e coperta morbida</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
            <img src="https://images.unsplash.com/photo-1540555700478-4be289fbec6d?q=80&w=1500&auto=format&fit=crop" alt="Zona relax dopo il massaggio" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
        </div>
    </div>
</section>

<!-- ═══════════════════ GLI OLI ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-5xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">I Nostri Oli</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">Dalla montagna, per il vostro corpo</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="fade-up-element text-center p-10 bg-white border border-alpine-border">
                <Leaf class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Arnica Montana</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Raccolta a mano negli alpeggi sopra i 1.800 metri. 
                    Potente antinfiammatorio naturale, è il rimedio della tradizione alpina 
                    per dolori muscolari e contusioni.
                </p>
            </div>
            <div class="fade-up-element text-center p-10 bg-white border border-alpine-border">
                <Droplets class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Pino Cembro</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    L'olio essenziale del "re delle Alpi". Distillato dal legno e dagli aghi, 
                    ha proprietà rilassanti scientificamente dimostrate: 
                    riduce la frequenza cardiaca e favorisce il sonno profondo.
                </p>
            </div>
            <div class="fade-up-element text-center p-10 bg-white border border-alpine-border">
                <Star class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Ginepro Alpino</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Dalle bacche del ginepro d'alta quota, un olio dal profumo fresco e resinoso. 
                    Stimola la circolazione, drena i liquidi 
                    e ridona leggerezza alle gambe affaticate.
                </p>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ INFO PRATICHE ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-5xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">Info Pratiche</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">Tutto quello che serve sapere</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="fade-up-element bg-alpine-bg p-10 border border-alpine-border">
                <h4 class="font-serif text-xl text-alpine-text mb-6 flex items-center gap-3">
                    <Clock class="w-5 h-5 text-alpine-gold" />
                    Orari & Prenotazioni
                </h4>
                <div class="space-y-4 text-sm text-alpine-muted font-light">
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Disponibilità</span>
                        <span class="font-bold text-alpine-text">Tutti i giorni</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Fascia oraria</span>
                        <span class="font-bold text-alpine-text">10:00 – 20:00</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Prenotazione</span>
                        <span class="font-bold text-alpine-text">Alla reception</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Preavviso consigliato</span>
                        <span class="font-bold text-alpine-text">Il giorno prima</span>
                    </div>
                    <div class="flex justify-between items-center">
                        <span>Cancellazione</span>
                        <span class="font-bold text-alpine-text">Gratuita entro 6h</span>
                    </div>
                </div>
            </div>

            <div class="fade-up-element bg-alpine-bg p-10 border border-alpine-border">
                <h4 class="font-serif text-xl text-alpine-text mb-6 flex items-center gap-3">
                    <ShieldCheck class="w-5 h-5 text-alpine-gold" />
                    Buono a Sapersi
                </h4>
                <div class="space-y-4 text-sm text-alpine-muted font-light">
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Accappatoio</span>
                        <span class="font-bold text-alpine-text">Incluso in camera</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Arrivo consigliato</span>
                        <span class="font-bold text-alpine-text">10 min prima</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Età minima</span>
                        <span class="font-bold text-alpine-text">16 anni</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Pacchetti</span>
                        <span class="font-bold text-alpine-text">3 sedute -15%</span>
                    </div>
                    <div class="flex justify-between items-center">
                        <span>Gift card</span>
                        <span class="font-bold text-alpine-text">Disponibile alla reception</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ CTA ═══════════════════ -->
<section class="bg-[#0a0a0a] py-32 px-6">
    <div class="max-w-3xl mx-auto text-center">
        <div class="fade-up-element">
            <h2 class="font-serif text-4xl text-white mb-6">Il Vostro Corpo Vi Ringrazierà</h2>
            <p class="text-white/50 text-sm font-light leading-relaxed max-w-lg mx-auto mb-12">
                Dopo una giornata in montagna, concedetevi il lusso del recupero perfetto. 
                I nostri terapisti vi aspettano.
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="/wellness/spa" class="inline-flex items-center justify-center gap-3 bg-white text-alpine-text px-10 py-4 text-[11px] tracking-[0.2em] uppercase font-bold hover:bg-alpine-gold hover:text-white transition-all duration-300">
                    Scopri la SPA <ArrowRight class="w-4 h-4" />
                </a>
                <a href="/wellness/trattamenti" class="inline-flex items-center justify-center gap-3 border border-white/30 text-white px-10 py-4 text-[11px] tracking-[0.2em] uppercase font-bold hover:border-white hover:bg-white/10 transition-all duration-300">
                    Trattamenti Corpo <ArrowRight class="w-4 h-4" />
                </a>
            </div>
        </div>
    </div>
</section>
