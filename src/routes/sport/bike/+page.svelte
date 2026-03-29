<script lang="ts">
    import { Bike, Mountain, Map, MapPin, Clock, Users, ShieldCheck, TreePine, Gauge, Wrench, Zap, ArrowRight, Sun, Star, Compass, Flag, TrendingUp, ChevronDown, Heart } from 'lucide-svelte';

    let scrollY = $state(0);
</script>

<svelte:window bind:scrollY />

<svelte:head>
    <title>Mountain Bike & E-Bike | Hotel du Soleil</title>
    <meta name="description" content="Mountain bike ed e-bike a Torgnon, Valle d'Aosta. Percorsi panoramici tra alpeggi, boschi e vette con vista sul Cervino. Hotel bike-friendly con deposito e officina." />
</svelte:head>

<!-- ═══════════════════ HERO ═══════════════════ -->
<header class="relative h-[85vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div
        class="absolute inset-0 scale-110"
        style="transform: translateY({scrollY * 0.25}px) scale(1.1);"
    >
        <img src="https://images.unsplash.com/photo-1544191714-3d71bc294943?q=80&w=2000&auto=format&fit=crop" class="h-full w-full object-cover opacity-60" alt="Mountain bike nelle Alpi di Torgnon" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/30 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-28 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            Pedalata nel Cuore delle Alpi · Torgnon
        </span>
        <h1 class="font-serif text-5xl md:text-8xl leading-tight font-light text-white fade-up-element">
            MTB & E-Bike
        </h1>
        <p class="mt-6 text-white/50 text-sm font-light max-w-md fade-up-element">
            Sentieri panoramici, alpeggi e vette a portata di pedale
        </p>
    </div>
</header>

<!-- ═══════════════════ INTRO ═══════════════════ -->
<section class="bg-alpine-bg px-6 py-28">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <Bike class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            Dove ogni pedalata diventa un ricordo.
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            Torgnon è un paradiso per i bikers: una rete di sentieri che si snodano tra alpeggi fioriti, 
            boschi di larici e creste panoramiche con vista sul Cervino e il Monte Rosa. 
            Dai trail tecnici per i più esperti alle dolci strade sterrate adatte a tutta la famiglia, 
            qui la mountain bike si vive a 1.500 metri, con un'aria che non troverai altrove.
        </p>
    </div>
</section>

<!-- ═══════════════════ IL TERRITORIO ═══════════════════ -->
<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
        <img src="https://images.unsplash.com/photo-1594942816234-33aa22f4a0b1?q=80&w=1500&auto=format&fit=crop" alt="Sentiero mountain bike con vista alpina" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
    </div>

    <div class="fade-up-element">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">Il Territorio</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">Un Bike Park<br/>Naturale</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            La conca di Torgnon offre oltre 200 km di sentieri ciclabili che si sviluppano 
            dai 1.100 ai 2.500 metri di quota. Strade forestali, single track, mulattiere storiche 
            e percorsi in cresta si alternano tra panorami mozzafiato e momenti di pura adrenalina.
        </p>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
            In estate, gli impianti di risalita di Torgnon diventano bike-lift: carichi la bici 
            in seggiovia e ti godi solo la discesa. Il compromesso perfetto tra fatica e divertimento.
        </p>
        <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
            <div class="flex items-center gap-3">
                <TrendingUp class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">200+ km di sentieri</span>
            </div>
            <div class="flex items-center gap-3">
                <Mountain class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">1.100 – 2.500m</span>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ STATS ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-20 px-6">
    <div class="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-12 text-center">
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">200+</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Km di sentieri</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">15</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Percorsi segnalati</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">2.500m</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Quota massima</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">Giu–Set</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Stagione bike</p>
        </div>
    </div>
</section>

