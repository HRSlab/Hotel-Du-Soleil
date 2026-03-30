<script lang="ts">
    import { PackageCheck, ShieldCheck, Snowflake, ArrowRight, X, Thermometer, Lock, Eye, CalendarDays, User, Mail, Phone, ChevronDown } from 'lucide-svelte';
    import { fade, fly } from 'svelte/transition';
    import { clickOutside } from '$lib/utils/clickOutside';

    let scrollY = $state(0);
    let showRentalForm = $state(false);

    // Form state
    let formName = $state('');
    let formEmail = $state('');
    let formPhone = $state('');
    let formArrival = $state('');
    let formDeparture = $state('');
    let formAdults = $state(1);
    let formChildren = $state(0);
    let formEquipment = $state('sci');
    let formLevel = $state('intermedio');
    let formBootSizeAdult = $state('');
    let formBootSizeChild = $state('');
    let formHelmet = $state(true);
    let formNotes = $state('');
    let formSubmitted = $state(false);

    const PARTNER_EMAIL = 'bellocarlo@gmail.com';

    function handleSubmit(e: Event) {
        e.preventDefault();

        const subject = encodeURIComponent(`Prenotazione Noleggio – Chalet do Soleil – ${formName}`);

        let body = `RICHIESTA NOLEGGIO ATTREZZATURA\n`;
        body += `Chalet do Soleil – Torgnon\n`;
        body += `${'\u2500'.repeat(40)}\n\n`;
        body += `DATI OSPITE\n`;
        body += `Nome: ${formName}\n`;
        body += `Email: ${formEmail}\n`;
        body += `Telefono: ${formPhone || 'Non indicato'}\n\n`;
        body += `PERIODO\n`;
        body += `Arrivo: ${formArrival}\n`;
        body += `Partenza: ${formDeparture}\n`;
        body += `Adulti: ${formAdults}\n`;
        body += `Bambini: ${formChildren}\n\n`;
        body += `ATTREZZATURA\n`;
        body += `Tipo: ${formEquipment === 'sci' ? 'Sci alpino' : formEquipment === 'snowboard' ? 'Snowboard' : formEquipment === 'ciaspole' ? 'Ciaspole' : 'Sci di fondo'}\n`;
        body += `Livello: ${formLevel === 'principiante' ? 'Principiante' : formLevel === 'intermedio' ? 'Intermedio' : 'Esperto'}\n`;
        body += `Taglia scarponi adulto: ${formBootSizeAdult || 'Da definire'}\n`;
        if (formChildren > 0) {
            body += `Taglia scarponi bambino: ${formBootSizeChild || 'Da definire'}\n`;
        }
        body += `Casco: ${formHelmet ? 'S\u00ec, incluso' : 'No'}\n`;
        if (formNotes) {
            body += `\nNOTE\n${formNotes}\n`;
        }
        body += `\n${'\u2500'.repeat(40)}\n`;
        body += `Inviato tramite il sito Chalet do Soleil`;

        const mailtoUrl = `mailto:${PARTNER_EMAIL}?subject=${subject}&body=${encodeURIComponent(body)}`;
        const link = document.createElement('a');
        link.href = mailtoUrl;
        link.click();

        setTimeout(() => {
            formSubmitted = true;
            setTimeout(() => {
                formSubmitted = false;
                showRentalForm = false;
            }, 3000);
        }, 500);
    }
</script>

<svelte:window bind:scrollY />

<svelte:head>
    <title>Ski Box & Noleggio | Chalet do Soleil</title>
    <meta name="description" content="Deposito sci con ski box dedicati e servizio noleggio attrezzatura a Torgnon. Scarponi al caldo, sci sempre pronti." />
</svelte:head>

<!-- \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 HERO \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 -->
<header class="relative h-[85vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div
        class="absolute inset-0 scale-110"
        style="transform: translateY({scrollY * 0.25}px) scale(1.1);"
    >
        <img src="https://images.unsplash.com/photo-1551698618-1fed5d97530d?q=80&w=2000&auto=format&fit=crop" class="h-full w-full object-cover opacity-60" alt="Noleggio Sci Torgnon" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/30 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-28 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            Deposito & Attrezzatura \u00b7 Torgnon
        </span>
        <h1 class="font-serif text-5xl md:text-8xl leading-tight font-light text-white fade-up-element">
            Ski Box & Noleggio
        </h1>
        <p class="mt-6 text-white/50 text-sm font-light max-w-md fade-up-element">
            I tuoi sci al sicuro, i tuoi scarponi sempre caldi e asciutti
        </p>
    </div>
</header>

