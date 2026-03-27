/* eslint-disable svelte/require-each-key */
/* eslint-disable svelte/require-each-key */
<script lang="ts">
    import { Snowflake, ShieldCheck, Sparkles, Mountain } from 'lucide-svelte';

    // Svelte 5 reactivity for scroll-based animations
    let scrollY = $state(0);
    let heroRef: HTMLElement;
    let observer: IntersectionObserver;

    // Remove complex gallery state and animation code
    // Keeping only essential scroll and observer

    // Gallery images - simplified premium horizontal scroll
    let galleryImages = $state([
        { src: '/imgs/skier-torgnon.webp', alt: 'Skier in Torgnon' },
        { src: '/imgs/Ski_slope.webp', alt: 'Slopes From Torgnon' },
        { src: '/imgs/ski-gondola-view.webp', alt: 'View from the gondola' },
        { src: '/imgs/slope-torgnon.webp', alt: 'Torgnon slope' },
        { src: '/imgs/ski-ome-activities.webp', alt: 'Winter activities' },
        { src: '/imgs/ski-sport-hero.webp', alt: 'Winter sports' },
        { src: '/imgs/torgnon-view.webp', alt: 'Torgnon view' }
    ]);

    // Remove lerp and animate functions - using simple scroll

    // Intersection Observer for fade-ups
    $effect(() => {
        observer = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('animate-fade-up');
                    }
                });
            },
            { threshold: 0.1, rootMargin: '0px 0px -100px 0px' }
        );

        const fadeElements = document.querySelectorAll('.fade-up-element');
        fadeElements.forEach((el) => observer.observe(el));

        return () => {
            if (observer) {
                observer.disconnect();
            }
        };
    });



    // Scroll handler for parallax
    $effect(() => {
        const handleScroll = () => {
            scrollY = window.scrollY;
        };

        window.addEventListener('scroll', handleScroll);

        return () => {
            window.removeEventListener('scroll', handleScroll);
        };
    });
</script>

<svelte:head>
    <title>Ski & Snowboard | Hotel du Soleil</title>
</svelte:head>

<!-- Hero Section with Parallax -->
<header
    bind:this={heroRef}
    class="relative h-[80vh] w-full overflow-hidden bg-[#1a1a1a]"
    style="transform: scale({1 + scrollY * 0.0002})"
>
    <div class="absolute inset-0">
        <img
            src="/imgs/torgnon-view.webp"
            class="h-full w-full object-cover"
            alt="Ski in Torgnon"
            style="transform: scale({1 + scrollY * 0.0001})"
        />
        <div class="absolute inset-0 bg-linear-to-b from-black/90 via-black/50 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col justify-end px-6 pb-32 md:pb-40">
        <div class="max-w-4xl">
            <span class="mb-6 block text-[10px] font-bold tracking-[0.4em] text-white/70 uppercase fade-up-element">
                SKI-IN SKI-OUT
            </span>
            <h1 class="font-serif text-6xl md:text-8xl leading-none font-light text-white fade-up-element mb-8">
                Ski &<br/>Snowboard
            </h1>
            <p class="text-white/80 text-lg font-light leading-relaxed max-w-lg fade-up-element">
                Just 50 meters from the Torgnon ski lifts. Experience world-class slopes in the shadow of the Matterhorn.
            </p>
        </div>
    </div>
</header>

<!-- Asymmetrical Content Section -->
<section class="bg-alpine-bg px-6 py-32 relative">
    <div class="max-w-7xl mx-auto">
        <!-- Overlapping layout -->
        <div class="relative">
            <div class="md:absolute md:right-0 md:top-0 md:w-2/5 fade-up-element">
                <div class="bg-white p-12 border border-alpine-border shadow-2xl">
                    <Snowflake class="w-8 h-8 text-alpine-gold mb-6" strokeWidth={1} />
                    <h3 class="font-serif text-2xl text-alpine-text mb-4 italic">
                        Sun-Kissed Slopes
                    </h3>
                    <p class="text-alpine-muted font-light leading-relaxed text-sm">
                        Torgnon's ski area offers perfectly groomed pistes for all levels, surrounded by breathtaking views from the Matterhorn to Monte Rosa.
                    </p>
                </div>
            </div>

            <div class="md:w-3/5 md:pr-24 fade-up-element md:mt-24">
                <div class="mb-16">
                    <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-8 block">
                        THE EXPERIENCE
                    </span>
                    <h2 class="font-serif text-5xl md:text-6xl text-alpine-text font-light leading-tight mb-12">
                        Pure Alpine<br/>Adventure
                    </h2>
                </div>

                <div class="space-y-12">
                    <div class="border-l-2 border-alpine-gold pl-8">
                        <h4 class="font-serif text-2xl text-alpine-text mb-4 italic">Slopes for Every Level</h4>
                        <p class="text-alpine-muted font-light leading-relaxed">
                            From gentle beginner trails to challenging black runs, our ski area caters to all abilities with professional instruction available.
                        </p>
                    </div>

                    <div class="border-l-2 border-alpine-gold pl-8">
                        <h4 class="font-serif text-2xl text-alpine-text mb-4 italic">Guided Off-Piste</h4>
                        <p class="text-alpine-muted font-light leading-relaxed">
                            Explore fresh powder with our certified guides for safe and unforgettable backcountry experiences.
                        </p>
                    </div>

                    <div class="border-l-2 border-alpine-gold pl-8">
                        <h4 class="font-serif text-2xl text-alpine-text mb-4 italic">Snow Park Excellence</h4>
                        <p class="text-alpine-muted font-light leading-relaxed">
                            State-of-the-art snow park with jumps, rails, and halfpipe for freestyle skiing and snowboarding.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Services Section -->
