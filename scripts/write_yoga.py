#!/usr/bin/env python3
"""Write the fully translated yoga page."""
import pathlib

YOGA_PATH = pathlib.Path(__file__).resolve().parent.parent / "src" / "routes" / "esperienze" / "yoga" / "+page.svelte"

content = r'''<script lang="ts">
    import { Flower, Wind, Sparkles, Sun, Moon, Mountain, Clock, Users, ShieldCheck, Star, Heart, ArrowRight, Sunrise, CloudSun, TreePine, Leaf } from 'lucide-svelte';
    import { t } from '$lib/i18n';

    let scrollY = $state(0);
</script>

<svelte:window bind:scrollY />

<svelte:head>
    <title>{$t('yoga_page.meta_title')}</title>
    <meta name="description" content={$t('yoga_page.meta_description')} />
</svelte:head>

<!-- ═══════════════════ HERO ═══════════════════ -->
<header class="relative h-[85vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div
        class="absolute inset-0 scale-110"
        style="transform: translateY({scrollY * 0.25}px) scale(1.1);"
    >
        <img src="https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?q=80&w=2000&auto=format&fit=crop" class="h-full w-full object-cover opacity-50" alt="Yoga in montagna con vista sulle Alpi" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/30 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-28 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            {$t('yoga_page.hero_label')}
        </span>
        <h1 class="font-serif text-5xl md:text-8xl leading-tight font-light text-white fade-up-element">
            {$t('yoga_page.hero_title')}
        </h1>
        <p class="mt-6 text-white/50 text-sm font-light max-w-md fade-up-element">
            {$t('yoga_page.hero_subtitle')}
        </p>
    </div>
</header>

<!-- ═══════════════════ INTRO ═══════════════════ -->
<section class="bg-alpine-bg px-6 py-28">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <Flower class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            {$t('yoga_page.intro_title')}
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            {$t('yoga_page.intro_text')}
        </p>
    </div>
</section>

<!-- ═══════════════════ L'ESPERIENZA ═══════════════════ -->
<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
        <img src="https://images.unsplash.com/photo-1506126613408-eca07ce68773?q=80&w=1500&auto=format&fit=crop" alt="Yoga all'aperto con vista sulle montagne" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
    </div>

    <div class="fade-up-element">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">{$t('yoga_page.experience_label')}</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">{$t('yoga_page.experience_title')}</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            {$t('yoga_page.experience_text1')}
        </p>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
            {$t('yoga_page.experience_text2')}
        </p>
        <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
            <div class="flex items-center gap-3">
                <Heart class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('yoga_page.experience_badge_levels')}</span>
            </div>
            <div class="flex items-center gap-3">
                <Mountain class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('yoga_page.experience_badge_view')}</span>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ STATS ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-20 px-6">
    <div class="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-12 text-center">
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">1.500m</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">{$t('yoga_page.stats_altitude')}</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">60'</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">{$t('yoga_page.stats_session')}</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">7</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">{$t('yoga_page.stats_days')}</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">8</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">{$t('yoga_page.stats_places')}</p>
        </div>
    </div>
</section>

<!-- ═══════════════════ LE SESSIONI ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">{$t('yoga_page.sessions_title')}</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">{$t('yoga_page.sessions_subtitle')}</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12">
            <!-- Alba -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="overflow-hidden aspect-3/2 bg-linear-to-b from-amber-100 to-orange-200 flex items-center justify-center">
                    <Sunrise class="w-16 h-16 text-alpine-gold/60 group-hover:scale-110 transition-transform duration-700" />
                </div>
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Sun class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">{$t('yoga_page.session_dawn_time')}</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('yoga_page.session_dawn_name')}</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">{$t('yoga_page.session_dawn_type')}</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed">
                        {$t('yoga_page.session_dawn_text')}
                    </p>
                </div>
            </div>

            <!-- Pomeriggio -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="overflow-hidden aspect-3/2 bg-linear-to-b from-sky-100 to-blue-200 flex items-center justify-center">
                    <Wind class="w-16 h-16 text-alpine-gold/60 group-hover:scale-110 transition-transform duration-700" />
                </div>
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <CloudSun class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">{$t('yoga_page.session_afternoon_time')}</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('yoga_page.session_afternoon_name')}</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">{$t('yoga_page.session_afternoon_type')}</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed">
                        {$t('yoga_page.session_afternoon_text')}
                    </p>
                </div>
            </div>

            <!-- Tramonto -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="overflow-hidden aspect-3/2 bg-linear-to-b from-orange-100 to-rose-200 flex items-center justify-center">
                    <Moon class="w-16 h-16 text-alpine-gold/60 group-hover:scale-110 transition-transform duration-700" />
                </div>
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Moon class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">{$t('yoga_page.session_sunset_time')}</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">{$t('yoga_page.session_sunset_name')}</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">{$t('yoga_page.session_sunset_type')}</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed">
                        {$t('yoga_page.session_sunset_text')}
                    </p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ RETREAT SETTIMANALE ═══════════════════ -->
<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element order-2 md:order-1">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">{$t('yoga_page.retreat_label')}</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">{$t('yoga_page.retreat_title')}</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            {$t('yoga_page.retreat_text')}
        </p>
        <ul class="space-y-3 text-xs text-alpine-muted font-light mb-8">
            {#each $t('yoga_page.retreat_items') as item}
            <li class="flex items-start gap-3"><Star class="w-3.5 h-3.5 text-alpine-gold shrink-0 mt-0.5" /> {item}</li>
            {/each}
        </ul>
        <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
            <div class="flex items-center gap-3">
                <Clock class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('yoga_page.retreat_badge_days')}</span>
            </div>
            <div class="flex items-center gap-3">
                <Users class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">{$t('yoga_page.retreat_badge_places')}</span>
            </div>
        </div>
    </div>

    <div class="fade-up-element order-1 md:order-2 overflow-hidden bg-alpine-border shadow-xl">
        <img src="https://images.unsplash.com/photo-1545389336-cf090694435e?q=80&w=1500&auto=format&fit=crop" alt="Meditazione in montagna" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
    </div>
</section>

<!-- ═══════════════════ BENEFICI ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">{$t('yoga_page.benefits_title')}</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">{$t('yoga_page.benefits_subtitle')}</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            <div class="fade-up-element text-center p-10">
                <Wind class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-[1.5px]" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('yoga_page.benefit_air_title')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('yoga_page.benefit_air_text')}
                </p>
            </div>
            <div class="fade-up-element text-center p-10">
                <Sparkles class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-[1.5px]" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('yoga_page.benefit_silence_title')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('yoga_page.benefit_silence_text')}
                </p>
            </div>
            <div class="fade-up-element text-center p-10">
                <Leaf class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-[1.5px]" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('yoga_page.benefit_nature_title')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('yoga_page.benefit_nature_text')}
                </p>
            </div>
            <div class="fade-up-element text-center p-10">
                <Heart class="w-8 h-8 text-alpine-gold mx-auto mb-6 stroke-[1.5px]" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">{$t('yoga_page.benefit_recovery_title')}</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    {$t('yoga_page.benefit_recovery_text')}
                </p>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ L'INSEGNANTE ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-5xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">{$t('yoga_page.teacher_title')}</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">{$t('yoga_page.teacher_subtitle')}</p>
        </div>

        <div class="fade-up-element bg-white p-12 md:p-16 border border-alpine-border max-w-3xl mx-auto">
            <div class="text-center">
                <Flower class="w-10 h-10 text-alpine-gold mx-auto mb-8 stroke-[1.5px]" />
                <p class="text-alpine-muted text-sm font-light leading-relaxed italic mb-8 max-w-xl mx-auto">
                    "{$t('yoga_page.teacher_quote')}"
                </p>
                <p class="text-xs text-alpine-muted font-light leading-relaxed max-w-xl mx-auto mb-8">
                    {$t('yoga_page.teacher_text')}
                </p>
                <div class="flex flex-wrap justify-center gap-4">
                    <span class="text-[9px] uppercase tracking-[0.2em] font-bold text-alpine-gold border border-alpine-gold/30 px-4 py-2">RYT-500</span>
                    <span class="text-[9px] uppercase tracking-[0.2em] font-bold text-alpine-gold border border-alpine-gold/30 px-4 py-2">Hatha</span>
                    <span class="text-[9px] uppercase tracking-[0.2em] font-bold text-alpine-gold border border-alpine-gold/30 px-4 py-2">Yin</span>
                    <span class="text-[9px] uppercase tracking-[0.2em] font-bold text-alpine-gold border border-alpine-gold/30 px-4 py-2">Pranayama</span>
                    <span class="text-[9px] uppercase tracking-[0.2em] font-bold text-alpine-gold border border-alpine-gold/30 px-4 py-2">Mindfulness</span>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ INFO PRATICHE ═══════════════════ -->
<section class="bg-alpine-bg pb-32 px-6">
    <div class="max-w-5xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">{$t('yoga_page.info_title')}</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">{$t('yoga_page.info_subtitle')}</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="fade-up-element bg-white p-10 border border-alpine-border">
                <h4 class="font-serif text-xl text-alpine-text mb-6 flex items-center gap-3">
                    <Clock class="w-5 h-5 text-alpine-gold" />
                    {$t('yoga_page.info_schedule_title')}
                </h4>
                <div class="space-y-4 text-sm text-alpine-muted font-light">
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('yoga_page.info_schedule_sun')}</span>
                        <span class="font-bold text-alpine-text">07:00 – 08:00</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('yoga_page.info_schedule_pranayama')}</span>
                        <span class="font-bold text-alpine-text">15:00 – 16:00</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('yoga_page.info_schedule_sunset')}</span>
                        <span class="font-bold text-alpine-text">18:30 – 19:30</span>
                    </div>
                    <div class="flex justify-between items-center">
                        <span>{$t('yoga_page.info_schedule_availability')}</span>
                        <span class="font-bold text-alpine-text">{$t('yoga_page.info_schedule_everyday')}</span>
                    </div>
                </div>
            </div>

            <div class="fade-up-element bg-white p-10 border border-alpine-border">
                <h4 class="font-serif text-xl text-alpine-text mb-6 flex items-center gap-3">
                    <ShieldCheck class="w-5 h-5 text-alpine-gold" />
                    {$t('yoga_page.info_know_title')}
                </h4>
                <div class="space-y-4 text-sm text-alpine-muted font-light">
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('yoga_page.info_level')}</span>
                        <span class="font-bold text-alpine-text">{$t('yoga_page.info_level_value')}</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('yoga_page.info_mat')}</span>
                        <span class="font-bold text-alpine-text">{$t('yoga_page.info_mat_value')}</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>{$t('yoga_page.info_booking')}</span>
                        <span class="font-bold text-alpine-text">{$t('yoga_page.info_booking_value')}</span>
                    </div>
                    <div class="flex justify-between items-center">
                        <span>{$t('yoga_page.info_cost')}</span>
                        <span class="font-bold text-alpine-text">{$t('yoga_page.info_cost_value')}</span>
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
            <h2 class="font-serif text-4xl text-white mb-6">{$t('yoga_page.cta_title')}</h2>
            <p class="text-white/50 text-sm font-light leading-relaxed max-w-lg mx-auto mb-12">
                {$t('yoga_page.cta_text')}
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="/wellness" class="inline-flex items-center justify-center gap-3 bg-white text-alpine-text px-10 py-4 text-[11px] tracking-[0.2em] uppercase font-bold hover:bg-alpine-gold hover:text-white transition-all duration-300">
                    {$t('yoga_page.cta_wellness')} <ArrowRight class="w-4 h-4" />
                </a>
                <a href="/wellness/massaggi" class="inline-flex items-center justify-center gap-3 border border-white/30 text-white px-10 py-4 text-[11px] tracking-[0.2em] uppercase font-bold hover:border-white hover:bg-white/10 transition-all duration-300">
                    {$t('yoga_page.cta_massage')} <ArrowRight class="w-4 h-4" />
                </a>
            </div>
        </div>
    </div>
</section>
'''

YOGA_PATH.write_text(content, encoding='utf-8')
print(f"Yoga page written to {YOGA_PATH}")
