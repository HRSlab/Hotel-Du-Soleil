<script lang="ts">
    import { Moon, Snowflake, Sparkles, Map, Mountain, Clock, Users, ShieldCheck, TreePine, Utensils, Sun, Star, Footprints, Lamp } from 'lucide-svelte';
    import { t } from '$lib/i18n';

    let scrollY = $state(0);
</script>

<svelte:window bind:scrollY />

<svelte:head>
    <title>{$t('ciaspolate_page.meta_title')}</title>
    <meta name="description" content={$t('ciaspolate_page.meta_description')} />
</svelte:head>

<!-- ═══════════════════ HERO ═══════════════════ -->
<header class="relative h-[85vh] w-full overflow-hidden bg-[#0a0a0a]">
    <div
        class="absolute inset-0 scale-110"
        style="transform: translateY({scrollY * 0.25}px) scale(1.1);"
    >
        <img src="/imgs/hotel_by_night.jpg" class="h-full w-full object-cover opacity-50" alt="Ciaspolata notturna nei boschi innevati" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/30 to-[#0a0a0a]"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-28 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            {$t('ciaspolate_page.hero_label')}
        </span>
        <h1 class="font-serif text-5xl md:text-8xl leading-tight font-light text-white fade-up-element">
            {$t('ciaspolate_page.hero_title')}
        </h1>
        <p class="mt-6 text-white/50 text-sm font-light max-w-md fade-up-element">
            {$t('ciaspolate_page.hero_subtitle')}
        </p>
    </div>
</header>

<!-- ═══════════════════ INTRO ═══════════════════ -->
<section class="bg-[#0a0a0a] text-white px-6 py-28">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <Moon class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-white md:text-4xl italic">
            "{$t('ciaspolate_page.intro_quote')}"
        </h3>
        <p class="text-white/60 leading-relaxed font-light text-sm md:text-base border-t border-white/10 pt-12 mt-12 mx-auto max-w-xl">
            {$t('ciaspolate_page.intro_text')}
        </p>
    </div>
</section>

<!-- ═══════════════════ L’ESPERIENZA ═══════════════════ -->
<section class="bg-[#0a0a0a] pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element overflow-hidden shadow-xl border border-white/10">
        <img src="/imgs/hotel_by_night.jpg" alt="Escursione con racchette da neve al tramonto" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-75">
    </div>
    <div class="fade-up-element">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">{$t('ciaspolate_page.experience_label')}</span>
        <h2 class="font-serif text-4xl text-white mb-6">{$t('ciaspolate_page.experience_title')}</h2>
        <p class="text-white/60 text-sm font-light leading-relaxed mb-6">
            {$t('ciaspolate_page.experience_text1')}
        </p>
        <p class="text-white/60 text-sm font-light leading-relaxed mb-8">
            {$t('ciaspolate_page.experience_text2')}
        </p>
        <div class="grid grid-cols-2 gap-6 pt-6 border-t border-white/10">
            <div class="flex items-center gap-3">
                <Lamp class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-white/80">{$t('ciaspolate_page.experience_badge_lamps')}</span>
            </div>
            <div class="flex items-center gap-3">
                <ShieldCheck class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-white/80">{$t('ciaspolate_page.experience_badge_guides')}</span>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ 3 HIGHLIGHTS ═══════════════════ -->
<section class="bg-[#0a0a0a] pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
    <div class="bg-white/5 border border-white/10 p-12 fade-up-element">
        <Snowflake class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-1" />
        <h4 class="font-serif text-xl text-white mb-4">{$t('ciaspolate_page.highlight_trail_title')}</h4>
        <p class="text-xs text-white/50 font-light leading-relaxed">{$t('ciaspolate_page.highlight_trail_text')}</p>
    </div>
    <div class="bg-white/5 border border-white/10 p-12 fade-up-element">
        <Utensils class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-1" />
        <h4 class="font-serif text-xl text-white mb-4">{$t('ciaspolate_page.highlight_dinner_title')}</h4>
        <p class="text-xs text-white/50 font-light leading-relaxed">{$t('ciaspolate_page.highlight_dinner_text')}</p>
    </div>
    <div class="bg-white/5 border border-white/10 p-12 fade-up-element">
        <Sparkles class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-1" />
        <h4 class="font-serif text-xl text-white mb-4">{$t('ciaspolate_page.highlight_return_title')}</h4>
        <p class="text-xs text-white/50 font-light leading-relaxed">{$t('ciaspolate_page.highlight_return_text')}</p>
    </div>
</section>

<!-- ═══════════════════ STATS STRIP ═══════════════════ -->
<section class="border-y border-white/10 bg-[#111] py-20 px-6">
    <div class="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-12 text-center">
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-white mb-2">3h</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-white/40 font-bold">{$t('ciaspolate_page.stats_duration')}</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-white mb-2">300m</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-white/40 font-bold">{$t('ciaspolate_page.stats_elevation')}</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-white mb-2">Dic–Mar</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-white/40 font-bold">{$t('ciaspolate_page.stats_season')}</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-white mb-2">4–15</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-white/40 font-bold">{$t('ciaspolate_page.stats_group')}</p>
        </div>
    </div>
</section>

<!-- ═══════════════════ I PERCORSI ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">{$t('ciaspolate_page.trails_title')}</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">{$t('ciaspolate_page.trails_subtitle')}</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12">
            <div class="fade-up-element text-center p-12 md:p-14 border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <TreePine class="w-8 h-8 text-alpine-gold mx-auto mb-8 stroke-1" />
                <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('ciaspolate_page.trail_easy_name')}</h4>
                <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-6">{$t('ciaspolate_page.trail_easy_level')}</p>
                <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed max-w-xs mx-auto">
                    {$t('ciaspolate_page.trail_easy_text')}
                </p>
            </div>
            <div class="fade-up-element text-center p-12 md:p-14 border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <Moon class="w-8 h-8 text-alpine-gold mx-auto mb-8 stroke-1" />
                <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('ciaspolate_page.trail_medium_name')}</h4>
                <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-6">{$t('ciaspolate_page.trail_medium_level')}</p>
                <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed max-w-xs mx-auto">
                    {$t('ciaspolate_page.trail_medium_text')}
                </p>
            </div>
            <div class="fade-up-element text-center p-12 md:p-14 border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <Mountain class="w-8 h-8 text-alpine-gold mx-auto mb-8 stroke-1" />
                <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('ciaspolate_page.trail_hard_name')}</h4>
                <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-6">{$t('ciaspolate_page.trail_hard_level')}</p>
                <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed max-w-xs mx-auto">
                    {$t('ciaspolate_page.trail_hard_text')}
                </p>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ LA CENA IN RIFUGIO ═══════════════════ -->
