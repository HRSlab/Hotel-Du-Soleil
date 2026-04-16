<script lang="ts">
  import OfferLeadForm from '$lib/components/OfferLeadForm.svelte';
</script>

<svelte:head>
  <title>Family Base Camp | Chalet du Soleil</title>
  <meta
    name="description"
    content="Pacchetto Family Base Camp luglio: settimana in mezza pensione con vantaggi famiglia, merenda del pastore e Family SPA."
  />
</svelte:head>

<header class="relative h-[82vh] w-full overflow-hidden bg-[#1a1a1a]">
  <div class="absolute inset-0">
    <img
      src="https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?q=80&w=2200&auto=format&fit=crop"
      alt="Family Base Camp"
      class="h-full w-full object-cover opacity-55"
    />
    <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/35 to-alpine-bg"></div>
  </div>

  <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
    <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase">Luglio 2026</span>
    <h1 class="font-serif text-5xl leading-tight font-light text-white md:text-7xl">FAMILY BASE CAMP</h1>
    <p class="mt-6 max-w-2xl text-sm font-light text-white/65 md:text-base">
      I bambini esplorano, i genitori si rilassano: la montagna a misura di famiglia.
    </p>
  </div>
</header>

<section class="bg-alpine-bg px-6 py-24">
  <div class="mx-auto grid max-w-7xl grid-cols-1 gap-12 lg:grid-cols-2">
    <div>
      <h2 class="font-serif text-4xl text-alpine-text md:text-5xl">Settimana Family</h2>
      <p class="mt-6 text-sm leading-relaxed font-light text-alpine-muted md:text-base">
        Formula settimanale pensata per famiglie con bambini 4-12 anni, con servizi concreti e valore percepito alto.
      </p>
      <div class="mt-10 border border-alpine-border bg-white p-8">
        <span class="text-[10px] font-bold tracking-[0.2em] text-alpine-muted uppercase">Prezzo famiglia</span>
        <p class="mt-3 font-serif text-5xl text-alpine-text">EUR 1.250,00</p>
        <p class="text-sm text-alpine-muted">totale 7 notti in Mezza Pensione</p>
        <p class="mt-2 text-sm text-alpine-muted">Base 2 adulti + 1 bambino fino a 8 anni non compiuti</p>
      </div>
    </div>

    <div class="space-y-4">
      <article class="border border-alpine-border bg-white p-6">
        <h3 class="font-serif text-3xl text-alpine-text">Merenda del Pastore</h3>
        <p class="mt-2 text-sm font-light text-alpine-muted">Ogni pomeriggio dalle 16:00 alle 17:00 con prodotti artigianali e bio.</p>
      </article>
      <article class="border border-alpine-border bg-white p-6">
        <h3 class="font-serif text-3xl text-alpine-text">Family SPA</h3>
        <p class="mt-2 text-sm font-light text-alpine-muted">Ingresso dedicato in fascia family per piscina riscaldata e relax condiviso.</p>
      </article>
      <article class="border border-alpine-border bg-white p-6">
        <h3 class="font-serif text-3xl text-alpine-text">Baby Trekking Maps</h3>
        <p class="mt-2 text-sm font-light text-alpine-muted">Mappe pratiche di percorsi facili, parchi gioco e aree picnic.</p>
      </article>
    </div>
  </div>
</section>

<OfferLeadForm
  title="Blocca la tua settimana family"
  subtitle="Richiedi disponibilita e proposta con eventuale sconto secondo bambino."
  notesPlaceholder="Numero adulti/bambini e settimana di interesse"
  successText="Il team family booking ti contattera al piu presto."
/>
