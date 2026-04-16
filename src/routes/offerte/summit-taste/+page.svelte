<script lang="ts">
  import OfferLeadForm from '$lib/components/OfferLeadForm.svelte';
</script>

<svelte:head>
  <title>Summit Taste | Chalet du Soleil</title>
  <meta
    name="description"
    content="Summit Taste: weekend gourmet di luglio con camera superior, cena degustazione e massaggio di coppia."
  />
</svelte:head>

<header class="relative h-[82vh] w-full overflow-hidden bg-[#1a1a1a]">
  <div class="absolute inset-0">
    <img
      src="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?q=80&w=2200&auto=format&fit=crop"
      alt="Summit Taste"
      class="h-full w-full object-cover opacity-55"
    />
    <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/35 to-alpine-bg"></div>
  </div>

  <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
    <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase">Weekend di Luglio</span>
    <h1 class="font-serif text-5xl leading-tight font-light text-white md:text-7xl">SUMMIT TASTE</h1>
    <p class="mt-6 max-w-2xl text-sm font-light text-white/65 md:text-base">
      Sapori di vetta e relax d'autore in una fuga di coppia ad alta intensita.
    </p>
  </div>
</header>

<section class="bg-alpine-bg px-6 py-24">
  <div class="mx-auto grid max-w-7xl grid-cols-1 gap-12 lg:grid-cols-2">
    <div>
      <h2 class="font-serif text-4xl text-alpine-text md:text-5xl">2 notti di eccellenza</h2>
      <p class="mt-6 text-sm leading-relaxed font-light text-alpine-muted md:text-base">
        Un pacchetto signature per coppie che desiderano vivere il meglio tra cucina, cantina e benessere.
      </p>
      <div class="mt-10 border border-alpine-border bg-white p-8">
        <span class="text-[10px] font-bold tracking-[0.2em] text-alpine-muted uppercase">Prezzo coppia</span>
        <p class="mt-3 font-serif text-5xl text-alpine-text">EUR 450,00</p>
        <p class="text-sm text-alpine-muted">totale per 2 notti (venerdi-domenica)</p>
      </div>
    </div>

    <div class="space-y-4">
      <article class="border border-alpine-border bg-white p-6">
        <h3 class="font-serif text-3xl text-alpine-text">Camera Superior</h3>
        <p class="mt-2 text-sm font-light text-alpine-muted">Sistemazione garantita in camera rinnovata con vista panoramica e balcone.</p>
      </article>
      <article class="border border-alpine-border bg-white p-6">
        <h3 class="font-serif text-3xl text-alpine-text">Cena Alchimia Alpina</h3>
        <p class="mt-2 text-sm font-light text-alpine-muted">Menu degustazione 5 portate con bottiglia selezionata di Blanc de Morgex et de La Salle.</p>
      </article>
      <article class="border border-alpine-border bg-white p-6">
        <h3 class="font-serif text-3xl text-alpine-text">Massaggio di Coppia</h3>
        <p class="mt-2 text-sm font-light text-alpine-muted">30 minuti con olio al pino cembro per un momento di benessere condiviso.</p>
      </article>
    </div>
  </div>
</section>

<OfferLeadForm
  title="Prenota il tuo weekend gourmet"
  subtitle="Compila il form e ricevi disponibilita immediata per i weekend Summit Taste."
  notesPlaceholder="Weekend preferito e richieste speciali"
  successText="Ti risponderemo con la proposta Summit Taste disponibile."
/>
