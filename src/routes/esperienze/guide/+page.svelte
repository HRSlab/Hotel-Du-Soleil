<script lang="ts">
    import { ShieldCheck, Mountain, Users, Star, Clock, MapPin, Compass, ArrowRight, Snowflake, Sun, TreePine, Wind, Heart, Flag, Award, Binoculars } from 'lucide-svelte';

    let scrollY = $state(0);
</script>

<svelte:window bind:scrollY />

<svelte:head>
    <title>Guide Alpine Partner | Hotel du Soleil</title>
    <meta name="description" content="Guide alpine certificate in Valle d'Aosta. Escursioni, alpinismo, freeride, ciaspolate e trekking guidati da professionisti che conoscono ogni sentiero di Torgnon." />
</svelte:head>

<!-- ═══════════════════ HERO ═══════════════════ -->
<header class="relative h-[85vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div
        class="absolute inset-0 scale-110"
        style="transform: translateY({scrollY * 0.25}px) scale(1.1);"
    >
        <img src="https://images.unsplash.com/photo-1544450531-64d7fa39b400?q=80&w=2000&auto=format&fit=crop" class="h-full w-full object-cover opacity-55" alt="Guida alpina in Valle d'Aosta" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/30 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-28 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            Esperti della Montagna · Valle d'Aosta
        </span>
        <h1 class="font-serif text-5xl md:text-8xl leading-tight font-light text-white fade-up-element">
            Guide Alpine
        </h1>
        <p class="mt-6 text-white/50 text-sm font-light max-w-md fade-up-element">
            Professionisti che trasformano ogni uscita in un'esperienza sicura e indimenticabile
        </p>
    </div>
</header>

<!-- ═══════════════════ INTRO ═══════════════════ -->
<section class="bg-alpine-bg px-6 py-28">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <ShieldCheck class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            La montagna si svela solo a chi la conosce davvero.
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            Collaboriamo con le migliori guide alpine certificate della Valle d'Aosta, 
            professionisti che hanno percorso ogni sentiero, ogni cresta e ogni parete di queste montagne. 
            Con loro, anche il percorso più semplice diventa una scoperta, 
            e quelli più impegnativi si affrontano con la sicurezza di chi conosce ogni passo.
        </p>
    </div>
</section>

<!-- ═══════════════════ I NOSTRI PARTNER ═══════════════════ -->
<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
        <img src="https://images.unsplash.com/photo-1522163182402-834f871fd851?q=80&w=1500&auto=format&fit=crop" alt="Guida alpina con gruppo in montagna" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
    </div>

    <div class="fade-up-element">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">I Nostri Partner</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">Guide Alpine<br/>Certificate UIAGM</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            Le nostre guide sono iscritte al Collegio Regionale delle Guide Alpine della Valle d'Aosta 
            e certificate UIAGM (Union Internationale des Associations de Guides de Montagnes). 
            Questo significa formazione continua, competenza tecnica ai massimi livelli 
            e la capacità di gestire qualsiasi situazione in ambiente montano.
        </p>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
            Conoscono Torgnon, la Valtournenche e tutto il comprensorio come le loro tasche. 
            Sono cresciuti su queste montagne e le vivono ogni giorno dell'anno.
        </p>
        <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
            <div class="flex items-center gap-3">
                <Award class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Certificati UIAGM</span>
            </div>
            <div class="flex items-center gap-3">
                <MapPin class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Locali del territorio</span>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ STATS ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-20 px-6">
    <div class="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-12 text-center">
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">20+</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Anni di esperienza</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">365</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Giorni all'anno</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">4.000m</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Quota massima</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">8</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Max per gruppo</p>
        </div>
    </div>
</section>