<!-- ═══════════════════ PERCORSI ICONICI ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">I Percorsi</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">I trail che rendono Torgnon unica</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12">
            <!-- Percorso 1 -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="overflow-hidden aspect-3/2">
                    <img src="https://images.unsplash.com/photo-1534787238916-9ba6764efd4f?q=80&w=800&auto=format&fit=crop" alt="Tour del Monte Zerbion in mountain bike" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
                </div>
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <span class="inline-block w-2 h-2 rounded-full bg-green-500"></span>
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">Facile</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Tour del Monte Zerbion</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">28 km · 850m D+ · 3h</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed">
                        L'anello classico di Torgnon. Un percorso panoramico su strade forestali che offre 
                        una vista a 360° sulla valle centrale, il Cervino e il Grand Combin. 
                        Ideale per E-Bike e per chi vuole godersi il panorama senza troppa fatica.
                    </p>
                </div>
            </div>

            <!-- Percorso 2 -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="overflow-hidden aspect-3/2">
                    <img src="https://images.unsplash.com/photo-1605235186583-a8272b1a0413?q=80&w=800&auto=format&fit=crop" alt="Anello degli Alpeggi mountain bike" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
                </div>
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <span class="inline-block w-2 h-2 rounded-full bg-blue-400"></span>
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">Medio</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Anello degli Alpeggi</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">35 km · 1.200m D+ · 4h</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed">
                        Attraversa gli alpeggi più belli della Valtournenche, toccando diverse malghe 
                        dove è possibile fermarsi a degustare la Fontina DOP e assaporare la polenta concia. 
                        Single track e sterrati si alternano tra pascoli e boschi di conifere.
                    </p>
                </div>
            </div>

            <!-- Percorso 3 -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="overflow-hidden aspect-3/2">
                    <img src="https://images.unsplash.com/photo-1558618666-fcd25c85f82e?q=80&w=800&auto=format&fit=crop" alt="Cresta del Cervino enduro trail" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
                </div>
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <span class="inline-block w-2 h-2 rounded-full bg-red-500"></span>
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">Esperto</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Enduro Trail Mongnod</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">18 km · 1.600m D+ · 5h</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed">
                        Per chi cerca l'adrenalina pura. Single track tecnici, radici, tornanti stretti 
                        e discese vertiginose dalla cresta del Mongnod fino a fondovalle. 
                        Si sale con il bike-lift e si scende con il cuore in gola.
                    </p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ E-BIKE ═══════════════════ -->
<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element order-2 md:order-1">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">Accessibile a Tutti</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">E-Bike:<br/>La Montagna Senza Limiti</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            Non serve essere atleti per vivere l'emozione delle Alpi in sella. 
            Con le E-Bike a pedalata assistita, anche i percorsi più impegnativi diventano 
            accessibili: sali senza fatica e ti godi ogni metro di panorama.
        </p>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
            Ideale per coppie con livelli diversi, famiglie con bambini o semplicemente 
            per chi vuole esplorare di più con meno sforzo. La batteria dura un'intera giornata 
            e i percorsi E-Bike dedicati garantiscono sentieri larghi e sicuri.
        </p>
        <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
            <div class="flex items-center gap-3">
                <Zap class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Autonomia 8h</span>
            </div>
            <div class="flex items-center gap-3">
                <Heart class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Adatto a tutti</span>
            </div>
        </div>
    </div>

    <div class="fade-up-element order-1 md:order-2 overflow-hidden bg-alpine-border shadow-xl">
        <img src="https://images.unsplash.com/photo-1571068316344-75bc76f77890?q=80&w=1500&auto=format&fit=crop" alt="E-bike sulle Alpi" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
    </div>
</section>

