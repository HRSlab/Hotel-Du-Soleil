<script lang="ts">
  import { Wine } from 'lucide-svelte';
</script>

<svelte:head>
  <title>La Cantina | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
  <img src="https://images.unsplash.com/photo-1506377247377-2a5b3b417ebb?q=80&w=2000&auto=format&fit=crop" class="ken-burns h-full w-full object-cover opacity-70" alt="Wine Cellar" />
  <div class="absolute inset-0 bg-gradient-to-b from-black/80 via-black/40 to-alpine-bg"></div>
  <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
    <h1 class="font-serif text-5xl md:text-7xl leading-tight font-light text-white fade-up-element">La Cantina</h1>
  </div>
</header>

<section class="bg-alpine-bg px-6 py-32">
  <div class="fade-up-element mx-auto max-w-3xl text-center">
    <Wine class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
    <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
      Viticoltura eroica d'alta quota.
    </h3>
    <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12">
      Selezioniamo con cura e passione le migliori e più esclusive etichette valdostane per valorizzare una terra complessa e fiera. 
      I nostri maîtres vi guideranno in un viaggio enologico unico, pensato per esaltare ogni sfumatura culinaria.
    </p>
  </div>
</section>
