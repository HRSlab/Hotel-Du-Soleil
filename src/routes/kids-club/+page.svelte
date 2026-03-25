<script lang="ts">
    import { t } from '$lib/i18n';
    import { Baby, Palette, Puzzle } from 'lucide-svelte';
</script>

<svelte:head>
    <title>{$t('kids_club.title')} | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div class="absolute inset-0">
        <img src="/imgs/Winter_Park.jpeg" class="ken-burns h-full w-full object-cover opacity-80" alt="Kids Club" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/40 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            {$t('kids_club.subtitle')}
        </span>
        <h1 class="font-serif text-5xl md:text-7xl leading-tight font-light text-white fade-up-element">
            {$t('kids_club.title')}
        </h1>
    </div>
</header>

<section class="bg-alpine-bg px-6 py-20 lg:py-32">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <Baby class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            {$t('kids_club.title')}
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            {$t('kids_club.description')}
        </p>
    </div>
</section>

<section class="bg-alpine-bg pb-20 lg:pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-12 text-center">
    <div class="fade-up-element p-8 bg-white border border-alpine-border shadow-sm">
        <Palette class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
        <h4 class="font-serif text-2xl text-alpine-text mb-4">Laboratori Creativi</h4>
        <p class="text-xs text-alpine-muted font-light leading-relaxed">
            Dalla pittura alla creazione di piccoli ricordi montani, stimoliamo la manualità e la fantasia dei bambini.
        </p>
    </div>
    <div class="fade-up-element p-8 bg-white border border-alpine-border shadow-sm">
        <Puzzle class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
        <h4 class="font-serif text-2xl text-alpine-text mb-4">Giochi & Sfide</h4>
        <p class="text-xs text-alpine-muted font-light leading-relaxed">
            Un'ampia selezione di giochi da tavolo e attività di gruppo per socializzare e divertirsi in sicurezza.
        </p>
    </div>
    <div class="fade-up-element p-8 bg-white border border-alpine-border shadow-sm">
        <Baby class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
        <h4 class="font-serif text-2xl text-alpine-text mb-4">Baby Sitting</h4>
        <p class="text-xs text-alpine-muted font-light leading-relaxed">
            Su richiesta, offriamo un servizio di baby sitting personalizzato per le esigenze di ogni famiglia.
        </p>
    </div>
</section>
