<script lang="ts">
    import { t } from '$lib/i18n';
    import { Wind } from 'lucide-svelte';
</script>

<svelte:head>
    <title>{$t('wellness.trattamenti.title')} | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div class="absolute inset-0">
        <img src="https://images.unsplash.com/photo-1544161515-4af6b1d46bdc?q=80&w=2000&auto=format&fit=crop" class="ken-burns h-full w-full object-cover opacity-70" alt="Trattamenti" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/20 to-alpine-bg"></div>
    </div>
    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            {$t('wellness.trattamenti.subtitle')}
        </span>
        <h1 class="font-serif text-5xl md:text-7xl leading-tight font-light text-white fade-up-element">
            {$t('wellness.trattamenti.title')}
        </h1>
    </div>
</header>

<section class="bg-alpine-bg px-6 py-24">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <Wind class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            {$t('wellness.trattamenti.subtitle')}
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
             Trattamenti corpo e viso con essenze alpine.
        </p>
    </div>
</section>
