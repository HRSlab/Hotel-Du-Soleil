<script lang="ts">
    import { t } from '$lib/i18n';
    import { Utensils, Moon, Flower2, Compass, ArrowRight, Mountain, Snowflake, Wind, MapPin } from 'lucide-svelte';

    let scrollY = $state(0);
</script>

<svelte:window bind:scrollY />

<svelte:head>
    <title>{$t('experiences.main_title')} | Chalet du Soleil</title>
    <meta name="description" content={$t('experiences.page_meta_description')} />
</svelte:head>

<!-- ═══════════════════ HERO ═══════════════════ -->
<header class="relative h-[85vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div
        class="absolute inset-0 scale-110"
        style="transform: translateY({scrollY * 0.25}px) scale(1.1);"
    >
        <img src="https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=2000&auto=format&fit=crop" class="h-full w-full object-cover opacity-55" alt="Panorama alpino Valle d'Aosta" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/30 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-28 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            {$t('experiences.main_subtitle')}
        </span>
        <h1 class="font-serif text-5xl md:text-8xl leading-tight font-light text-white fade-up-element">
            {$t('experiences.main_title')}
        </h1>
        <p class="mt-6 text-white/50 text-sm font-light max-w-md fade-up-element">
            {$t('experiences.page_hero_text')}
        </p>
    </div>
</header>

<!-- ═══════════════════ INTRO ═══════════════════ -->
<section class="bg-alpine-bg px-6 py-28">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <Mountain class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            {$t('experiences.page_intro_title')}
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            {$t('experiences.page_intro_text')}
        </p>
    </div>
</section>

<!-- ═══════════════════ HIGHLIGHTS GRID ═══════════════════ -->
<section class="bg-alpine-bg pb-24 px-6">
    <div class="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
        <div class="fade-up-element">
            <div class="h-20 w-20 rounded-full border border-alpine-border bg-white flex items-center justify-center mx-auto mb-5">
                <Utensils class="w-7 h-7 text-alpine-gold" />
            </div>
            <h4 class="font-serif text-lg text-alpine-text mb-2">{$t('experiences.page_highlight_flavours')}</h4>
            <p class="text-xs text-alpine-muted font-light">{$t('experiences.page_highlight_flavours_text')}</p>
        </div>
        <div class="fade-up-element">
            <div class="h-20 w-20 rounded-full border border-alpine-border bg-white flex items-center justify-center mx-auto mb-5">
                <Moon class="w-7 h-7 text-alpine-gold" />
            </div>
            <h4 class="font-serif text-lg text-alpine-text mb-2">{$t('experiences.page_highlight_nights')}</h4>
            <p class="text-xs text-alpine-muted font-light">{$t('experiences.page_highlight_nights_text')}</p>
        </div>
        <div class="fade-up-element">
            <div class="h-20 w-20 rounded-full border border-alpine-border bg-white flex items-center justify-center mx-auto mb-5">
                <Flower2 class="w-7 h-7 text-alpine-gold" />
            </div>
            <h4 class="font-serif text-lg text-alpine-text mb-2">{$t('experiences.page_highlight_balance')}</h4>
            <p class="text-xs text-alpine-muted font-light">{$t('experiences.page_highlight_balance_text')}</p>
        </div>
        <div class="fade-up-element">
            <div class="h-20 w-20 rounded-full border border-alpine-border bg-white flex items-center justify-center mx-auto mb-5">
                <Compass class="w-7 h-7 text-alpine-gold" />
            </div>
            <h4 class="font-serif text-lg text-alpine-text mb-2">{$t('experiences.page_highlight_adventure')}</h4>
            <p class="text-xs text-alpine-muted font-light">{$t('experiences.page_highlight_adventure_text')}</p>
        </div>
    </div>
</section>

<!-- ═══════════════════ DEGUSTAZIONE ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
        <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
            <img src="https://images.unsplash.com/photo-1452195125355-903496c21e64?q=80&w=1500&auto=format&fit=crop" alt="Degustazione Fontina DOP" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
        </div>

        <div class="fade-up-element">
            <div class="flex items-center gap-3 mb-6">
                <Utensils class="w-5 h-5 text-alpine-gold" />
                <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold">{$t('experiences.degustazione.label')}</span>
            </div>
            <h2 class="font-serif text-4xl text-alpine-text mb-6">{$t('experiences.degustazione.title')}</h2>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
                {$t('experiences.degustazione.desc1')}
            </p>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
                {$t('experiences.degustazione.desc2')}
            </p>
            <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border mb-10">
                <div class="flex items-center gap-3">
                    <MapPin class="w-4 h-4 text-alpine-gold shrink-0" />
                    <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('experiences.degustazione.badge_distance')}</span>
                </div>
                <div class="flex items-center gap-3">
                    <Utensils class="w-4 h-4 text-alpine-gold shrink-0" />
                    <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('experiences.degustazione.badge_tastings')}</span>
                </div>
            </div>
            <a href="/esperienze/degustazione" class="inline-flex items-center gap-3 text-[11px] tracking-[0.2em] uppercase font-bold text-alpine-text hover:text-alpine-gold transition-colors duration-300">
                {$t('experiences.degustazione.cta')} <ArrowRight class="w-4 h-4" />
            </a>
        </div>
    </div>
