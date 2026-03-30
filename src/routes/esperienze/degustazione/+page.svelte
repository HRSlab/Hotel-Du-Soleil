<script lang="ts">
    import { t } from '$lib/i18n';
    import { Utensils, GlassWater, MapPin, Heart, Mountain, Users, Award, MilkOff, ExternalLink, Milk, Timer, Thermometer, FlaskConical } from 'lucide-svelte';

    let scrollY = $state(0);
</script>

<svelte:window bind:scrollY />

<svelte:head>
    <title>{$t('degustazione_page.meta_title')}</title>
    <meta name="description" content={$t('degustazione_page.meta_description')} />
</svelte:head>

<header class="relative h-[85vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div
        class="absolute inset-0 scale-110"
        style="transform: translateY({scrollY * 0.25}px) scale(1.1);"
    >
        <video
            autoplay
            loop
            muted
            playsinline
            class="h-full w-full object-cover opacity-70"
            poster="https://images.unsplash.com/photo-1486297678162-eb2a19b7ec50?q=80&w=2000&auto=format&fit=crop"
        >
            <source src="/imgs/fontina-dop-hero.mp4" type="video/mp4" />
        </video>
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/20 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-28 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            {$t('degustazione_page.hero_label')}
        </span>
        <h1 class="font-serif text-5xl md:text-8xl leading-tight font-light text-white fade-up-element">
            {$t('degustazione_page.hero_title')}
        </h1>
        <p class="mt-6 text-white/60 text-sm font-light max-w-md fade-up-element">
            {$t('degustazione_page.hero_subtitle')}
        </p>
    </div>
</header>

<section class="bg-alpine-bg px-6 py-28">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <Utensils class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            {$t('degustazione_page.intro_title')}
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            {$t('degustazione_page.intro_text')}
        </p>
    </div>
</section>

<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
        <img src="https://images.unsplash.com/photo-1500595046743-cd271d694d30?q=80&w=1500&auto=format&fit=crop" alt="Alpeggio Valle d'Aosta" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90">
    </div>
    <div class="fade-up-element">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">{$t('degustazione_page.family_label')}</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">{$t('degustazione_page.family_title')}</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            {$t('degustazione_page.family_text1')}
        </p>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
            {$t('degustazione_page.family_text2')}
        </p>
        <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
            <div class="flex items-center gap-3">
                 <Heart class="w-5 h-5 text-alpine-gold shrink-0" />
                 <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('degustazione_page.family_badge_history')}</span>
            </div>
            <div class="flex items-center gap-3">
                 <Award class="w-5 h-5 text-alpine-gold shrink-0" />
                 <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('degustazione_page.family_badge_award')}</span>
            </div>
        </div>
    </div>
</section>

<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element order-2 md:order-1">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">{$t('degustazione_page.milk_label')}</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">{$t('degustazione_page.milk_title')}</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            {$t('degustazione_page.milk_text1')}
        </p>
        <p class="text-alpine-muted text-sm font-light leading-relaxed">
            {$t('degustazione_page.milk_text2')}
        </p>
    </div>
    <div class="fade-up-element order-1 md:order-2 overflow-hidden bg-alpine-border shadow-xl">
        <img src="https://images.unsplash.com/photo-1594731884638-8197c3102d1d?q=80&w=1500&auto=format&fit=crop" alt="Bovine al pascolo in alpeggio" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90">
    </div>
</section>

<section class="border-y border-alpine-border bg-white py-20 px-6">
    <div class="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-12 text-center">
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">4ª</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">{$t('degustazione_page.stats_generation')}</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">120</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">{$t('degustazione_page.stats_dairy_heads')}</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">1500+</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">{$t('degustazione_page.stats_wheels_year')}</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">3</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">{$t('degustazione_page.stats_alpine_pastures')}</p>
        </div>
    </div>
</section>

<!-- ═══════════════════ LA DENOMINAZIONE DOP ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-16 lg:gap-24 items-center">
        <div class="fade-up-element">
            <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">{$t('degustazione_page.dop_label')}</span>
            <h2 class="font-serif text-4xl text-alpine-text mb-6">{$t('degustazione_page.dop_title')}</h2>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
                {$t('degustazione_page.dop_text1')}
            </p>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
                {$t('degustazione_page.dop_text2')}
            </p>
            <p class="text-alpine-muted text-sm font-light leading-relaxed">
                {$t('degustazione_page.dop_text3')}
            </p>
        </div>
        <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
            <img src="https://images.unsplash.com/photo-1589985270826-4b7bb135bc9d?q=80&w=1500&auto=format&fit=crop" alt="Forme di Fontina DOP in stagionatura" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90">
        </div>
    </div>
</section>

