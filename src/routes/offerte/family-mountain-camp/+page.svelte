<script lang="ts">
  import OfferLeadForm from '$lib/components/OfferLeadForm.svelte';
</script>

<svelte:head>
  <title>Family Mountain Camp | Chalet du Soleil</title>
  <meta
    name="description"
    content="Family Mountain Camp luglio: pacchetto settimanale all-inclusive con Kids Outdoor Kit e piano famiglia potenziato."
  />
</svelte:head>

<header class="relative h-[82vh] w-full overflow-hidden bg-[#1a1a1a]">
  <div class="absolute inset-0">
    <img
      src="https://images.unsplash.com/photo-1511895426328-dc8714191300?q=80&w=2200&auto=format&fit=crop"
      alt="Family Mountain Camp"
      class="h-full w-full object-cover opacity-55"
    />
    <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/35 to-alpine-bg"></div>
  </div>

  <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
    <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase">Special Luglio</span>
    <h1 class="font-serif text-5xl leading-tight font-light text-white md:text-7xl">FAMILY MOUNTAIN CAMP</h1>
    <p class="mt-6 max-w-2xl text-sm font-light text-white/65 md:text-base">Settimana full-immersion in montagna con massima comodita per tutta la famiglia.</p>
  </div>
</header>

<section class="bg-alpine-bg px-6 py-24">
  <div class="mx-auto grid max-w-7xl grid-cols-1 gap-8 md:grid-cols-2">
    <article class="border border-alpine-border bg-white p-8">
      <h3 class="font-serif text-3xl text-alpine-text">Tariffa Flat Settimanale</h3>
      <p class="mt-4 font-serif text-5xl text-alpine-text">EUR 1.150,00</p>
      <p class="mt-2 text-sm text-alpine-muted">totale 7 notti in Mezza Pensione</p>
      <p class="mt-2 text-sm text-alpine-muted">Base: 2 adulti + 1 bambino</p>
    </article>

    <article class="border border-alpine-border bg-white p-8">
      <h3 class="font-serif text-3xl text-alpine-text">Plus del pacchetto</h3>
      <ul class="mt-5 space-y-3 text-sm text-alpine-muted">
        <li>• Kids Outdoor Kit omaggio</li>
        <li>• Menù bimbi dedicato</li>
        <li>• Garage coperto incluso (1 auto)</li>
        <li>• Bambini fino a 8 anni non compiuti gratis</li>
      </ul>
    </article>
  </div>
</section>

<OfferLeadForm
  title="Richiedi il tuo pacchetto famiglia"
  subtitle="Indicaci composizione famiglia e settimana preferita."
  notesPlaceholder="Numero bambini, eta e periodo"
  successText="Riceverai la proposta Family Mountain Camp al piu presto."
/>
