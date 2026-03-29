<script lang="ts">
    import { t } from '$lib/i18n';
    import { Moon, Star, Clock, Wine, Gem, ArrowRight, ShieldCheck, Users, Heart, Lock, Sparkles, Flame, Droplets, Music } from 'lucide-svelte';

    let scrollY = $state(0);
</script>

<svelte:window bind:scrollY />

<svelte:head>
    <title>{$t('wellness.private_spa.title')} | Hotel du Soleil</title>
    <meta name="description" content="Private SPA esclusiva all'Hotel du Soleil di Torgnon. Idromassaggio, sauna finlandese e piscina in uso privato per coppie e piccoli gruppi. Bottiglia di vino e amenità incluse." />
</svelte:head>

<!-- ═══════════════════ HERO ═══════════════════ -->
<header class="relative h-[85vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div
        class="absolute inset-0 scale-110"
        style="transform: translateY({scrollY * 0.25}px) scale(1.1);"
    >
        <img src="https://images.unsplash.com/photo-1582719508461-905c673771fd?q=80&w=2000&auto=format&fit=crop" class="h-full w-full object-cover opacity-50" alt="Private SPA notturna" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/30 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-28 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            {$t('wellness.private_spa.subtitle')}
        </span>
        <h1 class="font-serif text-5xl md:text-8xl leading-tight font-light text-white fade-up-element">
            {$t('wellness.private_spa.title')}
        </h1>
        <p class="mt-6 text-white/50 text-sm font-light max-w-md fade-up-element">
            L'intera area wellness riservata solo a voi
        </p>
    </div>
</header>

<!-- ═══════════════════ INTRO ═══════════════════ -->
<section class="bg-alpine-bg px-6 py-28">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <Moon class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            Chiudete la porta. Il mondo resta fuori.
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            Idromassaggio, sauna finlandese e piscina riscaldata — tutto in uso esclusivo, 
            solo per voi. Nessun altro ospite, nessuna fretta. 
            Una bottiglia di vino valdostano, frutta fresca e amenità premium vi aspettano. 
            L'esperienza più intima che il nostro hotel possa offrire.
        </p>
    </div>
</section>

<!-- ═══════════════════ L'AREA ═══════════════════ -->
<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
        <img src="https://images.unsplash.com/photo-1600334129128-685c5582fd35?q=80&w=1500&auto=format&fit=crop" alt="Area idromassaggio privata" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
    </div>

    <div class="fade-up-element">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">Accesso Esclusivo</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">Tre Ambienti,<br/>Un Solo Privilegio</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
            Quando prenotate la Private SPA, l'intera area wellness viene chiusa 
            al resto degli ospiti e diventa il vostro rifugio privato. 
            Potete muovervi liberamente tra gli ambienti, scegliere la musica, 
            regolare le luci e vivere ogni momento secondo il vostro ritmo.
        </p>
        <div class="space-y-4">
            <div class="flex items-start gap-4 p-4 border border-alpine-border bg-white">
                <Droplets class="w-5 h-5 text-alpine-gold shrink-0 mt-0.5" />
                <div>
                    <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">Idromassaggio</p>
                    <p class="text-xs text-alpine-muted font-light">Vasca con getti massaggianti a temperatura controllata, cromoterapia e aromaterapia incluse</p>
                </div>
            </div>
            <div class="flex items-start gap-4 p-4 border border-alpine-border bg-white">
                <Flame class="w-5 h-5 text-alpine-gold shrink-0 mt-0.5" />
                <div>
                    <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">Sauna Finlandese</p>
                    <p class="text-xs text-alpine-muted font-light">Temperatura regolabile fino a 90°C, legno di cirmolo valdostano, gettate di vapore con oli essenziali</p>
                </div>
            </div>
            <div class="flex items-start gap-4 p-4 border border-alpine-border bg-white">
                <Sparkles class="w-5 h-5 text-alpine-gold shrink-0 mt-0.5" />
                <div>
                    <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">Piscina Riscaldata</p>
                    <p class="text-xs text-alpine-muted font-light">Acqua a 32°C, nuoto libero e zona relax con lettini riscaldati e vista sulle Alpi</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ STATS ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-20 px-6">
    <div class="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-12 text-center">
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">3</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Ambienti esclusivi</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">32°C</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Piscina riscaldata</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">2h</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Accesso minimo</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">6</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Ospiti max</p>
        </div>
    </div>
