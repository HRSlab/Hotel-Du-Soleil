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
    <title>{$t('wellness.main_title')} | Hotel du Soleil</title>
    <meta name="description" content="Wellness area at Hotel du Soleil in Torgnon. Massages, private SPA, Finnish sauna, hydromassage and heated pool in the heart of the Aosta Valley Alps." />
</svelte:head>

<!-- ═══════════════════ HERO ═══════════════════ -->
<header class="relative h-[85vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div
        class="absolute inset-0 scale-110"
        style="transform: translateY({scrollY * 0.25}px) scale(1.1);"
    >
        <img src="/imgs/massaggi-ingresso.webp" class="h-full w-full object-cover opacity-55" alt="Massage area at Hotel Du Soleil" />
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
        <img src="/imgs/sauna-hds.webp" alt="Sauna at Hotel Du Soleil" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
    </div>

    <div class="fade-up-element">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">Our Philosophy</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">Sport & Wellness,<br/>A Natural Bond</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
            We don't offer a generic treatment menu. Every massage is designed
            for those who live the mountains actively: skiers, hikers, cyclists, climbers.
            Our therapists assess your specific needs before each session.
        </p>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
            We use local essential oils — arnica montana, stone pine, alpine juniper —
            combining the mountain's fragrance with the anti-inflammatory
            and muscle-relaxing properties of the Aosta Valley herbal tradition.
        </p>
        <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
            <div class="flex items-center gap-3">
                <Leaf class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Natural alpine oils</span>
            </div>
            <div class="flex items-center gap-3">
                <ShieldCheck class="w-5 h-5 text-alpine-gold shrink-0" />
                <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">Certified therapists</span>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ STATS ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-20 px-6">
    <div class="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-12 text-center">
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">6</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Massage types</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">3</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Exclusive SPA rooms</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">32°C</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Heated pool</p>
        </div>
        <div class="fade-up-element">
            <p class="font-serif text-4xl md:text-5xl text-alpine-text mb-2">7/7</p>
            <p class="text-[10px] uppercase tracking-[0.25em] text-alpine-muted font-bold">Days by appointment</p>
        </div>
    </div>
</section>

