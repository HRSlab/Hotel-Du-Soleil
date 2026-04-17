<script lang="ts">
	import { t } from '$lib/i18n';
</script>

<svelte:head>
  <title>{$t('offers_page.head_title')}</title>
  <meta
    name="description"
    content={$t('offers_page.meta_description')}
  />
</svelte:head>

<header class="relative h-[70vh] w-full overflow-hidden bg-[#1a1a1a]">
  <div class="absolute inset-0">
    <img
      src="/imgs/exterior-snow-back-2026.webp"
      alt={$t('offers_page.hero_alt')}
      class="h-full w-full object-cover opacity-55"
    />
    <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/30 to-alpine-bg"></div>
  </div>

  <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
    <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase">
      {$t('offers_page.hero_tag')}
    </span>
    <h1 class="font-serif text-5xl leading-tight font-light text-white md:text-7xl">
      {$t('offers_page.hero_title')}
    </h1>
    <p class="mt-6 max-w-2xl text-sm font-light text-white/60 md:text-base">
      {$t('offers_page.hero_text')}
    </p>
  </div>
</header>

<section class="bg-alpine-bg px-6 py-20 md:py-28">
  <div class="mx-auto max-w-7xl">
    <div class="mb-16 border-b border-alpine-border pb-8">
      <h2 class="font-serif text-4xl text-alpine-text md:text-5xl">{$t('offers_page.section_title')}</h2>
      <p class="mt-4 max-w-2xl text-sm leading-relaxed font-light text-alpine-muted md:text-base">
        {$t('offers_page.section_text')}
      </p>
    </div>

    <div class="grid grid-cols-1 gap-8 md:max-w-2xl">
      <article class="group border border-alpine-border bg-white transition-all duration-500 hover:-translate-y-1 hover:border-alpine-gold hover:shadow-2xl">
        <a href="/offerte/restart" class="block">
          <div class="aspect-16/10 overflow-hidden">
            <img
              src="https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=1600&auto=format&fit=crop"
              alt="RESTART"
              class="h-full w-full object-cover img-elegant transition-transform duration-700 group-hover:scale-105"
            />
          </div>
          <div class="p-8">
            <span class="text-[10px] font-bold tracking-[0.22em] text-alpine-gold uppercase">{$t('offers_page.card_tag')}</span>
            <h3 class="mt-3 font-serif text-3xl text-alpine-text">RESTART</h3>
            <p class="mt-3 text-sm leading-relaxed font-light text-alpine-muted">
              {$t('offers_page.card_text')}
            </p>
            <span class="mt-6 inline-flex border-b border-alpine-text pb-1 text-[11px] font-bold tracking-[0.2em] text-alpine-text uppercase transition-colors group-hover:border-alpine-gold group-hover:text-alpine-gold">
              {$t('offers_page.card_cta')}
            </span>
          </div>
        </a>
      </article>
    </div>
  </div>
</section>
