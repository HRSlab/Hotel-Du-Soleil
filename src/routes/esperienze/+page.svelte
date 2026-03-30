<script lang="ts">
    import { t } from '$lib/i18n';
    import { Utensils, Moon, Flower2, Compass, ArrowRight, Mountain, Snowflake, Wind, MapPin } from 'lucide-svelte';

    let scrollY = $state(0);
</script>

<svelte:window bind:scrollY />

<svelte:head>
    <title>{$t('experiences.main_title')} | Hotel du Soleil</title>
    <meta name="description" content="Esperienze alpine autentiche a Torgnon, Valle d'Aosta. Degustazione Fontina DOP, ciaspolate notturne, yoga in quota e guide alpine certificate." />
</svelte:head>

<!-- ═══════════════════ HERO ═══════════════════ -->
<header class="relative h-[85vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div
        class="absolute inset-0 scale-110"
        style="transform: translateY({scrollY * 0.25}px) scale(1.1);"
    >
        <img src="https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=2000&auto=format&fit=crop" class="h-full w-full object-cover opacity-55" alt="Panorama alpino Valle d'Aosta" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/30 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-28 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            {$t('experiences.main_subtitle')}
        </span>
        <h1 class="font-serif text-5xl md:text-8xl leading-tight font-light text-white fade-up-element">
            {$t('experiences.main_title')}
        </h1>
        <p class="mt-6 text-white/50 text-sm font-light max-w-md fade-up-element">
            Non una semplice vacanza, ma una collezione di ricordi
        </p>
    </div>
</header>

<!-- ═══════════════════ INTRO ═══════════════════ -->
<section class="bg-alpine-bg px-6 py-28">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <Mountain class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            La montagna si vive con tutti i sensi.
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            A Torgnon, a 1.500 metri di quota, ogni stagione offre esperienze 
            che non troverete da nessun'altra parte. Il sapore della Fontina 
            appena stagionata, il silenzio di una ciaspolata sotto le stelle, 
            il respiro consapevole tra le cime \u2014 sono questi i ricordi 
            che vi porterete a casa.
        </p>
    </div>
</section>

<!-- ═══════════════════ HIGHLIGHTS GRID ═══════════════════ -->
<section class="bg-alpine-bg pb-24 px-6">
    <div class="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
        <div class="fade-up-element">
            <div class="h-20 w-20 rounded-full border border-alpine-border bg-white flex items-center justify-center mx-auto mb-5">
                <Utensils class="w-7 h-7 text-alpine-gold" />
            </div>
            <h4 class="font-serif text-lg text-alpine-text mb-2">Sapori</h4>
            <p class="text-xs text-alpine-muted font-light">Fontina DOP e tradizione</p>
        </div>
        <div class="fade-up-element">
            <div class="h-20 w-20 rounded-full border border-alpine-border bg-white flex items-center justify-center mx-auto mb-5">
                <Moon class="w-7 h-7 text-alpine-gold" />
            </div>
            <h4 class="font-serif text-lg text-alpine-text mb-2">Notti Stellate</h4>
            <p class="text-xs text-alpine-muted font-light">Ciaspolate al chiaro di luna</p>
        </div>
        <div class="fade-up-element">
            <div class="h-20 w-20 rounded-full border border-alpine-border bg-white flex items-center justify-center mx-auto mb-5">
                <Flower2 class="w-7 h-7 text-alpine-gold" />
            </div>
            <h4 class="font-serif text-lg text-alpine-text mb-2">Equilibrio</h4>
            <p class="text-xs text-alpine-muted font-light">Yoga a 1.500 metri</p>
        </div>
        <div class="fade-up-element">
            <div class="h-20 w-20 rounded-full border border-alpine-border bg-white flex items-center justify-center mx-auto mb-5">
                <Compass class="w-7 h-7 text-alpine-gold" />
            </div>
            <h4 class="font-serif text-lg text-alpine-text mb-2">Avventura</h4>
            <p class="text-xs text-alpine-muted font-light">Guide alpine certificate</p>
        </div>
    </div>
</section>