<!-- ═══════════════════ I MASSAGGI ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">Our Massages</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">Every treatment, a tailored experience</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12">
            <!-- LING -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Waves class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">Relaxing & Soothing</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Ling Massage</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">1 hr · €50</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        A soothing muscle massage with essential oils.
                        Releases tension, improves circulation and drainage,
                        promotes overall wellbeing and relieves stress.
                    </p>
                    <div class="pt-6 border-t border-alpine-border">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">Best for</p>
                        <p class="text-xs text-alpine-text mt-2 font-light">Stress · Tension · General wellbeing</p>
                    </div>
                </div>
            </div>

            <!-- ANTICELLULITE -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Droplets class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">Draining</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Anticellulite</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">1 hr · €55</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        Reactivates blood and lymphatic circulation
                        to reduce fluid retention.
                        A targeted treatment that restores lightness and tone.
                    </p>
                    <div class="pt-6 border-t border-alpine-border">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">Best for</p>
                        <p class="text-xs text-alpine-text mt-2 font-light">Water retention · Heavy legs</p>
                    </div>
                </div>
            </div>

            <!-- SPORTIVO -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Flame class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">Pre & Post Activity</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Sports Deep Tissue</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">1 hr · €50 · 30 min · €30</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        Stimulates tissues and muscles under strain,
                        inducing deep relaxation and releasing knots,
                        tension and pain. Also available as a 30-minute
                        session on a specific area (legs or back).
                    </p>
                    <div class="pt-6 border-t border-alpine-border">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">Best for</p>
                        <p class="text-xs text-alpine-text mt-2 font-light">Skiers · Cyclists · Hikers</p>
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
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">Mind-Body Balance</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Foot Reflexology</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">30 min · €30 · 1 hr · €45</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        Restores mind-body balance, reduces stress,
                        anxiety and muscle tension. Improves circulation
                        and promotes deep, lasting relaxation.
                    </p>
                    <div class="pt-6 border-t border-alpine-border">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">Best for</p>
                        <p class="text-xs text-alpine-text mt-2 font-light">Stress · Anxiety · Muscle tension</p>
                    </div>
                </div>
            </div>

            <!-- KOBIDO -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Sparkles class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">Japanese Anti-Ageing</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Kobido</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">30 min · €30 · 1 hr · €50</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        Japanese massage on face, neck and décolleté.
                        Natural lifting effect: stimulates circulation, collagen
                        and elastin production to tone and brighten the skin.
                        Helps with bruxism and headaches.
                    </p>
                    <div class="pt-6 border-t border-alpine-border">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">Best for</p>
                        <p class="text-xs text-alpine-text mt-2 font-light">Anti-ageing · Radiance · Bruxism</p>
                    </div>
                </div>
            </div>

            <!-- TERRA & CIELO -->
            <div class="fade-up-element group border-2 border-alpine-gold bg-white shadow-xl hover:shadow-2xl transition-all duration-500 relative">
                <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-alpine-gold text-white px-5 py-1.5 text-[10px] uppercase tracking-[0.3em] font-bold">
                    Complete Ritual
                </div>
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Star class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">Body & Face</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Terra & Cielo</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-4">1 hr · €55</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        The best of both worlds: foot reflexology (30 min)
                        combined with anti-ageing face, neck and décolleté massage (30 min).
                        A complete ritual that rebalances body and mind
                        in a single experience.
                    </p>
                    <div class="pt-6 border-t border-alpine-gold/30">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold">Includes</p>
                        <p class="text-xs text-alpine-text mt-2 font-light">Foot reflexology + Anti-ageing facial</p>
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
            <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">The Ritual</span>
            <h2 class="font-serif text-4xl text-alpine-text mb-6">Every Massage<br/>Is a Complete Experience</h2>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
                We never start directly with the treatment.
                Every session begins with a brief consultation to understand your needs,
                areas of tension and desired intensity.
                Afterwards, a warm alpine herbal tea and a few minutes
                of rest in the relaxation area complete the experience.
            </p>
            <div class="space-y-6">
                <div class="flex items-start gap-4">
                    <div class="w-8 h-8 rounded-full border border-alpine-gold flex items-center justify-center shrink-0 mt-0.5">
                        <span class="text-xs font-serif text-alpine-gold">1</span>
                    </div>
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">Welcome</p>
                        <p class="text-xs text-alpine-muted font-light">Welcome tea and consultation with your therapist</p>
                    </div>
                </div>
                <div class="flex items-start gap-4">
                    <div class="w-8 h-8 rounded-full border border-alpine-gold flex items-center justify-center shrink-0 mt-0.5">
                        <span class="text-xs font-serif text-alpine-gold">2</span>
                    </div>
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">The Treatment</p>
                        <p class="text-xs text-alpine-muted font-light">30–60 minutes of your chosen massage</p>
                    </div>
                </div>
                <div class="flex items-start gap-4">
                    <div class="w-8 h-8 rounded-full border border-alpine-gold flex items-center justify-center shrink-0 mt-0.5">
                        <span class="text-xs font-serif text-alpine-gold">3</span>
                    </div>
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">Rest</p>
                        <p class="text-xs text-alpine-muted font-light">Relaxation area with warm tea and soft blanket</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
            <img src="/imgs/piscina.webp" alt="Relaxation area and pool" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
        </div>
    </div>
</section>

