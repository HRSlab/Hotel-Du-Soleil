<script lang="ts">
    import { t } from '$lib/i18n';
    import { Users, Tv, GlassWater, Maximize } from 'lucide-svelte';
</script>

<svelte:head>
    <title>{$t('eventi.title')} | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div class="absolute inset-0">
        <img src="https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?q=80&w=2000&auto=format&fit=crop" class="ken-burns h-full w-full object-cover opacity-80" alt="Meetings and Events" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/40 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            {$t('eventi.subtitle')}
        </span>
        <h1 class="font-serif text-5xl md:text-7xl leading-tight font-light text-white fade-up-element">
            {$t('eventi.title')}
        </h1>
    </div>
</header>

<section class="bg-alpine-bg px-6 py-20 lg:py-32">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <Users class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            {$t('eventi.title')}
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            {$t('eventi.description')}
        </p>
    </div>
</section>

<section class="bg-alpine-bg pb-20 lg:pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-12 text-center">
    <div class="fade-up-element p-8 bg-white border border-alpine-border shadow-sm">
        <Tv class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
        <h4 class="font-serif text-2xl text-alpine-text mb-4">Tecnologia</h4>
        <p class="text-xs text-alpine-muted font-light leading-relaxed">
            Sale meeting dotate di proiettori, connessione Wi-Fi ad alta velocità e sistemi audio moderni.
        </p>
    </div>
    <div class="fade-up-element p-8 bg-white border border-alpine-border shadow-sm">
        <Maximize class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
        <h4 class="font-serif text-2xl text-alpine-text mb-4">Flessibilità</h4>
        <p class="text-xs text-alpine-muted font-light leading-relaxed">
            Spazi modulabili adatti a piccoli meeting board o eventi di team building aziendali.
        </p>
    </div>
    <div class="fade-up-element p-8 bg-white border border-alpine-border shadow-sm">
        <GlassWater class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
        <h4 class="font-serif text-2xl text-alpine-text mb-4">Catering</h4>
        <p class="text-xs text-alpine-muted font-light leading-relaxed">
            Coffee break, light lunch o cene di gala preparati con i migliori ingredienti del territorio.
        </p>
    </div>
</section>
