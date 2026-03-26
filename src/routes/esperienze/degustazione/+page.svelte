<script lang="ts">
    import { Utensils, GlassWater, MapPin, Heart, Mountain, Users, Award, MilkOff, ExternalLink, Milk, Timer, Thermometer, FlaskConical } from 'lucide-svelte';

    let scrollY = $state(0);
</script>

<svelte:window bind:scrollY />

<svelte:head>
    <title>Degustazione Fontina DOP | Hotel du Soleil</title>
    <meta name="description" content="Degustazione di Fontina DOP e formaggi d'alpeggio in collaborazione con l'Azienda Agricola Lo Copafen, famiglia Perraillon." />
</svelte:head>

<header class="relative h-[85vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div
        class="absolute inset-0 scale-110"
        style="transform: translateY({scrollY * 0.25}px) scale(1.1);"
    >
        <video
            autoplay
            loop
            muted
            playsinline
            class="h-full w-full object-cover opacity-70"
            poster="https://www.fontina-dop.it/wp-content/uploads/2025/07/fontina-dop-forma.jpg"
        >
            <source src="/imgs/fontina-dop-hero.mp4" type="video/mp4" />
        </video>
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/20 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-28 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            Esperienza Gastronomica &middot; In Collaborazione con Lo Copafen
        </span>
        <h1 class="font-serif text-5xl md:text-8xl leading-tight font-light text-white fade-up-element">
            Fontina DOP
        </h1>
        <p class="mt-6 text-white/60 text-sm font-light max-w-md fade-up-element">
            Denominazione d'Origine Protetta della Valle d'Aosta
        </p>
    </div>
</header>

<section class="bg-alpine-bg px-6 py-28">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <Utensils class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            L'espressione più pura del latte di montagna.
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            Al nostro ristorante serviamo esclusivamente Fontina DOP prodotta dall'Azienda Agricola Lo Copafen della famiglia Perraillon &mdash; quattro generazioni di allevatori e casari nel cuore della Valle d'Aosta.
            Un formaggio autentico, lavorato a mano con latte crudo, che racconta il territorio in ogni morso.
        </p>
    </div>
</section>

<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
        <img src="https://images.unsplash.com/photo-1500595046743-cd271d694d30?q=80&w=1500&auto=format&fit=crop" alt="Alpeggio Valle d'Aosta" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90">
    </div>
    <div class="fade-up-element">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">La Famiglia Perraillon</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">Quattro Generazioni <br/>di Passione</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            Una famiglia di agricoltori valdostani, arrivati alla quarta generazione di lavoro diretto nei campi, con gli animali, con il latte.
            L'azienda si divide tra la fattoria di fondovalle a Chambave, dove vivono e lavorano tutto l'anno, e gli alpeggi di montagna dove si spostano in estate con le mandrie.
        </p>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
            Non una realtà costruita per i turisti, ma un'azienda agricola viva, concreta, che apre le porte a chi ha voglia di conoscere come si lavora davvero &mdash; con passione.
        </p>
        <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
            <div class="flex items-center gap-3">
                 <Heart class="w-5 h-5 text-alpine-gold shrink-0" />
                 <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Quasi 100 anni di storia</span>
            </div>
            <div class="flex items-center gap-3">
                 <Award class="w-5 h-5 text-alpine-gold shrink-0" />
                 <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">RAI Linea Verde 2018</span>
            </div>
        </div>
    </div>
</section>

<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element order-2 md:order-1">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">Allevamento Diretto</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">Il Latte <br/>di Montagna</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            L'azienda è fondata sull'allevamento diretto: 80 bovine in lattazione e 40 capre, allevate con cura secondo i ritmi della natura.
            Gli animali vivono in ambienti sani, si nutrono di foraggi locali e pascolano liberi in estate negli alpeggi di Crespin a Brusson e Chavanne ad Ayas, producendo un latte ricco e genuino.
        </p>
        <p class="text-alpine-muted text-sm font-light leading-relaxed">
            Ogni giorno, dai 500 ai 1000 litri di latte bovino e dai 40 ai 100 litri di latte caprino vengono trasformati con lavorazione artigianale nel caseificio aziendale, nel rispetto della materia prima e della tradizione.
        </p>
    </div>
    <div class="fade-up-element order-1 md:order-2 overflow-hidden bg-alpine-border shadow-xl">
        <img src="https://images.unsplash.com/photo-1594731884638-8197c3102d1d?q=80&w=1500&auto=format&fit=crop" alt="Bovine al pascolo in alpeggio" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90">
    </div>
</section>

<section class="border-y border-alpine-border bg-white py-20 px-6">
    <div class="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-12 text-center">
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">4ª</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Generazione</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">120</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Capi in lattazione</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">1500+</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Forme di Fontina / anno</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">3</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Alpeggi in quota</p>
        </div>
    </div>