<!-- \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 INTRO \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 -->
<section class="bg-alpine-bg px-6 py-28">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <PackageCheck class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            Tutto ci\u00f2 di cui hai bisogno, proprio qui in hotel.
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            Per offrirti la massima comodit\u00e0, mettiamo a disposizione ski box dedicati per la tua attrezzatura
            e un deposito scarponi riscaldato all\u2019interno dell\u2019hotel.
            Grazie alla collaborazione con il nostro partner noleggio, puoi prenotare l\u2019attrezzatura prima del tuo arrivo
            e trovarla gi\u00e0 pronta ad aspettarti.
        </p>
    </div>
</section>

<!-- \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 SKI BOX \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 -->
<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
        <img src="https://images.unsplash.com/photo-1565992441121-4367c2967103?q=80&w=1500&auto=format&fit=crop" alt="Ski box deposito sci" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90">
    </div>
    <div class="fade-up-element">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">Deposito Attrezzatura</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">Ski Box <br/>Dedicati</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            Ogni camera dispone del proprio ski box riservato, situato all\u2019esterno dell\u2019hotel, accanto alla reception.
            I box non sono riscaldati ma sono chiusi a chiave e videosorvegliati 24 ore su 24,
            per garantire la massima sicurezza della tua attrezzatura.
        </p>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
            La posizione strategica dei box \u2014 a pochi metri dall\u2019ingresso e dalla pista \u2014
            ti permette di prendere sci e bastoncini e partire direttamente verso gli impianti senza perdere tempo.
        </p>
        <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
            <div class="flex items-center gap-3">
                <Lock class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Chiusi a chiave</span>
            </div>
            <div class="flex items-center gap-3">
                <Eye class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Videosorveglianza 24h</span>
            </div>
        </div>
    </div>
</section>

<!-- \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 DEPOSITO SCARPONI \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 -->
<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element order-2 md:order-1">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">Comfort & Calore</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">Deposito Scarponi <br/>Riscaldato</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            Gli scarponi da sci meritano un trattamento speciale. Per questo abbiamo dedicato una stanza riscaldata all\u2019interno dell\u2019hotel,
            proprio accanto alla reception, dove potrete riporre i vostri scarponi ogni sera.
        </p>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
            Grazie al riscaldamento costante, ogni mattina troverete scarponi perfettamente asciutti e caldi,
            pronti per una nuova giornata sulle piste. Niente pi\u00f9 la spiacevole sensazione di infilare scarponi gelati e umidi.
        </p>
        <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
            <div class="flex items-center gap-3">
                <Thermometer class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Ambiente riscaldato</span>
            </div>
            <div class="flex items-center gap-3">
                <ShieldCheck class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Accesso reception</span>
            </div>
        </div>
    </div>
    <div class="fade-up-element order-1 md:order-2 overflow-hidden bg-alpine-border shadow-xl">
        <img src="https://images.unsplash.com/photo-1605540436563-5bca919ae766?q=80&w=1500&auto=format&fit=crop" alt="Deposito scarponi riscaldato" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90">
    </div>
</section>

<!-- \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 STATS \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 -->
<section class="border-y border-alpine-border bg-white py-20 px-6">
    <div class="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-12 text-center">
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">1</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Box per camera</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">24h</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Videosorveglianza</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">22\u00b0C</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Deposito scarponi</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">50m</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Dalla pista</p>
        </div>
    </div>
</section>

<!-- \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 NOLEGGIO PARTNER \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">Noleggio Attrezzatura</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">In collaborazione con il nostro partner locale</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12">
            <div class="fade-up-element text-center p-12 md:p-14 border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <Snowflake class="w-8 h-8 text-alpine-gold mx-auto mb-8 stroke-1" />
                <h4 class="font-serif text-2xl text-alpine-text mb-2">Sci & Snowboard</h4>
                <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-6">Attrezzatura completa</p>
                <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed max-w-xs mx-auto">
                    Sci alpino, snowboard, scarponi, bastoncini e casco. Attrezzatura di ultima generazione, regolata e preparata per il tuo livello e peso.
                </p>
            </div>
            <div class="fade-up-element text-center p-12 md:p-14 border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <PackageCheck class="w-8 h-8 text-alpine-gold mx-auto mb-8 stroke-1" />
                <h4 class="font-serif text-2xl text-alpine-text mb-2">Consegna in Hotel</h4>
                <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-6">Zero code, zero stress</p>
                <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed max-w-xs mx-auto">
                    Prenota prima del tuo arrivo e troverai l\u2019attrezzatura direttamente nel tuo ski box.
                    Zero file al noleggio, zero perdite di tempo. Arrivi e scii.
                </p>
            </div>
            <div class="fade-up-element text-center p-12 md:p-14 border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <ShieldCheck class="w-8 h-8 text-alpine-gold mx-auto mb-8 stroke-1" />
                <h4 class="font-serif text-2xl text-alpine-text mb-2">Assistenza Dedicata</h4>
                <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-6">Supporto durante il soggiorno</p>
                <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed max-w-xs mx-auto">
                    Problemi con gli attacchi? Scarponi scomodi? Il nostro partner \u00e8 a disposizione per sostituzioni e regolazioni durante tutto il tuo soggiorno.
                </p>
            </div>
        </div>

        <div class="fade-up-element text-center mt-16">
            <button
                onclick={() => showRentalForm = true}
                class="inline-flex items-center gap-3 border-2 border-alpine-text text-alpine-text px-10 py-4 text-[11px] tracking-[0.2em] uppercase hover:bg-alpine-text hover:text-white transition-all duration-300 font-bold cursor-pointer"
            >
                Prenota Attrezzatura
                <ArrowRight class="w-4 h-4" />
            </button>
        </div>
    </div>