<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element order-2 md:order-1">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">{$t('ciaspolate_page.dinner_label')}</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">{$t('ciaspolate_page.dinner_title')}</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            {$t('ciaspolate_page.dinner_text1')}
        </p>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
            {$t('ciaspolate_page.dinner_text2')}
        </p>
        <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
            <div class="flex items-center gap-3">
                <Utensils class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('ciaspolate_page.dinner_badge_menu')}</span>
            </div>
            <div class="flex items-center gap-3">
                <Star class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('ciaspolate_page.dinner_badge_wine')}</span>
            </div>
        </div>
    </div>
    <div class="fade-up-element order-1 md:order-2 overflow-hidden bg-alpine-border shadow-xl">
        <img src="https://images.unsplash.com/photo-1414235077428-338989a2e8c0?q=80&w=1500&auto=format&fit=crop" alt="Cena in rifugio di montagna" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90">
    </div>
</section>

<!-- ═══════════════════ CIASPOLATE DIURNE ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-16 lg:gap-24 items-center">
        <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
            <img src="https://images.unsplash.com/photo-1551524559-8af4e6624178?q=80&w=1500&auto=format&fit=crop" alt="Ciaspolata diurna con vista sulle Alpi" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90">
        </div>
        <div class="fade-up-element">
            <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">{$t('ciaspolate_page.daytime_label')}</span>
            <h2 class="font-serif text-4xl text-alpine-text mb-6">{$t('ciaspolate_page.daytime_title')}</h2>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
                {$t('ciaspolate_page.daytime_text1')}
            </p>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
                {$t('ciaspolate_page.daytime_text2')}
            </p>
            <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
                <div class="flex items-center gap-3">
                    <Sun class="w-5 h-5 text-alpine-gold shrink-0" />
                    <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('ciaspolate_page.daytime_badge_departure')}</span>
                </div>
                <div class="flex items-center gap-3">
                    <Users class="w-5 h-5 text-alpine-gold shrink-0" />
                    <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('ciaspolate_page.daytime_badge_families')}</span>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ COSA INCLUDE ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">{$t('ciaspolate_page.includes_title')}</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">{$t('ciaspolate_page.includes_subtitle')}</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
            <div class="fade-up-element text-center p-10 border border-alpine-border bg-white">
                <Footprints class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-1" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('ciaspolate_page.includes_gear_title')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('ciaspolate_page.includes_gear_text')}
                </p>
            </div>
            <div class="fade-up-element text-center p-10 border border-alpine-border bg-white">
                <ShieldCheck class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-1" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('ciaspolate_page.includes_guide_title')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('ciaspolate_page.includes_guide_text')}
                </p>
            </div>
            <div class="fade-up-element text-center p-10 border border-alpine-border bg-white">
                <Utensils class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-1" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('ciaspolate_page.includes_dinner_title')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('ciaspolate_page.includes_dinner_text')}
                </p>
            </div>
            <div class="fade-up-element text-center p-10 border border-alpine-border bg-white">
                <Clock class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-1" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('ciaspolate_page.includes_flex_title')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('ciaspolate_page.includes_flex_text')}
                </p>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ INFO PRATICHE ═══════════════════ -->
<section class="bg-[#0a0a0a] py-32 px-6">
    <div class="max-w-4xl mx-auto">
        <div class="fade-up-element text-center mb-16">
            <h2 class="font-serif text-4xl text-white mb-5">{$t('ciaspolate_page.info_title')}</h2>
        </div>

        <div class="fade-up-element grid grid-cols-1 md:grid-cols-2 gap-12">
            <div>
                <h4 class="font-serif text-lg text-white mb-4 flex items-center gap-3">
                    <Moon class="w-5 h-5 text-alpine-gold" /> {$t('ciaspolate_page.info_night_title')}
                </h4>
                <ul class="space-y-3 text-white/50 text-sm font-light">
                    {#each $t('ciaspolate_page.info_night_items') as item}
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">•</span> {item}</li>
                    {/each}
                </ul>
            </div>
            <div>
                <h4 class="font-serif text-lg text-white mb-4 flex items-center gap-3">
                    <Sun class="w-5 h-5 text-alpine-gold" /> {$t('ciaspolate_page.info_day_title')}
                </h4>
                <ul class="space-y-3 text-white/50 text-sm font-light">
                    {#each $t('ciaspolate_page.info_day_items') as item}
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">•</span> {item}</li>
                    {/each}
                </ul>
            </div>
        </div>

        <div class="fade-up-element mt-16 pt-12 border-t border-white/10 text-center">
            <p class="text-white/40 text-xs font-light leading-relaxed max-w-xl mx-auto">
                {$t('ciaspolate_page.info_disclaimer')}
            </p>
        </div>
    </div>
</section>
