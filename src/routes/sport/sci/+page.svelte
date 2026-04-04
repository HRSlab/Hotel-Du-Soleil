/* eslint-disable svelte/require-each-key */
/* eslint-disable svelte/require-each-key */
<script lang="ts">
    import { locale } from '$lib/i18n';
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

    // Enforce no vertical/horizontal overflow while this page is mounted
    $effect(() => {
        const previousOverflowY = document.body.style.overflowY;
        const previousOverflowX = document.body.style.overflowX;
        document.body.style.overflowY = 'hidden';
        document.body.style.overflowX = 'hidden';

        return () => {
            document.body.style.overflowY = previousOverflowY || '';
            document.body.style.overflowX = previousOverflowX || '';
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

    const copy = $derived($locale === 'ru'
        ? {
            title: 'Лыжи и сноуборд',
            heroLabel: 'SKI-IN SKI-OUT',
            heroText: 'Всего в 50 метрах от подъемников Торньона. Испытайте первоклассные трассы под взглядом Маттерхорна.',
            sideTitle: 'Солнечные склоны',
            sideText: 'Горнолыжная зона Торньона предлагает идеально подготовленные трассы для любого уровня с захватывающими видами от Маттерхорна до Монте-Роза.',
            expLabel: 'ВПЕЧАТЛЕНИЕ',
            expTitle: 'Чистое альпийское приключение',
            features: [
                { title: 'Трассы для любого уровня', text: 'От мягких учебных склонов до сложных черных трасс: здесь комфортно и новичкам, и опытным лыжникам.' },
                { title: 'Фрирайд с гидом', text: 'Исследуйте свежий снег с сертифицированными гидами и открывайте безопасные и незабываемые маршруты вне трасс.' },
                { title: 'Snow Park', text: 'Современный snow park с трамплинами, рейлами и зонами для freestyle-катания на лыжах и сноуборде.' }
            ],
            servicesLabel: 'ПРЕМИУМ-СЕРВИС',
            servicesTitle: 'Удобства Ski Club',
            services: [
                { title: 'Надежное хранение лыж', text: 'Лыжная комната с видеонаблюдением, персональными шкафчиками и зоной подогрева ботинок.' },
                { title: 'Сервис оборудования', text: 'Профессиональная подготовка лыж, waxing и прокат оборудования через наших партнеров.' },
                { title: 'Сертифицированные инструкторы', text: 'Сотрудничество с лыжными школами для индивидуальных и групповых занятий.' }
            ],
            galleryLabel: 'ВИЗУАЛЬНОЕ ПУТЕШЕСТВИЕ',
            galleryTitle: 'Проживите снег',
            galleryText: 'Прокручивайте галерею по горизонтали и открывайте нашу зимнюю вселенную через альпийские фотографии.'
        }
        : {
            title: 'Ski & Snowboard',
            heroLabel: 'SKI-IN SKI-OUT',
            heroText: 'Just 50 meters from the Torgnon ski lifts. Experience world-class slopes in the shadow of the Matterhorn.',
            sideTitle: 'Sun-Kissed Slopes',
            sideText: "Torgnon's ski area offers perfectly groomed pistes for all levels, surrounded by breathtaking views from the Matterhorn to Monte Rosa.",
            expLabel: 'THE EXPERIENCE',
            expTitle: 'Pure Alpine Adventure',
            features: [
                { title: 'Slopes for Every Level', text: 'From gentle beginner trails to challenging black runs, our ski area caters to all abilities with professional instruction available.' },
                { title: 'Guided Off-Piste', text: 'Explore fresh powder with our certified guides for safe and unforgettable backcountry experiences.' },
                { title: 'Snow Park Excellence', text: 'State-of-the-art snow park with jumps, rails, and halfpipe for freestyle skiing and snowboarding.' }
            ],
            servicesLabel: 'PREMIUM SERVICES',
            servicesTitle: 'Ski Club Amenities',
            services: [
                { title: 'Secure Ski Storage', text: 'CCTV-monitored ski room with individual lockers and boot warming area.' },
                { title: 'Equipment Services', text: 'Professional ski tuning, waxing, and on-site rental equipment.' },
                { title: 'Certified Instruction', text: 'Partnered with certified ski schools for private and group lessons.' }
            ],
            galleryLabel: 'VISUAL JOURNEY',
            galleryTitle: 'Live the Snow',
            galleryText: 'Scroll horizontally to explore our winter wonderland through stunning alpine photography'
        });
</script>

<svelte:head>
    <title>{copy.title} | Hotel du Soleil</title>
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
                {copy.heroLabel}
            </span>
            <h1 class="font-serif text-6xl md:text-8xl leading-none font-light text-white fade-up-element mb-8">
                {copy.title}
            </h1>
            <p class="text-white/80 text-lg font-light leading-relaxed max-w-lg fade-up-element">
                {copy.heroText}
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
                        {copy.sideTitle}
                    </h3>
                    <p class="text-alpine-muted font-light leading-relaxed text-sm">
                        {copy.sideText}
                    </p>
                </div>
            </div>

            <div class="md:w-3/5 md:pr-24 fade-up-element md:mt-24">
                <div class="mb-16">
                    <span class="text-[10px] uppercase tracking-[0.3em] text-alpine-gold font-bold mb-8 block">
                        {copy.expLabel}
                    </span>
                    <h2 class="font-serif text-5xl md:text-6xl text-alpine-text font-light leading-tight mb-12">
                        {copy.expTitle}
                    </h2>
                </div>

                <div class="space-y-12">
                    <div class="border-l-2 border-alpine-gold pl-8">
                        <h4 class="font-serif text-2xl text-alpine-text mb-4 italic">{copy.features[0].title}</h4>
                        <p class="text-alpine-muted font-light leading-relaxed">
                            {copy.features[0].text}
                        </p>
                    </div>

                    <div class="border-l-2 border-alpine-gold pl-8">
                        <h4 class="font-serif text-2xl text-alpine-text mb-4 italic">{copy.features[1].title}</h4>
                        <p class="text-alpine-muted font-light leading-relaxed">
                            {copy.features[1].text}
                        </p>
                    </div>

                    <div class="border-l-2 border-alpine-gold pl-8">
                        <h4 class="font-serif text-2xl text-alpine-text mb-4 italic">{copy.features[2].title}</h4>
                        <p class="text-alpine-muted font-light leading-relaxed">
                            {copy.features[2].text}
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
                {copy.servicesLabel}
            </span>
            <h2 class="font-serif text-4xl md:text-5xl text-white font-light">
                {copy.servicesTitle}
            </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="bg-white/5 backdrop-blur-sm border border-white/10 p-8 fade-up-element">
                <ShieldCheck class="w-6 h-6 text-alpine-gold mb-6" />
                <h4 class="text-white text-lg font-serif mb-4">{copy.services[0].title}</h4>
                <p class="text-white/70 font-light text-sm leading-relaxed">
                    {copy.services[0].text}
                </p>
            </div>

            <div class="bg-white/5 backdrop-blur-sm border border-white/10 p-8 fade-up-element md:mt-12">
                <Sparkles class="w-6 h-6 text-alpine-gold mb-6" />
                <h4 class="text-white text-lg font-serif mb-4">{copy.services[1].title}</h4>
                <p class="text-white/70 font-light text-sm leading-relaxed">
                    {copy.services[1].text}
                </p>
            </div>

            <div class="bg-white/5 backdrop-blur-sm border border-white/10 p-8 fade-up-element md:mt-24">
                <Mountain class="w-6 h-6 text-alpine-gold mb-6" />
                <h4 class="text-white text-lg font-serif mb-4">{copy.services[2].title}</h4>
                <p class="text-white/70 font-light text-sm leading-relaxed">
                    {copy.services[2].text}
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
                {copy.galleryLabel}
            </span>
            <h2 class="font-serif text-5xl md:text-6xl text-alpine-text font-light leading-tight">
                {copy.galleryTitle}
            </h2>
        </div>

        <!-- Horizontal scroll container with smooth scrolling -->
        <div class="overflow-x-auto scrollbar-hide pb-8 px-2">
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
                {copy.galleryText}
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

