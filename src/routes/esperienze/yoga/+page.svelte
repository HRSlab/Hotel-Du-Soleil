<script lang="ts">
    import { Flower, Wind, Sparkles, Sun } from 'lucide-svelte';
</script>

<svelte:head>
    <title>Yoga in Quota | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div class="absolute inset-0">
        <img src="https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?q=80&w=2000&auto=format&fit=crop" class="ken-burns h-full w-full object-cover opacity-80" alt="Yoga in Quota" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/40 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            Equilibrio Interiore
        </span>
        <h1 class="font-serif text-5xl md:text-7xl leading-tight font-light text-white fade-up-element">
            Yoga in Quota
        </h1>
    </div>
</header>

<section class="bg-alpine-bg px-6 py-24">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <Flower class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            Il respiro si fonde con l'aria sottile dei 1500 metri.
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            Le nostre sessioni di yoga si svolgono all'alba o al tramonto nella magnifica cornice delle Alpi valdostane. 
            Sentite l'energia della terra e la freschezza dell'aria pura mentre ritrovate il vostro equilibrio interiore.
        </p>
    </div>
</section>

<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
    <div class="bg-white p-10 border border-alpine-border shadow-sm fade-up-element">
         <Sun class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
         <h4 class="font-serif text-2xl mb-4 italic">Saluto al Sole</h4>
         <p class="text-xs text-alpine-muted font-light leading-relaxed">Immergetevi nella luce del mattino per risvegliare dolcemente i sensi.</p>
    </div>
    <div class="bg-white p-10 border border-alpine-border shadow-sm fade-up-element">
         <Wind class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
         <h4 class="font-serif text-2xl mb-4 italic">Pranayama Alpino</h4>
         <p class="text-xs text-alpine-muted font-light leading-relaxed">Tecniche di respirazione per rinvigorire i polmoni con l'aria d'alta quota.</p>
    </div>
    <div class="bg-white p-10 border border-alpine-border shadow-sm fade-up-element">
         <Sparkles class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
         <h4 class="font-serif text-2xl mb-4 italic">Meditazione Guidata</h4>
         <p class="text-xs text-alpine-muted font-light leading-relaxed">Un'immersione nel silenzio profondo della montagna.</p>
    </div>
</section>
