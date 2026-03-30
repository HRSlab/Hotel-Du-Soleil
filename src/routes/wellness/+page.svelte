<script lang="ts">
    import { t } from '$lib/i18n';
    import {
        Heart, Clock, Droplets, Flame, Leaf, ArrowRight, ShieldCheck, Star, Sparkles, Waves, Footprints,
        Moon, Wine, Gem, Users, Lock, Music
    } from 'lucide-svelte';

    let scrollY = $state(0);
</script>

<svelte:window bind:scrollY />

<svelte:head>
    <title>{$t('wellness.main_title')} | Chalet du Soleil</title>
    <meta name="description" content={$t('wellness.meta_description')} />
</svelte:head>

<!-- ═══════════════════ HERO ═══════════════════ -->
<header class="relative h-[85vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div
        class="absolute inset-0 scale-110"
        style="transform: translateY({scrollY * 0.25}px) scale(1.1);"
    >
        <img src="/imgs/massaggi-ingresso.webp" class="h-full w-full object-cover opacity-55" alt={$t('wellness.meta_description')} />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/30 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-28 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            {$t('wellness.main_subtitle')}
        </span>
        <h1 class="font-serif text-5xl md:text-8xl leading-tight font-light text-white fade-up-element">
            {$t('wellness.main_title')}
        </h1>
        <p class="mt-6 text-white/50 text-sm font-light max-w-md fade-up-element">
            {$t('wellness.hero_description')}
        </p>
    </div>
</header>

<!-- ═══════════════════ INTRO ═══════════════════ -->
<section class="bg-alpine-bg px-6 py-28">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <Sparkles class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            {$t('wellness.philosophy_title')}
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            {$t('wellness.philosophy_text')}
        </p>
    </div>
</section>

<!-- ═══════════════════ LA FILOSOFIA ═══════════════════ -->
<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
        <img src="/imgs/sauna-hds.webp" alt="Sauna at Chalet du Soleil" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
    </div>

    <div class="fade-up-element">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">{$t('wellness.philosophy_label')}</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">{@html $t('wellness.philosophy_heading')}</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            {$t('wellness.philosophy_p1')}
        </p>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
            {$t('wellness.philosophy_p2')}
        </p>
        <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
            <div class="flex items-center gap-3">
                <Leaf class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('wellness.natural_oils')}</span>
            </div>
            <div class="flex items-center gap-3">
                <ShieldCheck class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('wellness.certified_therapists')}</span>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ STATS ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-20 px-6">
    <div class="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-12 text-center">
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">6</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">{$t('wellness.stat_massage_types')}</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">3</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">{$t('wellness.stat_spa_rooms')}</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">32°C</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">{$t('wellness.stat_pool')}</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">7/7</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">{$t('wellness.stat_days')}</p>
        </div>
    </div>
</section>