<!-- ═══════════════════ GLI OLI ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-5xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">Our Oils</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">From the mountain, for your body</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="fade-up-element text-center p-10 bg-white border border-alpine-border">
                <Leaf class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Arnica Montana</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Hand-picked in alpine pastures above 1,800 metres.
                    A powerful natural anti-inflammatory, it is the traditional alpine remedy
                    for muscle pain and bruises.
                </p>
            </div>
            <div class="fade-up-element text-center p-10 bg-white border border-alpine-border">
                <Droplets class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Stone Pine</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    The essential oil of the “king of the Alps”. Distilled from wood and needles,
                    it has scientifically proven relaxing properties:
                    it lowers heart rate and promotes deep sleep.
                </p>
            </div>
            <div class="fade-up-element text-center p-10 bg-white border border-alpine-border">
                <Star class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Alpine Juniper</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    From high-altitude juniper berries, an oil with a fresh, resinous fragrance.
                    Stimulates circulation, drains fluids
                    and restores lightness to tired legs.
                </p>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ DIVIDER: PRIVATE SPA ═══════════════════ -->
<section class="bg-[#0a0a0a] py-28 px-6">
    <div class="max-w-3xl mx-auto text-center fade-up-element">
        <Moon class="w-10 h-10 text-alpine-gold mx-auto mb-8" />
        <h2 class="font-serif text-4xl md:text-5xl text-white mb-6 leading-tight">Private SPA</h2>
        <p class="text-white/50 text-sm font-light leading-relaxed max-w-lg mx-auto">
            Close the door. The world stays outside. Hydromassage, Finnish sauna
            and heated pool — all for your exclusive use, just for you.
        </p>
    </div>
</section>

<!-- ═══════════════════ L'AREA ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
    <div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
        <img src="/imgs/jacuzzi-spa-hds-2026.webp" alt="Hydromassage Private SPA" class="w-full h-full object-cover img-elegant aspect-4/3 brightness-90" />
    </div>

    <div class="fade-up-element">
        <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">Exclusive Access</span>
        <h2 class="font-serif text-4xl text-alpine-text mb-6">Three Spaces,<br/>One Privilege</h2>
        <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
            When you book the Private SPA, the entire wellness area is closed
            to other guests and becomes your private sanctuary.
            Move freely between spaces, choose the music,
            adjust the lighting and enjoy every moment at your own pace.
        </p>
        <div class="space-y-4">
            <div class="flex items-start gap-4 p-4 border border-alpine-border bg-white">
                <Droplets class="w-5 h-5 text-alpine-gold shrink-0 mt-0.5" />
                <div>
                    <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">Hydromassage</p>
                    <p class="text-xs text-alpine-muted font-light">Jet pool at controlled temperature, chromotherapy and aromatherapy included</p>
                </div>
            </div>
            <div class="flex items-start gap-4 p-4 border border-alpine-border bg-white">
                <Flame class="w-5 h-5 text-alpine-gold shrink-0 mt-0.5" />
                <div>
                    <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">Finnish Sauna</p>
                    <p class="text-xs text-alpine-muted font-light">Temperature adjustable up to 90°C, Aosta Valley stone pine wood, steam infusions with essential oils</p>
                </div>
            </div>
            <div class="flex items-start gap-4 p-4 border border-alpine-border bg-white">
                <Sparkles class="w-5 h-5 text-alpine-gold shrink-0 mt-0.5" />
                <div>
                    <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">Heated Pool</p>
                    <p class="text-xs text-alpine-muted font-light">Water at 32°C, open swimming and relaxation area with heated loungers and Alpine views</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ I PACCHETTI ═══════════════════ -->
