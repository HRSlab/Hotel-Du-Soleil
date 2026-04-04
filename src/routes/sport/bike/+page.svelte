<script lang="ts">
    import { locale } from '$lib/i18n';
    import { Bike, ShieldCheck, Sparkles } from 'lucide-svelte';

    const copy = $derived($locale === 'ru'
        ? {
            title: 'MTB и E-Bike',
            heroLabel: 'Педалирование в сердце Альп',
            introTitle: 'Откройте для себя километры панорамных маршрутов.',
            introText: 'От более техничных трасс до туристических маршрутов для всей семьи: Тоньон это рай для велосипедистов. А современные E-Bike делают горы доступными каждому, кто хочет наслаждаться природой без лишней нагрузки.',
            sectionTitle: 'Знаковые маршруты',
            routes: [
                { title: 'Тур вокруг Монте Дзербьон', text: 'Панорамный маршрут с обзором на центральную долину и Маттерхорн на 360°.' },
                { title: 'Кольцо альпийских пастбищ', text: 'Идеально для E-Bike: путь проходит через горные фермы, где можно попробовать Fontina DOP.' }
            ],
            servicesTitle: 'Bike Friendly сервисы',
            services: ['Безопасное велохранилище с видеонаблюдением', 'Мастерская для мелкого ремонта', 'Зона мойки велосипедов', 'Сотрудничество с сертифицированными гидами']
        }
        : {
            title: 'MTB & E-Bike',
            heroLabel: 'Pedalata nel Cuore delle Alpi',
            introTitle: 'Esplora chilometri di sentieri panoramici.',
            introText: 'Dai tracciati piu impegnativi ai percorsi turistici adatti a tutta la famiglia, Torgnon e un paradiso per i bikers. E con le moderne E-Bike, la montagna diventa accessibile a chiunque desideri godersi la natura senza eccessivo sforzo.',
            sectionTitle: 'Percorsi Iconici',
            routes: [
                { title: 'Tour del Monte Zerbion', text: 'Un percorso panoramico che offre una vista a 360° sulla valle centrale e il Cervino.' },
                { title: 'Anello degli Alpeggi', text: 'Perfetto per E-Bike, tocca diverse malghe dove e possibile degustare la Fontina DOP.' }
            ],
            servicesTitle: 'Servizi Bike Friendly',
            services: ['Deposito Bici sicuro e videosorvegliato', 'Officina per piccole manutenzioni', 'Zona lavaggio bici', 'Collaborazione con guide certificate']
        });
</script>

<svelte:head>
    <title>{copy.title} | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div class="absolute inset-0">
        <img src="https://images.unsplash.com/photo-1544191714-3d71bc294943?q=80&w=2000&auto=format&fit=crop" class="ken-burns h-full w-full object-cover opacity-80" alt="Mountain Bike a Torgnon" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/40 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            {copy.heroLabel}
        </span>
        <h1 class="font-serif text-5xl md:text-7xl leading-tight font-light text-white fade-up-element">
            {copy.title}
        </h1>
    </div>
</header>

<section class="bg-alpine-bg px-6 py-24">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <Bike class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            {copy.introTitle}
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            {copy.introText}
        </p>
    </div>
</section>

<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto space-y-12">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20 items-center">
         <div class="fade-up-element">
            <h4 class="font-serif text-4xl text-alpine-text mb-6 italic">{copy.sectionTitle}</h4>
            <div class="space-y-10">
                 <div class="flex items-start gap-4 border-b border-alpine-border pb-6">
                    <div class="w-2 h-2 rounded-full bg-alpine-gold mt-2 shrink-0"></div>
                    <div>
                         <h5 class="text-lg font-serif italic text-alpine-text mb-2">{copy.routes[0].title}</h5>
                         <p class="text-xs text-alpine-muted leading-relaxed font-light">{copy.routes[0].text}</p>
                    </div>
                 </div>
                 <div class="flex items-start gap-4 border-b border-alpine-border pb-6">
                    <div class="w-2 h-2 rounded-full bg-alpine-gold mt-2 shrink-0"></div>
                    <div>
                         <h5 class="text-lg font-serif italic text-alpine-text mb-2">{copy.routes[1].title}</h5>
                         <p class="text-xs text-alpine-muted leading-relaxed font-light">{copy.routes[1].text}</p>
                    </div>
                 </div>
            </div>
         </div>
         <div class="fade-up-element bg-white p-12 border border-alpine-border">
            <div class="flex items-center gap-4 mb-6"><ShieldCheck class="w-6 h-6 text-alpine-gold" /><h4 class="text-[12px] uppercase font-bold tracking-[0.2em] text-alpine-text">{copy.servicesTitle}</h4></div>
            <ul class="space-y-4 text-sm font-light text-alpine-muted">
                {#each copy.services as service (service)}
                    <li class="flex items-center gap-3"><Sparkles class="w-4 h-4 text-alpine-gold/50 shrink-0" /> {service}</li>
                {/each}
            </ul>
         </div>
    </div>
</section>
