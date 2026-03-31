<script lang="ts">
    import { ShieldCheck, Mountain, Users, Star, Clock, MapPin, Compass, ArrowRight, Snowflake, Sun, TreePine, Wind, Heart, Flag, Award, Binoculars } from 'lucide-svelte';
    import { t, locale } from '$lib/i18n';

    let scrollY = $state(0);
</script>

<svelte:window bind:scrollY />

<svelte:head>
    <title>{$t('guide_page.meta_title')}</title>
    <meta name="description" content={$t('guide_page.meta_description')} />
</svelte:head>

<!-- ═══════════════════ HERO ═══════════════════ -->
<header class="relative h-[85vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div
        class="absolute inset-0 scale-110"
        style="transform: translateY({scrollY * 0.25}px) scale(1.1);"
    >
        <img src="/imgs/ski-sport-hero.webp" class="h-full w-full object-cover opacity-55" alt="Guida alpina in Valle d'Aosta" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/30 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-28 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            {$t('guide_page.hero_label')}
        </span>
        <h1 class="font-serif text-5xl md:text-8xl leading-tight font-light text-white fade-up-element">
            {$t('guide_page.hero_title')}
        </h1>
        <p class="mt-6 text-white/50 text-sm font-light max-w-md fade-up-element">
            {$t('guide_page.hero_subtitle')}
        </p>
    </div>
</header>

<!-- ═══════════════════ INTRO ═══════════════════ -->
<section class="bg-alpine-bg px-6 py-28">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <ShieldCheck class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            {$t('guide_page.intro_title')}
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            {$t('guide_page.intro_text')}
        </p>
    </div>
</section>

<!-- ═══════════════════ I NOSTRI PARTNER ═══════════════════ -->
<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
        <img src="/imgs/skiers-torgnon.webp" alt="Guida alpina con gruppo in montagna" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
    </div>

    <div class="fade-up-element">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">{$t('guide_page.partner_label')}</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">{$t('guide_page.partner_title')}</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            {$t('guide_page.partner_text1')}
        </p>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
            {$t('guide_page.partner_text2')}
        </p>
        <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
            <div class="flex items-center gap-3">
                <Award class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('guide_page.partner_badge_cert')}</span>
            </div>
            <div class="flex items-center gap-3">
                <MapPin class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('guide_page.partner_badge_local')}</span>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ STATS ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-20 px-6">
    <div class="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-12 text-center">
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">20+</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">{$t('guide_page.stats_experience')}</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">365</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">{$t('guide_page.stats_days')}</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">4.000m</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">{$t('guide_page.stats_altitude')}</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">8</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">{$t('guide_page.stats_group')}</p>
        </div>
    </div>
</section>