<section class="bg-alpine-bg pb-32 px-6">
    <div class="max-w-7xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">Packages</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">Choose the perfect experience for you</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12">
            <!-- Coppia -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Heart class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">For Two</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Romantic Escape</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-6">2 hrs · 2 guests · €180</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        Two hours of absolute exclusivity for couples.
                        The entire wellness area is yours: hydromassage with chromotherapy,
                        Finnish sauna and heated pool.
                    </p>
                    <div class="pt-6 border-t border-alpine-border space-y-3">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-3">Includes</p>
                        <div class="flex items-center gap-2">
                            <Wine class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">Bottle of Aosta Valley wine</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Gem class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">Fresh fruit and chocolates</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Sparkles class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">Premium bathrobes and slippers</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Music class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">Music selection of your choice</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Piccolo Gruppo -->
            <div class="fade-up-element group border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500">
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Users class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">Small Group</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Friends & Family</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-6">2 hrs · 3–6 guests · €280</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        Perfect for celebrating a special occasion with close friends
                        or a family evening. Same amenities as the couple's package,
                        scaled up for the group.
                    </p>
                    <div class="pt-6 border-t border-alpine-border space-y-3">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-3">Includes</p>
                        <div class="flex items-center gap-2">
                            <Wine class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">2 bottles of Aosta Valley wine</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Gem class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">Cheese and fruit board</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Sparkles class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">Bathrobes and slippers for everyone</span>
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
                    Exclusive
                </div>
                <div class="p-8 md:p-10">
                    <div class="flex items-center gap-2 mb-4">
                        <Moon class="w-4 h-4 text-alpine-gold" />
                        <span class="text-[10px] uppercase tracking-[0.2em] text-alpine-muted font-bold">Premium</span>
                    </div>
                    <h4 class="font-serif text-2xl text-alpine-text mb-2">Private SPA by Night</h4>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-6">3 hrs · 2–4 guests · €380</p>
                    <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed mb-6">
                        The ultimate experience. From 9 PM to midnight, the wellness area
                        transforms into a nocturnal sanctuary with dim lights, candles
                        and the absolute silence of the mountains. Three hours to lose track of time.
                    </p>
                    <div class="pt-6 border-t border-alpine-gold/30 space-y-3">
                        <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mb-3">Everything included, and more</p>
                        <div class="flex items-center gap-2">
                            <Wine class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">Bottle of Champagne or premium wine</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Gem class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">Gourmet board and artisan pralines</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Star class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">Scented candles and mood lighting</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Sparkles class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">Premium beauty kit and warm bathrobes</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Music class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">Curated playlist or total silence</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <Clock class="w-3.5 h-3.5 text-alpine-gold shrink-0" />
                            <span class="text-xs text-alpine-text font-light">Full 3 hours (9 PM – midnight)</span>
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
            <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">Private SPA by Night</span>
            <h2 class="font-serif text-4xl text-alpine-text mb-6">When the Mountain<br/>Sleeps, You Shine</h2>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-6">
                From 9 PM, the hotel enters a special quiet.
                The wellness lights dim, the candles come alive
                and the only sound is flowing water.
                It is the most exclusive hour of our hotel.
            </p>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
                Champagne awaits you at the poolside. The gourmet board —
                Fontina DOP, Lardo d'Arnad, mountain honey, artisan pralines —
                is prepared by our chef. Three hours that will never feel like enough.
            </p>
            <div class="grid grid-cols-2 gap-6 pt-6 border-t border-alpine-border">
                <div class="flex items-center gap-3">
                    <Moon class="w-5 h-5 text-alpine-gold shrink-0" />
                    <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">21:00 – 00:00</span>
                </div>
                <div class="flex items-center gap-3">
                    <Lock class="w-5 h-5 text-alpine-gold shrink-0" />
                    <span class="text-xs font-bold uppercase tracking-widest text-alpine-text">100% Private</span>
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
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">Every Detail Matters</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">Included in all Private SPA packages</p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
            <div class="fade-up-element text-center p-8 bg-white border border-alpine-border">
                <Wine class="w-8 h-8 text-alpine-gold mx-auto mb-5" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Wine & Bubbles</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Aosta Valley wine or Champagne (By Night package).
                    Served poolside at the perfect temperature.
                </p>
            </div>
            <div class="fade-up-element text-center p-8 bg-white border border-alpine-border">
                <Gem class="w-8 h-8 text-alpine-gold mx-auto mb-5" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Tasting</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Fresh fruit, artisan chocolates and local cheeses.
                    The night package includes a full gourmet board.
                </p>
            </div>
            <div class="fade-up-element text-center p-8 bg-white border border-alpine-border">
                <Sparkles class="w-8 h-8 text-alpine-gold mx-auto mb-5" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Premium Comfort</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    Warm bathrobes, soft slippers, towels and beauty kit
                    with natural alpine products.
                </p>
            </div>
            <div class="fade-up-element text-center p-8 bg-white border border-alpine-border">
                <Lock class="w-8 h-8 text-alpine-gold mx-auto mb-5" />
                <h4 class="font-serif text-lg text-alpine-text mb-3">Total Privacy</h4>
                <p class="text-xs text-alpine-muted font-light leading-relaxed">
                    The area is closed to all other guests.
                    No interruptions, no schedule to keep within your booked time slot.
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
            <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-4 block">Tailor-Made</span>
            <h2 class="font-serif text-4xl text-alpine-text mb-6">Special Occasions</h2>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-8">
                The Private SPA is the perfect place to make a special moment
                even more unforgettable. Anniversaries, birthdays, marriage proposals:
                tell us what you're celebrating and we'll personalise everything for you.
            </p>
            <div class="space-y-5">
                <div class="flex items-start gap-4">
                    <Heart class="w-5 h-5 text-alpine-gold shrink-0 mt-0.5" />
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">Anniversaries & Proposals</p>
                        <p class="text-xs text-alpine-muted font-light">Rose petals, Champagne and a personalised message</p>
                    </div>
                </div>
                <div class="flex items-start gap-4">
                    <Star class="w-5 h-5 text-alpine-gold shrink-0 mt-0.5" />
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">Birthdays</p>
                        <p class="text-xs text-alpine-muted font-light">Custom cake and themed decorations</p>
                    </div>
                </div>
                <div class="flex items-start gap-4">
                    <Users class="w-5 h-5 text-alpine-gold shrink-0 mt-0.5" />
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-1">Team & Hen/Stag Parties</p>
                        <p class="text-xs text-alpine-muted font-light">Group package with prosecco, boards and party atmosphere</p>
                    </div>
                </div>
            </div>
            <p class="mt-8 text-[10px] uppercase tracking-widest text-alpine-muted font-bold">
                Speak with reception to personalise your experience
            </p>
        </div>
    </div>
