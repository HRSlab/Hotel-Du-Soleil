#!/usr/bin/env python3
"""Write the fully translated massaggi page."""
import pathlib

PAGE_PATH = pathlib.Path(__file__).resolve().parent.parent / "src" / "routes" / "wellness" / "massaggi" / "+page.svelte"

content = r'''<script lang="ts">
    import { t } from '$lib/i18n';
    import { Heart, Clock, Droplets, Flame, Leaf, ArrowRight, ShieldCheck, Star, Hand, Sparkles, Waves } from 'lucide-svelte';

    let scrollY = $state(0);
</script>

<svelte:window bind:scrollY />

<svelte:head>
    <title>{$t('massaggi_page.meta_title')}</title>
    <meta name="description" content={$t('massaggi_page.meta_description')} />
</svelte:head>

<!-- ═══════════════════ HERO ═══════════════════ -->
<header class="relative h-[85vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div
        class="absolute inset-0 scale-110"
        style="transform: translateY({scrollY * 0.25}px) scale(1.1);"
    >
        <img src="https://images.unsplash.com/photo-1544161515-4af6b1d46bdc?q=80&w=2000&auto=format&fit=crop" class="h-full w-full object-cover opacity-55" alt="Massaggio sportivo" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/30 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-28 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            {$t('massaggi_page.hero_label')}
        </span>
        <h1 class="font-serif text-5xl md:text-8xl leading-tight font-light text-white fade-up-element">
            {$t('massaggi_page.hero_title')}
        </h1>
        <p class="mt-6 text-white/50 text-sm font-light max-w-md fade-up-element">
            {$t('massaggi_page.hero_subtitle')}
        </p>
    </div>
</header>

<!-- ═══════════════════ INTRO ═══════════════════ -->
<section class="bg-alpine-bg px-6 py-28">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <Heart class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            {$t('massaggi_page.intro_title')}
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            {$t('massaggi_page.intro_text')}
        </p>
    </div>
</section>

<!-- ═══════════════════ LA FILOSOFIA ═══════════════════ -->
<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
        <img src="https://images.unsplash.com/photo-1600334129128-685c5582fd35?q=80&w=1500&auto=format&fit=crop" alt="Ambiente massaggi wellness" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
    </div>

    <div class="fade-up-element">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">{$t('massaggi_page.philosophy_label')}</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">{$t('massaggi_page.philosophy_title')}</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            {$t('massaggi_page.philosophy_text1')}
        </p>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
            {$t('massaggi_page.philosophy_text2')}
        </p>
        <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
            <div class="flex items-center gap-3">
                <Leaf class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('massaggi_page.philosophy_badge_oils')}</span>
            </div>
            <div class="flex items-center gap-3">
                <ShieldCheck class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('massaggi_page.philosophy_badge_cert')}</span>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ STATS ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-20 px-6">
    <div class="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-12 text-center">
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">6</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">{$t('massaggi_page.stats_types')}</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">50'</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">{$t('massaggi_page.stats_duration')}</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">2</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">{$t('massaggi_page.stats_rooms')}</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">7/7</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">{$t('massaggi_page.stats_days')}</p>
        </div>
    </div>
</section>

<!-- ═══════════════════ I MASSAGGI ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">{$t('massaggi_page.massages_title')}</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">{$t('massaggi_page.massages_subtitle')}</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12">
            <!-- Decontratturante -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Flame class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">{$t('massaggi_page.m_sport_badge')}</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('massaggi_page.m_sport_name')}</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">{$t('massaggi_page.m_sport_price')}</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        {$t('massaggi_page.m_sport_text')}
                    </p>
                    <div class="pt-6 border-t border-alpine-border">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">{$t('massaggi_page.best_for')}</p>
                        <p class="text-xs text-alpine-text mt-2 font-light">{$t('massaggi_page.m_sport_for')}</p>
                    </div>
                </div>
            </div>

            <!-- Hot Stone -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Sparkles class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">{$t('massaggi_page.m_hotstone_badge')}</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('massaggi_page.m_hotstone_name')}</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">{$t('massaggi_page.m_hotstone_price')}</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        {$t('massaggi_page.m_hotstone_text')}
                    </p>
                    <div class="pt-6 border-t border-alpine-border">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">{$t('massaggi_page.best_for')}</p>
                        <p class="text-xs text-alpine-text mt-2 font-light">{$t('massaggi_page.m_hotstone_for')}</p>
                    </div>
                </div>
            </div>

            <!-- Arnica -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Leaf class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">{$t('massaggi_page.m_arnica_badge')}</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('massaggi_page.m_arnica_name')}</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">{$t('massaggi_page.m_arnica_price')}</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        {$t('massaggi_page.m_arnica_text')}
                    </p>
                    <div class="pt-6 border-t border-alpine-border">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">{$t('massaggi_page.best_for')}</p>
                        <p class="text-xs text-alpine-text mt-2 font-light">{$t('massaggi_page.m_arnica_for')}</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Seconda riga -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12 mt-8 lg:mt-12">
            <!-- Rilassante -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Waves class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">{$t('massaggi_page.m_relax_badge')}</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('massaggi_page.m_relax_name')}</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">{$t('massaggi_page.m_relax_price')}</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        {$t('massaggi_page.m_relax_text')}
                    </p>
                    <div class="pt-6 border-t border-alpine-border">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">{$t('massaggi_page.best_for')}</p>
                        <p class="text-xs text-alpine-text mt-2 font-light">{$t('massaggi_page.m_relax_for')}</p>
                    </div>
                </div>
            </div>

            <!-- Gambe -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Hand class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">{$t('massaggi_page.m_legs_badge')}</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('massaggi_page.m_legs_name')}</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">{$t('massaggi_page.m_legs_price')}</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        {$t('massaggi_page.m_legs_text')}
                    </p>
                    <div class="pt-6 border-t border-alpine-border">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">{$t('massaggi_page.best_for')}</p>
                        <p class="text-xs text-alpine-text mt-2 font-light">{$t('massaggi_page.m_legs_for')}</p>
                    </div>
                </div>
            </div>

            <!-- Coppia -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Heart class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">{$t('massaggi_page.m_couple_badge')}</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('massaggi_page.m_couple_name')}</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">{$t('massaggi_page.m_couple_price')}</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        {$t('massaggi_page.m_couple_text')}
                    </p>
                    <div class="pt-6 border-t border-alpine-border">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">{$t('massaggi_page.best_for')}</p>
                        <p class="text-xs text-alpine-text mt-2 font-light">{$t('massaggi_page.m_couple_for')}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ L'ESPERIENZA ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
        <div class="fade-up-element">
            <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">{$t('massaggi_page.ritual_label')}</span>
            <h2 class="font-serif text-4xl text-alpine-text mb-6">{$t('massaggi_page.ritual_title')}</h2>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
                {$t('massaggi_page.ritual_text')}
            </p>
            <div class="space-y-6">
                <div class="flex items-start gap-4">
                    <div class="w-8 h-8 rounded-full border border-alpine-gold flex items-center justify-center shrink-0 mt-0.5">
                        <span class="text-xs font-serif text-alpine-gold">1</span>
                    </div>
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">{$t('massaggi_page.ritual_step1')}</p>
                        <p class="text-xs text-alpine-muted font-light">{$t('massaggi_page.ritual_step1_text')}</p>
                    </div>
                </div>
                <div class="flex items-start gap-4">
                    <div class="w-8 h-8 rounded-full border border-alpine-gold flex items-center justify-center shrink-0 mt-0.5">
                        <span class="text-xs font-serif text-alpine-gold">2</span>
                    </div>
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">{$t('massaggi_page.ritual_step2')}</p>
                        <p class="text-xs text-alpine-muted font-light">{$t('massaggi_page.ritual_step2_text')}</p>
                    </div>
                </div>
                <div class="flex items-start gap-4">
                    <div class="w-8 h-8 rounded-full border border-alpine-gold flex items-center justify-center shrink-0 mt-0.5">
                        <span class="text-xs font-serif text-alpine-gold">3</span>
                    </div>
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">{$t('massaggi_page.ritual_step3')}</p>
                        <p class="text-xs text-alpine-muted font-light">{$t('massaggi_page.ritual_step3_text')}</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
            <img src="https://images.unsplash.com/photo-1540555700478-4be289fbec6d?q=80&w=1500&auto=format&fit=crop" alt="Zona relax dopo il massaggio" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
        </div>
    </div>
</section>

<!-- ═══════════════════ GLI OLI ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-5xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">{$t('massaggi_page.oils_title')}</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">{$t('massaggi_page.oils_subtitle')}</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="fade-up-element text-center p-10 bg-white border border-alpine-border">
                <Leaf class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('massaggi_page.oil_arnica_name')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('massaggi_page.oil_arnica_text')}
                </p>
            </div>
            <div class="fade-up-element text-center p-10 bg-white border border-alpine-border">
                <Droplets class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('massaggi_page.oil_pine_name')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('massaggi_page.oil_pine_text')}
                </p>
            </div>
            <div class="fade-up-element text-center p-10 bg-white border border-alpine-border">
                <Star class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('massaggi_page.oil_juniper_name')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('massaggi_page.oil_juniper_text')}
                </p>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ INFO PRATICHE ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-5xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">{$t('massaggi_page.info_title')}</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">{$t('massaggi_page.info_subtitle')}</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="fade-up-element bg-alpine-bg p-10 border border-alpine-border">
                <h4 class="font-serif text-xl text-alpine-text mb-6 flex items-center gap-3">
                    <Clock class="w-5 h-5 text-alpine-gold" />
                    {$t('massaggi_page.info_schedule_title')}
                </h4>
                <div class="space-y-4 text-sm text-alpine-muted font-light">
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('massaggi_page.info_availability')}</span>
                        <span class="font-bold text-alpine-text">{$t('massaggi_page.info_availability_value')}</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('massaggi_page.info_timeslot')}</span>
                        <span class="font-bold text-alpine-text">10:00 – 20:00</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('massaggi_page.info_booking')}</span>
                        <span class="font-bold text-alpine-text">{$t('massaggi_page.info_booking_value')}</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('massaggi_page.info_notice')}</span>
                        <span class="font-bold text-alpine-text">{$t('massaggi_page.info_notice_value')}</span>
                    </div>
                    <div class="flex justify-between items-center">
                        <span>{$t('massaggi_page.info_cancel')}</span>
                        <span class="font-bold text-alpine-text">{$t('massaggi_page.info_cancel_value')}</span>
                    </div>
                </div>
            </div>

            <div class="fade-up-element bg-alpine-bg p-10 border border-alpine-border">
                <h4 class="font-serif text-xl text-alpine-text mb-6 flex items-center gap-3">
                    <ShieldCheck class="w-5 h-5 text-alpine-gold" />
                    {$t('massaggi_page.info_know_title')}
                </h4>
                <div class="space-y-4 text-sm text-alpine-muted font-light">
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('massaggi_page.info_robe')}</span>
                        <span class="font-bold text-alpine-text">{$t('massaggi_page.info_robe_value')}</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('massaggi_page.info_arrival')}</span>
                        <span class="font-bold text-alpine-text">{$t('massaggi_page.info_arrival_value')}</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('massaggi_page.info_age')}</span>
                        <span class="font-bold text-alpine-text">{$t('massaggi_page.info_age_value')}</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('massaggi_page.info_packages')}</span>
                        <span class="font-bold text-alpine-text">{$t('massaggi_page.info_packages_value')}</span>
                    </div>
                    <div class="flex justify-between items-center">
                        <span>{$t('massaggi_page.info_giftcard')}</span>
                        <span class="font-bold text-alpine-text">{$t('massaggi_page.info_giftcard_value')}</span>
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
            <h2 class="font-serif text-4xl text-white mb-6">{$t('massaggi_page.cta_title')}</h2>
            <p class="text-white/50 text-sm font-light leading-relaxed max-w-lg mx-auto mb-12">
                {$t('massaggi_page.cta_text')}
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="/wellness/spa" class="inline-flex items-center justify-center gap-3 bg-white text-alpine-text px-10 py-4 text-[11px] tracking-[0.2em] uppercase font-bold hover:bg-alpine-gold hover:text-white transition-all duration-300">
                    {$t('massaggi_page.cta_spa')} <ArrowRight class="w-4 h-4" />
                </a>
                <a href="/wellness/trattamenti" class="inline-flex items-center justify-center gap-3 border border-white/30 text-white px-10 py-4 text-[11px] tracking-[0.2em] uppercase font-bold hover:border-white hover:bg-white/10 transition-all duration-300">
                    {$t('massaggi_page.cta_treatments')} <ArrowRight class="w-4 h-4" />
                </a>
            </div>
        </div>
    </div>
</section>
'''

PAGE_PATH.write_text(content, encoding='utf-8')
print(f"Massaggi page written to {PAGE_PATH}")
