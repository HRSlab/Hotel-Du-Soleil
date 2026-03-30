<script lang="ts">
    import { t } from '$lib/i18n';
    import { History, Heart } from 'lucide-svelte';
</script>

<svelte:head>
    <title>{$t('storia.title')} | Chalet do Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div class="absolute inset-0">
        <img src="https://images.unsplash.com/photo-1554034483-04fda0d3507b?q=80&w=2000&auto=format&fit=crop" class="ken-burns h-full w-full object-cover opacity-80 grayscale" alt="History of Chalet do Soleil" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/40 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            {$t('storia.subtitle')}
        </span>
        <h1 class="font-serif text-5xl md:text-7xl leading-tight font-light text-white fade-up-element">
            {$t('storia.title')}
        </h1>
    </div>
</header>

<section class="bg-alpine-bg px-6 py-24">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <History class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            {$t('storia.philosophy_title')}
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            {$t('storia.philosophy_text')}
        </p>
    </div>
</section>

<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto space-y-32">
    <div class="flex flex-col md:flex-row gap-12 items-center fade-up-element">
        <div class="w-full md:w-1/2 overflow-hidden bg-alpine-border relative group cursor-default">
            <img src="https://images.unsplash.com/photo-1544984243-ec57ea16fe75?q=80&w=1500&auto=format&fit=crop" alt="Old Look of Torgnon" class="w-full h-full object-cover img-elegant aspect-4/3 grayscale hover:grayscale-0 transition-all duration-700">
        </div>
        <div class="w-full md:w-1/2">
            <Heart class="w-8 h-8 text-alpine-gold mb-6 stroke-[1.5px]" />
            <h2 class="font-serif text-4xl text-alpine-text mb-4">{$t('storia.roots_title')}</h2>
            <p class="text-[10px] uppercase tracking-widest text-alpine-muted mb-6 font-bold">{$t('storia.roots_label')}</p>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
                {$t('storia.roots_text')}
            </p>
        </div>
    </div>
</section>