</section>

<!-- ═══════════════════ INFO PRATICHE ═══════════════════ -->
<section class="bg-alpine-bg py-32 px-6">
    <div class="max-w-5xl mx-auto">
        <div class="fade-up-element text-center mb-20 max-w-xl mx-auto">
            <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">Practical Information</h2>
            <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">Everything you need to know</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <!-- Massaggi -->
            <div class="fade-up-element bg-white p-10 border border-alpine-border">
                <h4 class="font-serif text-xl text-alpine-text mb-6 flex items-center gap-3">
                    <Clock class="w-5 h-5 text-alpine-gold" />
                    Massages
                </h4>
                <div class="space-y-4 text-sm text-alpine-muted font-light">
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Availability</span>
                        <span class="font-bold text-alpine-text">Every day</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Time slot</span>
                        <span class="font-bold text-alpine-text">10:00 – 20:00</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Booking</span>
                        <span class="font-bold text-alpine-text">At reception</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Recommended notice</span>
                        <span class="font-bold text-alpine-text">The day before</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Cancellation</span>
                        <span class="font-bold text-alpine-text">Free up to 6h before</span>
                    </div>
                    <div class="flex justify-between items-center">
                        <span>Packages</span>
                        <span class="font-bold text-alpine-text">3 sessions -15%</span>
                    </div>
                </div>
            </div>

            <!-- Private SPA -->
            <div class="fade-up-element bg-white p-10 border border-alpine-border">
                <h4 class="font-serif text-xl text-alpine-text mb-6 flex items-center gap-3">
                    <Lock class="w-5 h-5 text-alpine-gold" />
                    Private SPA
                </h4>
                <div class="space-y-4 text-sm text-alpine-muted font-light">
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Daytime slots</span>
                        <span class="font-bold text-alpine-text">10–12 / 14–16 / 17–19</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>By Night slot</span>
                        <span class="font-bold text-alpine-text">21:00 – 00:00</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Minimum notice</span>
                        <span class="font-bold text-alpine-text">24 hours</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Cancellation</span>
                        <span class="font-bold text-alpine-text">Free up to 24h before</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                        <span>Add-on massage</span>
                        <span class="font-bold text-alpine-text">Can be combined (-10%)</span>
                    </div>
                    <div class="flex justify-between items-center">
                        <span>Gift card</span>
                        <span class="font-bold text-alpine-text">Available at reception</span>
                    </div>
                </div>
            </div>
        </div>

        <div class="fade-up-element mt-8 bg-white p-10 border border-alpine-border">
            <h4 class="font-serif text-xl text-alpine-text mb-6 flex items-center gap-3">
                <ShieldCheck class="w-5 h-5 text-alpine-gold" />
                Good to Know
            </h4>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-x-12 gap-y-4 text-sm text-alpine-muted font-light">
                <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                    <span>Bathrobe</span>
                    <span class="font-bold text-alpine-text">Included in room</span>
                </div>
                <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                    <span>Swimsuit (Private SPA)</span>
                    <span class="font-bold text-alpine-text">Required</span>
                </div>
                <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                    <span>Recommended arrival</span>
                    <span class="font-bold text-alpine-text">10 min early</span>
                </div>
                <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                    <span>Minimum age</span>
                    <span class="font-bold text-alpine-text">16 years</span>
                </div>
                <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                    <span>Max guests (Private SPA)</span>
                    <span class="font-bold text-alpine-text">6 people</span>
                </div>
                <div class="flex justify-between items-center border-b border-alpine-border pb-3">
                    <span>Booking</span>
                    <span class="font-bold text-alpine-text">At reception</span>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════ RIEPILOGO PREZZI ═══════════════════ -->