<!-- ═══════════════════ LA LAVORAZIONE ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">{$t('degustazione_page.process_title')}</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">{$t('degustazione_page.process_subtitle')}</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
            <div class="fade-up-element text-center p-10 border border-alpine-border bg-alpine-bg">
                <Milk class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-1" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('degustazione_page.process_milk_title')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('degustazione_page.process_milk_text')}
                </p>
            </div>
            <div class="fade-up-element text-center p-10 border border-alpine-border bg-alpine-bg">
                <FlaskConical class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-1" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('degustazione_page.process_curd_title')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('degustazione_page.process_curd_text')}
                </p>
            </div>
            <div class="fade-up-element text-center p-10 border border-alpine-border bg-alpine-bg">
                <Thermometer class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-1" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('degustazione_page.process_brine_title')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('degustazione_page.process_brine_text')}
                </p>
            </div>
            <div class="fade-up-element text-center p-10 border border-alpine-border bg-alpine-bg">
                <Timer class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-1" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('degustazione_page.process_ageing_title')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('degustazione_page.process_ageing_text')}
                </p>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ I FORMAGGI (Lo Copafen) ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">{$t('degustazione_page.cheeses_title')}</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">{$t('degustazione_page.cheeses_subtitle')}</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12">
            <div class="fade-up-element text-center p-12 md:p-14 border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <MilkOff class="w-8 h-8 text-alpine-gold mx-auto mb-8 stroke-1" />
                <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('degustazione_page.cheese_fondovalle_name')}</h4>
                <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-6">{$t('degustazione_page.cheese_fondovalle_season')}</p>
                <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed max-w-xs mx-auto">
                    {$t('degustazione_page.cheese_fondovalle_text')}
                </p>
            </div>
            <div class="fade-up-element text-center p-12 md:p-14 border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <Mountain class="w-8 h-8 text-alpine-gold mx-auto mb-8 stroke-1" />
                <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('degustazione_page.cheese_alpeggio_name')}</h4>
                <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-6">{$t('degustazione_page.cheese_alpeggio_season')}</p>
                <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed max-w-xs mx-auto">
                    {$t('degustazione_page.cheese_alpeggio_text')}
                </p>
            </div>
            <div class="fade-up-element text-center p-12 md:p-14 border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <Award class="w-8 h-8 text-alpine-gold mx-auto mb-8 stroke-1" />
                <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('degustazione_page.cheese_riserva_name')}</h4>
                <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-6">{$t('degustazione_page.cheese_riserva_season')}</p>
                <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed max-w-xs mx-auto">
                    {$t('degustazione_page.cheese_riserva_text')}
                </p>
            </div>
        </div>

        <div class="fade-up-element grid grid-cols-2 md:grid-cols-4 gap-6 mt-12">
            {#each $t('degustazione_page.products') as prodotto (prodotto)}
                <div class="text-center py-6 px-4 border border-alpine-border bg-white/50">
                    <p class="text-xs text-alpine-muted font-light">{prodotto}</p>
                </div>
            {/each}
        </div>
    </div>
</section>

<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
        <img src="https://images.unsplash.com/photo-1452195125355-903496c21e64?q=80&w=1500&auto=format&fit=crop" alt="Degustazione di formaggi" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90">
    </div>
    <div class="fade-up-element">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">{$t('degustazione_page.tasting_label')}</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">{$t('degustazione_page.tasting_title')}</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            {$t('degustazione_page.tasting_text1')}
        </p>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
            {$t('degustazione_page.tasting_text2')}
        </p>
        <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
            <div class="flex items-center gap-3">
                 <GlassWater class="w-5 h-5 text-alpine-gold shrink-0" />
                 <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('degustazione_page.tasting_badge_wine')}</span>
            </div>
            <div class="flex items-center gap-3">
                 <MapPin class="w-5 h-5 text-alpine-gold shrink-0" />
                 <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('degustazione_page.tasting_badge_local')}</span>
            </div>
        </div>
    </div>
</section>

<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element order-2 md:order-1">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">{$t('degustazione_page.farm_label')}</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">{$t('degustazione_page.farm_title')}</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            {$t('degustazione_page.farm_text1')}
        </p>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
            {$t('degustazione_page.farm_text2')}
        </p>
        <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
            <div class="flex items-center gap-3">
                 <Users class="w-5 h-5 text-alpine-gold shrink-0" />
                 <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('degustazione_page.farm_badge_groups')}</span>
            </div>
            <div class="flex items-center gap-3">
                 <Mountain class="w-5 h-5 text-alpine-gold shrink-0" />
                 <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('degustazione_page.farm_badge_summer')}</span>
            </div>
        </div>
    </div>
    <div class="fade-up-element order-1 md:order-2 overflow-hidden bg-alpine-border shadow-xl">
        <img src="https://images.unsplash.com/photo-1516467508483-a7212febe31a?q=80&w=1500&auto=format&fit=crop" alt="Visita in fattoria" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90">
    </div>
</section>

<section class="border-t border-alpine-border bg-white py-20 px-6">
    <div class="max-w-3xl mx-auto text-center fade-up-element">
        <p class="text-[10px] uppercase tracking-[0.3em] text-alpine-muted font-bold mb-6">{$t('degustazione_page.partner_label')}</p>
        <h3 class="font-serif text-3xl md:text-4xl text-alpine-text mb-4">{$t('degustazione_page.partner_name')}</h3>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-2">{$t('degustazione_page.partner_address')}</p>
        <p class="text-alpine-muted text-xs font-light mb-8">{$t('degustazione_page.partner_distance')}</p>
        <a href="https://locopafen.it" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-alpine-gold hover:text-alpine-text transition-colors duration-300">
            {$t('degustazione_page.partner_link')}
            <ExternalLink class="w-4 h-4" />
        </a>
    </div>
</section>