<!-- ═══════════════════ DEGUSTAZIONE ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
        <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
            <img src="https://images.unsplash.com/photo-1452195125355-903496c21e64?q=80&w=1500&auto=format&fit=crop" alt="Degustazione Fontina DOP" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
        </div>

        <div class="fade-up-element">
            <div class="flex items-center gap-3 mb-6">
                <Utensils class="w-5 h-5 text-alpine-gold" />
                <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold">Esperienza Gastronomica</span>
            </div>
            <h2 class="font-serif text-4xl text-alpine-text mb-6">{$t('experiences.degustazione.title')}</h2>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
                A dieci minuti dall\u2019hotel, la famiglia Perraillon produce Fontina DOP 
                come si faceva cento anni fa. Visitate l'alpeggio, accarezzate le bovine 
                al pascolo e assaggiate il formaggio appena tolto dalle forme di stagionatura. 
                Un'esperienza che coinvolge tutti i sensi.
            </p>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
                La degustazione include cinque stagionature diverse, dal giovane al 18 mesi, 
                accompagnate da miele di montagna, pane nero e un calice di vino valdostano. 
                La reception organizza la visita su prenotazione.
            </p>
            <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border mb-10">
                <div class="flex items-center gap-3">
                    <MapPin class="w-4 h-4 text-alpine-gold shrink-0" />
                    <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">10 min dall'hotel</span>
                </div>
                <div class="flex items-center gap-3">
                    <Utensils class="w-4 h-4 text-alpine-gold shrink-0" />
                    <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">5 stagionature</span>
                </div>
            </div>
            <a href="/esperienze/degustazione" class="inline-flex items-center gap-3 text-[11px] tracking-[0.2em] uppercase font-bold text-alpine-text hover:text-alpine-gold transition-colors duration-300">
                {$t('experiences.degustazione.cta')} <ArrowRight class="w-4 h-4" />
            </a>
        </div>
    </div>
</section>

<!-- ═══════════════════ CIASPOLATE ═══════════════════ -->
<section class="bg-[#0a0a0a] py-32 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
        <div class="fade-up-element order-2 md:order-1">
            <div class="flex items-center gap-3 mb-6">
                <Moon class="w-5 h-5 text-alpine-gold" />
                <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold">La Magia della Notte</span>
            </div>
            <h2 class="font-serif text-4xl text-white mb-6">{$t('experiences.ciaspolate.title')}</h2>
            <p class="text-white/60 text-sm font-light leading-relaxed mb-6">
                Quando il sole tramonta dietro il Cervino, la montagna si trasforma. 
                Indossate le ciaspole, accendete la frontale e seguite la guida 
                nel silenzio assoluto del bosco innevato. Sopra di voi, 
                un cielo stellato che in citt\u00e0 non vedrete mai.
            </p>
            <p class="text-white/60 text-sm font-light leading-relaxed mb-8">
                Il percorso di 2 ore si conclude al Rifugio con una cena valdostana: 
                fonduta, polenta concia e vin br\u00fbl\u00e9. La guida racconta leggende locali 
                mentre la neve scricchiola sotto i passi. Un'esperienza indimenticabile 
                da dicembre a marzo.
            </p>
            <div class="grid grid-cols-2 gap-6 pt-6 border-t border-white/20 mb-10">
                <div class="flex items-center gap-3">
                    <Snowflake class="w-4 h-4 text-alpine-gold shrink-0" />
                    <span class="text-xs font-bold uppercase tracking-widest text-white/80">Dicembre \u2013 Marzo</span>
                </div>
                <div class="flex items-center gap-3">
                    <Moon class="w-4 h-4 text-alpine-gold shrink-0" />
                    <span class="text-xs font-bold uppercase tracking-widest text-white/80">Partenza ore 18:00</span>
                </div>
            </div>
            <a href="/esperienze/ciaspolate" class="inline-flex items-center gap-3 text-[11px] tracking-[0.2em] uppercase font-bold text-white hover:text-alpine-gold transition-colors duration-300">
                {$t('experiences.ciaspolate.cta')} <ArrowRight class="w-4 h-4" />
            </a>
        </div>

        <div class="fade-up-element overflow-hidden shadow-xl order-1 md:order-2">
            <img src="https://images.unsplash.com/photo-1551524559-8af4e6624178?q=80&w=1500&auto=format&fit=crop" alt="Ciaspolata notturna nelle Alpi" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-85" />
        </div>
    </div>
