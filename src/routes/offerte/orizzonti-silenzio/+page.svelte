<script lang="ts">
  import OfferLeadForm from '$lib/components/OfferLeadForm.svelte';
</script>

<svelte:head>
  <title>Orizzonti e Silenzio | Chalet du Soleil</title>
  <meta
    name="description"
    content="Pacchetto Orizzonti e Silenzio: trekking e slow travel con mappe dedicate, zaino gourmet e late check-out."
  />
</svelte:head>

<header class="relative h-[82vh] w-full overflow-hidden bg-[#1a1a1a]">
  <div class="absolute inset-0">
    <img
      src="https://images.unsplash.com/photo-1472396961693-142e6e269027?q=80&w=2200&auto=format&fit=crop"
      alt="Orizzonti e Silenzio"
      class="h-full w-full object-cover opacity-55"
    />
    <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/35 to-alpine-bg"></div>
  </div>
  <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
    <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase">Giugno - Luglio</span>
    <h1 class="font-serif text-5xl leading-tight font-light text-white md:text-7xl">ORIZZONTI E SILENZIO</h1>
    <p class="mt-6 max-w-2xl text-sm font-light text-white/65 md:text-base">Il pacchetto trekking per chi vuole tempo lento e panorami autentici.</p>
  </div>
</header>

<section class="bg-alpine-bg px-6 py-24">
  <div class="mx-auto grid max-w-7xl grid-cols-1 gap-8 md:grid-cols-2">
    <article class="border border-alpine-border bg-white p-8">
      <h3 class="font-serif text-3xl text-alpine-text">Tariffe suggerite</h3>
      <ul class="mt-5 space-y-3 text-sm text-alpine-muted">
        <li>• Giugno (Tier 1): EUR 130,00 / notte (camera doppia)</li>
        <li>• Luglio (Tier 2): EUR 160,00 / notte (camera doppia)</li>
        <li>• Minimo soggiorno: 4 notti</li>
        <li>• Sconto automatico 10% sulla quarta notte</li>
      </ul>
    </article>
    <article class="border border-alpine-border bg-white p-8">
      <h3 class="font-serif text-3xl text-alpine-text">Inclusioni</h3>
      <ul class="mt-5 space-y-3 text-sm text-alpine-muted">
        <li>• Briefing mattutino e mappa sentieri "segreti"</li>
        <li>• Zaino gourmet per il pranzo in quota</li>
        <li>• Signature dinner con Zuppa Sosta in Quota</li>
        <li>• Late check-out ore 16:00 (su disponibilita)</li>
      </ul>
    </article>
  </div>
</section>

<OfferLeadForm
  title="Richiedi disponibilita"
  subtitle="Ricevi proposta personalizzata per il tuo soggiorno slow travel."
  notesPlaceholder="Periodo desiderato e livello escursionistico"
  successText="Ti risponderemo con disponibilita e proposta dedicata."
/>