</section>

<!-- ═══════════════════ I PACCHETTI ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">I Pacchetti</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">Scegliete l'esperienza perfetta per voi</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12">
            <!-- Coppia -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Heart class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">Per Due</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Romantic Escape</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-6">2 ore · 2 persone · €180</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        Due ore di esclusività assoluta per la coppia. 
                        L'intera area wellness è vostra: idromassaggio con cromoterapia, 
                        sauna finlandese e piscina riscaldata.
                    </p>
                    <div class="pt-6 border-t border-alpine-border space-y-3">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-3">Include</p>
                        <div class="flex items-center gap-2">
                            <Wine class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">Bottiglia di vino valdostano</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Gem class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">Frutta fresca e cioccolatini</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Sparkles class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">Accappatoi e ciabatte premium</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Music class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">Selezione musicale a scelta</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Piccolo Gruppo -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Users class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">Piccolo Gruppo</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Friends & Family</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-6">2 ore · 3–6 persone · €280</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        Perfetto per festeggiare un'occasione speciale con gli amici più cari 
                        o per una serata in famiglia. Stesse amenità del pacchetto coppia, 
                        ampliate per il gruppo.
                    </p>
                    <div class="pt-6 border-t border-alpine-border space-y-3">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-3">Include</p>
                        <div class="flex items-center gap-2">
                            <Wine class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">2 bottiglie di vino valdostano</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Gem class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">Tagliere di formaggi e frutta</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Sparkles class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">Accappatoi e ciabatte per tutti</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Music class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">Selezione musicale a scelta</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- BY NIGHT — PREMIUM -->
            <div class="fade-up-element group border-2 border-alpine-gold bg-white shadow-xl hover:shadow-2xl transition-all duration-500 relative">
                <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-alpine-gold text-white px-5 py-1.5 text-[10px] uppercase tracking-[0.3em] font-bold">
                    Esclusivo
                </div>
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Moon class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">Premium</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Private SPA by Night</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-6">3 ore · 2–4 persone · €380</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        L'esperienza definitiva. Dalle 21:00 a mezzanotte, l'area wellness 
                        si trasforma in un santuario notturno con luci soffuse, candele 
                        e il silenzio assoluto della montagna. Tre ore per perdersi nel tempo.
                    </p>
                    <div class="pt-6 border-t border-alpine-gold/30 space-y-3">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-3">Include tutto, e di più</p>
                        <div class="flex items-center gap-2">
                            <Wine class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">Bottiglia di Champagne o vino premium</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Gem class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">Tagliere gourmet e praline artigianali</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Star class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">Candele profumate e luci d'atmosfera</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Sparkles class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">Kit beauty premium e accappatoi caldi</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Music class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">Playlist curata o silenzio totale</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Clock class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">3 ore complete (21:00 – 00:00)</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ L'ATMOSFERA NOTTURNA ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
        <div class="fade-up-element">
            <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">Private SPA by Night</span>
            <h2 class="font-serif text-4xl text-alpine-text mb-6">Quando la Montagna<br/>Dorme, Voi Brillate</h2>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
                Dalle 21:00, l'hotel entra in una quiete speciale. 
                Le luci dell'area wellness si abbassano, le candele si accendono 
                e l'unico suono è quello dell'acqua che scorre. 
                È l'ora più esclusiva del nostro hotel.
            </p>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
                Lo Champagne vi aspetta al bordo vasca. Il tagliere gourmet — 
                Fontina DOP, lardo d'Arnad, miele di montagna, praline artigianali — 
                è preparato dal nostro chef. Tre ore che non vi sembreranno mai abbastanza.
            </p>
            <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
                <div class="flex items-center gap-3">
                    <Moon class="w-5 h-5 text-alpine-gold shrink-0" />
                    <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">21:00 – 00:00</span>
                </div>
                <div class="flex items-center gap-3">
                    <Lock class="w-5 h-5 text-alpine-gold shrink-0" />
                    <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">100% Privata</span>
                </div>
            </div>
        </div>

        <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
            <img src="https://images.unsplash.com/photo-1545579133-99bb5ab189bd?q=80&w=1500&auto=format&fit=crop" alt="SPA notturna con candele" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-85" />
        </div>
    </div>
</section>

