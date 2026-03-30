<script lang="ts">
    import { Mountain, Map, Sun, Wind } from 'lucide-svelte';
</script>

<svelte:head>
    <title>Trekking in Alpeggio | Chalet du Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div class="absolute inset-0">
        <img src="https://images.unsplash.com/photo-1551632811-561732d1e306?q=80&w=2000&auto=format&fit=crop" class="ken-burns h-full w-full object-cover opacity-80" alt="Trekking a Torgnon" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/40 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            Tra Cielo e Terra
        </span>
        <h1 class="font-serif text-5xl md:text-7xl leading-tight font-light text-white fade-up-element">
            Trekking
        </h1>
    </div>
</header>

<section class="bg-alpine-bg px-6 py-24">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <Mountain class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            Il respiro profondo dei sentieri di montagna.
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            Torgnon offre un'incredibile varietà di percorsi escursionistici, dalle rilassanti passeggiate nei boschi di conifere fino alle ascese più sfidanti verso le creste che dominano la valle.
        </p>
    </div>
</section>

<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-8">
    <div class="bg-white p-10 border border-alpine-border shadow-sm text-center fade-up-element">
        <Sun class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
        <h4 class="font-serif text-2xl mb-4 italic">Percorsi Famiglia</h4>
        <p class="text-[10px] uppercase font-bold tracking-widest text-alpine-muted mb-4">Facile — 1-2h</p>
        <p class="text-xs text-alpine-muted font-light leading-relaxed">Itinerari con poco dislivello, ideali per bambini e per chi vuole godersi la natura con calma.</p>
    </div>
    <div class="bg-white p-10 border border-alpine-border shadow-sm text-center fade-up-element">
        <Map class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
        <h4 class="font-serif text-2xl mb-4 italic">Sentiero dell'Acqua</h4>
        <p class="text-[10px] uppercase font-bold tracking-widest text-alpine-muted mb-4">Medio — 3h</p>
        <p class="text-xs text-alpine-muted font-light leading-relaxed">Un percorso che segue gli antichi canali di irrigazione (ru), costeggiando ruscelli e cascate immerse nel verde.</p>
    </div>
    <div class="bg-white p-10 border border-alpine-border shadow-sm text-center fade-up-element">
        <Wind class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
        <h4 class="font-serif text-2xl mb-4 italic">Alta Quota Mongnod</h4>
        <p class="text-[10px] uppercase font-bold tracking-widest text-alpine-muted mb-4">Esperti — 5h+</p>
        <p class="text-xs text-alpine-muted font-light leading-relaxed">Per chi cerca la vetta. Dislivelli significativi e panorami immensi che ripagano ogni fatica.</p>
    </div>
</section>
