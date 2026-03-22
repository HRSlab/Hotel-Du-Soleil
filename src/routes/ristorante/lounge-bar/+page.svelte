<script lang="ts">
  import { Coffee } from 'lucide-svelte';
</script>

<svelte:head>
  <title>Lounge Bar & Camino | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
  <img src="https://images.unsplash.com/photo-1542460225-8356d2528eed?q=80&w=2000&auto=format&fit=crop" class="ken-burns h-full w-full object-cover opacity-70" alt="Lounge Fireplace" />
  <div class="absolute inset-0 bg-gradient-to-b from-black/80 via-black/40 to-alpine-bg"></div>
  <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
    <h1 class="font-serif text-5xl md:text-7xl leading-tight font-light text-white fade-up-element">Lounge Bar & Camino</h1>
  </div>
</header>

<section class="bg-alpine-bg px-6 py-32">
  <div class="fade-up-element mx-auto max-w-3xl text-center">
    <Coffee class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
    <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
      Ritrova il tepore.
    </h3>
    <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12">
      Il salotto caldo dell'hotel è il luogo ideale dove fermare il tempo. 
      Lasciatevi avvolgere dal crepitio del fuoco con una cioccolata calda alpina o un distillato artigianale alle erbe (Genepì, Artemisia) dopo una giornata d'inverno trascorsa sulle piste innevate.
    </p>
  </div>
</section>