<!-- ═══════════════════ COSA INCLUDE ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-5xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">Ogni Dettaglio Conta</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">Incluso in tutti i pacchetti</p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
            <div class="fade-up-element text-center p-8 bg-white border border-alpine-border">
                <Wine class="w-8 h-8 text-alpine-gold mx-auto mb-5" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Vino & Bollicine</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Vino della Valle d'Aosta o Champagne (pacchetto By Night). 
                    Servito a bordo vasca alla temperatura perfetta.
                </p>
            </div>
            <div class="fade-up-element text-center p-8 bg-white border border-alpine-border">
                <Gem class="w-8 h-8 text-alpine-gold mx-auto mb-5" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Degustazione</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Frutta fresca, cioccolatini artigianali e formaggi locali. 
                    Il pacchetto notturno include un tagliere gourmet completo.
                </p>
            </div>
            <div class="fade-up-element text-center p-8 bg-white border border-alpine-border">
                <Sparkles class="w-8 h-8 text-alpine-gold mx-auto mb-5" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Comfort Premium</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Accappatoi caldi, ciabatte morbide, teli di spugna e kit beauty 
                    con prodotti naturali alpini.
                </p>
            </div>
            <div class="fade-up-element text-center p-8 bg-white border border-alpine-border">
                <Lock class="w-8 h-8 text-alpine-gold mx-auto mb-5" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Privacy Totale</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    L'area è chiusa a tutti gli altri ospiti. 
                    Nessuna interruzione, nessun orario da rispettare all'interno della fascia prenotata.
                </p>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ OCCASIONI SPECIALI ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
        <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl order-2 md:order-1">
            <img src="https://images.unsplash.com/photo-1540555700478-4be289fbec6d?q=80&w=1500&auto=format&fit=crop" alt="Occasione speciale in SPA" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
        </div>

        <div class="fade-up-element order-1 md:order-2">
            <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">Su Misura</span>
            <h2 class="font-serif text-4xl text-alpine-text mb-6">Occasioni Speciali</h2>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
                La Private SPA è il luogo perfetto per rendere un momento speciale 
                ancora più indimenticabile. Anniversari, compleanni, proposte di matrimonio: 
                diteci cosa volete celebrare e personalizziamo tutto per voi.
            </p>
            <div class="space-y-5">
                <div class="flex items-start gap-4">
                    <Heart class="w-5 h-5 text-alpine-gold shrink-0 mt-0.5" />
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">Anniversari & Proposte</p>
                        <p class="text-xs text-alpine-muted font-light">Petali di rosa, Champagne e un messaggio personalizzato</p>
                    </div>
                </div>
                <div class="flex items-start gap-4">
                    <Star class="w-5 h-5 text-alpine-gold shrink-0 mt-0.5" />
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">Compleanni</p>
                        <p class="text-xs text-alpine-muted font-light">Torta personalizzata e decorazioni a tema</p>
                    </div>
                </div>
                <div class="flex items-start gap-4">
                    <Users class="w-5 h-5 text-alpine-gold shrink-0 mt-0.5" />
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">Team & Addii al Nubilato</p>
                        <p class="text-xs text-alpine-muted font-light">Pacchetto gruppo con prosecco, taglieri e atmosfera festa</p>
                    </div>
                </div>
            </div>
            <p class="mt-8 text-[10px] uppercase tracking-widest text-alpine-muted font-bold">
                Parlate con la reception per personalizzare la vostra esperienza
            </p>
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
                    Orari & Prenotazioni
                </h4>
                <div class="space-y-4 text-sm text-alpine-muted font-light">
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Fasce giornaliere</span>
                        <span class="font-bold text-alpine-text">10–12 / 14–16 / 17–19</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Fascia By Night</span>
                        <span class="font-bold text-alpine-text">21:00 – 00:00</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Prenotazione</span>
                        <span class="font-bold text-alpine-text">Alla reception</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Preavviso minimo</span>
                        <span class="font-bold text-alpine-text">24 ore</span>
                    </div>
                    <div class="flex justify-between items-center">
                        <span>Cancellazione</span>
                        <span class="font-bold text-alpine-text">Gratuita entro 24h</span>
                    </div>
                </div>
            </div>

            <div class="fade-up-element bg-white p-10 border border-alpine-border">
                <h4 class="font-serif text-xl text-alpine-text mb-6 flex items-center gap-3">
                    <ShieldCheck class="w-5 h-5 text-alpine-gold" />
                    Buono a Sapersi
                </h4>
                <div class="space-y-4 text-sm text-alpine-muted font-light">
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Età minima</span>
                        <span class="font-bold text-alpine-text">16 anni</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Costume</span>
                        <span class="font-bold text-alpine-text">Obbligatorio</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Accappatoio</span>
                        <span class="font-bold text-alpine-text">Incluso</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Massaggio aggiuntivo</span>
                        <span class="font-bold text-alpine-text">Combinabile (-10%)</span>
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

