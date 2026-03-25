<script lang="ts">
    import { Snowflake, ShieldCheck, Sparkles } from 'lucide-svelte';
</script>

<svelte:head>
    <title>Sci & Snowboard | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div class="absolute inset-0">
        <img src="/imgs/Torgnon_View.jpeg" class="ken-burns h-full w-full object-cover opacity-80" alt="Sci a Torgnon" />
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
        <Snowflake class="w-10 h-10 text-alpine-gold mx-auto mb-10" strokeWidth={1.5} />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            Siamo a soli 50 metri dagli impianti del Comprensorio di Torgnon.
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            Il comprensorio di Torgnon offre piste soleggiate e divertenti per ogni livello di abilità, circondate da un panorama mozzafiato che spazia dal Cervino al Monte Rosa.
        </p>
    </div>
</section>

<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto space-y-12">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
         <div class="fade-up-element">
            <h4 class="font-serif text-4xl text-alpine-text mb-6 italic">Piste per Tutti i Livelli</h4>
            <div class="space-y-10">
                 <div class="flex items-start gap-4 border-b border-alpine-border pb-6">
                    <div class="w-2 h-2 rounded-full bg-alpine-gold mt-2 shrink-0"></div>
                    <div>
                         <h5 class="text-lg font-serif italic text-alpine-text mb-2">Piste Soleggiate</h5>
                         <p class="text-xs text-alpine-muted leading-relaxed font-light">Ampie piste perfettamente innevate, ideali per principianti e famiglie.</p>
                    </div>
                 </div>
                 <div class="flex items-start gap-4 border-b border-alpine-border pb-6">
                    <div class="w-2 h-2 rounded-full bg-alpine-gold mt-2 shrink-0"></div>
                    <div>
                         <h5 class="text-lg font-serif italic text-alpine-text mb-2">Fuoripista Guidato</h5>
                         <p class="text-xs text-alpine-muted leading-relaxed font-light">Esplora la neve fresca con le nostre guide certificate per un'esperienza sicura e indimenticabile.</p>
                    </div>
                 </div>
                 <div class="flex items-start gap-4 border-b border-alpine-border pb-6">
                    <div class="w-2 h-2 rounded-full bg-alpine-gold mt-2 shrink-0"></div>
                    <div>
                         <h5 class="text-lg font-serif italic text-alpine-text mb-2">Snow Park</h5>
                         <p class="text-xs text-alpine-muted leading-relaxed font-light">Modulo per snowboard e freestyle con salti, rails e halfpipe.</p>
                    </div>
                 </div>
            </div>
         </div>
         <div class="fade-up-element bg-white p-12 border border-alpine-border">
            <div class="flex items-center gap-4 mb-6"><ShieldCheck class="w-6 h-6 text-alpine-gold" /><h4 class="text-[12px] uppercase font-bold tracking-[0.2em] text-alpine-text">Servizi Sci Club</h4></div>
            <ul class="space-y-4 text-sm font-light text-alpine-muted">
                <li class="flex items-center gap-3"><Sparkles class="w-4 h-4 text-alpine-gold/50 shrink-0" /> Deposito sci sicuro e videosorvegliato</li>
                <li class="flex items-center gap-3"><Sparkles class="w-4 h-4 text-alpine-gold/50 shrink-0" /> Zona riscaldamento scarponi</li>
                <li class="flex items-center gap-3"><Sparkles class="w-4 h-4 text-alpine-gold/50 shrink-0" /> Servizio di preparazione sci</li>
                <li class="flex items-center gap-3"><Sparkles class="w-4 h-4 text-alpine-gold/50 shrink-0" /> Scuola sci convenzionata</li>
                <li class="flex items-center gap-3"><Sparkles class="w-4 h-4 text-alpine-gold/50 shrink-0" /> Noleggio attrezzatura in hotel</li>
            </ul>
         </div>
    </div>
</section>