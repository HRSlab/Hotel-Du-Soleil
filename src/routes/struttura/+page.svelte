<script lang="ts">
    import { t } from '$lib/i18n';
    import { Building2, Maximize, Sparkles } from 'lucide-svelte';
</script>

<svelte:head>
    <title>{$t('struttura.title')} | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div class="absolute inset-0">
        <img src="/imgs/Winter_entrance_hero.webp" class="ken-burns h-full w-full object-cover opacity-80" alt="Hotel du Soleil Exterior" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/40 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            {$t('struttura.subtitle')}
        </span>
        <h1 class="font-serif text-5xl md:text-7xl leading-tight font-light text-white fade-up-element">
            {$t('struttura.title')}
        </h1>
    </div>
</header>

<section class="bg-alpine-bg px-6 py-24">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <Building2 class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            {$t('struttura.philosophy_title')}
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            {$t('struttura.philosophy_text')}
        </p>
    </div>
</section>

<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element order-2 md:order-1">
        <Maximize class="w-8 h-8 text-alpine-gold mb-6 stroke-[1.5px]" />
        <h2 class="font-serif text-4xl text-alpine-text mb-6">{$t('struttura.common_spaces_title')}</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            {$t('struttura.common_spaces_text')}
        </p>
        <ul class="space-y-4 text-xs tracking-widest uppercase font-bold text-alpine-text">
            {#each (Array.isArray($t('struttura.amenities')) ? $t('struttura.amenities') : []) as amenity, i (i)}
                <li class="flex items-center gap-3"><Sparkles class="w-4 h-4 text-alpine-gold" /> {amenity}</li>
            {/each}
        </ul>
    </div>
    <div class="fade-up-element order-1 md:order-2 overflow-hidden bg-alpine-border">
        <img src="/imgs/lobby.webp" alt="Hotel Interior" class="w-full h-full object-cover img-elegant aspect-4/3">
    </div>
</section>