<!-- ═══════════════════ LE ESPERIENZE ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">Le Esperienze</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">Ogni stagione, un'avventura diversa</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12">
            <!-- Alpinismo -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="overflow-hidden aspect-3/2">
                    <img src="https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=800&auto=format&fit=crop" alt="Alpinismo in Valle d'Aosta" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
                </div>
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Mountain class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">Alta Quota</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Alpinismo</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">Giornata intera · Da 2.500m</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed">
                        Salite su ghiacciaio, creste panoramiche e vie normali alle vette più emblematiche 
                        della zona. Dal Breithorn al Monte Rosa, passando per il Gran Tournalin. 
                        Per chi vuole toccare il cielo con un dito.
                    </p>
                </div>
            </div>

            <!-- Freeride -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="overflow-hidden aspect-3/2">
                    <img src="https://images.unsplash.com/photo-1565992441121-4367c2967103?q=80&w=800&auto=format&fit=crop" alt="Freeride neve fresca" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
                </div>
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Snowflake class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">Inverno</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Freeride & Scialpinismo</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">Mezza giornata o intera · Dic–Apr</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed">
                        Neve fresca fuori pista in totale sicurezza. Le guide conoscono ogni pendio, 
                        ogni esposizione e le condizioni nivologiche del giorno. 
                        Scialpinismo all'alba per tracciare le prime linee sulla neve vergine.
                    </p>
                </div>
            </div>

            <!-- Trekking -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="overflow-hidden aspect-3/2">
                    <img src="https://images.unsplash.com/photo-1551632811-561732d1e306?q=80&w=800&auto=format&fit=crop" alt="Trekking guidato nelle Alpi" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
                </div>
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Sun class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">Estate</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Trekking & Escursioni</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">Da 2h a giornata intera · Giu–Set</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed">
                        Dai sentieri panoramici adatti alle famiglie alle traversate d'alta quota. 
                        Le guide vi svelano la flora, la fauna e le storie antiche 
                        di queste montagne. Ogni camminata è una lezione di natura.
                    </p>
                </div>
            </div>
        </div>

        <!-- Seconda riga -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12 mt-8 lg:mt-12">
            <!-- Ciaspolate -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="overflow-hidden aspect-3/2">
                    <img src="https://images.unsplash.com/photo-1483728642387-6c3bdd6c93e5?q=80&w=800&auto=format&fit=crop" alt="Ciaspolata guidata" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
                </div>
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <TreePine class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">Inverno</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Ciaspolate Guidate</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">2–3h · Notturne e diurne · Dic–Mar</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed">
                        Immersione nel bosco innevato con racchette da neve. 
                        Le uscite notturne con lampada frontale sono un'esperienza magica, 
                        spesso conclusa con cena in rifugio.
                    </p>
                    <a href="/esperienze/ciaspolate" class="inline-flex items-center gap-2 text-[10px] uppercase tracking-[0.2em] font-bold text-alpine-text hover:text-alpine-gold transition-colors mt-6">
                        Scopri di più <ArrowRight class="w-3.5 h-3.5" />
                    </a>
                </div>
            </div>

            <!-- MTB -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="overflow-hidden aspect-3/2">
                    <img src="https://images.unsplash.com/photo-1544191714-3d71bc294943?q=80&w=800&auto=format&fit=crop" alt="Mountain bike guidata" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
                </div>
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Compass class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">Estate</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Tour MTB & E-Bike</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">Mezza giornata o intera · Giu–Set</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed">
                        I sentieri più spettacolari di Torgnon in sella con una guida esperta. 
                        Percorsi personalizzati per livello, da quelli panoramici alle discese enduro.
                    </p>
                    <a href="/sport/bike" class="inline-flex items-center gap-2 text-[10px] uppercase tracking-[0.2em] font-bold text-alpine-text hover:text-alpine-gold transition-colors mt-6">
                        Scopri i percorsi <ArrowRight class="w-3.5 h-3.5" />
                    </a>
                </div>
            </div>

            <!-- Natura & Fauna -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="overflow-hidden aspect-3/2">
                    <img src="https://images.unsplash.com/photo-1474511320723-9a56873571b7?q=80&w=800&auto=format&fit=crop" alt="Osservazione fauna alpina" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
                </div>
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Binoculars class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">Tutto l'anno</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Natura & Fauna</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">2–4h · Famiglie benvenute</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed">
                        Escursioni naturalistiche per osservare stambecchi, camosci, marmotte e aquile reali. 
                        Le guide portano binocoli professionali e vi insegnano 
                        a leggere le tracce nella neve e nel terreno.
                    </p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ COME FUNZIONA ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-5xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">Come Funziona</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">Prenotare è semplicissimo</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
            <div class="fade-up-element text-center">
                <div class="w-12 h-12 rounded-full border-2 border-alpine-gold flex items-center justify-center mx-auto mb-6">
                    <span class="font-serif text-xl text-alpine-gold">1</span>
                </div>
                <h4 class="font-serif text-lg text-alpine-text mb-3">Scegliete</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Consultate le esperienze disponibili e scegliete quella che vi ispira di più.
                </p>
            </div>
            <div class="fade-up-element text-center">
                <div class="w-12 h-12 rounded-full border-2 border-alpine-gold flex items-center justify-center mx-auto mb-6">
                    <span class="font-serif text-xl text-alpine-gold">2</span>
                </div>
                <h4 class="font-serif text-lg text-alpine-text mb-3">Chiedete a Noi</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Alla reception, organizziamo tutto noi: data, orario, attrezzatura e livello del gruppo.
                </p>
            </div>
            <div class="fade-up-element text-center">
                <div class="w-12 h-12 rounded-full border-2 border-alpine-gold flex items-center justify-center mx-auto mb-6">
                    <span class="font-serif text-xl text-alpine-gold">3</span>
                </div>
                <h4 class="font-serif text-lg text-alpine-text mb-3">La Guida Vi Raggiunge</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    La guida viene direttamente in hotel. Niente spostamenti, niente complicazioni.
                </p>
            </div>
            <div class="fade-up-element text-center">
                <div class="w-12 h-12 rounded-full border-2 border-alpine-gold flex items-center justify-center mx-auto mb-6">
                    <span class="font-serif text-xl text-alpine-gold">4</span>
                </div>
                <h4 class="font-serif text-lg text-alpine-text mb-3">Vivete l'Avventura</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Partite insieme alla guida e tornate con ricordi che dureranno una vita.
                </p>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ SICUREZZA ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
        <div class="fade-up-element order-2 md:order-1">
            <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">La Vostra Tranquillità</span>
            <h2 class="font-serif text-4xl text-alpine-text mb-6">Sicurezza<br/>Senza Compromessi</h2>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
                Ogni uscita è pianificata con la massima attenzione alle condizioni meteo, 
                al manto nevoso (in inverno) e al livello fisico dei partecipanti. 
                Le guide portano sempre con sé kit di primo soccorso, ARTVA, pala e sonda 
                per le uscite invernali, e GPS satellitare per qualsiasi emergenza.
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                <div class="flex items-start gap-3">
                    <ShieldCheck class="w-5 h-5 text-alpine-gold shrink-0 mt-0.5" />
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">Assicurazione</p>
                        <p class="text-xs text-alpine-muted font-light">RC professionale inclusa per tutti i partecipanti</p>
                    </div>
                </div>
                <div class="flex items-start gap-3">
                    <Wind class="w-5 h-5 text-alpine-gold shrink-0 mt-0.5" />
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">Meteo Check</p>
                        <p class="text-xs text-alpine-muted font-light">Bollettino verificato il giorno stesso. Riprogrammazione gratuita in caso di maltempo</p>
                    </div>
                </div>
                <div class="flex items-start gap-3">
                    <Flag class="w-5 h-5 text-alpine-gold shrink-0 mt-0.5" />
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">ARTVA & GPS</p>
                        <p class="text-xs text-alpine-muted font-light">Equipaggiamento di sicurezza completo per ogni uscita invernale</p>
                    </div>
                </div>
                <div class="flex items-start gap-3">
                    <Heart class="w-5 h-5 text-alpine-gold shrink-0 mt-0.5" />
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">Primo Soccorso</p>
                        <p class="text-xs text-alpine-muted font-light">Guide certificate in primo soccorso e gestione emergenze in montagna</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="fade-up-element order-1 md:order-2 overflow-hidden bg-alpine-border shadow-xl">
            <img src="https://images.unsplash.com/photo-1486911278844-a81c5267e227?q=80&w=1500&auto=format&fit=crop" alt="Guida alpina in cresta" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
        </div>
    </div>