</section>

<!-- ═══════════════════ LA DENOMINAZIONE DOP ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-16 lg:gap-24 items-center">
        <div class="fade-up-element">
            <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">Denominazione d'Origine Protetta</span>
            <h2 class="font-serif text-4xl text-alpine-text mb-6">La Fontina &egrave; <br/>la Valle d'Aosta</h2>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
                La Fontina DOP si colloca tra le punte di diamante dei formaggi di montagna. Con la sua pasta morbida ed elastica, fondente, dal profumo intenso e con un'occhiatura caratteristica, &egrave; un formaggio da gustare in tutte le occasioni.
            </p>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
                Tutto si svolge esclusivamente in Valle d'Aosta, l'unica area geografica dove pu&ograve; avvenire la produzione della Fontina DOP. Il latte deve essere crudo, intero, proveniente da una sola mungitura, di bovina appartenente alla razza valdostana &mdash; Pezzata Rossa, Pezzata Nera o Castana.
            </p>
            <p class="text-alpine-muted text-sm font-light leading-relaxed">
                Il Consorzio Produttori e Tutela della DOP Fontina conta su 169 soci e marchia circa 400.000 forme all'anno, difendendo un'eccellenza che si tramanda di padre in figlio da generazioni.
            </p>
        </div>
        <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
            <img src="https://images.unsplash.com/photo-1589985270826-4b7bb135bc9d?q=80&w=1500&auto=format&fit=crop" alt="Forme di Fontina DOP in stagionatura" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90">
        </div>
    </div>
</section>

