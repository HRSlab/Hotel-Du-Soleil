<script lang="ts">
  import OfferLeadForm from '$lib/components/OfferLeadForm.svelte';
</script>

<svelte:head>
  <title>Workation Alpino | Chalet du Soleil</title>
  <meta
    name="description"
    content="Pacchetto Workation Alpino: soggiorno long stay a 1.500 metri con servizi dedicati a professionisti e remote worker."
  />
</svelte:head>

<header class="relative h-[82vh] w-full overflow-hidden bg-[#1a1a1a]">
  <div class="absolute inset-0">
    <img
      src="https://images.unsplash.com/photo-1522199755839-a2bacb67c546?q=80&w=2200&auto=format&fit=crop"
      alt="Workation Alpino"
      class="h-full w-full object-cover opacity-50"
    />
    <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/35 to-alpine-bg"></div>
  </div>

  <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
    <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase">Giugno - Luglio</span>
    <h1 class="font-serif text-5xl leading-tight font-light text-white md:text-7xl">WORKATION ALPINO</h1>
    <p class="mt-6 max-w-2xl text-sm font-light text-white/65 md:text-base">
      Lavorare meglio, vivere meglio: il tuo ufficio ad alta quota.
    </p>
  </div>
</header>

<section class="bg-alpine-bg px-6 py-24">
  <div class="mx-auto grid max-w-7xl grid-cols-1 gap-12 lg:grid-cols-2">
    <div>
      <h2 class="font-serif text-4xl text-alpine-text md:text-5xl">Formula Long Stay</h2>
      <p class="mt-6 text-sm leading-relaxed font-light text-alpine-muted md:text-base">
        Pacchetto dedicato a professionisti e digital nomad che desiderano una settimana produttiva in montagna,
        senza rinunciare a comfort, ristorazione e tempo di qualita.
      </p>
      <div class="mt-10 border border-alpine-border bg-white p-8">
        <span class="text-[10px] font-bold tracking-[0.2em] text-alpine-muted uppercase">Tariffa dedicata</span>
        <p class="mt-3 font-serif text-5xl text-alpine-text">EUR 154,00</p>
        <p class="text-sm text-alpine-muted">a notte in Mezza Pensione</p>
        <p class="mt-3 text-sm text-alpine-muted">Soggiorno minimo 7 notti</p>
      </div>
    </div>

    <div class="space-y-4">
      <article class="border border-alpine-border bg-white p-6">
        <h3 class="font-serif text-3xl text-alpine-text">Coffee & Power</h3>
        <p class="mt-2 text-sm font-light text-alpine-muted">
          Caffe e bevande analcoliche illimitate al bar dalle 09:00 alle 12:00, con aree silenziose e prese disponibili.
        </p>
      </article>
      <article class="border border-alpine-border bg-white p-6">
        <h3 class="font-serif text-3xl text-alpine-text">Late Check-out</h3>
        <p class="mt-2 text-sm font-light text-alpine-muted">
          Partenza estesa alle 16:00 nel giorno di check-out per lavorare con calma e goderti ancora la montagna.
        </p>
      </article>
      <article class="border border-alpine-border bg-white p-6">
        <h3 class="font-serif text-3xl text-alpine-text">Upgrade Smart</h3>
        <p class="mt-2 text-sm font-light text-alpine-muted">
          Upgrade gratuito alla camera con scrivania dedicata, su disponibilita.
        </p>
      </article>
    </div>
  </div>
</section>

<OfferLeadForm
  title="Ricevi proposta personalizzata"
  subtitle="Inviaci il periodo desiderato: prepareremo una proposta Workation su misura."
  notesPlaceholder="Periodo, esigenze di lavoro, preferenze camera"
  successText="Ti risponderemo al piu presto con la proposta Workation."
/>
