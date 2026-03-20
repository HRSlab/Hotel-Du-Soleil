<script lang="ts">
  import { t } from '$lib/i18n';
</script>

<svelte:head>
  <title>Sport & Outdoor | Hotel du Soleil</title>
</svelte:head>

<div class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
  <div class="absolute inset-0">
    <img 
      src="https://images.unsplash.com/photo-1518602164578-cd0074062767?q=80&w=1000&auto=format&fit=crop" 
      alt="Alpine Sport" 
      class="w-full h-full object-cover ken-burns opacity-70"
    >
    <div class="absolute inset-0 bg-gradient-to-b from-black/40 via-transparent to-alpine-bg"></div>
  </div>
  <div class="absolute inset-0 flex flex-col items-center justify-center px-6 text-center z-10 pt-20">
    <h1 class="font-serif text-5xl md:text-7xl text-white font-light tracking-tight">Sport & Outdoor</h1>
  </div>
</div>

<div class="py-24 px-6 bg-alpine-bg min-h-screen">
  <div class="max-w-4xl mx-auto">
    <div class="fade-up-element text-center mb-16">
      <p class="text-xl md:text-2xl text-alpine-text font-light leading-relaxed">
        L'adrenalina inizia a 20 metri dalla nostra porta. Accesso diretto agli impianti in inverno e a infiniti sentieri panoramici in estate.
      </p>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-2 gap-12 fade-up-element mt-20">
      <div class="bg-white p-12 border border-alpine-border shadow-sm">
        <h3 class="font-serif text-3xl mb-6 text-alpine-text">Ski-in / Ski-out</h3>
        <p class="text-alpine-muted font-light leading-relaxed">
          Siamo situati direttamente sulle piste di Torgnon. Niente code, niente navette: solo neve e divertimento.
        </p>
      </div>
      <div class="bg-white p-12 border border-alpine-border shadow-sm">
        <h3 class="font-serif text-3xl mb-6 text-alpine-text">Mountain Bike</h3>
        <p class="text-alpine-muted font-light leading-relaxed">
          Noleggio E-bike in loco e percorsi guidati per ogni livello di esperienza, dalle famiglie ai biker esperti.
        </p>
      </div>
    </div>
  </div>
</div>
