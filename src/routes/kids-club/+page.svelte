<script lang="ts">
    import { t } from '$lib/i18n';
    import { Baby, Palette, Puzzle, Clock, Users, ShieldCheck, Star, TreePine, Sun, Snowflake, Mountain, Music, BookOpen, Sparkles, ArrowRight, Heart, Smile, Cookie } from 'lucide-svelte';

    let scrollY = $state(0);
</script>

<svelte:window bind:scrollY />

<svelte:head>
    <title>{$t('kids_club.title')} | Chalet Du Soleil</title>
    <meta name="description" content="Kids Club dell'Chalet Du Soleil a Torgnon: laboratori creativi, giochi all'aperto, cacce al tesoro nella neve e attività dedicate ai bambini dai 3 ai 12 anni." />
</svelte:head>

<!-- ═══════════════════ HERO ═══════════════════ -->
<header class="relative h-[85vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div
        class="absolute inset-0 scale-110"
        style="transform: translateY({scrollY * 0.25}px) scale(1.1);"
    >
        <img src="/imgs/winter-park.webp" class="h-full w-full object-cover opacity-60" alt="Kids Club Chalet Du Soleil" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/30 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-28 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            {$t('kids_club.subtitle')} · Torgnon
        </span>
        <h1 class="font-serif text-5xl md:text-8xl leading-tight font-light text-white fade-up-element">
            {$t('kids_club.title')}
        </h1>
        <p class="mt-6 text-white/50 text-sm font-light max-w-md fade-up-element">
            Uno spazio magico dove i piccoli esploratori vivono la montagna
        </p>
    </div>
</header>

<!-- ═══════════════════ INTRO ═══════════════════ -->
<section class="bg-alpine-bg px-6 py-28">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <Baby class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            {$t('kids_club.description')}
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            Il nostro Kids Club è pensato per bambini dai 3 ai 12 anni e offre un programma ricco 
            di attività che cambiano con le stagioni. Dalle mattine creative ai pomeriggi avventurosi 
            all'aria aperta, ogni giorno è un'esperienza nuova.
        </p>
    </div>
</section>

<!-- ═══════════════════ IL NOSTRO SPAZIO ═══════════════════ -->
<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
        <img src="https://images.unsplash.com/photo-1587654780291-39c9404d7dd0?q=80&w=1500&auto=format&fit=crop" alt="Spazio giochi bambini" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
    </div>

    <div class="fade-up-element">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">Il Nostro Spazio</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">Un Mondo<br/>a Misura di Bambino</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            Il Kids Club occupa una sala luminosa e spaziosa al piano terra dell'hotel, 
            con accesso diretto al giardino. Arredi colorati, angolo morbido per i più piccoli, 
            tavoli da lavoro per i laboratori e un'area gioco con tutto ciò che serve 
            per scatenare la fantasia.
        </p>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
            Lo spazio è stato progettato con attenzione alla sicurezza: pavimenti antiurto, 
            spigoli protetti e una visuale aperta che permette alle nostre animatrici 
            di avere sempre tutti sotto controllo.
        </p>
        <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
            <div class="flex items-center gap-3">
                <ShieldCheck class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Sicurezza totale</span>
            </div>
            <div class="flex items-center gap-3">
                <Sun class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Luce naturale</span>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ STATS ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-20 px-6">
    <div class="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-12 text-center">
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">3–12</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Anni</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">6</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Giorni a settimana</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">2</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Animatrici dedicate</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">∞</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Sorrisi garantiti</p>
        </div>
    </div>
</section>