<!-- ═══════════════════ SERVIZI BIKE-FRIENDLY ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">Hotel Bike-Friendly</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">Tutto ciò che serve al biker, sotto lo stesso tetto</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            <div class="fade-up-element text-center p-10">
                <ShieldCheck class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-[1.5px]" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Deposito Sicuro</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Locale chiuso a chiave e videosorvegliato 24h. Le tue bici al sicuro come in casa tua.
                </p>
            </div>
            <div class="fade-up-element text-center p-10">
                <Wrench class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-[1.5px]" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Officina Attrezzata</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Attrezzi, pompa, camera d'aria di scorta e cavalletto per le manutenzioni di base tra un'uscita e l'altra.
                </p>
            </div>
            <div class="fade-up-element text-center p-10">
                <Zap class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-[1.5px]" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Ricarica E-Bike</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Stazione di ricarica dedicata nel deposito bici. Colleghi la batteria la sera, al mattino sei al 100%.
                </p>
            </div>
            <div class="fade-up-element text-center p-10">
                <Sun class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-[1.5px]" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Zona Lavaggio</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Area esterna con idropulitrice e getto d'acqua per lavare la bici dopo ogni uscita nel fango alpino.
                </p>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ NOLEGGIO & GUIDE ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20">
        <!-- Noleggio -->
        <div class="fade-up-element bg-white p-12 md:p-14 border border-alpine-border hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
            <Bike class="w-8 h-8 text-alpine-gold mb-8 stroke-[1.5px]" />
            <h4 class="font-serif text-2xl text-alpine-text mb-2">Noleggio MTB & E-Bike</h4>
            <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-6">Partner convenzionato</p>
            <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-8">
                Non hai la bici con te? Nessun problema. Grazie alla collaborazione con il noleggio locale, 
                puoi ritirare MTB full-suspension o E-Bike di ultima generazione direttamente in hotel. 
                Casco e protezioni inclusi.
            </p>
            <ul class="space-y-3 text-xs text-alpine-muted font-light mb-8">
                <li class="flex items-center gap-3"><Star class="w-3.5 h-3.5 text-alpine-gold shrink-0" /> MTB front e full-suspension</li>
                <li class="flex items-center gap-3"><Star class="w-3.5 h-3.5 text-alpine-gold shrink-0" /> E-Bike Bosch e Shimano</li>
                <li class="flex items-center gap-3"><Star class="w-3.5 h-3.5 text-alpine-gold shrink-0" /> Casco e protezioni incluse</li>
                <li class="flex items-center gap-3"><Star class="w-3.5 h-3.5 text-alpine-gold shrink-0" /> Consegna e ritiro in hotel</li>
            </ul>
            <a href="/sport/noleggio" class="inline-flex items-center gap-2 text-[10px] uppercase tracking-[0.2em] font-bold text-alpine-text hover:text-alpine-gold transition-colors">
                Scopri il noleggio <ArrowRight class="w-4 h-4" />
            </a>
        </div>

        <!-- Guide -->
        <div class="fade-up-element bg-white p-12 md:p-14 border border-alpine-border hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
            <Compass class="w-8 h-8 text-alpine-gold mb-8 stroke-[1.5px]" />
            <h4 class="font-serif text-2xl text-alpine-text mb-2">Guide MTB Certificate</h4>
            <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-6">Esplora con un esperto</p>
            <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-8">
                Le nostre guide conoscono ogni sentiero, ogni scorciatoia, ogni punto panoramico segreto. 
                Che tu sia un principiante o un endurista esperto, ti porteranno nei posti giusti 
                al ritmo giusto. Escursioni di mezza giornata o giornata intera.
            </p>
            <ul class="space-y-3 text-xs text-alpine-muted font-light mb-8">
                <li class="flex items-center gap-3"><Star class="w-3.5 h-3.5 text-alpine-gold shrink-0" /> Tour personalizzati per livello</li>
                <li class="flex items-center gap-3"><Star class="w-3.5 h-3.5 text-alpine-gold shrink-0" /> Uscite alba e tramonto</li>
                <li class="flex items-center gap-3"><Star class="w-3.5 h-3.5 text-alpine-gold shrink-0" /> Gruppi piccoli (max 8 persone)</li>
                <li class="flex items-center gap-3"><Star class="w-3.5 h-3.5 text-alpine-gold shrink-0" /> Primo soccorso e GPS tracking</li>
            </ul>
            <a href="/esperienze/guide" class="inline-flex items-center gap-2 text-[10px] uppercase tracking-[0.2em] font-bold text-alpine-text hover:text-alpine-gold transition-colors">
                Prenota una guida <ArrowRight class="w-4 h-4" />
            </a>
        </div>
    </div>
</section>

