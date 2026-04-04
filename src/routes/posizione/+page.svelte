<script lang="ts">
    import { t, locale } from '$lib/i18n';
    import { MapPin, Mountain, Car, Train, Plane, Map } from 'lucide-svelte';

    const copy = $derived($locale === 'ru' ? { region: 'Торньон, Валле-д’Аоста' } : { region: "Torgnon, Valle d'Aosta" });
</script>

<svelte:head>
    <title>{$t('posizione.title')} | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div class="absolute inset-0">
        <img src="https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=2000&auto=format&fit=crop" class="ken-burns h-full w-full object-cover opacity-80" alt="Mountain Landscape around Torgnon" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/40 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            {$t('posizione.subtitle')}
        </span>
        <h1 class="font-serif text-5xl md:text-7xl leading-tight font-light text-white fade-up-element">
            {$t('posizione.title')}
        </h1>
    </div>
</header>

<section class="bg-alpine-bg px-6 py-24">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <MapPin class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            {$t('posizione.philosophy_title')}
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            {$t('posizione.philosophy_text')}
        </p>
    </div>
</section>

<section class="bg-alpine-bg pb-24 px-6 max-w-7xl mx-auto">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center border-b border-alpine-border pb-24">
        <div class="fade-up-element overflow-hidden bg-alpine-border relative group">
            <img src="/imgs/map-hds.webp" alt="Esterno Hotel du Soleil" class="w-full h-full object-cover img-elegant aspect-4/3 grayscale group-hover:grayscale-0 transition-all duration-700">
        </div>
        <div class="fade-up-element">
            <Mountain class="w-8 h-8 text-alpine-gold mb-6 stroke-[1.5px]" />
            <h2 class="font-serif text-4xl text-alpine-text mb-6">{$t('posizione.arrival_title')}</h2>
            <p class="text-alpine-muted text-sm font-light leading-relaxed mb-10">
                {$t('posizione.arrival_text')}
            </p>
            
            <a href="https://maps.google.com/?q=Hotel+du+Soleil+Torgnon" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-3 text-xs tracking-widest uppercase font-bold text-alpine-text border border-alpine-text px-8 py-4 hover:bg-alpine-text hover:text-white transition-colors">
                <Map class="w-4 h-4" /> {$t('posizione.maps_cta')}
            </a>
        </div>
    </div>
</section>

<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto">
    
    <div class="fade-up-element text-center mb-16">
        <h2 class="font-serif text-3xl md:text-4xl text-alpine-text mb-4">{$t('posizione.directions_title')}</h2>
        <p class="text-[10px] uppercase tracking-widest text-alpine-muted">{copy.region}</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-12 fade-up-element">
        
        <div class="text-center p-8 bg-white border border-alpine-border">
            <Car class="w-6 h-6 text-alpine-gold mx-auto mb-6" />
            <h4 class="font-serif text-2xl text-alpine-text mb-4">{$t('posizione.by_car_title')}</h4>
            <p class="text-xs text-alpine-muted font-light leading-relaxed">
                {$t('posizione.by_car_text')}
            </p>
        </div>

        <div class="text-center p-8 bg-white border border-alpine-border">
            <Train class="w-6 h-6 text-alpine-gold mx-auto mb-6" />
            <h4 class="font-serif text-2xl text-alpine-text mb-4">{$t('posizione.by_train_title')}</h4>
            <p class="text-xs text-alpine-muted font-light leading-relaxed">
                {$t('posizione.by_train_text')}
            </p>
        </div>

        <div class="text-center p-8 bg-white border border-alpine-border">
            <Plane class="w-6 h-6 text-alpine-gold mx-auto mb-6" />
            <h4 class="font-serif text-2xl text-alpine-text mb-4">{$t('posizione.by_plane_title')}</h4>
            <p class="text-xs text-alpine-muted font-light leading-relaxed">
                {$t('posizione.by_plane_text')}
            </p>
        </div>

    </div>

    <div class="mt-24 max-w-3xl mx-auto fade-up-element">
        <h4 class="text-[10px] font-bold uppercase tracking-[0.2em] text-alpine-text mb-8 text-center border-b border-alpine-border pb-4">
            {$t('posizione.distances_title')}
        </h4>
        
        <div class="space-y-4">
            <div class="flex items-baseline justify-between text-alpine-text text-sm">
                <span class="font-medium">{$t('posizione.dist_ski')}</span>
                <div class="grow border-b border-dotted border-alpine-border mx-4 relative top-[-4px]"></div>
                <span class="text-alpine-gold font-bold">20 m</span>
            </div>
            <div class="flex items-baseline justify-between text-alpine-text text-sm">
                <span class="font-medium">{$t('posizione.dist_cervinia')}</span>
                <div class="grow border-b border-dotted border-alpine-border mx-4 relative top-[-4px]"></div>
                <span class="text-alpine-gold font-bold">22 km</span>
            </div>
            <div class="flex items-baseline justify-between text-alpine-text text-sm">
                <span class="font-medium">{$t('posizione.dist_aosta')}</span>
                <div class="grow border-b border-dotted border-alpine-border mx-4 relative top-[-4px]"></div>
                <span class="text-alpine-gold font-bold">45 km</span>
            </div>
            <div class="flex items-baseline justify-between text-alpine-text text-sm">
                <span class="font-medium">{$t('posizione.dist_milano')}</span>
                <div class="grow border-b border-dotted border-alpine-border mx-4 relative top-[-4px]"></div>
                <span class="text-alpine-gold font-bold">160 km</span>
            </div>
        </div>
    </div>

</section>