</section>

<!-- ═══════════════════ CIASPOLATE ═══════════════════ -->
<section class="bg-[#0a0a0a] py-32 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
        <div class="fade-up-element order-2 md:order-1">
            <div class="flex items-center gap-3 mb-6">
                <Moon class="w-5 h-5 text-alpine-gold" />
                <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold">{$t('experiences.ciaspolate.label')}</span>
            </div>
            <h2 class="font-serif text-4xl text-white mb-6">{$t('experiences.ciaspolate.title')}</h2>
            <p class="text-white/60 text-sm font-light leading-relaxed mb-6">
                {$t('experiences.ciaspolate.desc1')}
            </p>
            <p class="text-white/60 text-sm font-light leading-relaxed mb-8">
                {$t('experiences.ciaspolate.desc2')}
            </p>
            <div class="grid grid-cols-2 gap-6 pt-6 border-t border-white/20 mb-10">
                <div class="flex items-center gap-3">
                    <Snowflake class="w-4 h-4 text-alpine-gold shrink-0" />
                    <span class="text-xs font-bold uppercase tracking-widest text-white/80">{$t('experiences.ciaspolate.badge_season')}</span>
                </div>
                <div class="flex items-center gap-3">
                    <Moon class="w-4 h-4 text-alpine-gold shrink-0" />
                    <span class="text-xs font-bold uppercase tracking-widest text-white/80">{$t('experiences.ciaspolate.badge_departure')}</span>
                </div>
            </div>
            <a href="/esperienze/ciaspolate" class="inline-flex items-center gap-3 text-[11px] tracking-[0.2em] uppercase font-bold text-white hover:text-alpine-gold transition-colors duration-300">
                {$t('experiences.ciaspolate.cta')} <ArrowRight class="w-4 h-4" />
            </a>
        </div>

        <div class="fade-up-element overflow-hidden shadow-xl order-1 md:order-2">
            <img src="https://images.unsplash.com/photo-1551524559-8af4e6624178?q=80&w=1500&auto=format&fit=crop" alt="Ciaspolata notturna nelle Alpi" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-85" />
        </div>
    </div>
</section>

<!-- ═══════════════════ YOGA ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
        <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
            <img src="https://images.unsplash.com/photo-1506126613408-eca07ce68773?q=80&w=1500&auto=format&fit=crop" alt="Yoga all'aperto con vista sulle Alpi" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
        </div>

        <div class="fade-up-element">
            <div class="flex items-center gap-3 mb-6">
                <Flower2 class="w-5 h-5 text-alpine-gold" />
                <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold">{$t('experiences.yoga.label')}</span>
            </div>
            <h2 class="font-serif text-4xl text-alpine-text mb-6">{$t('experiences.yoga.title')}</h2>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
                {$t('experiences.yoga.desc1')}
            </p>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
                {$t('experiences.yoga.desc2')}
            </p>
            <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border mb-10">
                <div class="flex items-center gap-3">
                    <Wind class="w-4 h-4 text-alpine-gold shrink-0" />
                    <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('experiences.yoga.badge_time')}</span>
                </div>
                <div class="flex items-center gap-3">
                    <Flower2 class="w-4 h-4 text-alpine-gold shrink-0" />
                    <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('experiences.yoga.badge_level')}</span>
                </div>
            </div>
            <a href="/esperienze/yoga" class="inline-flex items-center gap-3 text-[11px] tracking-[0.2em] uppercase font-bold text-alpine-text hover:text-alpine-gold transition-colors duration-300">
                {$t('experiences.yoga.cta')} <ArrowRight class="w-4 h-4" />
            </a>
        </div>
    </div>
</section>

<!-- ═══════════════════ GUIDE ALPINE ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
        <div class="fade-up-element order-2 md:order-1">
            <div class="flex items-center gap-3 mb-6">
                <Compass class="w-5 h-5 text-alpine-gold" />
                <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold">{$t('experiences.guide.label')}</span>
            </div>
            <h2 class="font-serif text-4xl text-alpine-text mb-6">{$t('experiences.guide.title')}</h2>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
                {$t('experiences.guide.desc1')}
            </p>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
                {$t('experiences.guide.desc2')}
            </p>
            <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border mb-10">
                <div class="flex items-center gap-3">
                    <Compass class="w-4 h-4 text-alpine-gold shrink-0" />
                    <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('experiences.guide.badge_certified')}</span>
                </div>
                <div class="flex items-center gap-3">
                    <Mountain class="w-4 h-4 text-alpine-gold shrink-0" />
                    <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('experiences.guide.badge_season')}</span>
                </div>
            </div>
            <a href="/esperienze/guide" class="inline-flex items-center gap-3 text-[11px] tracking-[0.2em] uppercase font-bold text-alpine-text hover:text-alpine-gold transition-colors duration-300">
                {$t('experiences.guide.cta')} <ArrowRight class="w-4 h-4" />
            </a>
        </div>

        <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl order-1 md:order-2">
            <img src="https://images.unsplash.com/photo-1522163182402-834f871fd851?q=80&w=1500&auto=format&fit=crop" alt="Guida alpina con gruppo in montagna" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
        </div>
    </div>
