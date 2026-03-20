<script lang="ts">
  import { t } from '$lib/i18n';
</script>

<svelte:head>
  <title>Area Benessere | Hotel du Soleil</title>
</svelte:head>

<div class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
  <div class="absolute inset-0">
    <img 
      src="https://images.unsplash.com/photo-1544161515-4ab6ce6db874?q=80&w=1000&auto=format&fit=crop" 
      alt="Wellness Area" 
      class="w-full h-full object-cover ken-burns opacity-70"
    >
    <div class="absolute inset-0 bg-gradient-to-b from-black/40 via-transparent to-alpine-bg"></div>
  </div>
  <div class="absolute inset-0 flex flex-col items-center justify-center px-6 text-center z-10 pt-20">
    <h1 class="font-serif text-5xl md:text-7xl text-white font-light tracking-tight">Area Benessere</h1>
  </div>
</div>

<div class="py-24 px-6 bg-alpine-bg min-h-screen">
  <div class="max-w-4xl mx-auto">
    <div class="fade-up-element text-center mb-16">
      <p class="text-xl md:text-2xl text-alpine-text font-light leading-relaxed">
        Il lusso del silenzio. Ritrova il tuo equilibrio con i nostri percorsi benessere e lasciati coccolare dalle mani esperte dei nostri terapisti a 1.500 metri di quota.
      </p>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-2 gap-12 fade-up-element mt-20">
      <div class="bg-white p-12 border border-alpine-border shadow-sm">
        <h3 class="font-serif text-3xl mb-6 text-alpine-text">SPA in Quota</h3>
        <p class="text-alpine-muted font-light leading-relaxed">
          Sauna finlandese, bagno turco e una zona relax con vista panoramica sulle vette della Valle d'Aosta.
        </p>
      </div>
      <div class="bg-white p-12 border border-alpine-border shadow-sm">
        <h3 class="font-serif text-3xl mb-6 text-alpine-text">Trattamenti</h3>
        <p class="text-alpine-muted font-light leading-relaxed">
          Massaggi sportivi post-sci e trattamenti personalizzati con profumi essenziali alpini.
        </p>
      </div>
    </div>
  </div>
</div>
