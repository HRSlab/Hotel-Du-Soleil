<script lang="ts">
  import OfferLeadForm from '$lib/components/OfferLeadForm.svelte';
</script>

<svelte:head>
  <title>Wheels & Relax | Chalet du Soleil</title>
  <meta
    name="description"
    content="Pacchetto Wheels & Relax: bike experience premium con servizi tecnici, ride fuel e recupero benessere."
  />
</svelte:head>

<header class="relative h-[82vh] w-full overflow-hidden bg-[#1a1a1a]">
  <div class="absolute inset-0">
    <img
      src="https://images.unsplash.com/photo-1517654443271-21cf74ed7a5d?q=80&w=2200&auto=format&fit=crop"
      alt="Wheels and Relax"
      class="h-full w-full object-cover opacity-55"
    />
    <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/35 to-alpine-bg"></div>
  </div>
  <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
    <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase">Sport & Outdoor</span>
    <h1 class="font-serif text-5xl leading-tight font-light text-white md:text-7xl">WHEELS & RELAX</h1>
    <p class="mt-6 max-w-2xl text-sm font-light text-white/65 md:text-base">La bike experience specialistica tra performance e recupero.</p>
  </div>
</header>

<section class="bg-alpine-bg px-6 py-24">
  <div class="mx-auto grid max-w-7xl grid-cols-1 gap-8 md:grid-cols-2">
    <article class="border border-alpine-border bg-white p-8">
      <h3 class="font-serif text-3xl text-alpine-text">Tariffe suggerite</h3>
      <ul class="mt-5 space-y-3 text-sm text-alpine-muted">
        <li>• Giugno (Tier 1): EUR 135,00 / notte (camera doppia)</li>
        <li>• Luglio (Tier 2): EUR 165,00 / notte (camera doppia)</li>
        <li>• Minimo soggiorno: 3 notti</li>
      </ul>
    </article>
    <article class="border border-alpine-border bg-white p-8">
      <h3 class="font-serif text-3xl text-alpine-text">Inclusioni Pro</h3>
      <ul class="mt-5 space-y-3 text-sm text-alpine-muted">
        <li>• Bike room videosorvegliata + ricarica e-bike</li>
        <li>• Packet lunch Ride Fuel</li>
        <li>• Aperitivo Biker Debriefing</li>
        <li>• Sconto 20% su massaggi sportivi</li>
      </ul>
    </article>
  </div>
</section>

<OfferLeadForm
  title="Richiedi il pacchetto bike"
  subtitle="Indicaci livello, periodo e numero partecipanti."
  notesPlaceholder="Periodo, livello tecnico, eventuale noleggio e-bike"
  successText="Ti risponderemo con proposta e disponibilita bike."
/>