<!-- ═══════════════════ LA TUA GIORNATA TIPO ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-5xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">La Tua Giornata Tipo</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">Dal risveglio alla birra della sera</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            <div class="fade-up-element text-center">
                <div class="w-12 h-12 rounded-full border-2 border-alpine-gold flex items-center justify-center mx-auto mb-6">
                    <span class="font-serif text-lg text-alpine-gold">07</span>
                </div>
                <h4 class="font-serif text-lg text-alpine-text mb-3">Colazione Energetica</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Buffet ricco con opzioni proteiche, frutta fresca e dolci fatti in casa per partire carichi.
                </p>
            </div>
            <div class="fade-up-element text-center">
                <div class="w-12 h-12 rounded-full border-2 border-alpine-gold flex items-center justify-center mx-auto mb-6">
                    <span class="font-serif text-lg text-alpine-gold">09</span>
                </div>
                <h4 class="font-serif text-lg text-alpine-text mb-3">Sui Sentieri</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Prendi la bici dal deposito e sei sui trail in 5 minuti. Niente auto, niente transfer.
                </p>
            </div>
            <div class="fade-up-element text-center">
                <div class="w-12 h-12 rounded-full border-2 border-alpine-gold flex items-center justify-center mx-auto mb-6">
                    <span class="font-serif text-lg text-alpine-gold">13</span>
                </div>
                <h4 class="font-serif text-lg text-alpine-text mb-3">Pranzo in Alpeggio</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Fermati in una delle malghe lungo il percorso per una polenta concia con vista sulle vette.
                </p>
            </div>
            <div class="fade-up-element text-center">
                <div class="w-12 h-12 rounded-full border-2 border-alpine-gold flex items-center justify-center mx-auto mb-6">
                    <span class="font-serif text-lg text-alpine-gold">17</span>
                </div>
                <h4 class="font-serif text-lg text-alpine-text mb-3">Relax & Wellness</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Lavi la bici, fai una doccia e ti immergi nella nostra spa. Gambe stanche, anima felice.
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
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">Tutto quello che devi sapere</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="fade-up-element bg-white p-10 border border-alpine-border">
                <h4 class="font-serif text-xl text-alpine-text mb-6 flex items-center gap-3">
                    <Sun class="w-5 h-5 text-alpine-gold" />
                    Stagione
                </h4>
                <div class="space-y-4 text-sm text-alpine-muted font-light">
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Apertura sentieri</span>
                        <span class="font-bold text-alpine-text">Giugno</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Chiusura sentieri</span>
                        <span class="font-bold text-alpine-text">Settembre</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Bike-lift attivo</span>
                        <span class="font-bold text-alpine-text">Luglio – Agosto</span>
                    </div>
                    <div class="flex justify-between items-center">
                        <span>Periodo migliore</span>
                        <span class="font-bold text-alpine-text">Luglio</span>
                    </div>
                </div>
            </div>

            <div class="fade-up-element bg-white p-10 border border-alpine-border">
                <h4 class="font-serif text-xl text-alpine-text mb-6 flex items-center gap-3">
                    <Flag class="w-5 h-5 text-alpine-gold" />
                    Consigli
                </h4>
                <div class="space-y-4 text-sm text-alpine-muted font-light">
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Casco</span>
                        <span class="font-bold text-alpine-text">Obbligatorio</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Protezioni</span>
                        <span class="font-bold text-alpine-text">Raccomandate</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Acqua</span>
                        <span class="font-bold text-alpine-text">Min. 1.5L</span>
                    </div>
                    <div class="flex justify-between items-center">
                        <span>Crema solare</span>
                        <span class="font-bold text-alpine-text">SPF 50+</span>
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
            <h2 class="font-serif text-4xl text-white mb-6">Pronto a Pedalare?</h2>
            <p class="text-white/50 text-sm font-light leading-relaxed max-w-lg mx-auto mb-12">
                Prenota il tuo soggiorno bike-friendly e scopri i sentieri più belli delle Alpi valdostane.
                Le tue ruote non vedono l'ora di toccare la terra.
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="/sport/noleggio" class="inline-flex items-center justify-center gap-3 bg-white text-alpine-text px-10 py-4 text-[11px] tracking-[0.2em] uppercase font-bold hover:bg-alpine-gold hover:text-white transition-all duration-300">
                    Noleggia una Bike <ArrowRight class="w-4 h-4" />
                </a>
                <a href="/esperienze/guide" class="inline-flex items-center justify-center gap-3 border border-white/30 text-white px-10 py-4 text-[11px] tracking-[0.2em] uppercase font-bold hover:border-white hover:bg-white/10 transition-all duration-300">
                    Prenota una Guida <ArrowRight class="w-4 h-4" />
                </a>
            </div>
        </div>
    </div>
</section>