</section>

<!-- \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 COME FUNZIONA \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-5xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">Come Funziona</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">In 4 semplici passi</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
            <div class="fade-up-element text-center">
                <div class="w-12 h-12 rounded-full border-2 border-alpine-gold flex items-center justify-center mx-auto mb-6">
                    <span class="font-serif text-xl text-alpine-gold">1</span>
                </div>
                <h4 class="font-serif text-lg text-alpine-text mb-3">Prenota Online</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Compila il modulo con le tue preferenze e le date del soggiorno.
                </p>
            </div>
            <div class="fade-up-element text-center">
                <div class="w-12 h-12 rounded-full border-2 border-alpine-gold flex items-center justify-center mx-auto mb-6">
                    <span class="font-serif text-xl text-alpine-gold">2</span>
                </div>
                <h4 class="font-serif text-lg text-alpine-text mb-3">Conferma</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Il nostro partner ti contatter\u00e0 per confermare disponibilit\u00e0 e prezzi.
                </p>
            </div>
            <div class="fade-up-element text-center">
                <div class="w-12 h-12 rounded-full border-2 border-alpine-gold flex items-center justify-center mx-auto mb-6">
                    <span class="font-serif text-xl text-alpine-gold">3</span>
                </div>
                <h4 class="font-serif text-lg text-alpine-text mb-3">Consegna</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    L\u2019attrezzatura viene consegnata direttamente nel tuo ski box prima del tuo arrivo.
                </p>
            </div>
            <div class="fade-up-element text-center">
                <div class="w-12 h-12 rounded-full border-2 border-alpine-gold flex items-center justify-center mx-auto mb-6">
                    <span class="font-serif text-xl text-alpine-gold">4</span>
                </div>
                <h4 class="font-serif text-lg text-alpine-text mb-3">Sci!</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Prendi i tuoi sci dal box e sei in pista in meno di un minuto.
                </p>
            </div>
        </div>
    </div>
</section>

<!-- \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 CTA \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 -->
<section class="bg-[#0a0a0a] py-32 px-6">
    <div class="max-w-3xl mx-auto text-center">
        <div class="fade-up-element">
            <h2 class="font-serif text-4xl text-white mb-6">Pronto a Sciare?</h2>
            <p class="text-white/50 text-sm font-light leading-relaxed max-w-lg mx-auto mb-12">
                Prenota la tua attrezzatura adesso e goditi le vacanze senza pensieri.
                Il nostro partner si occuper\u00e0 di tutto: dalla preparazione alla consegna nel tuo ski box.
            </p>
            <button
                onclick={() => showRentalForm = true}
                class="inline-flex items-center gap-3 bg-alpine-gold text-white px-10 py-4 text-[11px] tracking-[0.2em] uppercase hover:bg-alpine-gold/90 transition-all duration-300 font-bold cursor-pointer"
            >
                Prenota Attrezzatura
                <ArrowRight class="w-4 h-4" />
            </button>
        </div>
    </div>
</section>