<!-- ═══════════════════ LE ESPERIENZE ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">{$t('guide_page.activities_title')}</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">{$t('guide_page.activities_subtitle')}</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12">
            <!-- Alpinismo -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="overflow-hidden aspect-3/2">
                    <img src="/imgs/slope-torgnon.webp" alt="Alpinismo in Valle d'Aosta" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
                </div>
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Mountain class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">{$t('guide_page.activity_alpinism_season')}</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('guide_page.activity_alpinism_name')}</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">{$t('guide_page.activity_alpinism_level')}</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed">
                        {$t('guide_page.activity_alpinism_text')}
                    </p>
                </div>
            </div>

            <!-- Freeride -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="overflow-hidden aspect-3/2">
                    <img src="/imgs/freeride-guide.jpg" alt="Sciatore freeride in neve fresca" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
                </div>
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Snowflake class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">{$t('guide_page.activity_freeride_season')}</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('guide_page.activity_freeride_name')}</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">{$t('guide_page.activity_freeride_level')}</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed">
                        {$t('guide_page.activity_freeride_text')}
                    </p>
                </div>
            </div>

            <!-- Trekking -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="overflow-hidden aspect-3/2">
                    <img src="/imgs/torgnon-view.webp" alt="Trekking guidato nelle Alpi" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
                </div>
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Sun class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">{$t('guide_page.activity_trekking_season')}</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('guide_page.activity_trekking_name')}</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">{$t('guide_page.activity_trekking_level')}</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed">
                        {$t('guide_page.activity_trekking_text')}
                    </p>
                </div>
            </div>
        </div>

        <!-- Seconda riga -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12 mt-8 lg:mt-12">
            <!-- Ciaspolate -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="overflow-hidden aspect-3/2">
                    <img src="/imgs/snowshoe-guide.jpg" alt="Escursione con ciaspole in montagna" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
                </div>
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <TreePine class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">{$t('guide_page.activity_snowshoe_season')}</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('guide_page.activity_snowshoe_name')}</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">{$t('guide_page.activity_snowshoe_level')}</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed">
                        {$t('guide_page.activity_snowshoe_text')}
                    </p>
                    <a href="/esperienze/ciaspolate" class="inline-flex items-center gap-2 text-[10px] uppercase tracking-[0.2em] font-bold text-alpine-text hover:text-alpine-gold transition-colors mt-6">
                        {$t('guide_page.activity_snowshoe_cta')} <ArrowRight class="w-3.5 h-3.5" />
                    </a>
                </div>
            </div>

            <!-- MTB -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="overflow-hidden aspect-3/2">
                    <img src="/imgs/mtb-torgnon-1.webp" alt="Mountain bike guidata" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
                </div>
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Compass class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">{$t('guide_page.activity_mtb_season')}</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('guide_page.activity_mtb_name')}</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">{$t('guide_page.activity_mtb_level')}</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed">
                        {$t('guide_page.activity_mtb_text')}
                    </p>
                    <a href={$locale === 'en' ? '/sport' : '/sport/bike'} class="inline-flex items-center gap-2 text-[10px] uppercase tracking-[0.2em] font-bold text-alpine-text hover:text-alpine-gold transition-colors mt-6">
                        {$t('guide_page.activity_mtb_cta')} <ArrowRight class="w-3.5 h-3.5" />
                    </a>
                </div>
            </div>

            <!-- Natura & Fauna -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="overflow-hidden aspect-3/2">
                    <img src="/imgs/nature-fauna-ibex.jpg" alt="Stambecco alpino in ambiente naturale" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
                </div>
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Binoculars class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">{$t('guide_page.activity_nature_season')}</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('guide_page.activity_nature_name')}</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">{$t('guide_page.activity_nature_level')}</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed">
                        {$t('guide_page.activity_nature_text')}
                    </p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ COME FUNZIONA ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-5xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">{$t('guide_page.howto_title')}</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">{$t('guide_page.howto_subtitle')}</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
            <div class="fade-up-element text-center">
                <div class="w-12 h-12 rounded-full border-2 border-alpine-gold flex items-center justify-center mx-auto mb-6">
                    <span class="font-serif text-xl text-alpine-gold">1</span>
                </div>
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('guide_page.howto_step1_title')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('guide_page.howto_step1_text')}
                </p>
            </div>
            <div class="fade-up-element text-center">
                <div class="w-12 h-12 rounded-full border-2 border-alpine-gold flex items-center justify-center mx-auto mb-6">
                    <span class="font-serif text-xl text-alpine-gold">2</span>
                </div>
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('guide_page.howto_step2_title')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('guide_page.howto_step2_text')}
                </p>
            </div>
            <div class="fade-up-element text-center">
                <div class="w-12 h-12 rounded-full border-2 border-alpine-gold flex items-center justify-center mx-auto mb-6">
                    <span class="font-serif text-xl text-alpine-gold">3</span>
                </div>
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('guide_page.howto_step3_title')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('guide_page.howto_step3_text')}
                </p>
            </div>
            <div class="fade-up-element text-center">
                <div class="w-12 h-12 rounded-full border-2 border-alpine-gold flex items-center justify-center mx-auto mb-6">
                    <span class="font-serif text-xl text-alpine-gold">4</span>
                </div>
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('guide_page.howto_step4_title')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('guide_page.howto_step4_text')}
                </p>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ SICUREZZA ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
        <div class="fade-up-element order-2 md:order-1">
            <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">{$t('guide_page.safety_label')}</span>
            <h2 class="font-serif text-4xl text-alpine-text mb-6">{$t('guide_page.safety_title')}</h2>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
                {$t('guide_page.safety_text')}
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                <div class="flex items-start gap-3">
                    <ShieldCheck class="w-5 h-5 text-alpine-gold shrink-0 mt-0.5" />
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">{$t('guide_page.safety_insurance_title')}</p>
                        <p class="text-xs text-alpine-muted font-light">{$t('guide_page.safety_insurance_text')}</p>
                    </div>
                </div>
                <div class="flex items-start gap-3">
                    <Wind class="w-5 h-5 text-alpine-gold shrink-0 mt-0.5" />
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">{$t('guide_page.safety_weather_title')}</p>
                        <p class="text-xs text-alpine-muted font-light">{$t('guide_page.safety_weather_text')}</p>
                    </div>
                </div>
                <div class="flex items-start gap-3">
                    <Flag class="w-5 h-5 text-alpine-gold shrink-0 mt-0.5" />
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">{$t('guide_page.safety_artva_title')}</p>
                        <p class="text-xs text-alpine-muted font-light">{$t('guide_page.safety_artva_text')}</p>
                    </div>
                </div>
                <div class="flex items-start gap-3">
                    <Heart class="w-5 h-5 text-alpine-gold shrink-0 mt-0.5" />
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">{$t('guide_page.safety_firstaid_title')}</p>
                        <p class="text-xs text-alpine-muted font-light">{$t('guide_page.safety_firstaid_text')}</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="fade-up-element order-1 md:order-2 overflow-hidden bg-alpine-border shadow-xl">
            <img src="/imgs/alpine-safety.jpg" alt="Squadra di sicurezza alpina sulla neve" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
        </div>
    </div>
</section>