<!-- ═══════════════════ I MASSAGGI ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">{$t('wellness.massages_title')}</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">{$t('wellness.massages_subtitle')}</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12">
            <!-- LING -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Waves class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">{$t('wellness.m_ling_type')}</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('wellness.m_ling_name')}</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">1 hr · €50</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        {$t('wellness.m_ling_desc')}
                    </p>
                    <div class="pt-6 border-t border-alpine-border">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">{$t('wellness.best_for')}</p>
                        <p class="text-xs text-alpine-text mt-2 font-light">{$t('wellness.m_ling_for')}</p>
                    </div>
                </div>
            </div>

            <!-- ANTICELLULITE -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Droplets class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">{$t('wellness.m_anti_type')}</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('wellness.m_anti_name')}</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">1 hr · €55</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        {$t('wellness.m_anti_desc')}
                    </p>
                    <div class="pt-6 border-t border-alpine-border">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">{$t('wellness.best_for')}</p>
                        <p class="text-xs text-alpine-text mt-2 font-light">{$t('wellness.m_anti_for')}</p>
                    </div>
                </div>
            </div>

            <!-- SPORTIVO -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Flame class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">{$t('wellness.m_sport_type')}</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('wellness.m_sport_name')}</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">1 hr · €50 · 30 min · €30</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        {$t('wellness.m_sport_desc')}
                    </p>
                    <div class="pt-6 border-t border-alpine-border">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">{$t('wellness.best_for')}</p>
                        <p class="text-xs text-alpine-text mt-2 font-light">{$t('wellness.m_sport_for')}</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Seconda riga -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12 mt-8 lg:mt-12">
            <!-- RIFLESSOLOGIA PLANTARE -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Footprints class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">{$t('wellness.m_reflex_type')}</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('wellness.m_reflex_name')}</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">30 min · €30 · 1 hr · €45</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        {$t('wellness.m_reflex_desc')}
                    </p>
                    <div class="pt-6 border-t border-alpine-border">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">{$t('wellness.best_for')}</p>
                        <p class="text-xs text-alpine-text mt-2 font-light">{$t('wellness.m_reflex_for')}</p>
                    </div>
                </div>
            </div>

            <!-- KOBIDO -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Sparkles class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">{$t('wellness.m_kobido_type')}</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('wellness.m_kobido_name')}</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">30 min · €30 · 1 hr · €50</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        {$t('wellness.m_kobido_desc')}
                    </p>
                    <div class="pt-6 border-t border-alpine-border">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">{$t('wellness.best_for')}</p>
                        <p class="text-xs text-alpine-text mt-2 font-light">{$t('wellness.m_kobido_for')}</p>
                    </div>
                </div>
            </div>

            <!-- TERRA & CIELO -->
            <div class="fade-up-element group border-2 border-alpine-gold bg-white shadow-xl hover:shadow-2xl transition-all duration-500 relative">
                <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-alpine-gold text-white px-5 py-1.5 text-[10px] uppercase tracking-[0.3em] font-bold">
                    {$t('wellness.m_terra_badge')}
                </div>
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Star class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">{$t('wellness.m_terra_type')}</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('wellness.m_terra_name')}</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">1 hr · €55</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        {$t('wellness.m_terra_desc')}
                    </p>
                    <div class="pt-6 border-t border-alpine-gold/30">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold">{$t('wellness.m_terra_includes_label')}</p>
                        <p class="text-xs text-alpine-text mt-2 font-light">{$t('wellness.m_terra_includes')}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!--         </div>
    </div>
</section>

<!-- ═══════════════════ L'ESPERIENZA ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
        <div class="fade-up-element">
            <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">{$t('wellness.ritual_label')}</span>
            <h2 class="font-serif text-4xl text-alpine-text mb-6">{@html $t('wellness.ritual_heading')}</h2>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
                {$t('wellness.ritual_desc')}
            </p>
            <div class="space-y-6">
                <div class="flex items-start gap-4">
                    <div class="w-8 h-8 rounded-full border border-alpine-gold flex items-center justify-center shrink-0 mt-0.5">
                        <span class="text-xs font-serif text-alpine-gold">1</span>
                    </div>
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">{$t('wellness.ritual_step1')}</p>
                        <p class="text-xs text-alpine-muted font-light">{$t('wellness.ritual_step1_desc')}</p>
                    </div>
                </div>
                <div class="flex items-start gap-4">
                    <div class="w-8 h-8 rounded-full border border-alpine-gold flex items-center justify-center shrink-0 mt-0.5">
                        <span class="text-xs font-serif text-alpine-gold">2</span>
                    </div>
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">{$t('wellness.ritual_step2')}</p>
                        <p class="text-xs text-alpine-muted font-light">{$t('wellness.ritual_step2_desc')}</p>
                    </div>
                </div>
                <div class="flex items-start gap-4">
                    <div class="w-8 h-8 rounded-full border border-alpine-gold flex items-center justify-center shrink-0 mt-0.5">
                        <span class="text-xs font-serif text-alpine-gold">3</span>
                    </div>
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">{$t('wellness.ritual_step3')}</p>
                        <p class="text-xs text-alpine-muted font-light">{$t('wellness.ritual_step3_desc')}</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
            <img src="/imgs/piscina.webp" alt={$t('wellness.area_pool')} class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
        </div>
    </div>
</section>

