<script lang="ts">
  import OfferLeadForm from '$lib/components/OfferLeadForm.svelte';
</script>

<svelte:head>
  <title>Pacchetto RESTART | Chalet du Soleil</title>
  <meta
    name="description"
    content="Pacchetto RESTART giugno: 3 notti infrasettimanali con escursione guidata, SPA illimitata e degustazione valdostana."
  />
</svelte:head>

<header class="relative h-[88vh] w-full overflow-hidden bg-[#1a1a1a]">
  <div class="absolute inset-0">
    <img
      src="https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=2200&auto=format&fit=crop"
      alt="Pacchetto RESTART"
      class="h-full w-full object-cover opacity-55"
    />
    <div class="absolute inset-0 bg-linear-to-b from-black/85 via-black/30 to-alpine-bg"></div>
  </div>

  <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-28 text-center">
    <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase">
      Esclusiva Giugno 2026
    </span>
    <h1 class="font-serif text-5xl leading-tight font-light text-white md:text-8xl">
      RESTART
      <span class="mt-2 block text-3xl italic md:text-5xl">Ritrova il tuo equilibrio tra le fioriture di Torgnon.</span>
    </h1>
    <p class="mt-6 max-w-2xl text-sm font-light text-white/60 md:text-base">
      Risveglio alpino e silenzio rigenerante: il momento perfetto per vivere la montagna lontano dalla folla.
    </p>
  </div>
</header>

<section class="bg-alpine-bg px-6 py-24 lg:py-32">
  <div class="mx-auto grid max-w-7xl grid-cols-1 items-center gap-14 lg:grid-cols-2 lg:gap-24">
    <div>
      <div class="mb-10 h-20 w-px bg-alpine-border"></div>
      <h2 class="font-serif text-4xl leading-tight text-alpine-text md:text-6xl">Il lusso di giugno in quota</h2>
      <p class="mt-6 text-sm leading-relaxed font-light text-alpine-muted md:text-base">
        RESTART nasce per coppie e ospiti in cerca di benessere, quiete e natura autentica. Un invito a staccare
        il ritmo e ritrovare energia tra fioriture alpine, sentieri panoramici e aria pura.
      </p>
      <p class="mt-4 text-sm leading-relaxed font-light text-alpine-muted md:text-base">
        Formula infrasettimanale: soggiorno minimo 3 notti con arrivo da domenica a martedi.
      </p>

      <div class="mt-10 border border-alpine-border bg-white p-8">
        <span class="text-[10px] font-bold tracking-[0.22em] text-alpine-muted uppercase">Offerta RESTART</span>
        <div class="mt-4 flex flex-wrap items-end gap-x-3 gap-y-1">
          <span class="font-serif text-5xl text-alpine-text">EUR 94,00</span>
          <span class="pb-2 text-sm font-light text-alpine-muted">a notte / persona</span>
        </div>
        <ul class="mt-4 space-y-2 text-sm leading-relaxed text-alpine-muted">
          <li>• Mezza pensione inclusa</li>
          <li>• Soggiorno minimo di 3 notti</li>
          <li class="text-alpine-text">• Sconto 25% rispetto alla tariffa alta stagione</li>
        </ul>
      </div>
    </div>

    <div>
      <div class="grid grid-cols-1 gap-6">
        <article class="border border-alpine-border bg-white p-7">
          <span class="text-[10px] font-bold tracking-[0.2em] text-alpine-gold uppercase">01</span>
          <h3 class="mt-3 font-serif text-3xl text-alpine-text">Trekking all'Alpe Gordza</h3>
          <p class="mt-3 text-sm leading-relaxed font-light text-alpine-muted">
            Escursione guidata di mezza giornata tra forest bathing e fioriture alpine, con picnic gourmet.
          </p>
        </article>

        <article class="border border-alpine-gold/40 bg-alpine-text p-7 text-white">
          <span class="text-[10px] font-bold tracking-[0.2em] text-alpine-gold uppercase">02</span>
          <h3 class="mt-3 font-serif text-3xl">Kit Nuvola & Wellness</h3>
          <p class="mt-3 text-sm leading-relaxed font-light text-white/75">
            Accesso illimitato alla SPA con kit comfort Nuvola: accappatoio, ciabattine e sali da bagno alpini.
          </p>
        </article>

        <article class="border border-alpine-border bg-white p-7">
          <span class="text-[10px] font-bold tracking-[0.2em] text-alpine-gold uppercase">03</span>
          <h3 class="mt-3 font-serif text-3xl text-alpine-text">Degustazione d'Autore</h3>
          <p class="mt-3 text-sm leading-relaxed font-light text-alpine-muted">
            Degustazione sensoriale di formaggi d'alpeggio e vini valdostani selezionati.
          </p>
        </article>
      </div>
    </div>
  </div>
</section>

<OfferLeadForm
  title="Richiedi il tuo preventivo RESTART"
  subtitle="Compila il modulo: il team booking ti inviera una proposta personalizzata con disponibilita aggiornata."
  notesPlaceholder="Data di arrivo (dom-martedi), numero notti e preferenze benessere"
  successText="Il nostro team ti rispondera al piu presto con disponibilita e proposta dedicata."
/>