<!-- ═══════════════════ ESCURSIONI PER TUTTI ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">{$t('guide_page.levels_title')}</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">{$t('guide_page.levels_subtitle')}</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            <div class="fade-up-element text-center p-10">
                <div class="w-10 h-10 rounded-full bg-green-100 flex items-center justify-center mx-auto mb-6">
                    <span class="w-3 h-3 rounded-full bg-green-500"></span>
                </div>
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('guide_page.level_family_name')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('guide_page.level_family_text')}
                </p>
            </div>
            <div class="fade-up-element text-center p-10">
                <div class="w-10 h-10 rounded-full bg-blue-100 flex items-center justify-center mx-auto mb-6">
                    <span class="w-3 h-3 rounded-full bg-blue-500"></span>
                </div>
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('guide_page.level_intermediate_name')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('guide_page.level_intermediate_text')}
                </p>
            </div>
            <div class="fade-up-element text-center p-10">
                <div class="w-10 h-10 rounded-full bg-stone-200 flex items-center justify-center mx-auto mb-6">
                    <span class="w-3 h-3 rounded-full bg-red-500"></span>
                </div>
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('guide_page.level_expert_name')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('guide_page.level_expert_text')}
                </p>
            </div>
            <div class="fade-up-element text-center p-10">
                <div class="w-10 h-10 rounded-full bg-gray-100 flex items-center justify-center mx-auto mb-6">
                    <Mountain class="w-5 h-5 text-alpine-gold" />
                </div>
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('guide_page.level_alpinism_name')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('guide_page.level_alpinism_text')}
                </p>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ INFO PRATICHE ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-5xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">{$t('guide_page.info_title')}</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">{$t('guide_page.info_subtitle')}</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="fade-up-element bg-white p-10 border border-alpine-border">
                <h4 class="font-serif text-xl text-alpine-text mb-6 flex items-center gap-3">
                    <Clock class="w-5 h-5 text-alpine-gold" />
                    {$t('guide_page.info_booking_title')}
                </h4>
                <div class="space-y-4 text-sm text-alpine-muted font-light">
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('guide_page.info_where')}</span>
                        <span class="font-bold text-alpine-text">{$t('guide_page.info_where_value')}</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('guide_page.info_notice')}</span>
                        <span class="font-bold text-alpine-text">{$t('guide_page.info_notice_value')}</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('guide_page.info_cancel')}</span>
                        <span class="font-bold text-alpine-text">{$t('guide_page.info_cancel_value')}</span>
                    </div>
                    <div class="flex justify-between items-center">
                        <span>{$t('guide_page.info_weather')}</span>
                        <span class="font-bold text-alpine-text">{$t('guide_page.info_weather_value')}</span>
                    </div>
                </div>
            </div>

            <div class="fade-up-element bg-white p-10 border border-alpine-border">
                <h4 class="font-serif text-xl text-alpine-text mb-6 flex items-center gap-3">
                    <ShieldCheck class="w-5 h-5 text-alpine-gold" />
                    {$t('guide_page.info_gear_title')}
                </h4>
                <div class="space-y-4 text-sm text-alpine-muted font-light">
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('guide_page.info_boots')}</span>
                        <span class="font-bold text-alpine-text">{$t('guide_page.info_boots_value')}</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('guide_page.info_backpack')}</span>
                        <span class="font-bold text-alpine-text">{$t('guide_page.info_backpack_value')}</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('guide_page.info_clothing')}</span>
                        <span class="font-bold text-alpine-text">{$t('guide_page.info_clothing_value')}</span>
                    </div>
                    <div class="flex justify-between items-center">
                        <span>{$t('guide_page.info_sunscreen')}</span>
                        <span class="font-bold text-alpine-text">{$t('guide_page.info_sunscreen_value')}</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ CTA ═══════════════════ -->
<section class="bg-[#0a0a0a] py-32 px-6">
    <div class="max-w-3xl mx-auto text-center">
        <div class="fade-up-element">
            <h2 class="font-serif text-4xl text-white mb-6">{$t('guide_page.cta_title')}</h2>
            <p class="text-white/50 text-sm font-light leading-relaxed max-w-lg mx-auto mb-12">
                {$t('guide_page.cta_text')}
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href={$locale === 'en' ? '/sport' : '/sport/trekking'} class="inline-flex items-center justify-center gap-3 bg-white text-alpine-text px-10 py-4 text-[11px] tracking-[0.2em] uppercase font-bold hover:bg-alpine-gold hover:text-white transition-all duration-300">
                    {$t('guide_page.cta_trails')} <ArrowRight class="w-4 h-4" />
                </a>
                <a href="/esperienze/ciaspolate" class="inline-flex items-center justify-center gap-3 border border-white/30 text-white px-10 py-4 text-[11px] tracking-[0.2em] uppercase font-bold hover:border-white hover:bg-white/10 transition-all duration-300">
                    {$t('guide_page.cta_snowshoe')} <ArrowRight class="w-4 h-4" />
                </a>
            </div>
        </div>
    </div>
</section>