<!-- ═══════════════════ GLI OLI ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-5xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">{$t('wellness.oils_title')}</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">{$t('wellness.oils_subtitle')}</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="fade-up-element text-center p-10 bg-white border border-alpine-border">
                <Leaf class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('wellness.oil_arnica_name')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('wellness.oil_arnica_desc')}
                </p>
            </div>
            <div class="fade-up-element text-center p-10 bg-white border border-alpine-border">
                <Droplets class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('wellness.oil_pine_name')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('wellness.oil_pine_desc')}
                </p>
            </div>
            <div class="fade-up-element text-center p-10 bg-white border border-alpine-border">
                <Star class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('wellness.oil_juniper_name')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('wellness.oil_juniper_desc')}
                </p>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ DIVIDER: PRIVATE SPA ═══════════════════ -->
<section class="bg-[#0a0a0a] py-28 px-6">
    <div class="max-w-3xl mx-auto text-center fade-up-element">
        <Moon class="w-10 h-10 text-alpine-gold mx-auto mb-8" />
        <h2 class="font-serif text-4xl md:text-5xl text-white mb-6 leading-tight">{$t('wellness.spa_title')}</h2>
        <p class="text-white/50 text-sm font-light leading-relaxed max-w-lg mx-auto">
            {$t('wellness.spa_divider')}
        </p>
    </div>
</section>

<!-- ═══════════════════ L'AREA ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
        <img src="/imgs/jacuzzi-spa-hds-2026.webp" alt={$t('wellness.area_hydro')} class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
    </div>

    <div class="fade-up-element">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">{$t('wellness.area_label')}</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">{@html $t('wellness.area_heading')}</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
            {$t('wellness.area_desc')}
        </p>
        <div class="space-y-4">
            <div class="flex items-start gap-4 p-4 border border-alpine-border bg-white">
                <Droplets class="w-5 h-5 text-alpine-gold shrink-0 mt-0.5" />
                <div>
                    <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">{$t('wellness.area_hydro')}</p>
                    <p class="text-xs text-alpine-muted font-light">{$t('wellness.area_hydro_desc')}</p>
                </div>
            </div>
            <div class="flex items-start gap-4 p-4 border border-alpine-border bg-white">
                <Flame class="w-5 h-5 text-alpine-gold shrink-0 mt-0.5" />
                <div>
                    <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">{$t('wellness.area_sauna')}</p>
                    <p class="text-xs text-alpine-muted font-light">{$t('wellness.area_sauna_desc')}</p>
                </div>
            </div>
            <div class="flex items-start gap-4 p-4 border border-alpine-border bg-white">
                <Sparkles class="w-5 h-5 text-alpine-gold shrink-0 mt-0.5" />
                <div>
                    <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">{$t('wellness.area_pool')}</p>
                    <p class="text-xs text-alpine-muted font-light">{$t('wellness.area_pool_desc')}</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ I PACCHETTI ═══════════════════ -->