<!-- ═══════════════════ ATTIVITÀ ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">Le Attività</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">Un programma diverso ogni giorno</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12">
            <!-- Laboratori Creativi -->
            <div class="fade-up-element text-center p-12 md:p-14 border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <Palette class="w-8 h-8 text-alpine-gold mx-auto mb-8 stroke-[1.5px]" />
                <h4 class="font-serif text-2xl text-alpine-text mb-2">Laboratori Creativi</h4>
                <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-6">Mani in pasta</p>
                <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed">
                    Pittura con colori naturali, sculture di argilla, creazione di maschere alpine, 
                    collage con foglie e fiori di montagna. Ogni bambino porta a casa 
                    un piccolo capolavoro fatto con le proprie mani.
                </p>
            </div>

            <!-- Giochi & Sfide -->
            <div class="fade-up-element text-center p-12 md:p-14 border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <Puzzle class="w-8 h-8 text-alpine-gold mx-auto mb-8 stroke-[1.5px]" />
                <h4 class="font-serif text-2xl text-alpine-text mb-2">Giochi di Gruppo</h4>
                <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-6">Amicizia & divertimento</p>
                <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed">
                    Cacce al tesoro nel giardino dell'hotel, giochi da tavolo, tornei di carte, 
                    staffette e gare a squadre. Le vacanze sono più belle 
                    quando si fanno nuovi amici.
                </p>
            </div>

            <!-- Storie & Musica -->
            <div class="fade-up-element text-center p-12 md:p-14 border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <BookOpen class="w-8 h-8 text-alpine-gold mx-auto mb-8 stroke-[1.5px]" />
                <h4 class="font-serif text-2xl text-alpine-text mb-2">Storie & Musica</h4>
                <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-6">L'angolo della quiete</p>
                <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed">
                    Letture animate di leggende valdostane, canzoni della montagna 
                    e piccoli spettacoli di marionette. Il momento perfetto per rilassarsi 
                    dopo un pomeriggio di avventure.
                </p>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ INVERNO & ESTATE ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">Ogni Stagione, una Nuova Avventura</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">Il programma si adatta alla natura</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20">
            <!-- Inverno -->
            <div class="fade-up-element bg-alpine-bg p-12 md:p-14 border border-alpine-border">
                <div class="flex items-center gap-4 mb-8">
                    <Snowflake class="w-8 h-8 text-alpine-gold stroke-[1.5px]" />
                    <div>
                        <h4 class="font-serif text-2xl text-alpine-text">Inverno</h4>
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">Dicembre – Marzo</p>
                    </div>
                </div>
                <ul class="space-y-4 text-sm text-alpine-muted font-light">
                    <li class="flex items-start gap-3">
                        <Star class="w-3.5 h-3.5 text-alpine-gold shrink-0 mt-0.5" />
                        <span>Pupazzi di neve e costruzioni con gli igloo</span>
                    </li>
                    <li class="flex items-start gap-3">
                        <Star class="w-3.5 h-3.5 text-alpine-gold shrink-0 mt-0.5" />
                        <span>Ciaspolatina nel bosco con le racchette mini</span>
                    </li>
                    <li class="flex items-start gap-3">
                        <Star class="w-3.5 h-3.5 text-alpine-gold shrink-0 mt-0.5" />
                        <span>Caccia al tesoro nella neve</span>
                    </li>
                    <li class="flex items-start gap-3">
                        <Star class="w-3.5 h-3.5 text-alpine-gold shrink-0 mt-0.5" />
                        <span>Merenda calda con cioccolata e biscotti fatti in casa</span>
                    </li>
                    <li class="flex items-start gap-3">
                        <Star class="w-3.5 h-3.5 text-alpine-gold shrink-0 mt-0.5" />
                        <span>Laboratorio di decorazioni natalizie (periodo festivo)</span>
                    </li>
                </ul>
            </div>

            <!-- Estate -->
            <div class="fade-up-element bg-alpine-bg p-12 md:p-14 border border-alpine-border">
                <div class="flex items-center gap-4 mb-8">
                    <Sun class="w-8 h-8 text-alpine-gold stroke-[1.5px]" />
                    <div>
                        <h4 class="font-serif text-2xl text-alpine-text">Estate</h4>
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">Giugno – Settembre</p>
                    </div>
                </div>
                <ul class="space-y-4 text-sm text-alpine-muted font-light">
                    <li class="flex items-start gap-3">
                        <Star class="w-3.5 h-3.5 text-alpine-gold shrink-0 mt-0.5" />
                        <span>Esplorazioni nel bosco con la lente d'ingrandimento</span>
                    </li>
                    <li class="flex items-start gap-3">
                        <Star class="w-3.5 h-3.5 text-alpine-gold shrink-0 mt-0.5" />
                        <span>Raccolta erbe aromatiche e fiori di montagna</span>
                    </li>
                    <li class="flex items-start gap-3">
                        <Star class="w-3.5 h-3.5 text-alpine-gold shrink-0 mt-0.5" />
                        <span>Pic-nic nel prato con giochi all'aperto</span>
                    </li>
                    <li class="flex items-start gap-3">
                        <Star class="w-3.5 h-3.5 text-alpine-gold shrink-0 mt-0.5" />
                        <span>Mini-trekking all'alpeggio per vedere le mucche</span>
                    </li>
                    <li class="flex items-start gap-3">
                        <Star class="w-3.5 h-3.5 text-alpine-gold shrink-0 mt-0.5" />
                        <span>Osservazione delle stelle con il telescopio (sera)</span>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ LA GIORNATA TIPO ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-5xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">La Giornata Tipo</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">Dalle risate del mattino ai sogni della sera</p>
        </div>

        <div class="space-y-0">
            <div class="fade-up-element grid grid-cols-[60px_1fr] md:grid-cols-[80px_1fr] gap-6 border-b border-alpine-border py-8">
                <div class="text-right">
                    <span class="font-serif text-2xl text-alpine-gold">09:30</span>
                </div>
                <div>
                    <h4 class="font-serif text-lg text-alpine-text mb-1">Accoglienza & Gioco Libero</h4>
                    <p class="text-xs text-alpine-muted font-light leading-relaxed">
                        I bambini arrivano dopo la colazione e si ambientano con gioco libero supervisionato.
                    </p>
                </div>
            </div>

            <div class="fade-up-element grid grid-cols-[60px_1fr] md:grid-cols-[80px_1fr] gap-6 border-b border-alpine-border py-8">
                <div class="text-right">
                    <span class="font-serif text-2xl text-alpine-gold">10:00</span>
                </div>
                <div>
                    <h4 class="font-serif text-lg text-alpine-text mb-1">Laboratorio del Mattino</h4>
                    <p class="text-xs text-alpine-muted font-light leading-relaxed">
                        Attività creative guidata: pittura, argilla, costruzioni o il tema del giorno.
                    </p>
                </div>
            </div>

            <div class="fade-up-element grid grid-cols-[60px_1fr] md:grid-cols-[80px_1fr] gap-6 border-b border-alpine-border py-8">
                <div class="text-right">
                    <span class="font-serif text-2xl text-alpine-gold">11:30</span>
                </div>
                <div>
                    <h4 class="font-serif text-lg text-alpine-text mb-1">Avventura all'Aperto</h4>
                    <p class="text-xs text-alpine-muted font-light leading-relaxed">
                        Uscita nel giardino o nel bosco adiacente: caccia al tesoro, giochi di gruppo o mini-escursione.
                    </p>
                </div>
            </div>

            <div class="fade-up-element grid grid-cols-[60px_1fr] md:grid-cols-[80px_1fr] gap-6 border-b border-alpine-border py-8">
                <div class="text-right">
                    <span class="font-serif text-2xl text-alpine-gold">12:30</span>
                </div>
                <div>
                    <h4 class="font-serif text-lg text-alpine-text mb-1">Pranzo con Mamma e Papà</h4>
                    <p class="text-xs text-alpine-muted font-light leading-relaxed">
                        I bambini tornano in famiglia per il pranzo. Menù bimbi disponibile al ristorante.
                    </p>
                </div>
            </div>

            <div class="fade-up-element grid grid-cols-[60px_1fr] md:grid-cols-[80px_1fr] gap-6 border-b border-alpine-border py-8">
                <div class="text-right">
                    <span class="font-serif text-2xl text-alpine-gold">15:00</span>
                </div>
                <div>
                    <h4 class="font-serif text-lg text-alpine-text mb-1">Pomeriggio di Giochi</h4>
                    <p class="text-xs text-alpine-muted font-light leading-relaxed">
                        Tornei, sfide a squadre, giochi da tavolo o attività a tema stagionale.
                    </p>
                </div>
            </div>

            <div class="fade-up-element grid grid-cols-[60px_1fr] md:grid-cols-[80px_1fr] gap-6 py-8">
                <div class="text-right">
                    <span class="font-serif text-2xl text-alpine-gold">17:00</span>
                </div>
                <div>
                    <h4 class="font-serif text-lg text-alpine-text mb-1">Merenda & Storie</h4>
                    <p class="text-xs text-alpine-muted font-light leading-relaxed">
                        Merenda con prodotti locali, lettura animata e saluti. I genitori vengono a riprendere i piccoli esploratori.
                    </p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ BABY SITTING ═══════════════════ -->
