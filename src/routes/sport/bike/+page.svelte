<script lang="ts">
    import { Bike, ShieldCheck, Sparkles } from 'lucide-svelte';
</script>

<svelte:head>
    <title>Mountain Bike & E-Bike | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div class="absolute inset-0">
        <img src="https://images.unsplash.com/photo-1544191714-3d71bc294943?q=80&w=2000&auto=format&fit=crop" class="ken-burns h-full w-full object-cover opacity-80" alt="Mountain Bike a Torgnon" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/40 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            Pedalata nel Cuore delle Alpi
        </span>
        <h1 class="font-serif text-5xl md:text-7xl leading-tight font-light text-white fade-up-element">
            MTB & E-Bike
        </h1>
    </div>
</header>

<section class="bg-alpine-bg px-6 py-24">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <Bike class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            Esplora chilometri di sentieri panoramici.
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            Dai tracciati più impegnativi ai percorsi turistici adatti a tutta la famiglia, Torgnon è un paradiso per i bikers. 
            E con le moderne E-Bike, la montagna diventa accessibile a chiunque desideri godersi la natura senza eccessivo sforzo.
        </p>
    </div>
</section>

<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto space-y-12">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
         <div class="fade-up-element">
            <h4 class="font-serif text-4xl text-alpine-text mb-6 italic">Percorsi Iconici</h4>
            <div class="space-y-10">
                 <div class="flex items-start gap-4 border-b border-alpine-border pb-6">
                    <div class="w-2 h-2 rounded-full bg-alpine-gold mt-2 shrink-0"></div>
                    <div>
                         <h5 class="text-lg font-serif italic text-alpine-text mb-2">Tour del Monte Zerbion</h5>
                         <p class="text-xs text-alpine-muted leading-relaxed font-light">Un percorso panoramico che offre una vista a 360° sulla valle centrale e il Cervino.</p>
                    </div>
                 </div>
                 <div class="flex items-start gap-4 border-b border-alpine-border pb-6">
                    <div class="w-2 h-2 rounded-full bg-alpine-gold mt-2 shrink-0"></div>
                    <div>
                         <h5 class="text-lg font-serif italic text-alpine-text mb-2">Anello degli Alpeggi</h5>
                         <p class="text-xs text-alpine-muted leading-relaxed font-light">Perfetto per E-Bike, tocca diverse malghe dove è possibile degustare la Fontina DOP.</p>
                    </div>
                 </div>
            </div>
         </div>
         <div class="fade-up-element bg-white p-12 border border-alpine-border">
            <div class="flex items-center gap-4 mb-6"><ShieldCheck class="w-6 h-6 text-alpine-gold" /><h4 class="text-[12px] uppercase font-bold tracking-[0.2em] text-alpine-text">Servizi Bike Friendly</h4></div>
            <ul class="space-y-4 text-sm font-light text-alpine-muted">
                <li class="flex items-center gap-3"><Sparkles class="w-4 h-4 text-alpine-gold/50 shrink-0" /> Deposito Bici sicuro e videosorvegliato</li>
                <li class="flex items-center gap-3"><Sparkles class="w-4 h-4 text-alpine-gold/50 shrink-0" /> Officina per piccole manutenzioni</li>
                <li class="flex items-center gap-3"><Sparkles class="w-4 h-4 text-alpine-gold/50 shrink-0" /> Zona lavaggio bici</li>
                <li class="flex items-center gap-3"><Sparkles class="w-4 h-4 text-alpine-gold/50 shrink-0" /> Collaborazione con guide certificate</li>
            </ul>
         </div>
    </div>
</section>