</section>

<!-- ═══════════════════ YOGA ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
        <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
            <img src="https://images.unsplash.com/photo-1506126613408-eca07ce68773?q=80&w=1500&auto=format&fit=crop" alt="Yoga all'aperto con vista sulle Alpi" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
        </div>

        <div class="fade-up-element">
            <div class="flex items-center gap-3 mb-6">
                <Flower2 class="w-5 h-5 text-alpine-gold" />
                <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold">Equilibrio Interiore</span>
            </div>
            <h2 class="font-serif text-4xl text-alpine-text mb-6">{$t('experiences.yoga.title')}</h2>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
                A 1.500 metri, l'aria \u00e8 pi\u00f9 pura, il silenzio pi\u00f9 profondo 
                e la mente si svuota naturalmente. Le nostre sessioni di yoga 
                si tengono all'aperto, sulla terrazza panoramica con vista 
                sul Cervino e la catena del Monte Rosa.
            </p>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
                Lezioni all'alba e al tramonto, guidate da istruttori certificati. 
                Hatha yoga, pranayama e meditazione alpina. 
                Tutti i livelli sono benvenuti \u2014 dai principianti ai praticanti esperti. 
                D'inverno le sessioni si spostano nella sala wellness con vetrate sulle cime.
            </p>
            <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border mb-10">
                <div class="flex items-center gap-3">
                    <Wind class="w-4 h-4 text-alpine-gold shrink-0" />
                    <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Alba & Tramonto</span>
                </div>
                <div class="flex items-center gap-3">
                    <Flower2 class="w-4 h-4 text-alpine-gold shrink-0" />
                    <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Tutti i livelli</span>
                </div>
            </div>
            <a href="/esperienze/yoga" class="inline-flex items-center gap-3 text-[11px] tracking-[0.2em] uppercase font-bold text-alpine-text hover:text-alpine-gold transition-colors duration-300">
                {$t('experiences.yoga.cta')} <ArrowRight class="w-4 h-4" />
            </a>
        </div>
    </div>
</section>

<!-- ═══════════════════ GUIDE ALPINE ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
        <div class="fade-up-element order-2 md:order-1">
            <div class="flex items-center gap-3 mb-6">
                <Compass class="w-5 h-5 text-alpine-gold" />
                <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold">Esperti della Montagna</span>
            </div>
            <h2 class="font-serif text-4xl text-alpine-text mb-6">{$t('experiences.guide.title')}</h2>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
                Le nostre guide alpine certificate conoscono ogni sentiero, 
                ogni cresta e ogni segreto delle montagne intorno a Torgnon. 
                Che vogliate un trekking panoramico in famiglia o un'ascensione 
                impegnativa, c'\u00e8 sempre un esperto pronto a guidarvi.
            </p>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
                Escursioni estive, freeride invernale, arrampicata su ghiaccio, 
                ciaspolate guidate e uscite di mountain bike. 
                Ogni avventura \u00e8 personalizzabile per livello ed esigenze. 
                La reception prenota per voi con 48 ore di anticipo.
            </p>
            <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border mb-10">
                <div class="flex items-center gap-3">
                    <Compass class="w-4 h-4 text-alpine-gold shrink-0" />
                    <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Guide certificate</span>
                </div>
                <div class="flex items-center gap-3">
                    <Mountain class="w-4 h-4 text-alpine-gold shrink-0" />
                    <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Estate & Inverno</span>
                </div>
            </div>
            <a href="/esperienze/guide" class="inline-flex items-center gap-3 text-[11px] tracking-[0.2em] uppercase font-bold text-alpine-text hover:text-alpine-gold transition-colors duration-300">
                {$t('experiences.guide.cta')} <ArrowRight class="w-4 h-4" />
            </a>
        </div>

        <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl order-1 md:order-2">
            <img src="https://images.unsplash.com/photo-1522163182402-834f871fd851?q=80&w=1500&auto=format&fit=crop" alt="Guida alpina con gruppo in montagna" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
        </div>
    </div>