<!-- \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 RENTAL FORM POPUP \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 -->
{#if showRentalForm}
    <div
        class="fixed inset-0 z-50 flex items-center justify-center p-4"
        transition:fade={{ duration: 200 }}
    >
        <!-- Backdrop -->
        <button type="button" class="absolute inset-0 bg-black/70 backdrop-blur-sm cursor-default" onclick={() => showRentalForm = false} aria-label="Chiudi"></button>

        <!-- Modal -->
        <div
            class="relative bg-white w-full max-w-lg max-h-[90vh] overflow-y-auto shadow-2xl"
            transition:fly={{ y: 40, duration: 300 }}
            use:clickOutside={() => showRentalForm = false}
        >
            {#if formSubmitted}
                <!-- Success state -->
                <div class="p-16 text-center">
                    <div class="w-16 h-16 rounded-full bg-green-100 flex items-center justify-center mx-auto mb-6">
                        <PackageCheck class="w-8 h-8 text-green-600" />
                    </div>
                    <h3 class="font-serif text-2xl text-alpine-text mb-4">Richiesta Inviata!</h3>
                    <p class="text-alpine-muted text-sm font-light">
                        Il tuo client email si \u00e8 aperto con tutti i dettagli. Invia l\u2019email per completare la richiesta.
                    </p>
                </div>
            {:else}
                <!-- Header -->
                <div class="sticky top-0 bg-white border-b border-alpine-border px-8 py-6 flex items-center justify-between z-10">
                    <div>
                        <h3 class="font-serif text-2xl text-alpine-text">Prenota Attrezzatura</h3>
                        <p class="text-xs text-alpine-muted font-light mt-1">Compila il modulo e invia la richiesta al nostro partner</p>
                    </div>
                    <button onclick={() => showRentalForm = false} class="p-2 hover:bg-alpine-bg rounded transition-colors cursor-pointer">
                        <X class="w-5 h-5 text-alpine-muted" />
                    </button>
                </div>

                <!-- Form -->
                <form onsubmit={handleSubmit} class="p-8 space-y-6">
                    <!-- Personal info -->
                    <div class="space-y-4">
                        <p class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold">Dati Personali</p>

                        <div>
                            <label for="rental-name" class="block text-xs font-medium text-alpine-text mb-1.5">Nome e Cognome *</label>
                            <input
                                id="rental-name"
                                type="text"
                                required
                                bind:value={formName}
                                class="w-full border border-alpine-border px-4 py-3 text-sm font-light focus:outline-none focus:border-alpine-gold transition-colors"
                                placeholder="Mario Rossi"
                            />
                        </div>

                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                            <div>
                                <label for="rental-email" class="block text-xs font-medium text-alpine-text mb-1.5">Email *</label>
                                <input
                                    id="rental-email"
                                    type="email"
                                    required
                                    bind:value={formEmail}
                                    class="w-full border border-alpine-border px-4 py-3 text-sm font-light focus:outline-none focus:border-alpine-gold transition-colors"
                                    placeholder="mario@email.com"
                                />
                            </div>
                            <div>
                                <label for="rental-phone" class="block text-xs font-medium text-alpine-text mb-1.5">Telefono</label>
                                <input
                                    id="rental-phone"
                                    type="tel"
                                    bind:value={formPhone}
                                    class="w-full border border-alpine-border px-4 py-3 text-sm font-light focus:outline-none focus:border-alpine-gold transition-colors"
                                    placeholder="+39 333 1234567"
                                />
                            </div>
                        </div>
                    </div>

                    <!-- Dates & guests -->
                    <div class="space-y-4 pt-4 border-t border-alpine-border">
                        <p class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold">Soggiorno</p>

                        <div class="grid grid-cols-2 gap-4">
                            <div>
                                <label for="rental-arrival" class="block text-xs font-medium text-alpine-text mb-1.5">Arrivo *</label>
                                <input
                                    id="rental-arrival"
                                    type="date"
                                    required
                                    bind:value={formArrival}
                                    class="w-full border border-alpine-border px-4 py-3 text-sm font-light focus:outline-none focus:border-alpine-gold transition-colors"
                                />
                            </div>
                            <div>
                                <label for="rental-departure" class="block text-xs font-medium text-alpine-text mb-1.5">Partenza *</label>
                                <input
                                    id="rental-departure"
                                    type="date"
                                    required
                                    bind:value={formDeparture}
                                    class="w-full border border-alpine-border px-4 py-3 text-sm font-light focus:outline-none focus:border-alpine-gold transition-colors"
                                />
                            </div>
                        </div>

                        <div class="grid grid-cols-2 gap-4">
                            <div>
                                <label for="rental-adults" class="block text-xs font-medium text-alpine-text mb-1.5">Adulti *</label>
                                <select
                                    id="rental-adults"
                                    bind:value={formAdults}
                                    class="w-full border border-alpine-border px-4 py-3 text-sm font-light focus:outline-none focus:border-alpine-gold transition-colors bg-white appearance-none cursor-pointer"
                                >
                                    {#each [1,2,3,4,5,6] as n}
                                        <option value={n}>{n}</option>
                                    {/each}
                                </select>
                            </div>
                            <div>
                                <label for="rental-children" class="block text-xs font-medium text-alpine-text mb-1.5">Bambini</label>
                                <select
                                    id="rental-children"
                                    bind:value={formChildren}
                                    class="w-full border border-alpine-border px-4 py-3 text-sm font-light focus:outline-none focus:border-alpine-gold transition-colors bg-white appearance-none cursor-pointer"
                                >
                                    {#each [0,1,2,3,4] as n}
                                        <option value={n}>{n}</option>
                                    {/each}
                                </select>
                            </div>
                        </div>
                    </div>

                    <!-- Equipment -->
                    <div class="space-y-4 pt-4 border-t border-alpine-border">
                        <p class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold">Attrezzatura</p>

                        <div class="grid grid-cols-2 gap-4">
                            <div>
                                <label for="rental-equipment" class="block text-xs font-medium text-alpine-text mb-1.5">Tipo *</label>
                                <select
                                    id="rental-equipment"
                                    bind:value={formEquipment}
                                    class="w-full border border-alpine-border px-4 py-3 text-sm font-light focus:outline-none focus:border-alpine-gold transition-colors bg-white appearance-none cursor-pointer"
                                >
                                    <option value="sci">Sci alpino</option>
                                    <option value="snowboard">Snowboard</option>
                                    <option value="ciaspole">Ciaspole</option>
                                    <option value="fondo">Sci di fondo</option>
                                </select>
                            </div>
                            <div>
                                <label for="rental-level" class="block text-xs font-medium text-alpine-text mb-1.5">Livello *</label>
                                <select
                                    id="rental-level"
                                    bind:value={formLevel}
                                    class="w-full border border-alpine-border px-4 py-3 text-sm font-light focus:outline-none focus:border-alpine-gold transition-colors bg-white appearance-none cursor-pointer"
                                >
                                    <option value="principiante">Principiante</option>
                                    <option value="intermedio">Intermedio</option>
                                    <option value="esperto">Esperto</option>
                                </select>
                            </div>
                        </div>

                        <div class="grid grid-cols-2 gap-4">
                            <div>
                                <label for="rental-boot-adult" class="block text-xs font-medium text-alpine-text mb-1.5">Taglia scarponi (adulto)</label>
                                <input
                                    id="rental-boot-adult"
                                    type="text"
                                    bind:value={formBootSizeAdult}
                                    class="w-full border border-alpine-border px-4 py-3 text-sm font-light focus:outline-none focus:border-alpine-gold transition-colors"
                                    placeholder="es. 42, 43.5"
                                />
                            </div>
                            {#if formChildren > 0}
                                <div>
                                    <label for="rental-boot-child" class="block text-xs font-medium text-alpine-text mb-1.5">Taglia scarponi (bambino)</label>
                                    <input
                                        id="rental-boot-child"
                                        type="text"
                                        bind:value={formBootSizeChild}
                                        class="w-full border border-alpine-border px-4 py-3 text-sm font-light focus:outline-none focus:border-alpine-gold transition-colors"
                                        placeholder="es. 32, 35"
                                    />
                                </div>
                            {/if}
                        </div>

                        <label class="flex items-center gap-3 cursor-pointer">
                            <input type="checkbox" bind:checked={formHelmet} class="w-4 h-4 accent-alpine-gold" />
                            <span class="text-sm text-alpine-text font-light">Includi casco (consigliato)</span>
                        </label>
                    </div>

                    <!-- Notes -->
                    <div class="space-y-4 pt-4 border-t border-alpine-border">
                        <p class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold">Note Aggiuntive</p>
                        <textarea
                            bind:value={formNotes}
                            rows="3"
                            class="w-full border border-alpine-border px-4 py-3 text-sm font-light focus:outline-none focus:border-alpine-gold transition-colors resize-none"
                            placeholder="Esigenze particolari, taglie per pi\u00f9 persone, ecc."
                        ></textarea>
                    </div>

                    <!-- Submit -->
                    <div class="pt-4">
                        <button
                            type="submit"
                            class="w-full bg-alpine-text text-white py-4 text-[11px] tracking-[0.2em] uppercase font-bold hover:bg-alpine-gold transition-colors duration-300 flex items-center justify-center gap-3 cursor-pointer"
                        >
                            <Mail class="w-4 h-4" />
                            Invia Richiesta al Partner
                        </button>
                        <p class="text-[10px] text-alpine-muted font-light text-center mt-3">
                            Si aprir\u00e0 il tuo client email con tutti i dettagli gi\u00e0 compilati
                        </p>
                    </div>
                </form>
            {/if}
        </div>
    </div>
{/if}