<section class="border-y border-alpine-border bg-white py-20 px-6">
    <div class="max-w-4xl mx-auto">
        <div class="fade-up-element text-center mb-12">
            <h3 class="font-serif text-3xl text-alpine-text">Price Summary</h3>
        </div>
        <div class="fade-up-element border border-alpine-border divide-y divide-alpine-border">
            <div class="grid grid-cols-4 p-5 bg-alpine-bg">
                <span class="text-[10px] uppercase tracking-widest font-bold text-alpine-text">Treatment / Package</span>
                <span class="text-[10px] uppercase tracking-widest font-bold text-alpine-text text-center">Guests</span>
                <span class="text-[10px] uppercase tracking-widest font-bold text-alpine-text text-center">Duration</span>
                <span class="text-[10px] uppercase tracking-widest font-bold text-alpine-text text-right">Price</span>
            </div>
            <!-- Massaggi -->
            <div class="grid grid-cols-4 p-5 items-center">
                <p class="font-serif text-sm text-alpine-text">Ling Massage</p>
                <p class="text-sm text-alpine-muted font-light text-center">1</p>
                <p class="text-sm text-alpine-muted font-light text-center">1 hour</p>
                <p class="text-sm font-bold text-alpine-text text-right">€50</p>
            </div>
            <div class="grid grid-cols-4 p-5 items-center bg-alpine-bg/50">
                <p class="font-serif text-sm text-alpine-text">Anticellulite</p>
                <p class="text-sm text-alpine-muted font-light text-center">1</p>
                <p class="text-sm text-alpine-muted font-light text-center">1 hour</p>
                <p class="text-sm font-bold text-alpine-text text-right">€55</p>
            </div>
            <div class="grid grid-cols-4 p-5 items-center">
                <p class="font-serif text-sm text-alpine-text">Sports Deep Tissue</p>
                <p class="text-sm text-alpine-muted font-light text-center">1</p>
                <p class="text-sm text-alpine-muted font-light text-center">1 hour / 30 min</p>
                <p class="text-sm font-bold text-alpine-text text-right">€50 / €30</p>
            </div>
            <div class="grid grid-cols-4 p-5 items-center bg-alpine-bg/50">
                <p class="font-serif text-sm text-alpine-text">Foot Reflexology</p>
                <p class="text-sm text-alpine-muted font-light text-center">1</p>
                <p class="text-sm text-alpine-muted font-light text-center">30 min / 1 hour</p>
                <p class="text-sm font-bold text-alpine-text text-right">€30 / €45</p>
            </div>
            <div class="grid grid-cols-4 p-5 items-center">
                <p class="font-serif text-sm text-alpine-text">Kobido</p>
                <p class="text-sm text-alpine-muted font-light text-center">1</p>
                <p class="text-sm text-alpine-muted font-light text-center">30 min / 1 hour</p>
                <p class="text-sm font-bold text-alpine-text text-right">€30 / €50</p>
            </div>
            <div class="grid grid-cols-4 p-5 items-center bg-alpine-bg/50 border-l-4 border-l-alpine-gold">
                <div>
                    <p class="font-serif text-sm text-alpine-text">Terra & Cielo</p>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mt-1">Ritual</p>
                </div>
                <p class="text-sm text-alpine-muted font-light text-center">1</p>
                <p class="text-sm text-alpine-muted font-light text-center">1 hour</p>
                <p class="text-sm font-bold text-alpine-gold text-right">€55</p>
            </div>
            <!-- Divider -->
            <div class="grid grid-cols-4 p-4 bg-alpine-bg">
                <span class="text-[10px] uppercase tracking-widest font-bold text-alpine-gold col-span-4">Private SPA</span>
            </div>
            <div class="grid grid-cols-4 p-5 items-center">
                <p class="font-serif text-sm text-alpine-text">Romantic Escape</p>
                <p class="text-sm text-alpine-muted font-light text-center">2</p>
                <p class="text-sm text-alpine-muted font-light text-center">2 hours</p>
                <p class="text-sm font-bold text-alpine-text text-right">€180</p>
            </div>
            <div class="grid grid-cols-4 p-5 items-center bg-alpine-bg/50">
                <p class="font-serif text-sm text-alpine-text">Friends & Family</p>
                <p class="text-sm text-alpine-muted font-light text-center">3–6</p>
                <p class="text-sm text-alpine-muted font-light text-center">2 hours</p>
                <p class="text-sm font-bold text-alpine-text text-right">€280</p>
            </div>
            <div class="grid grid-cols-4 p-5 items-center border-l-4 border-l-alpine-gold">
                <div>
                    <p class="font-serif text-sm text-alpine-text">Private SPA by Night</p>
                    <p class="text-[10px] uppercase tracking-widest text-alpine-gold font-bold mt-1">Premium</p>
                </div>
                <p class="text-sm text-alpine-muted font-light text-center">2–4</p>
                <p class="text-sm text-alpine-muted font-light text-center">3 hours</p>
                <p class="text-sm font-bold text-alpine-gold text-right">€380</p>
            </div>
        </div>
        <p class="text-center text-[10px] uppercase tracking-widest text-alpine-muted font-bold mt-6">
            Private SPA packages: wine, food & amenities included · Prices per person
        </p>
    </div>
</section>

<!-- ═══════════════════ CTA ═══════════════════ -->
<section class="bg-[#0a0a0a] py-32 px-6">
    <div class="max-w-3xl mx-auto text-center">
        <div class="fade-up-element">
            <h2 class="font-serif text-4xl text-white mb-6">Your Wellbeing Awaits</h2>
            <p class="text-white/50 text-sm font-light leading-relaxed max-w-lg mx-auto mb-12">
                After a day in the mountains, treat yourself to the luxury of perfect recovery.
                Expert massages, private SPA and alpine renewal.
            </p>
            <a href="mailto:info@hoteldusoleiltorgnon.com" class="inline-flex items-center justify-center gap-3 bg-white text-alpine-text px-10 py-4 text-[11px] tracking-[0.2em] uppercase font-bold hover:bg-alpine-gold hover:text-white transition-all duration-300">
                Book at Reception <ArrowRight class="w-4 h-4" />
            </a>
        </div>
    </div>
</section>