<section class="bg-[#050505] px-6 py-32">
    <div class="max-w-6xl mx-auto">
        <div class="text-center mb-20 fade-up-element">
            <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-6 block">
                PREMIUM SERVICES
            </span>
            <h2 class="font-serif text-4xl md:text-5xl text-white font-light">
                Ski Club Amenities
            </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="bg-white/5 backdrop-blur-sm border border-white/10 p-8 fade-up-element">
                <ShieldCheck class="w-6 h-6 text-alpine-gold mb-6" />
                <h4 class="text-white text-lg font-serif mb-4">Secure Ski Storage</h4>
                <p class="text-white/70 font-light text-sm leading-relaxed">
                    CCTV-monitored ski room with individual lockers and boot warming area.
                </p>
            </div>

            <div class="bg-white/5 backdrop-blur-sm border border-white/10 p-8 fade-up-element md:mt-12">
                <Sparkles class="w-6 h-6 text-alpine-gold mb-6" />
                <h4 class="text-white text-lg font-serif mb-4">Equipment Services</h4>
                <p class="text-white/70 font-light text-sm leading-relaxed">
                    Professional ski tuning, waxing, and on-site rental equipment.
                </p>
            </div>

            <div class="bg-white/5 backdrop-blur-sm border border-white/10 p-8 fade-up-element md:mt-24">
                <Mountain class="w-6 h-6 text-alpine-gold mb-6" />
                <h4 class="text-white text-lg font-serif mb-4">Certified Instruction</h4>
                <p class="text-white/70 font-light text-sm leading-relaxed">
                    Partnered with certified ski schools for private and group lessons.
                </p>
            </div>
        </div>
    </div>
</section>

<!-- Premium Horizontal Scroll Gallery -->
<section class="bg-alpine-bg px-6 py-32 relative overflow-hidden">
    <div class="max-w-7xl mx-auto">
        <div class="mb-20 fade-up-element">
            <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-6 block">
                VISUAL JOURNEY
            </span>
            <h2 class="font-serif text-5xl md:text-6xl text-alpine-text font-light leading-tight">
                Live the<br/>Snow
            </h2>
        </div>

        <!-- Horizontal scroll container with smooth scrolling -->
        <div class="overflow-x-auto scrollbar-hide pb-8 px-2 w-full max-w-full">
            <div class="inline-flex items-stretch gap-8 w-max py-4">
                {#each galleryImages as item (item.src)}
                    <div
                        class="min-w-[70vw] md:min-w-[42vw] lg:min-w-[34vw] xl:min-w-[28vw] h-[55vh] rounded-3xl overflow-hidden border border-alpine-border bg-[#0b0b0b] shadow-2xl"
                    >
                        <img
                            src={item.src}
                            alt={item.alt}
                            class="h-full w-full object-cover transition-transform duration-700 hover:scale-105"
                            loading="lazy"
                        />
                    </div>
                {/each}
            </div>
        </div>

        <div class="text-center mt-12 fade-up-element">
            <p class="text-alpine-muted font-light text-sm max-w-md mx-auto">
                Scroll horizontally to explore our winter wonderland through stunning alpine photography
            </p>
            <!-- Scroll indicator -->
            <div class="flex justify-center mt-6">
                <div class="flex space-x-2">
                    <div class="w-2 h-2 bg-alpine-gold rounded-full animate-pulse"></div>
                    <div class="w-2 h-2 bg-alpine-gold/50 rounded-full"></div>
                    <div class="w-2 h-2 bg-alpine-gold/30 rounded-full"></div>
                </div>
            </div>
        </div>
    </div>
</section>

<style>
    :global(.animate-fade-up) {
        animation: fadeUp 1s ease-out forwards;
    }

    @keyframes fadeUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* Hide scrollbar for horizontal scroll gallery */
    .scrollbar-hide {
        -ms-overflow-style: none;
        scrollbar-width: none;
    }
    .scrollbar-hide::-webkit-scrollbar {
        display: none;
    }
</style>