</section>

<!-- ═══════════════════ STAGIONI ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-20 px-6">
    <div class="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-12 text-center">
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">4</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Esperienze uniche</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">12</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Mesi di attivit\u00e0</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">1.500m</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Di altitudine</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">\u221e</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Ricordi da portare a casa</p>
        </div>
    </div>
</section>

<!-- ═══════════════════ GALLERY ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">Ogni Stagione, un'Avventura</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">La montagna non si ferma mai</p>
        </div>

        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
            <a href="/esperienze/degustazione" class="fade-up-element group relative overflow-hidden aspect-square">
                <img src="https://images.unsplash.com/photo-1500595046743-cd271d694d30?q=80&w=800&auto=format&fit=crop" alt="Alpeggio" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 brightness-90" />
                <div class="absolute inset-0 bg-linear-to-t from-black/70 via-transparent to-transparent flex items-end p-5">
                    <div>
                        <p class="text-[10px] uppercase tracking-widest text-white/70 font-bold">Tutto l'anno</p>
                        <p class="font-serif text-lg text-white">Degustazione</p>
                    </div>
                </div>
            </a>
            <a href="/esperienze/ciaspolate" class="fade-up-element group relative overflow-hidden aspect-square">
                <img src="https://images.unsplash.com/photo-1551524559-8af4e6624178?q=80&w=800&auto=format&fit=crop" alt="Ciaspolata" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 brightness-85" />
                <div class="absolute inset-0 bg-linear-to-t from-black/70 via-transparent to-transparent flex items-end p-5">
                    <div>
                        <p class="text-[10px] uppercase tracking-widest text-white/70 font-bold">Dic \u2013 Mar</p>
                        <p class="font-serif text-lg text-white">Ciaspolate</p>
                    </div>
                </div>
            </a>
            <a href="/esperienze/yoga" class="fade-up-element group relative overflow-hidden aspect-square">
                <img src="https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?q=80&w=800&auto=format&fit=crop" alt="Yoga in montagna" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 brightness-90" />
                <div class="absolute inset-0 bg-linear-to-t from-black/70 via-transparent to-transparent flex items-end p-5">
                    <div>
                        <p class="text-[10px] uppercase tracking-widest text-white/70 font-bold">Tutto l'anno</p>
                        <p class="font-serif text-lg text-white">Yoga in Quota</p>
                    </div>
                </div>
            </a>
            <a href="/esperienze/guide" class="fade-up-element group relative overflow-hidden aspect-square">
                <img src="https://images.unsplash.com/photo-1544450531-64d7fa39b400?q=80&w=800&auto=format&fit=crop" alt="Guide alpine" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 brightness-90" />
                <div class="absolute inset-0 bg-linear-to-t from-black/70 via-transparent to-transparent flex items-end p-5">
                    <div>
                        <p class="text-[10px] uppercase tracking-widest text-white/70 font-bold">Estate & Inverno</p>
                        <p class="font-serif text-lg text-white">Guide Alpine</p>
                    </div>
                </div>
            </a>
        </div>
    </div>
</section>

<!-- ═══════════════════ CTA ═══════════════════ -->
<section class="bg-[#0a0a0a] py-32 px-6">
    <div class="max-w-3xl mx-auto text-center">
        <div class="fade-up-element">
            <h2 class="font-serif text-4xl text-white mb-6">Quale Sar\u00e0 la Vostra Avventura?</h2>
            <p class="text-white/50 text-sm font-light leading-relaxed max-w-lg mx-auto mb-12">
                La reception \u00e8 a vostra disposizione per organizzare ogni esperienza. 
                Chiedete e personalizziamo tutto per voi.
            </p>
            <a href="mailto:info@hoteldusoleiltorgnon.com" class="inline-flex items-center justify-center gap-3 bg-white text-alpine-text px-10 py-4 text-[11px] tracking-[0.2em] uppercase font-bold hover:bg-alpine-gold hover:text-white transition-all duration-300">
                Parliamone Insieme <ArrowRight class="w-4 h-4" />
            </a>
        </div>
    </div>
</section>