</section>

<!-- ═══════════════════ STAGIONI ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-20 px-6">
    <div class="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-12 text-center">
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">4</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">{$t('experiences.page_stats_unique')}</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">12</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">{$t('experiences.page_stats_months')}</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">1.500m</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">{$t('experiences.page_stats_altitude')}</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">∞</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">{$t('experiences.page_stats_memories')}</p>
        </div>
    </div>
</section>

<!-- ═══════════════════ GALLERY ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">{$t('experiences.page_gallery_title')}</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">{$t('experiences.page_gallery_subtitle')}</p>
        </div>

        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
            <a href="/esperienze/degustazione" class="fade-up-element group relative overflow-hidden aspect-square">
                <img src="https://images.unsplash.com/photo-1500595046743-cd271d694d30?q=80&w=800&auto=format&fit=crop" alt="Alpeggio" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 brightness-90" />
                <div class="absolute inset-0 bg-linear-to-t from-black/70 via-transparent to-transparent flex items-end p-5">
                    <div>
                        <p class="text-[10px] uppercase tracking-widest text-white/70 font-bold">{$t('experiences.page_gallery_tasting_season')}</p>
                        <p class="font-serif text-lg text-white">{$t('experiences.page_gallery_tasting_name')}</p>
                    </div>
                </div>
            </a>
            <a href="/esperienze/ciaspolate" class="fade-up-element group relative overflow-hidden aspect-square">
                <img src="https://images.unsplash.com/photo-1551524559-8af4e6624178?q=80&w=800&auto=format&fit=crop" alt="Ciaspolata" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 brightness-85" />
                <div class="absolute inset-0 bg-linear-to-t from-black/70 via-transparent to-transparent flex items-end p-5">
                    <div>
                        <p class="text-[10px] uppercase tracking-widest text-white/70 font-bold">{$t('experiences.page_gallery_snowshoe_season')}</p>
                        <p class="font-serif text-lg text-white">{$t('experiences.page_gallery_snowshoe_name')}</p>
                    </div>
                </div>
            </a>
            <a href="/esperienze/yoga" class="fade-up-element group relative overflow-hidden aspect-square">
                <img src="https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?q=80&w=800&auto=format&fit=crop" alt="Yoga in montagna" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 brightness-90" />
                <div class="absolute inset-0 bg-linear-to-t from-black/70 via-transparent to-transparent flex items-end p-5">
                    <div>
                        <p class="text-[10px] uppercase tracking-widest text-white/70 font-bold">{$t('experiences.page_gallery_yoga_season')}</p>
                        <p class="font-serif text-lg text-white">{$t('experiences.page_gallery_yoga_name')}</p>
                    </div>
                </div>
            </a>
            <a href="/esperienze/guide" class="fade-up-element group relative overflow-hidden aspect-square">
                <img src="https://images.unsplash.com/photo-1544450531-64d7fa39b400?q=80&w=800&auto=format&fit=crop" alt="Guide alpine" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 brightness-90" />
                <div class="absolute inset-0 bg-linear-to-t from-black/70 via-transparent to-transparent flex items-end p-5">
                    <div>
                        <p class="text-[10px] uppercase tracking-widest text-white/70 font-bold">{$t('experiences.page_gallery_guides_season')}</p>
                        <p class="font-serif text-lg text-white">{$t('experiences.page_gallery_guides_name')}</p>
                    </div>
                </div>
            </a>
        </div>
    </div>
</section>

<!-- ═══════════════════ CTA ═══════════════════ -->
<section class="bg-[#0a0a0a] py-32 px-6">
    <div class="max-w-3xl mx-auto text-center">
        <div class="fade-up-element">
            <h2 class="font-serif text-4xl text-white mb-6">{$t('experiences.page_cta_title')}</h2>
            <p class="text-white/50 text-sm font-light leading-relaxed max-w-lg mx-auto mb-12">
                {$t('experiences.page_cta_text')}
            </p>
            <a href="mailto:info@hoteldusoleiltorgnon.com" class="inline-flex items-center justify-center gap-3 bg-white text-alpine-text px-10 py-4 text-[11px] tracking-[0.2em] uppercase font-bold hover:bg-alpine-gold hover:text-white transition-all duration-300">
                {$t('experiences.page_cta_button')} <ArrowRight class="w-4 h-4" />
            </a>
        </div>
    </div>
</section>