<section class="bg-alpine-bg pb-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">{$t('wellness.pkg_title')}</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">{$t('wellness.pkg_subtitle')}</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12">
            <!-- Coppia -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Heart class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">{$t('wellness.pkg_romantic_type')}</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('wellness.pkg_romantic_name')}</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-6">{$t('wellness.pkg_romantic_pricing')}</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        {$t('wellness.pkg_romantic_desc')}
                    </p>
                    <div class="pt-6 border-t border-alpine-border space-y-3">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-3">{$t('wellness.includes')}</p>
                        <div class="flex items-center gap-2">
                            <Wine class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">{$t('wellness.pkg_romantic_wine')}</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Gem class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">{$t('wellness.pkg_romantic_fruit')}</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Sparkles class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">{$t('wellness.pkg_romantic_robes')}</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Music class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">{$t('wellness.pkg_music')}</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Piccolo Gruppo -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Users class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">{$t('wellness.pkg_group_type')}</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('wellness.pkg_group_name')}</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-6">{$t('wellness.pkg_group_pricing')}</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        {$t('wellness.pkg_group_desc')}
                    </p>
                    <div class="pt-6 border-t border-alpine-border space-y-3">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-3">{$t('wellness.includes')}</p>
                        <div class="flex items-center gap-2">
                            <Wine class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">{$t('wellness.pkg_group_wine')}</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Gem class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">{$t('wellness.pkg_group_food')}</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Sparkles class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">{$t('wellness.pkg_group_robes')}</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Music class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">Music selection of your choice</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- BY NIGHT — PREMIUM -->
            <div class="fade-up-element group border-2 border-alpine-gold bg-white shadow-xl hover:shadow-2xl transition-all duration-500 relative">
                <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-alpine-gold text-white px-5 py-1.5 text-[10px] uppercase tracking-[0.3em] font-bold">
                    {$t('wellness.pkg_night_badge')}
                </div>
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Moon class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">{$t('wellness.pkg_night_type')}</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('wellness.pkg_night_name')}</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-6">{$t('wellness.pkg_night_pricing')}</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        {$t('wellness.pkg_night_desc')}
                    </p>
                    <div class="pt-6 border-t border-alpine-gold/30 space-y-3">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-3">{$t('wellness.pkg_night_includes')}</p>
                        <div class="flex items-center gap-2">
                            <Wine class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">{$t('wellness.pkg_night_champagne')}</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Gem class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">{$t('wellness.pkg_night_gourmet')}</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Star class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">{$t('wellness.pkg_night_candles')}</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Sparkles class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">{$t('wellness.pkg_night_beauty')}</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Music class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">{$t('wellness.pkg_night_playlist')}</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Clock class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">{$t('wellness.pkg_night_hours')}</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ L'ATMOSFERA NOTTURNA ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
        <div class="fade-up-element">
            <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">{$t('wellness.pkg_night_label')}</span>
            <h2 class="font-serif text-4xl text-alpine-text mb-6">{$t('wellness.night_heading')}</h2>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
                {$t('wellness.night_p1')}
            </p>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
                {$t('wellness.night_p2')}
            </p>
            <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
                <div class="flex items-center gap-3">
                    <Moon class="w-5 h-5 text-alpine-gold shrink-0" />
                    <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">21:00 – 00:00</span>
                </div>
                <div class="flex items-center gap-3">
                    <Lock class="w-5 h-5 text-alpine-gold shrink-0" />
                    <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('wellness.night_private')}</span>
                </div>
            </div>
        </div>

        <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
            <img src="/imgs/sauna-hds.webp" alt="Private SPA Sauna" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-85" />
        </div>
    </div>
</section>

<!-- ═══════════════════ OGNI DETTAGLIO CONTA ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-5xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">{$t('wellness.detail_title')}</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">{$t('wellness.detail_subtitle')}</p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
            <div class="fade-up-element text-center p-8 bg-white border border-alpine-border">
                <Wine class="w-8 h-8 text-alpine-gold mx-auto mb-5" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('wellness.detail_wine')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('wellness.detail_wine_desc')}
                </p>
            </div>
            <div class="fade-up-element text-center p-8 bg-white border border-alpine-border">
                <Gem class="w-8 h-8 text-alpine-gold mx-auto mb-5" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('wellness.detail_tasting')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('wellness.detail_tasting_desc')}
                </p>
            </div>
            <div class="fade-up-element text-center p-8 bg-white border border-alpine-border">
                <Sparkles class="w-8 h-8 text-alpine-gold mx-auto mb-5" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('wellness.detail_comfort')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('wellness.detail_comfort_desc')}
                </p>
            </div>
            <div class="fade-up-element text-center p-8 bg-white border border-alpine-border">
                <Lock class="w-8 h-8 text-alpine-gold mx-auto mb-5" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('wellness.detail_privacy')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('wellness.detail_privacy_desc')}
                </p>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ OCCASIONI SPECIALI ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
        <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl order-2 md:order-1">
            <img src="/imgs/jacuzzi-spa-hds-2026.webp" alt="Private SPA for special occasions" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
        </div>

        <div class="fade-up-element order-1 md:order-2">
            <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">{$t('wellness.occasions_label')}</span>
            <h2 class="font-serif text-4xl text-alpine-text mb-6">{$t('wellness.occasions_title')}</h2>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
                {$t('wellness.occasions_desc')}
            </p>
            <div class="space-y-5">
                <div class="flex items-start gap-4">
                    <Heart class="w-5 h-5 text-alpine-gold shrink-0 mt-0.5" />
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">{$t('wellness.occasions_anniversary')}</p>
                        <p class="text-xs text-alpine-muted font-light">{$t('wellness.occasions_anniversary_desc')}</p>
                    </div>
                </div>
                <div class="flex items-start gap-4">
                    <Star class="w-5 h-5 text-alpine-gold shrink-0 mt-0.5" />
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">{$t('wellness.occasions_birthday')}</p>
                        <p class="text-xs text-alpine-muted font-light">{$t('wellness.occasions_birthday_desc')}</p>
                    </div>
                </div>
                <div class="flex items-start gap-4">
                    <Users class="w-5 h-5 text-alpine-gold shrink-0 mt-0.5" />
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">{$t('wellness.occasions_team')}</p>
                        <p class="text-xs text-alpine-muted font-light">{$t('wellness.occasions_team_desc')}</p>
                    </div>
                </div>
            </div>
            <p class="mt-8 text-[10px] uppercase tracking-widest text-alpine-muted font-bold">
                {$t('wellness.occasions_footer')}
            </p>
        </div>
    </div>