<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element order-2 md:order-1">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">Servizio Dedicato</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">Baby Sitting<br/>Personalizzato</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            Per la serata romantica al ristorante, la sessione in spa o semplicemente un momento 
            di relax, offriamo un servizio di baby sitting su richiesta con personale qualificato 
            e referenziato.
        </p>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
            Il servizio è disponibile in camera o negli spazi comuni dell'hotel, 
            con orari flessibili e la possibilità di concordare attività specifiche 
            in base all'età e alle preferenze del bambino.
        </p>
        <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
            <div class="flex items-center gap-3">
                <Heart class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Personale qualificato</span>
            </div>
            <div class="flex items-center gap-3">
                <Clock class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Orari flessibili</span>
            </div>
        </div>
    </div>

    <div class="fade-up-element order-1 md:order-2 overflow-hidden bg-alpine-border shadow-xl">
        <img src="https://images.unsplash.com/photo-1503454537195-1dcabb73ffb9?q=80&w=1500&auto=format&fit=crop" alt="Bambina felice in montagna" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
    </div>
</section>

<!-- ═══════════════════ PER I GENITORI ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">Per Mamma & Papà</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">Mentre i bimbi si divertono, voi vi rilassate</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            <div class="fade-up-element text-center p-10">
                <Sparkles class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-[1.5px]" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Spa & Wellness</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Approfittate del Kids Club per una sessione di massaggi o un percorso benessere in coppia.
                </p>
            </div>
            <div class="fade-up-element text-center p-10">
                <Mountain class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-[1.5px]" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Sport & Outdoor</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Sciate in libertà, uscite in MTB o trekking impegnativi senza dovervi preoccupare dei bambini.
                </p>
            </div>
            <div class="fade-up-element text-center p-10">
                <Cookie class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-[1.5px]" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Pranzo in Pace</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    I bambini sono impegnati fino alle 12:30, abbastanza per un pranzo lungo e tranquillo al ristorante.
                </p>
            </div>
            <div class="fade-up-element text-center p-10">
                <Smile class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-[1.5px]" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Bimbi Felici</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    La cosa più bella? Ritrovare i vostri figli con un sorriso enorme e mille storie da raccontarvi.
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
                    Orari & Disponibilità
                </h4>
                <div class="space-y-4 text-sm text-alpine-muted font-light">
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Mattina</span>
                        <span class="font-bold text-alpine-text">09:30 – 12:30</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Pomeriggio</span>
                        <span class="font-bold text-alpine-text">15:00 – 17:00</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Giorni</span>
                        <span class="font-bold text-alpine-text">Lun – Sab</span>
                    </div>
                    <div class="flex justify-between items-center">
                        <span>Età</span>
                        <span class="font-bold text-alpine-text">3 – 12 anni</span>
                    </div>
                </div>
            </div>

            <div class="fade-up-element bg-white p-10 border border-alpine-border">
                <h4 class="font-serif text-xl text-alpine-text mb-6 flex items-center gap-3">
                    <ShieldCheck class="w-5 h-5 text-alpine-gold" />
                    Da Sapere
                </h4>
                <div class="space-y-4 text-sm text-alpine-muted font-light">
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Costo</span>
                        <span class="font-bold text-alpine-text">Incluso nel soggiorno</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Prenotazione</span>
                        <span class="font-bold text-alpine-text">Alla reception</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Baby sitting</span>
                        <span class="font-bold text-alpine-text">Su richiesta (extra)</span>
                    </div>
                    <div class="flex justify-between items-center">
                        <span>Merenda</span>
                        <span class="font-bold text-alpine-text">Inclusa</span>
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
            <h2 class="font-serif text-4xl text-white mb-6">Vacanza per Tutti</h2>
            <p class="text-white/50 text-sm font-light leading-relaxed max-w-lg mx-auto mb-12">
                Al Du Soleil, le famiglie sono di casa. I vostri bimbi troveranno nuovi amici, 
                nuove avventure e ricordi che porteranno nel cuore per sempre.
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="/camere" class="inline-flex items-center justify-center gap-3 bg-white text-alpine-text px-10 py-4 text-[11px] tracking-[0.2em] uppercase font-bold hover:bg-alpine-gold hover:text-white transition-all duration-300">
                    Scopri le Camere Familiari <ArrowRight class="w-4 h-4" />
                </a>
                <a href="/wellness" class="inline-flex items-center justify-center gap-3 border border-white/30 text-white px-10 py-4 text-[11px] tracking-[0.2em] uppercase font-bold hover:border-white hover:bg-white/10 transition-all duration-300">
                    La Spa per Voi <ArrowRight class="w-4 h-4" />
                </a>
            </div>
        </div>
    </div>
</section>
