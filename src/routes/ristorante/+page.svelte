<script lang="ts">
  import { t } from '$lib/i18n';
  import { Coffee, UtensilsCrossed, Wine } from 'lucide-svelte';
</script>

<svelte:head>
  <title>Ristorante | Hotel du Soleil Torgnon</title>
</svelte:head>

<!-- HERO SECTION -->
<header class="relative h-screen w-full overflow-hidden bg-[#1a1a1a]">
  <div class="absolute inset-0">
    <img
      src="https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?q=80&w=2000&auto=format&fit=crop"
      alt="Ristorante Hotel du Soleil"
      class="ken-burns h-full w-full object-cover opacity-80"
    />
    <div class="absolute inset-0 bg-black/40"></div>
    <div class="absolute inset-0 bg-gradient-to-b from-black/80 via-black/40 to-alpine-bg"></div>
  </div>

  <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-32 text-center">
    <div class="fade-up-element">
      <span class="mb-6 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs">
        Sapori Autentici
      </span>
      <h1 class="mb-10 font-serif text-5xl leading-tight font-light text-white md:text-7xl">
        Il Ristorante
      </h1>
    </div>
  </div>
</header>

<!-- FILOSOFIA -->
<section class="bg-alpine-bg px-6 py-32">
  <div class="fade-up-element mx-auto max-w-3xl text-center">
    <div class="deco-line mb-12"></div>
    <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-5xl">
      La tradizione valdostana incontra la freschezza degli ingredienti di montagna.
    </h3>
    <p class="mx-auto max-w-xl text-sm leading-relaxed font-light text-alpine-muted md:text-base">
      La nostra cucina è un omaggio sincero al territorio. Privilegiamo le materie prime a chilometro zero, selezionando personalmente i migliori formaggi degli alpeggi locali, le carni del territorio e le erbe spontanee per offrirvi un'esperienza gastronomica genuina e indimenticabile.
    </p>
  </div>
</section>

<!-- HIGHLIGHTS / SECTIONS -->
<section class="mx-auto max-w-7xl px-6 py-24 border-t border-alpine-border">
  <div class="grid grid-cols-1 md:grid-cols-3 gap-16">
    
    <!-- Colazione -->
    <div class="fade-up-element group text-center flex flex-col items-center">
      <div class="w-24 h-24 rounded-full border border-alpine-border flex items-center justify-center mb-8 relative overflow-hidden bg-white">
        <Coffee class="w-8 h-8 text-alpine-gold z-10 group-hover:scale-110 transition-transform duration-500" strokeWidth="1.5" />
      </div>
      <h4 class="font-serif text-2xl text-alpine-text mb-4">Il Risveglio</h4>
      <p class="text-sm font-light text-alpine-muted leading-relaxed">
        Il buongiorno inizia con il profumo del burro di montagna e delle torte fatte in casa. Il nostro buffet offre un'ampia selezione di dolce e salato: Fontina DOP, salumi tipici, yogurt locali, cereali e confetture artigianali.
      </p>
    </div>

    <!-- Cena -->
    <div class="fade-up-element group text-center flex flex-col items-center mt-12 md:mt-0">
      <div class="w-24 h-24 rounded-full border border-alpine-border flex items-center justify-center mb-8 relative overflow-hidden bg-white">
        <UtensilsCrossed class="w-8 h-8 text-alpine-gold z-10 group-hover:scale-110 transition-transform duration-500" strokeWidth="1.5" />
      </div>
      <h4 class="font-serif text-2xl text-alpine-text mb-4">La Cena</h4>
      <p class="text-sm font-light text-alpine-muted leading-relaxed">
        Ogni sera il nostro chef propone un menù curato che spazia dalle ricette classiche come la Valpellinentze o la polenta concia, a piatti internazionali, sempre accompagnati da un ricco buffet di verdure e sfiziosità.
      </p>
    </div>

    <!-- Cantina -->
    <div class="fade-up-element group text-center flex flex-col items-center mt-12 md:mt-0">
      <div class="w-24 h-24 rounded-full border border-alpine-border flex items-center justify-center mb-8 relative overflow-hidden bg-white">
        <Wine class="w-8 h-8 text-alpine-gold z-10 group-hover:scale-110 transition-transform duration-500" strokeWidth="1.5" />
      </div>
      <h4 class="font-serif text-2xl text-alpine-text mb-4">La Cantina</h4>
      <p class="text-sm font-light text-alpine-muted leading-relaxed">
        Una selezione attenta delle migliori etichette valdostane per esaltare ogni piatto. I nostri maîtres saranno felici di consigliarvi gli abbinamenti perfetti per esplorare l'eccellenza vitivinicola eroica della nostra regione.
      </p>
    </div>

  </div>
</section>

<!-- IMAGE GRID -->
<section class="bg-white py-24">
  <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-2 gap-8">
    <div class="aspect-[4/5] overflow-hidden group">
      <img src="https://images.unsplash.com/photo-1559339352-11d035aa65de?q=80&w=1000&auto=format&fit=crop" alt="Cucina Alpina" class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-105" />
    </div>
    <div class="flex flex-col gap-8">
      <div class="aspect-video overflow-hidden group">
        <img src="https://images.unsplash.com/photo-1505935428862-770b6f24f629?q=80&w=1000&auto=format&fit=crop" alt="Vini Valdostani" class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-105" />
      </div>
      <div class="bg-alpine-bg flex-1 p-12 flex flex-col justify-center items-start border border-alpine-border relative overflow-hidden">
        <span class="text-[10px] font-bold tracking-[0.2em] text-alpine-muted uppercase mb-4 block">Dietro le Quinte</span>
        <h4 class="font-serif text-3xl text-alpine-text mb-6 z-10 relative">Prodotti a KM Zero</h4>
        <p class="text-sm font-light text-alpine-muted leading-relaxed z-10 relative">La nostra Fontina arriva direttamente dagli alpeggi circostanti, e molte verdure dal nostro orto di famiglia. Una scelta di qualità e sostenibilità.</p>
        <div class="absolute -right-12 -bottom-12 opacity-5 pointer-events-none">
          <UtensilsCrossed class="w-64 h-64 text-alpine-text" />
        </div>
      </div>
    </div>
  </div>
</section>
