<script lang="ts">
  import { t } from '$lib/i18n';
</script>

<svelte:head>
  <title>Esperienze Alpine | Hotel du Soleil</title>
</svelte:head>

<div class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
  <div class="absolute inset-0">
    <img 
      src="https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=1000&auto=format&fit=crop" 
      alt="Alpine Experiences" 
      class="w-full h-full object-cover ken-burns opacity-70"
    >
    <div class="absolute inset-0 bg-gradient-to-b from-black/40 via-transparent to-alpine-bg"></div>
  </div>
  <div class="absolute inset-0 flex flex-col items-center justify-center px-6 text-center z-10 pt-20">
    <h1 class="font-serif text-5xl md:text-7xl text-white font-light tracking-tight">Esperienze Alpine</h1>
  </div>
</div>

<div class="py-24 px-6 bg-alpine-bg min-h-screen">
  <div class="max-w-4xl mx-auto">
    <div class="fade-up-element text-center mb-16">
      <p class="text-xl md:text-2xl text-alpine-text font-light leading-relaxed">
        Non una semplice vacanza, ma una collezione di ricordi. Esplora il territorio attraverso attività autentiche, in totale sintonia con i ritmi della montagna valdostana.
      </p>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-2 gap-12 fade-up-element mt-20">
      <div class="bg-white p-12 border border-alpine-border shadow-sm">
        <h3 class="font-serif text-3xl mb-6 text-alpine-text">Sci & Snowboard</h3>
        <p class="text-alpine-muted font-light leading-relaxed">
          Accesso diretto agli impianti (ski-in) per vivere al meglio il comprensorio Cervino Ski Paradise.
        </p>
      </div>
      <div class="bg-white p-12 border border-alpine-border shadow-sm">
        <h3 class="font-serif text-3xl mb-6 text-alpine-text">Trekking & Outdoor</h3>
        <p class="text-alpine-muted font-light leading-relaxed">
          Sentieri panoramici che partono dalla nostra porta, per scoprire alpeggi e laghi alpini incontaminati.
        </p>
      </div>
    </div>
  </div>
</div>
