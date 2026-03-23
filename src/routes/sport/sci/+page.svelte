<script lang="ts">
    import { Snowflake, MapPin, Wind, Thermometer } from 'lucide-svelte';
</script>

<svelte:head>
    <title>Sci & Snowboard | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div class="absolute inset-0">
        <img src="https://images.unsplash.com/photo-1551698618-1fed5d97530d?q=80&w=2000&auto=format&fit=crop" class="ken-burns h-full w-full object-cover opacity-80" alt="Sci & Snowboard a Torgnon" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/40 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            Ski-in Ski-out
        </span>
        <h1 class="font-serif text-5xl md:text-7xl leading-tight font-light text-white fade-up-element">
            Sci & Snowboard
        </h1>
    </div>
</header>

<section class="bg-alpine-bg px-6 py-24">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <Snowflake class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            Siamo a soli 50 metri dagli impianti del Comprensorio di Torgnon.
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            Il comprensorio di Torgnon offre piste soleggiate e divertenti per ogni livello di abilità, circondate da un panorama mozzafiato che spazia dal Cervino al Monte Rosa.
        </p>
    </div>
</section>

<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element overflow-hidden bg-white/5 border border-alpine-border p-12">
        <h4 class="font-serif text-2xl text-alpine-text mb-6">Dettagli Comprensorio</h4>
        <div class="space-y-8">
            <div class="flex items-center gap-4">
                <MapPin class="w-6 h-6 text-alpine-gold" />
                <div>
                     <p class="text-[10px] uppercase font-bold tracking-widest text-alpine-muted mb-1">Chilometri di Piste</p>
                     <h5 class="text-lg font-serif italic text-alpine-text">25 km di puro divertimento</h5>
                </div>
            </div>
            <div class="flex items-center gap-4 border-t border-alpine-border pt-8">
                <Wind class="w-6 h-6 text-alpine-gold" />
                <div>
                     <p class="text-[10px] uppercase font-bold tracking-widest text-alpine-muted mb-1">Quota Massima</p>
                     <h5 class="text-lg font-serif italic text-alpine-text">2.250 metri d’altitudine</h5>
                </div>
            </div>
            <div class="flex items-center gap-4 border-t border-alpine-border pt-8">
                <Thermometer class="w-6 h-6 text-alpine-gold" />
                <div>
                     <p class="text-[10px] uppercase font-bold tracking-widest text-alpine-muted mb-1">Esposizione</p>
                     <h5 class="text-lg font-serif italic text-alpine-text">Sud — Sole tutto il giorno</h5>
                </div>
            </div>
        </div>
    </div>
    <div class="fade-up-element">
        <h4 class="font-serif text-4xl text-alpine-text mb-6">Winter Park Torgnon</h4>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            Uno dei parchi gioco sulla neve più grandi d'Europa, situato proprio all'arrivo della telecabina. 
            Perfetto per i bambini che iniziano a sciare o per chi cerca divertimento extra tra ciambelle e bob.
        </p>
        <button class="flex items-center gap-3 text-xs tracking-widest uppercase font-bold text-alpine-gold">
            Acquista Skipass Online <Wind class="w-4 h-4 ml-2" />
        </button>
    </div>
</section>
