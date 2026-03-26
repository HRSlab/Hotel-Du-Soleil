<script lang="ts">
  import { Sparkles, UtensilsCrossed } from 'lucide-svelte';
</script>

<svelte:head>
  <title>Menù Degustazione | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[50vh] w-full overflow-hidden bg-[#1a1a1a]">
  <img src="/imgs/deer-dish-hero.webp" class="ken-burns h-full w-full object-cover opacity-60" alt="Cucina Alpina" />
  <div class="absolute inset-0 bg-linear-to-b from-black/80 to-alpine-bg"></div>
  <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-16 text-center">
    <span class="mb-4 block text-[10px] font-bold tracking-[0.4em] text-white/80 uppercase fade-up-element">Menù Degustazione</span>
    <h1 class="font-serif text-5xl md:text-7xl leading-tight font-light text-white fade-up-element">Alchimia Alpina</h1>
  </div>
</header>

<main class="min-h-screen pb-32 bg-alpine-bg">
  <div class="max-w-4xl mx-auto px-6 text-center fade-up-element pt-12">
    <Sparkles class="w-8 h-8 text-alpine-gold mx-auto mb-8" />
    <p class="font-serif text-2xl text-alpine-text italic mb-6">Un viaggio tra vette, boschi e torrenti in 7 atti.</p>
    <div class="deco-line mb-16 mx-auto"></div>
    
    <div class="space-y-16 text-left border-t border-alpine-border pt-16">
      
      <!-- Act 1 -->
      <div class="text-center group">
        <span class="text-[10px] font-bold tracking-[0.2em] text-alpine-gold uppercase block mb-3">Atto I</span>
        <h3 class="font-serif text-2xl text-alpine-text mb-2">Amuse-bouche: Aria di Fontina e Patata Croccante</h3>
        <p class="font-light text-xs uppercase tracking-widest text-alpine-muted mb-6">L'essenza del territorio in un soffio.</p>
        <p class="text-sm font-light text-alpine-muted leading-relaxed max-w-2xl mx-auto">
          Una nuvola impalpabile di Fontina DOP d'alpeggio, ottenuta tramite lecitina e sferificazione, adagiata su una cialda sottilissima di patata di Torgnon fritta in olio di vinaccioli. Un contrasto immediato tra l'evanescenza dell'aria e la croccantezza della terra.
        </p>
      </div>

      <!-- Act 2 -->
      <div class="text-center group border-t border-alpine-border/30 pt-16">
        <span class="text-[10px] font-bold tracking-[0.2em] text-alpine-gold uppercase block mb-3">Atto II</span>
        <h3 class="font-serif text-2xl text-alpine-text mb-2">Antipasto: Trota Alpina Marinata</h3>
        <p class="font-light text-xs uppercase tracking-widest text-alpine-muted mb-6">Freschezza dai torrenti glaciali.</p>
        <p class="text-sm font-light text-alpine-muted leading-relaxed max-w-2xl mx-auto">
          Filetto di trota salmonata marinato a secco con sale bilanciato e scorza di pino. Servito con una vellutata fredda di porri dolci di Cervere e brunoise di mela verde della Valle, per un'esplosione di acidità che pulisce il palato.
        </p>
      </div>

      <!-- Act 3 -->
      <div class="text-center group border-t border-alpine-border/30 pt-16">
        <span class="text-[10px] font-bold tracking-[0.2em] text-alpine-gold uppercase block mb-3">Atto III</span>
        <h3 class="font-serif text-2xl text-alpine-text mb-2">Primo: Raviolo Aperto di Patate e Burro Nocciola</h3>
        <p class="font-light text-xs uppercase tracking-widest text-alpine-muted mb-6">La decostruzione della memoria.</p>
        <p class="text-sm font-light text-alpine-muted leading-relaxed max-w-2xl mx-auto">
          Un velo di pasta all'uovo trasparente che ricopre una spuma leggera di patate Kennebec. Il piatto è ultimato al tavolo con un "filo d'oro" di burro nocciola infuso alla salvia e una grattugiata di tartufo nero estivo o polvere di funghi porcini.
        </p>
      </div>

      <!-- Act 4 -->
      <div class="text-center group border-t border-alpine-border/30 pt-16 relative">
        <UtensilsCrossed class="w-12 h-12 text-alpine-border/50 absolute left-1/2 -top-6 -translate-x-1/2 bg-alpine-bg px-2" />
        <span class="text-[10px] font-bold tracking-[0.2em] text-alpine-gold uppercase block mb-3 mt-4">Atto IV</span>
        <h3 class="font-serif text-3xl text-alpine-text mb-2">Piatto Firma: Torgnolette Contemporanea</h3>
        <p class="font-light text-xs uppercase tracking-widest text-alpine-muted mb-6">Il nostro omaggio al villaggio.</p>
        <p class="text-sm text-alpine-text font-medium leading-relaxed max-w-2xl mx-auto">
          La classica Torgnolette (patate, porri e fontina) viene reinventata: diverse consistenze di patata (fondente, in spuma e soffiata) si fondono con un cuore di fontina fluida e una riduzione di porri brasati al burro chiarificato. Un cuore antico, una forma moderna.
        </p>
      </div>

      <!-- Act 5 -->
      <div class="text-center group border-t border-alpine-border/30 pt-16">
        <span class="text-[10px] font-bold tracking-[0.2em] text-alpine-gold uppercase block mb-3">Atto V</span>
        <h3 class="font-serif text-2xl text-alpine-text mb-2">Secondo: Filetto di Cervo con Riduzione</h3>
        <p class="font-light text-xs uppercase tracking-widest text-alpine-muted mb-6">Il Re del Sottobosco.</p>
        <p class="text-sm font-light text-alpine-muted leading-relaxed max-w-2xl mx-auto">
          Filetto scottato al Cirmolo, mirtilli latto-fermentati e seta di patata affumicata. La nostra opera d'arte stellata, servita sotto cloche di fumo con una riduzione di vino rosso.
        </p>
      </div>

      <!-- Act 6 -->
      <div class="text-center group border-t border-alpine-border/30 pt-16">
        <span class="text-[10px] font-bold tracking-[0.2em] text-alpine-gold uppercase block mb-3">Atto VI</span>
        <h3 class="font-serif text-2xl text-alpine-text mb-2">Pre-Dessert: Granita alle Erbe Alpine</h3>
        <p class="font-light text-xs uppercase tracking-widest text-alpine-muted mb-6">Il respiro dei ghiacciai.</p>
        <p class="text-sm font-light text-alpine-muted leading-relaxed max-w-2xl mx-auto">
          Un intermezzo balsamico a base di timo serpillo, menta piperita e limoni di Sorrento, per resettare i sensi e prepararsi alla dolcezza finale.
        </p>
      </div>

      <!-- Act 7 -->
      <div class="text-center group border-t border-alpine-border/30 pt-16">
        <span class="text-[10px] font-bold tracking-[0.2em] text-alpine-gold uppercase block mb-3">Atto VII</span>
        <h3 class="font-serif text-2xl text-alpine-text mb-2">Dessert: Latte, Miele e Nocciole</h3>
        <p class="font-light text-xs uppercase tracking-widest text-alpine-muted mb-6">Bianco Montagna.</p>
        <p class="text-sm font-light text-alpine-muted leading-relaxed max-w-2xl mx-auto mt-4">
          Una mousse leggera di latte di montagna, un nido di miele di rododendro e terra di nocciole piemontesi tostate. Un dessert monocromatico che richiama la purezza della neve sulle nostre vette.
        </p>
      </div>

    </div>
  </div>
</main>
