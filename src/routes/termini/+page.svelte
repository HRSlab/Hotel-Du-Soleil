<script lang="ts">
    import { t } from '$lib/i18n';
</script>

<svelte:head>
    <title>{$t('termini.title')} | Chalet do Soleil</title>
</svelte:head>

<header class="relative h-[40vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div class="absolute inset-0">
        <div class="absolute inset-0 bg-alpine-text opacity-90"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-16 text-center">
        <h1 class="font-serif text-4xl md:text-6xl leading-tight font-light text-white fade-up-element">
            {$t('termini.title')}
        </h1>
    </div>
</header>

<section class="bg-alpine-bg px-6 py-24 min-h-screen">
    <div class="fade-up-element mx-auto max-w-3xl">
        <div class="space-y-12 text-alpine-muted font-light leading-relaxed text-sm">
            <div>
                <h2 class="font-serif text-2xl text-alpine-text mb-4 italic">{$t('termini.section1_title')}</h2>
                <p>{$t('termini.section1_text')}</p>
            </div>

            <div>
                 <h2 class="font-serif text-2xl text-alpine-text mb-4 italic">{$t('termini.section2_title')}</h2>
                 <p>{$t('termini.section2_text')}</p>
            </div>

            <div>
                 <h2 class="font-serif text-2xl text-alpine-text mb-4 italic">{$t('termini.section3_title')}</h2>
                 <p>{$t('termini.section3_text')}</p>
            </div>

            <div class="pt-12 border-t border-alpine-border">
                <p class="text-[10px] uppercase tracking-widest font-bold">{$t('termini.updated')}</p>
            </div>
        </div>
    </div>
</section>