</section>

<!-- ═══════════════════ ESCURSIONI PER TUTTI ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">Per Ogni Livello</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">Dalla passeggiata all'alta quota</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            <div class="fade-up-element text-center p-10">
                <div class="w-10 h-10 rounded-full bg-green-100 flex items-center justify-center mx-auto mb-6">
                    <span class="w-3 h-3 rounded-full bg-green-500"></span>
                </div>
                <h4 class="font-serif text-lg text-alpine-text mb-3">Famiglie</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Passeggiate con poco dislivello, ritmo adatto ai bambini, 
                    soste per osservare gli animali e raccontare le leggende della montagna.
                </p>
            </div>
            <div class="fade-up-element text-center p-10">
                <div class="w-10 h-10 rounded-full bg-blue-100 flex items-center justify-center mx-auto mb-6">
                    <span class="w-3 h-3 rounded-full bg-blue-500"></span>
                </div>
                <h4 class="font-serif text-lg text-alpine-text mb-3">Intermedio</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Trekking di 4-6 ore con dislivelli moderati. Alpeggi, laghi alpini 
                    e panorami che ripagano ogni goccia di sudore.
                </p>
            </div>
            <div class="fade-up-element text-center p-10">
                <div class="w-10 h-10 rounded-full bg-stone-200 flex items-center justify-center mx-auto mb-6">
                    <span class="w-3 h-3 rounded-full bg-red-500"></span>
                </div>
                <h4 class="font-serif text-lg text-alpine-text mb-3">Esperto</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Traversate d'alta quota, vie ferrate e percorsi tecnici. 
                    Per chi ha esperienza e cerca la sfida autentica della montagna.
                </p>
            </div>
            <div class="fade-up-element text-center p-10">
                <div class="w-10 h-10 rounded-full bg-gray-100 flex items-center justify-center mx-auto mb-6">
                    <Mountain class="w-5 h-5 text-alpine-gold" />
                </div>
                <h4 class="font-serif text-lg text-alpine-text mb-3">Alpinismo</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Ghiacciaio, corde, ramponi. Le vette più alte della zona 
                    per chi vuole vivere l'alpinismo nella sua forma più pura.
                </p>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ INFO PRATICHE ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-5xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">Info Pratiche</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">Tutto quello che serve sapere</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="fade-up-element bg-white p-10 border border-alpine-border">
                <h4 class="font-serif text-xl text-alpine-text mb-6 flex items-center gap-3">
                    <Clock class="w-5 h-5 text-alpine-gold" />
                    Prenotazioni
                </h4>
                <div class="space-y-4 text-sm text-alpine-muted font-light">
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Dove prenotare</span>
                        <span class="font-bold text-alpine-text">Alla reception</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Preavviso minimo</span>
                        <span class="font-bold text-alpine-text">24 ore</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Cancellazione</span>
                        <span class="font-bold text-alpine-text">Gratuita entro 48h</span>
                    </div>
                    <div class="flex justify-between items-center">
                        <span>Maltempo</span>
                        <span class="font-bold text-alpine-text">Riprogrammazione gratuita</span>
                    </div>
                </div>
            </div>

            <div class="fade-up-element bg-white p-10 border border-alpine-border">
                <h4 class="font-serif text-xl text-alpine-text mb-6 flex items-center gap-3">
                    <ShieldCheck class="w-5 h-5 text-alpine-gold" />
                    Cosa Portare
                </h4>
                <div class="space-y-4 text-sm text-alpine-muted font-light">
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Scarponi</span>
                        <span class="font-bold text-alpine-text">Da trekking (no sneakers)</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Zaino</span>
                        <span class="font-bold text-alpine-text">Con acqua e snack</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Abbigliamento</span>
                        <span class="font-bold text-alpine-text">A strati (vento in quota)</span>
                    </div>
                    <div class="flex justify-between items-center">
                        <span>Crema solare</span>
                        <span class="font-bold text-alpine-text">SPF 50+ (anche inverno)</span>
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
            <h2 class="font-serif text-4xl text-white mb-6">Pronti per l'Avventura?</h2>
            <p class="text-white/50 text-sm font-light leading-relaxed max-w-lg mx-auto mb-12">
                Le montagne vi aspettano. E con le nostre guide al vostro fianco, 
                ogni sentiero diventa una storia da raccontare.
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="/sport/trekking" class="inline-flex items-center justify-center gap-3 bg-white text-alpine-text px-10 py-4 text-[11px] tracking-[0.2em] uppercase font-bold hover:bg-alpine-gold hover:text-white transition-all duration-300">
                    I Sentieri <ArrowRight class="w-4 h-4" />
                </a>
                <a href="/esperienze/ciaspolate" class="inline-flex items-center justify-center gap-3 border border-white/30 text-white px-10 py-4 text-[11px] tracking-[0.2em] uppercase font-bold hover:border-white hover:bg-white/10 transition-all duration-300">
                    Ciaspolate Notturne <ArrowRight class="w-4 h-4" />
                </a>
            </div>
        </div>
    </div>
</section>