<!-- ═══════════════════ LA LAVORAZIONE ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">La Lavorazione Artigianale</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">Un processo tramandato da generazioni</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
            <div class="fade-up-element text-center p-10 border border-alpine-border bg-alpine-bg">
                <Milk class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-1" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Il Latte</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Latte crudo, intero, da una sola mungitura di bovine di razza valdostana. Almeno il 60% dell'alimentazione &egrave; prodotta in Valle d'Aosta.
                </p>
            </div>
            <div class="fade-up-element text-center p-10 border border-alpine-border bg-alpine-bg">
                <FlaskConical class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-1" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">La Cagliatura</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Il latte viene portato a max 36&deg;C, il coagulo rotto in granuli omogenei, poi cotto su fuoco fino alla spinatura. Il casaro decide quando lo spurgo &egrave; ottimale.
                </p>
            </div>
            <div class="fade-up-element text-center p-10 border border-alpine-border bg-alpine-bg">
                <Thermometer class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-1" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">La Salamoia</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    La massa caseosa viene avvolta in tele, posta in fascere a scalzo concavo e pressata. Ogni forma riceve una placchetta di caseina che la identifica. Poi salamoia per max 12 ore.
                </p>
            </div>
            <div class="fade-up-element text-center p-10 border border-alpine-border bg-alpine-bg">
                <Timer class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-1" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">La Stagionatura</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Minimo 80 giorni in magazzini con umidit&agrave; al 90% e temperatura 4&ndash;12&deg;C. Salatura, rivoltamento e strofinatura a mano, come da tradizione secolare.
                </p>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ I FORMAGGI (Lo Copafen) ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">I Formaggi</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">Latte crudo &middot; Lavorazione artigianale &middot; Tradizione DOP</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12">
            <div class="fade-up-element text-center p-12 md:p-14 border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <MilkOff class="w-8 h-8 text-alpine-gold mx-auto mb-8 stroke-1" />
                <h4 class="font-serif text-2xl text-alpine-text mb-2">Fontina DOP</h4>
                <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-6">Fondovalle &middot; Ott &mdash; Mag</p>
                <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed max-w-xs mx-auto">
                    Prodotta a latte intero e crudo durante i mesi invernali. Più fresca e dolce, dalla consistenza morbida e fondente. L'espressione quotidiana della tradizione casearia valdostana.
                </p>
            </div>
            <div class="fade-up-element text-center p-12 md:p-14 border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <Mountain class="w-8 h-8 text-alpine-gold mx-auto mb-8 stroke-1" />
                <h4 class="font-serif text-2xl text-alpine-text mb-2">Fontina DOP d'Alpeggio</h4>
                <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-6">Alta Quota &middot; Giu &mdash; Set</p>
                <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed max-w-xs mx-auto">
                    Prodotta negli alpeggi estivi con latte crudo di bovine al pascolo libero. Più saporita e gustosa, con sentori erbacei intensi che raccontano i prati d'alta quota.
                </p>
            </div>
            <div class="fade-up-element text-center p-12 md:p-14 border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <Award class="w-8 h-8 text-alpine-gold mx-auto mb-8 stroke-1" />
                <h4 class="font-serif text-2xl text-alpine-text mb-2">Alpeggio Gran Riserva</h4>
                <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-6">Stagionatura oltre 6 mesi</p>
                <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed max-w-xs mx-auto">
                    La Fontina DOP d'alpeggio a lunga stagionatura. Oltre sei mesi in cantina le regalano un sapore intenso e deciso, con una complessità aromatica straordinaria. Il gioiello della produzione.
                </p>
            </div>
        </div>

        <div class="fade-up-element grid grid-cols-2 md:grid-cols-4 gap-6 mt-12">
            {#each ['Tome fresche e stagionate', 'Tomette di capra', 'Fonduta di Fontina DOP', 'Burro e yogurt artigianali', 'Robiola di capra', 'Blu di capra', 'Boudin valdostano', 'Mocetta e salumi'] as prodotto (prodotto)}
                <div class="text-center py-6 px-4 border border-alpine-border bg-white/50">
                    <p class="text-xs text-alpine-muted font-light">{prodotto}</p>
                </div>
            {/each}
        </div>
    </div>
</section>

<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
        <img src="https://images.unsplash.com/photo-1452195125355-903496c21e64?q=80&w=1500&auto=format&fit=crop" alt="Degustazione di formaggi" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90">
    </div>
    <div class="fade-up-element">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">L'Esperienza</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">Degustazione <br/>in Hotel</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            Ogni settimana organizziamo serate di degustazione guidata dedicata ai formaggi di Lo Copafen: Fontina DOP di fondovalle e d'alpeggio, tome fresche e stagionate, accompagnate da vini valdostani selezionati e miele di montagna.
        </p>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
            Il nostro chef vi guiderà in un percorso sensoriale tra i sapori autentici della Valle, raccontando la storia di ogni formaggio &mdash; dal pascolo alla stagionatura. Un'esperienza Km 0 reale, non un'etichetta di marketing.
        </p>
        <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
            <div class="flex items-center gap-3">
                 <GlassWater class="w-5 h-5 text-alpine-gold shrink-0" />
                 <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Abbinamenti Vini</span>
            </div>
            <div class="flex items-center gap-3">
                 <MapPin class="w-5 h-5 text-alpine-gold shrink-0" />
                 <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Km 0 Reale</span>
            </div>
        </div>
    </div>
</section>

<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element order-2 md:order-1">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">Escursione</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">Visita <br/>in Fattoria</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            Per chi desidera toccare con mano la realtà di un'azienda agricola valdostana, organizziamo visite alla fattoria Lo Copafen a Chambave.
            Potrete incontrare gli animali, visitare il caseificio dove il latte viene trasformato ogni giorno, esplorare le cantine di stagionatura e assaggiare i prodotti direttamente nel punto vendita aziendale.
        </p>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
            D'estate, per gli ospiti più avventurosi, è possibile organizzare un'escursione agli alpeggi in quota &mdash; Crespin a Brusson e Chavanne ad Ayas &mdash; per assistere alla munta e alla caseificazione tra le vette.
            Il sapore del formaggio appena fatto, circondati dal silenzio della montagna, è un'emozione che resterà impressa nei vostri sensi.
        </p>
        <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
            <div class="flex items-center gap-3">
                 <Users class="w-5 h-5 text-alpine-gold shrink-0" />
                 <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Gruppi su prenotazione</span>
            </div>
            <div class="flex items-center gap-3">
                 <Mountain class="w-5 h-5 text-alpine-gold shrink-0" />
                 <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Alpeggi in estate</span>
            </div>
        </div>
    </div>
    <div class="fade-up-element order-1 md:order-2 overflow-hidden bg-alpine-border shadow-xl">
        <img src="https://images.unsplash.com/photo-1516467508483-a7212febe31a?q=80&w=1500&auto=format&fit=crop" alt="Visita in fattoria" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90">
    </div>
</section>

<section class="border-t border-alpine-border bg-white py-20 px-6">
    <div class="max-w-3xl mx-auto text-center fade-up-element">
        <p class="text-[10px] uppercase tracking-[0.3em] text-alpine-muted font-bold mb-6">Il nostro Partner</p>
        <h3 class="font-serif text-3xl md:text-4xl text-alpine-text mb-4">Azienda Agricola Lo Copafen</h3>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-2">Famiglia Perraillon &middot; Frazione Septumian 60, 11023 Chambave (AO)</p>
        <p class="text-alpine-muted text-xs font-light mb-8">A 5 minuti dal Castello di Fénis &mdash; Valle d'Aosta</p>
        <a href="https://locopafen.it" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-alpine-gold hover:text-alpine-text transition-colors duration-300">
            Visita il sito
            <ExternalLink class="w-4 h-4" />
        </a>
    </div>
</section>
