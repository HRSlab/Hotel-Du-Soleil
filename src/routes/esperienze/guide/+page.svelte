<script lang="ts">
    import { ShieldCheck, Mountain, Users } from 'lucide-svelte';
</script>

<svelte:head>
    <title>Guide Alpine Partner | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div class="absolute inset-0">
        <img src="https://images.unsplash.com/photo-1544450531-64d7fa39b400?q=80&w=2000&auto=format&fit=crop" class="ken-burns h-full w-full object-cover opacity-80" alt="Guide Alpine" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/40 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            Esperti della Montagna
        </span>
        <h1 class="font-serif text-5xl md:text-7xl leading-tight font-light text-white fade-up-element">
            Guide Alpine Partner
        </h1>
    </div>
</header>

<section class="bg-alpine-bg px-6 py-24">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <ShieldCheck class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            La vostra sicurezza è per noi una priorità assoluta.
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            Collaboriamo con le migliori guide alpine della Valle d'Aosta per offrirvi escursioni sicure ed emozionanti. 
            I nostri professionisti conoscono ogni anfratto di queste montagne e vi condurranno a scoprire luoghi invisibili ai più.
        </p>
    </div>
</section>

<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20">
    <div class="bg-white p-12 border border-alpine-border shadow-sm flex flex-col h-full fade-up-element">
         <Mountain class="w-8 h-8 text-alpine-gold mb-6 stroke-[1.5px]" />
         <h4 class="font-serif text-3xl text-alpine-text mb-6">Alpinismo & Freeride</h4>
         <p class="text-sm text-alpine-muted font-light leading-relaxed mb-8 grow">Prenotate un’uscita di alpinismo d’alta quota o fatevi accompagnare in sicurezza fuori dalle piste battute per sperimentare il vero freeride sulla neve fresca.</p>
         <div class="pt-6 border-t border-alpine-border">
              <span class="text-[10px] uppercase tracking-widest font-bold text-alpine-muted italic">Servizio su prenotazione</span>
         </div>
    </div>
    <div class="bg-white p-12 border border-alpine-border shadow-sm flex flex-col h-full fade-up-element">
         <Users class="w-8 h-8 text-alpine-gold mb-6 stroke-[1.5px]" />
         <h4 class="font-serif text-3xl text-alpine-text mb-6">Escursioni di Gruppo</h4>
         <p class="text-sm text-alpine-muted font-light leading-relaxed mb-8 grow">Unitevi alle nostre escursioni guidate giornaliere per scoprire la fauna e la flora locali in compagnia di altri ospiti dell'hotel.</p>
         <div class="pt-6 border-t border-alpine-border">
              <span class="text-[10px] uppercase tracking-widest font-bold text-alpine-muted italic">Incluso per i clienti Premium</span>
         </div>
    </div>
</section>