</section>

<!-- ═══════════════════ INFO PRATICHE ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-5xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">{$t('wellness.info_title')}</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">{$t('wellness.info_subtitle')}</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <!-- Massaggi -->
            <div class="fade-up-element bg-white p-10 border border-alpine-border">
                <h4 class="font-serif text-xl text-alpine-text mb-6 flex items-center gap-3">
                    <Clock class="w-5 h-5 text-alpine-gold" />
                    {$t('wellness.info_massages')}
                </h4>
                <div class="space-y-4 text-sm text-alpine-muted font-light">
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('wellness.info_availability')}</span>
                        <span class="font-bold text-alpine-text">{$t('wellness.info_everyday')}</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('wellness.info_timeslot')}</span>
                        <span class="font-bold text-alpine-text">10:00 – 20:00</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('wellness.info_booking')}</span>
                        <span class="font-bold text-alpine-text">{$t('wellness.info_at_reception')}</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('wellness.info_notice')}</span>
                        <span class="font-bold text-alpine-text">{$t('wellness.info_day_before')}</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('wellness.info_cancellation')}</span>
                        <span class="font-bold text-alpine-text">{$t('wellness.info_free_6h')}</span>
                    </div>
                    <div class="flex justify-between items-center">
                        <span>{$t('wellness.info_packages')}</span>
                        <span class="font-bold text-alpine-text">{$t('wellness.info_3sessions')}</span>
                    </div>
                </div>
            </div>

            <!-- Private SPA -->
            <div class="fade-up-element bg-white p-10 border border-alpine-border">
                <h4 class="font-serif text-xl text-alpine-text mb-6 flex items-center gap-3">
                    <Lock class="w-5 h-5 text-alpine-gold" />
                    {$t('wellness.info_private_spa')}
                </h4>
                <div class="space-y-4 text-sm text-alpine-muted font-light">
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('wellness.info_daytime')}</span>
                        <span class="font-bold text-alpine-text">10–12 / 14–16 / 17–19</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('wellness.info_bynight')}</span>
                        <span class="font-bold text-alpine-text">21:00 – 00:00</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('wellness.info_min_notice')}</span>
                        <span class="font-bold text-alpine-text">{$t('wellness.info_24h')}</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('wellness.info_cancellation')}</span>
                        <span class="font-bold text-alpine-text">{$t('wellness.info_free_24h')}</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('wellness.info_addon')}</span>
                        <span class="font-bold text-alpine-text">{$t('wellness.info_combinable')}</span>
                    </div>
                    <div class="flex justify-between items-center">
                        <span>{$t('wellness.info_giftcard')}</span>
                        <span class="font-bold text-alpine-text">{$t('wellness.info_giftcard_value')}</span>
                    </div>
                </div>
            </div>
        </div>

        <div class="fade-up-element mt-8 bg-white p-10 border border-alpine-border">
            <h4 class="font-serif text-xl text-alpine-text mb-6 flex items-center gap-3">
                <ShieldCheck class="w-5 h-5 text-alpine-gold" />
                {$t('wellness.good_to_know')}
            </h4>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-x-12 gap-y-4 text-sm text-alpine-muted font-light">
                <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                    <span>{$t('wellness.gtk_bathrobe')}</span>
                    <span class="font-bold text-alpine-text">{$t('wellness.gtk_bathrobe_val')}</span>
                </div>
                <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                    <span>{$t('wellness.gtk_swimsuit')}</span>
                    <span class="font-bold text-alpine-text">{$t('wellness.gtk_swimsuit_val')}</span>
                </div>
                <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                    <span>{$t('wellness.gtk_arrival')}</span>
                    <span class="font-bold text-alpine-text">{$t('wellness.gtk_arrival_val')}</span>
                </div>
                <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                    <span>{$t('wellness.gtk_minage')}</span>
                    <span class="font-bold text-alpine-text">{$t('wellness.gtk_minage_val')}</span>
                </div>
                <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                    <span>{$t('wellness.gtk_maxguests')}</span>
                    <span class="font-bold text-alpine-text">{$t('wellness.gtk_maxguests_val')}</span>
                </div>
                <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                    <span>{$t('wellness.info_booking')}</span>
                    <span class="font-bold text-alpine-text">{$t('wellness.info_at_reception')}</span>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ RIEPILOGO PREZZI ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-20 px-6">
    <div class="max-w-4xl mx-auto">
        <div class="fade-up-element text-center mb-12">
            <h3 class="font-serif text-3xl text-alpine-text">{$t('wellness.price_title')}</h3>
        </div>
        <div class="fade-up-element border border-alpine-border divide-y divide-alpine-border">
            <div class="grid grid-cols-4 p-5 bg-alpine-bg">
                <span class="text-[10px] uppercase tracking-widest font-bold text-alpine-text">{$t('wellness.price_col_treatment')}</span>
                <span class="text-[10px] uppercase tracking-widest font-bold text-alpine-text text-center">{$t('wellness.price_col_guests')}</span>
                <span class="text-[10px] uppercase tracking-widest font-bold text-alpine-text text-center">{$t('wellness.price_col_duration')}</span>
                <span class="text-[10px] uppercase tracking-widest font-bold text-alpine-text text-right">{$t('wellness.price_col_price')}</span>
            </div>
            <!-- Massaggi -->
            <div class="grid grid-cols-4 p-5 items-center">
                <p class="font-serif text-sm text-alpine-text">{$t('wellness.m_ling_name')}</p>
                <p class="text-sm text-alpine-muted font-light text-center">1</p>
                <p class="text-sm text-alpine-muted font-light text-center">{$t('wellness.price_1h')}</p>
                <p class="text-sm font-bold text-alpine-text text-right">€50</p>
            </div>
            <div class="grid grid-cols-4 p-5 items-center bg-alpine-bg/50">
                <p class="font-serif text-sm text-alpine-text">{$t('wellness.m_anti_name')}</p>
                <p class="text-sm text-alpine-muted font-light text-center">1</p>
                <p class="text-sm text-alpine-muted font-light text-center">{$t('wellness.price_1h')}</p>
                <p class="text-sm font-bold text-alpine-text text-right">€55</p>
            </div>
            <div class="grid grid-cols-4 p-5 items-center">
                <p class="font-serif text-sm text-alpine-text">{$t('wellness.m_sport_name')}</p>
                <p class="text-sm text-alpine-muted font-light text-center">1</p>
                <p class="text-sm text-alpine-muted font-light text-center">{$t('wellness.price_1h_30min')}</p>
                <p class="text-sm font-bold text-alpine-text text-right">€50 / €30</p>
            </div>
            <div class="grid grid-cols-4 p-5 items-center bg-alpine-bg/50">
                <p class="font-serif text-sm text-alpine-text">{$t('wellness.m_reflex_name')}</p>
                <p class="text-sm text-alpine-muted font-light text-center">1</p>
                <p class="text-sm text-alpine-muted font-light text-center">{$t('wellness.price_30min_1h')}</p>
                <p class="text-sm font-bold text-alpine-text text-right">€30 / €45</p>
            </div>
            <div class="grid grid-cols-4 p-5 items-center">
                <p class="font-serif text-sm text-alpine-text">{$t('wellness.m_kobido_name')}</p>
                <p class="text-sm text-alpine-muted font-light text-center">1</p>
                <p class="text-sm text-alpine-muted font-light text-center">{$t('wellness.price_30min_1h')}</p>
                <p class="text-sm font-bold text-alpine-text text-right">€30 / €50</p>
            </div>
            <div class="grid grid-cols-4 p-5 items-center bg-alpine-bg/50 border-l-4 border-l-alpine-gold">
                <div>
                    <p class="font-serif text-sm text-alpine-text">{$t('wellness.m_terra_name')}</p>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mt-1">{$t('wellness.price_ritual')}</p>
                </div>
                <p class="text-sm text-alpine-muted font-light text-center">1</p>
                <p class="text-sm text-alpine-muted font-light text-center">{$t('wellness.price_1h')}</p>
                <p class="text-sm font-bold text-alpine-gold text-right">€55</p>
            </div>
            <!-- Divider -->
            <div class="grid grid-cols-4 p-4 bg-alpine-bg">
                <span class="text-[10px] uppercase tracking-widest font-bold text-alpine-gold col-span-4">{$t('wellness.spa_title')}</span>
            </div>
            <div class="grid grid-cols-4 p-5 items-center">
                <p class="font-serif text-sm text-alpine-text">{$t('wellness.pkg_romantic_name')}</p>
                <p class="text-sm text-alpine-muted font-light text-center">2</p>
                <p class="text-sm text-alpine-muted font-light text-center">{$t('wellness.price_2h')}</p>
                <p class="text-sm font-bold text-alpine-text text-right">€180</p>
            </div>
            <div class="grid grid-cols-4 p-5 items-center bg-alpine-bg/50">
                <p class="font-serif text-sm text-alpine-text">{$t('wellness.pkg_group_name')}</p>
                <p class="text-sm text-alpine-muted font-light text-center">3–6</p>
                <p class="text-sm text-alpine-muted font-light text-center">{$t('wellness.price_2h')}</p>
                <p class="text-sm font-bold text-alpine-text text-right">€280</p>
            </div>
            <div class="grid grid-cols-4 p-5 items-center border-l-4 border-l-alpine-gold">
                <div>
                    <p class="font-serif text-sm text-alpine-text">{$t('wellness.pkg_night_name')}</p>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mt-1">{$t('wellness.pkg_night_type')}</p>
                </div>
                <p class="text-sm text-alpine-muted font-light text-center">2–4</p>
                <p class="text-sm text-alpine-muted font-light text-center">{$t('wellness.price_3h')}</p>
                <p class="text-sm font-bold text-alpine-gold text-right">€380</p>
            </div>
        </div>
        <p class="text-center text-[10px] uppercase tracking-widest text-alpine-muted font-bold mt-6">
            {$t('wellness.price_footer')}
        </p>
    </div>
</section>

<!-- ═══════════════════ CTA ═══════════════════ -->
<section class="bg-[#0a0a0a] py-32 px-6">
    <div class="max-w-3xl mx-auto text-center">
        <div class="fade-up-element">
            <h2 class="font-serif text-4xl text-white mb-6">{$t('wellness.cta_title')}</h2>
            <p class="text-white/50 text-sm font-light leading-relaxed max-w-lg mx-auto mb-12">
                {$t('wellness.cta_desc')}
            </p>
            <a href="mailto:info@hoteldusoleiltorgnon.com" class="inline-flex items-center justify-center gap-3 bg-white text-alpine-text px-10 py-4 text-[11px] tracking-[0.2em] uppercase font-bold hover:bg-alpine-gold hover:text-white transition-all duration-300">
                {$t('wellness.cta_button')} <ArrowRight class="w-4 h-4" />
            </a>
        </div>
    </div>
</section>
