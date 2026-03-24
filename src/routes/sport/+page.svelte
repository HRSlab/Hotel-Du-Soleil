<script lang="ts">
    import { t } from '$lib/i18n';
    import { Snowflake, Bike, Mountain, Wind, Map, Compass, ChevronDown, Check } from 'lucide-svelte';
    import { Motion } from 'svelte-motion';

    // Varianti per le animazioni di orchestrazione (stagger)
    // Questo crea l'effetto "rivelazione a cascata" tipico dei siti premiati
    const containerVariants = {
        hidden: { opacity: 0 },
        visible: {
            opacity: 1,
            transition: {
                staggerChildren: 0.2 // Ritardo tra un elemento figlio e l'altro
            }
        }
    };

    const itemVariants = {
        hidden: { y: 60, opacity: 0 },
        visible: {
            y: 0,
            opacity: 1,
            transition: {
                duration: 1.1,
                ease: [0.22, 1, 0.36, 1] // Quintic ease-out per un movimento organico
            }
        }
    };

    // Effetto Parallasse per l'Hero Image
    let scrollY = $state(0);
</script>

<svelte:window bind:scrollY />

<svelte:head>
    <title>{$t('sport.main_title')} | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[85vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div 
        class="absolute inset-0 scale-110"
        style="transform: translateY({scrollY * 0.3}px) scale(1.1);"
    >
        <img 
            src="/imgs/sport_hero.png" 
            alt="Alpine Sport" 
            class="w-full h-full object-cover ken-burns opacity-70"
        >
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/20 to-alpine-bg"></div>
    </div>
    
    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-32 text-center">
        <Motion initial="hidden" animate="visible" variants={containerVariants}>
            <div>
                <Motion variants={itemVariants}>
                    <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs">
                        {$t('sport.main_subtitle')}
                    </span>
                </Motion>
                <Motion variants={itemVariants}>
                    <h1 class="font-serif text-5xl md:text-8xl text-white font-light tracking-tight leading-none mb-16">
                        {$t('sport.main_title')}
                    </h1>
                </Motion>
                <Motion variants={itemVariants}>
                    <div class="w-full flex justify-center">
                        <ChevronDown class="w-10 h-10 text-alpine-gold animate-bounce" strokeWidth={1} />
                    </div>
                </Motion>
            </div>
        </Motion>
    </div>
</header>

<!-- @ts-ignore -->
<Motion initial="hidden" whileInView="visible" viewport={{ once: true, amount: 0.3 }} variants={itemVariants}>
    <section class="bg-alpine-bg px-6 py-32 border-b border-alpine-border">
        <div class="mx-auto max-w-3xl text-center">
            <Compass class="w-12 h-12 text-alpine-gold mx-auto mb-12" strokeWidth={1} />
            <h3 class="mb-12 font-serif text-3xl leading-snug text-alpine-text md:text-5xl lg:text-6xl max-w-xl mx-auto">
                {$t('sport.philosophy_title')}
            </h3>
            <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-lg border-t border-alpine-border pt-16 mt-16 mx-auto max-w-2xl">
                {$t('sport.philosophy_text')}
            </p>
        </div>
    </section>
</Motion>

<section class="bg-alpine-bg pb-32 px-6 max-w-360 mx-auto space-y-32 pt-32">

    <!-- @ts-ignore -->
    <Motion initial="hidden" whileInView="visible" viewport={{ once: true, amount: 0.3 }} variants={itemVariants}>
        <div class="flex flex-col md:flex-row gap-16 lg:gap-24 items-center">
            <div class="w-full md:w-3/5 overflow-hidden bg-alpine-border relative group cursor-default shadow-xl">
                <img src="https://www.lovevda.it/immagini/DisplayImage/61122?width=1920&guid=74950a9e-1379-467a-8149-9b31b6ae6ff1" alt="Sci a Torgnon" class="w-full h-full object-cover img-elegant aspect-16/10">
                <div class="absolute inset-0 bg-black/10 opacity-0 group-hover:opacity-100 transition-opacity"></div>
            </div>
            <div class="w-full md:w-2/5 p-4 lg:p-10">
                <Snowflake class="w-10 h-10 text-alpine-gold mb-8 stroke-1" />
                <h2 class="font-serif text-4xl lg:text-5xl text-alpine-text mb-6">{$t('sport.sci.title')}</h2>
                <p class="text-[11px] uppercase tracking-widest text-alpine-muted mb-8 font-bold">Ski-in / Ski-out Resort</p>
                <p class="text-alpine-muted text-sm md:text-base font-light leading-relaxed mb-12 max-w-md">
                    {$t('sport.sci.subtitle')}
                </p>
                <!-- @ts-ignore -->
                <Motion initial="hidden" whileInView="visible" viewport={{ once: true, amount: 0.8 }} variants={containerVariants}>
                    <ul class="space-y-5 text-sm font-medium text-alpine-text mb-12">
                        {#each ['Accesso diretto agli impianti', 'Ski Room e Deposito Scarponi Riscaldato', 'Skipass in Reception'] as service (service)}
                            <Motion variants={itemVariants}>
                                <li class="flex items-center gap-4 border-b border-alpine-border pb-4">
                                    <div class="w-6 h-6 rounded-full bg-alpine-gold/10 flex items-center justify-center">
                                        <Check class="w-4 h-4 text-alpine-gold" strokeWidth={3} />
                                    </div>
                                    {service}
                                </li>
                            </Motion>
                        {/each}
                    </ul>
                </Motion>
            </div>
        </div>
    </Motion>

    <!-- @ts-ignore -->
    <Motion initial="hidden" whileInView="visible" viewport={{ once: true, amount: 0.3 }} variants={itemVariants}>
        <div class="flex flex-col md:flex-row-reverse gap-16 lg:gap-24 items-center">
            <div class="w-full md:w-3/5 overflow-hidden bg-alpine-border relative group cursor-default shadow-xl">
                <img src="/imgs/MTB-Torgnon.png" alt="Mountain Bike" class="w-full h-full object-cover img-elegant aspect-16/10">
                <div class="absolute inset-0 bg-black/10 opacity-0 group-hover:opacity-100 transition-opacity"></div>
            </div>
            <div class="w-full md:w-2/5 p-4 lg:p-10">
                <Bike class="w-10 h-10 text-alpine-gold mb-8 stroke-1" />
                <h2 class="font-serif text-4xl lg:text-5xl text-alpine-text mb-6">{$t('sport.bike.title')}</h2>
                <p class="text-[11px] uppercase tracking-widest text-alpine-muted mb-8 font-bold">E-Bike & Trekking</p>
                <p class="text-alpine-muted text-sm md:text-base font-light leading-relaxed mb-12 max-w-md">
                    {$t('sport.bike.subtitle')}
                </p>
                <!-- @ts-ignore -->
                <Motion initial="hidden" whileInView="visible" viewport={{ once: true, amount: 0.8 }} variants={containerVariants}>
                    <ul class="space-y-5 text-sm font-medium text-alpine-text mb-12">
                        {#each ['Noleggio E-Bike convenzionato', 'Bike Room sicura con area lavaggio', 'Mappe e sentieri GPX'] as service (service)}
                            <Motion variants={itemVariants}>
                                <li class="flex items-center gap-4 border-b border-alpine-border pb-4">
                                    <div class="w-6 h-6 rounded-full bg-alpine-gold/10 flex items-center justify-center">
                                        <Check class="w-4 h-4 text-alpine-gold" strokeWidth={3} />
                                    </div>
                                    {service}
                                </li>
                            </Motion>
                        {/each}
                    </ul>
                </Motion>
            </div>
        </div>
    </Motion>

</section>

<section class="border-t border-alpine-border bg-white py-32 px-6">
    <div class="max-w-screen-2xl mx-auto">
        <!-- @ts-ignore -->
        <Motion initial="hidden" whileInView="visible" viewport={{ once: true, amount: 0.3 }} variants={itemVariants}>
            <div class="text-center mb-24 max-w-xl mx-auto">
                <h2 class="font-serif text-4xl md:text-5xl text-alpine-text mb-5 leading-tight">Servizi per lo Sportivo</h2>
                <p class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">Tutto ciò che ti serve, in un solo posto</p>
            </div>
        </Motion>

        <!-- @ts-ignore -->
        <Motion initial="hidden" whileInView="visible" viewport={{ once: true, amount: 0.1 }} variants={containerVariants}>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12">
                {#each [
                    { icon: Wind, title: 'Ski Room & Dry', text: 'Armadietti privati e sistema di asciugatura e riscaldamento per scarponi, sempre pronti.' },
                    { icon: Map, title: 'Guide Partner', text: 'Collaboriamo con le migliori guide locali per freeride invernale e scalate estive.' },
                    { icon: Mountain, title: 'Colazione Bio', text: 'Buffet mattutino rinforzato con proteine e carboidrati studiati per chi fa sport.' }
                ] as { icon: Icon, title, text } (title)}
                    <Motion variants={itemVariants}>
                        <div class="text-center p-12 md:p-16 border border-alpine-border bg-white hover:border-alpine-gold hover:shadow-2xl transition-all duration-500 flex flex-col items-center">
                            <Icon class="w-8 h-8 text-alpine-gold mb-8 stroke-1" />
                            <h4 class="font-serif text-3xl text-alpine-text mb-6">{title}</h4>
                            <p class="text-xs lg:text-sm text-alpine-muted font-light leading-relaxed max-w-xs mx-auto">
                                {text}
                            </p>
                        </div>
                    </Motion>
                {/each}
            </div>
        </Motion>
    </div>
</section>