<!-- ═══════════════════ RIEPILOGO PREZZI ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-20 px-6">
    <div class="max-w-4xl mx-auto">
        <div class="fade-up-element text-center mb-12">
            <h3 class="font-serif text-3xl text-alpine-text">Riepilogo Pacchetti</h3>
        </div>
        <div class="fade-up-element border border-alpine-border divide-y divide-alpine-border">
            <div class="grid grid-cols-4 p-5 bg-alpine-bg">
                <span class="text-[10px] uppercase tracking-widest font-bold text-alpine-text">Pacchetto</span>
                <span class="text-[10px] uppercase tracking-widest font-bold text-alpine-text text-center">Persone</span>
                <span class="text-[10px] uppercase tracking-widest font-bold text-alpine-text text-center">Durata</span>
                <span class="text-[10px] uppercase tracking-widest font-bold text-alpine-text text-right">Prezzo</span>
            </div>
            <div class="grid grid-cols-4 p-5 items-center">
                <div>
                    <p class="font-serif text-sm text-alpine-text">Romantic Escape</p>
                </div>
                <p class="text-sm text-alpine-muted font-light text-center">2</p>
                <p class="text-sm text-alpine-muted font-light text-center">2 ore</p>
                <p class="text-sm font-bold text-alpine-text text-right">€180</p>
            </div>
            <div class="grid grid-cols-4 p-5 items-center bg-alpine-bg/50">
                <div>
                    <p class="font-serif text-sm text-alpine-text">Friends & Family</p>
                </div>
                <p class="text-sm text-alpine-muted font-light text-center">3–6</p>
                <p class="text-sm text-alpine-muted font-light text-center">2 ore</p>
                <p class="text-sm font-bold text-alpine-text text-right">€280</p>
            </div>
            <div class="grid grid-cols-4 p-5 items-center border-l-4 border-l-alpine-gold">
                <div>
                    <p class="font-serif text-sm text-alpine-text">Private SPA by Night</p>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mt-1">Premium</p>
                </div>
                <p class="text-sm text-alpine-muted font-light text-center">2–4</p>
                <p class="text-sm text-alpine-muted font-light text-center">3 ore</p>
                <p class="text-sm font-bold text-alpine-gold text-right">€380</p>
            </div>
        </div>
        <p class="text-center text-[10px] uppercase tracking-widest text-alpine-muted font-bold mt-6">
            Tutti i prezzi includono vino, food & amenità · Personalizzazioni su richiesta
        </p>
    </div>
</section>

<!-- ═══════════════════ CTA ═══════════════════ -->
<section class="bg-[#0a0a0a] py-32 px-6">
    <div class="max-w-3xl mx-auto text-center">
        <div class="fade-up-element">
            <Moon class="w-10 h-10 text-alpine-gold mx-auto mb-8" />
            <h2 class="font-serif text-4xl text-white mb-6">Riservate la Vostra Serata</h2>
            <p class="text-white/50 text-sm font-light leading-relaxed max-w-lg mx-auto mb-12">
                Pochi slot disponibili ogni settimana. 
                Chiedete alla reception per assicurarvi la vostra Private SPA.
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="/wellness/massaggi" class="inline-flex items-center justify-center gap-3 bg-white text-alpine-text px-10 py-4 text-[11px] tracking-[0.2em] uppercase font-bold hover:bg-alpine-gold hover:text-white transition-all duration-300">
                    I Massaggi <ArrowRight class="w-4 h-4" />
                </a>
                <a href="/wellness/spa" class="inline-flex items-center justify-center gap-3 border border-white/30 text-white px-10 py-4 text-[11px] tracking-[0.2em] uppercase font-bold hover:border-white hover:bg-white/10 transition-all duration-300">
                    Area Wellness <ArrowRight class="w-4 h-4" />
                </a>
            </div>
        </div>
    </div>
</section>
