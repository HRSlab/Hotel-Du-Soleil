<script lang="ts">
    import { Moon, Snowflake, Sparkles, Map, Mountain, Clock, Users, ShieldCheck, TreePine, Utensils, Sun, Star, Footprints, Lamp } from 'lucide-svelte';

    let scrollY = $state(0);
</script>

<svelte:window bind:scrollY />

<svelte:head>
    <title>Ciaspolate Notturne | Hotel du Soleil</title>
    <meta name="description" content="Ciaspolate notturne e diurne a Torgnon, Valle d'Aosta. Escursioni con racchette da neve tra boschi di larici con cena in rifugio e vista sul Cervino." />
</svelte:head>

<!-- ═══════════════════ HERO ═══════════════════ -->
<header class="relative h-[85vh] w-full overflow-hidden bg-[#0a0a0a]">
    <div
        class="absolute inset-0 scale-110"
        style="transform: translateY({scrollY * 0.25}px) scale(1.1);"
    >
        <img src="/imgs/hotel_by_night.jpg" class="h-full w-full object-cover opacity-50" alt="Ciaspolata notturna nei boschi innevati" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/30 to-[#0a0a0a]"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-28 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            La Magia della Notte · Torgnon
        </span>
        <h1 class="font-serif text-5xl md:text-8xl leading-tight font-light text-white fade-up-element">
            Ciaspolate Notturne
        </h1>
        <p class="mt-6 text-white/50 text-sm font-light max-w-md fade-up-element">
            Tra boschi di larici e il silenzio della neve, fino alla cena in rifugio
        </p>
    </div>
</header>

<!-- ═══════════════════ INTRO ═══════════════════ -->
<section class="bg-[#0a0a0a] text-white px-6 py-28">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <Moon class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-white md:text-4xl italic">
            “Sotto il chiarore lunare, la neve sussurra i suoi segreti.”
        </h3>
        <p class="text-white/60 leading-relaxed font-light text-sm md:text-base border-t border-white/10 pt-12 mt-12 mx-auto max-w-xl">
            Un’escursione notturna con le racchette da neve è un’esperienza quasi mistica.
            Accompagnati dalle nostre guide alpine, camminerete nel silenzio assoluto dei boschi innevati di Torgnon,
            illuminati solo dalle lampade frontali e dal riflesso della luna sulla neve,
            fino a raggiungere un rifugio dove vi attende una cena tipica valdostana davanti al fuoco.
        </p>
    </div>
</section>

<!-- ═══════════════════ L’ESPERIENZA ═══════════════════ -->
<section class="bg-[#0a0a0a] pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element overflow-hidden shadow-xl border border-white/10">
        <img src="/imgs/hotel_by_night.jpg" alt="Escursione con racchette da neve al tramonto" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-75">
    </div>
    <div class="fade-up-element">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">L’Esperienza</span>
        <h2 class="font-serif text-4xl text-white mb-6">Quando il Bosco <br/>si Addormenta</h2>
        <p class="text-white/60 text-sm font-light leading-relaxed mb-6">
            La partenza avviene al tramonto dall’hotel. Le guide vi equipaggiano con racchette da neve, bastoncini e lampade frontali, poi si parte lungo sentieri battuti che si inoltrano nei boschi di larici secolari sopra Torgnon.
        </p>
        <p class="text-white/60 text-sm font-light leading-relaxed mb-8">
            Man mano che la luce del giorno svanisce, il paesaggio si trasforma: il silenzio diventa totale, la neve brilla sotto le stelle e ogni passo scricchiola nel bianco. Niente telefoni, niente fretta — solo il respiro e la montagna.
        </p>
        <div class="grid grid-cols-2 gap-6 pt-6 border-t border-white/10">
            <div class="flex items-center gap-3">
                <Lamp class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-white/80">Lampade frontali</span>
            </div>
            <div class="flex items-center gap-3">
                <ShieldCheck class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-white/80">Guide certificate</span>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ 3 HIGHLIGHTS ═══════════════════ -->
<section class="bg-[#0a0a0a] pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
    <div class="bg-white/5 border border-white/10 p-12 fade-up-element">
        <Snowflake class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-1" />
        <h4 class="font-serif text-xl text-white mb-4">Percorso Magico</h4>
        <p class="text-xs text-white/50 font-light leading-relaxed">Attraversiamo boschi di larici e radure silenziose, con la neve fresca che attutisce ogni suono e le stelle come unica compagnia.</p>
    </div>
    <div class="bg-white/5 border border-white/10 p-12 fade-up-element">
        <Utensils class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-1" />
        <h4 class="font-serif text-xl text-white mb-4">Cena in Rifugio</h4>
        <p class="text-xs text-white/50 font-light leading-relaxed">Arrivo in baita per gustare polenta concia alla valdostana, carbonada, Fontina DOP fusa e dolci della tradizione, accanto al camino.</p>
    </div>
    <div class="bg-white/5 border border-white/10 p-12 fade-up-element">
        <Sparkles class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-1" />
        <h4 class="font-serif text-xl text-white mb-4">Rientro sotto le Stelle</h4>
        <p class="text-xs text-white/50 font-light leading-relaxed">Dopo la cena, il ritorno a piedi attraverso il bosco innevato è il momento più magico: il cielo di Torgnon, lontano dalle luci, rivela migliaia di stelle.</p>
    </div>
</section>

<!-- ═══════════════════ STATS STRIP ═══════════════════ -->
<section class="border-y border-white/10 bg-[#111] py-20 px-6">
    <div class="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-12 text-center">
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-white mb-2">3h</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-white/40 font-bold">Durata escursione</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-white mb-2">300m</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-white/40 font-bold">Dislivello massimo</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-white mb-2">Dic–Mar</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-white/40 font-bold">Stagione</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-white mb-2">4–15</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-white/40 font-bold">Partecipanti per gruppo</p>
        </div>
    </div>
</section>

<!-- ═══════════════════ I PERCORSI ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">I Percorsi</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">Tre itinerari per ogni livello di esperienza</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12">
            <div class="fade-up-element text-center p-12 md:p-14 border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <TreePine class="w-8 h-8 text-alpine-gold mx-auto mb-8 stroke-1" />
                <h4 class="font-serif text-2xl text-alpine-text mb-2">Bosco dei Larici</h4>
                <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-6">Facile · 1,5h · 150m dislivello</p>
                <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed max-w-xs mx-auto">
                    L’itinerario ideale per chi si avvicina per la prima volta alle ciaspolate. Un anello dolce attraverso il bosco di larici sopra Torgnon, con panorama finale sulla vallata. Adatto anche ai bambini dai 10 anni.
                </p>
            </div>
            <div class="fade-up-element text-center p-12 md:p-14 border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <Moon class="w-8 h-8 text-alpine-gold mx-auto mb-8 stroke-1" />
                <h4 class="font-serif text-2xl text-alpine-text mb-2">Sentiero della Luna</h4>
                <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-6">Medio · 3h · 300m dislivello</p>
                <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed max-w-xs mx-auto">
                    Il percorso classico della ciaspolata notturna con cena in rifugio. Si sale attraverso radure e boschi fino alla baita, dove vi attende una cena completa. Il rientro sotto il cielo stellato è indimenticabile.
                </p>
            </div>
            <div class="fade-up-element text-center p-12 md:p-14 border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <Mountain class="w-8 h-8 text-alpine-gold mx-auto mb-8 stroke-1" />
                <h4 class="font-serif text-2xl text-alpine-text mb-2">Cresta del Cervino</h4>
                <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-6">Impegnativo · 4h · 500m dislivello</p>
                <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed max-w-xs mx-auto">
                    Per escursionisti esperti. Un itinerario diurno che sale fino al belvedere con vista impareggiabile sul Cervino e la catena del Monte Rosa. Neve profonda, panorami sterminati, silenzio assoluto.
                </p>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ LA CENA IN RIFUGIO ═══════════════════ -->
<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element order-2 md:order-1">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">Il Cuore dell’Esperienza</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">La Cena <br/>in Rifugio</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            Dopo un’ora e mezza di cammino nella neve, arrivare in una baita calda e illuminata dal fuoco del camino è un’emozione che non si dimentica.
            I rifugisti vi accolgono con un bombardino caldo — la tradizionale bevanda delle Alpi a base di zabaione e brandy — prima di servire una cena autentica.
        </p>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
            Il menù cambia con le stagioni ma segue sempre la tradizione valdostana: zuppa alla valpellinentze con fontina e verza, polenta concia con Fontina DOP fusa, carbonada con polenta, e per finire tegole e dolci alle castagne. Il tutto accompagnato da vini rossi della Valle d’Aosta.
        </p>
        <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
            <div class="flex items-center gap-3">
                <Utensils class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Menù completo</span>
            </div>
            <div class="flex items-center gap-3">
                <Star class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Vini valdostani</span>
            </div>
        </div>
    </div>
    <div class="fade-up-element order-1 md:order-2 overflow-hidden bg-alpine-border shadow-xl">
        <img src="https://images.unsplash.com/photo-1414235077428-338989a2e8c0?q=80&w=1500&auto=format&fit=crop" alt="Cena in rifugio di montagna" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90">
    </div>
</section>

<!-- ═══════════════════ CIASPOLATE DIURNE ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-16 lg:gap-24 items-center">
        <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
            <img src="https://images.unsplash.com/photo-1551524559-8af4e6624178?q=80&w=1500&auto=format&fit=crop" alt="Ciaspolata diurna con vista sulle Alpi" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90">
        </div>
        <div class="fade-up-element">
            <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">Anche di Giorno</span>
            <h2 class="font-serif text-4xl text-alpine-text mb-6">Ciaspolate <br/>Diurne</h2>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
                Per chi preferisce la luce del sole o viaggia con bambini, organizziamo ciaspolate mattutine e pomeridiane lungo gli stessi sentieri incantati sopra Torgnon.
                La vista diurna sulle vette è spettacolare: il Cervino, il Gran Combin, la catena del Monte Rosa e tutta la valle che si apre ai vostri piedi.
            </p>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
                Le escursioni diurne sono ideali anche per chi non ha mai provato le racchette da neve. I nostri accompagnatori adattano il ritmo e il percorso al gruppo, fermandosi per ammirare i panorami, osservare le tracce degli animali nel bosco e raccontare la storia del territorio.
            </p>
            <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
                <div class="flex items-center gap-3">
                    <Sun class="w-5 h-5 text-alpine-gold shrink-0" />
                    <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Partenza ore 10:00</span>
                </div>
                <div class="flex items-center gap-3">
                    <Users class="w-5 h-5 text-alpine-gold shrink-0" />
                    <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Adatto a famiglie</span>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ COSA INCLUDE ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">Cosa Include</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">Tutto il necessario per un’esperienza senza pensieri</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
            <div class="fade-up-element text-center p-10 border border-alpine-border bg-white">
                <Footprints class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-1" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Attrezzatura</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Racchette da neve, bastoncini telescopici e lampade frontali fornite dall’hotel. Voi portate solo scarponi caldi e voglia di avventura.
                </p>
            </div>
            <div class="fade-up-element text-center p-10 border border-alpine-border bg-white">
                <ShieldCheck class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-1" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Guida Alpina</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Accompagnatore di media montagna certificato, con conoscenza perfetta dei sentieri e delle condizioni meteo e nivologiche del territorio.
                </p>
            </div>
            <div class="fade-up-element text-center p-10 border border-alpine-border bg-white">
                <Utensils class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-1" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Cena Completa</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Inclusa nell’escursione notturna: antipasto, primo, secondo, dolce e una bevanda. Piatti della tradizione valdostana preparati nel rifugio.
                </p>
            </div>
            <div class="fade-up-element text-center p-10 border border-alpine-border bg-white">
                <Clock class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-1" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Flessibilità</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Partenza direttamente dall’hotel. Escursioni programmate ogni mercoledì e sabato, o su richiesta per gruppi privati a partire da 4 persone.
                </p>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ INFO PRATICHE ═══════════════════ -->
<section class="bg-[#0a0a0a] py-32 px-6">
    <div class="max-w-4xl mx-auto">
        <div class="fade-up-element text-center mb-16">
            <h2 class="font-serif text-4xl text-white mb-5">Informazioni Pratiche</h2>
        </div>

        <div class="fade-up-element grid grid-cols-1 md:grid-cols-2 gap-12">
            <div>
                <h4 class="font-serif text-lg text-white mb-4 flex items-center gap-3">
                    <Moon class="w-5 h-5 text-alpine-gold" /> Ciaspolata Notturna + Cena
                </h4>
                <ul class="space-y-3 text-white/50 text-sm font-light">
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">•</span> Partenza alle 17:30 dall’hotel</li>
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">•</span> Durata circa 3 ore (cena inclusa)</li>
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">•</span> Difficoltà: facile/media</li>
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">•</span> Età minima: 12 anni</li>
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">•</span> Ogni mercoledì e sabato, Dic–Mar</li>
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">•</span> Min. 4 — Max. 15 partecipanti</li>
                </ul>
            </div>
            <div>
                <h4 class="font-serif text-lg text-white mb-4 flex items-center gap-3">
                    <Sun class="w-5 h-5 text-alpine-gold" /> Ciaspolata Diurna
                </h4>
                <ul class="space-y-3 text-white/50 text-sm font-light">
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">•</span> Partenza alle 10:00 dall’hotel</li>
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">•</span> Durata 2–4 ore (a scelta)</li>
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">•</span> Difficoltà: facile</li>
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">•</span> Età minima: 8 anni</li>
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">•</span> Su richiesta, tutti i giorni</li>
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">•</span> Ideale per famiglie con bambini</li>
                </ul>
            </div>
        </div>

        <div class="fade-up-element mt-16 pt-12 border-t border-white/10 text-center">
            <p class="text-white/40 text-xs font-light leading-relaxed max-w-xl mx-auto">
                Tutte le escursioni sono soggette a condizioni meteo e nivologiche favorevoli.
                La reception è a disposizione per informazioni, prenotazioni e per aiutarvi a scegliere il percorso più adatto a voi.
            </p>
        </div>
    </div>
</section>
