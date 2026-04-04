<script lang="ts">
    import { locale } from '$lib/i18n';
    import { PackageCheck, ShieldCheck, Snowflake, ArrowRight } from 'lucide-svelte';

    const copy = $derived($locale === 'ru'
        ? {
            title: 'Ski Box и прокат',
            heroLabel: 'Удобные и надежные сервисы',
            introTitle: 'Все, что нужно, уже ждет вас в отеле.',
            introText: 'Чтобы сделать отдых максимально удобным, мы сотрудничаем с лучшими пунктами проката Торньона и предоставляем теплую безопасную ski room для хранения вашего снаряжения.',
            boxTitle: 'Индивидуальные ski box',
            boxText: 'У каждого номера есть собственный шкаф в нашей ski room с кодовым доступом. Боксы оснащены таймерным подогревом, чтобы каждое утро вас ждали сухие и теплые ботинки.',
            boxItems: ['Прямой вход с улицы', 'Автоматический подогрев', 'Видеонаблюдение 24/7'],
            rentalTitle: 'Партнерский прокат',
            rentalText: 'Забронируйте лыжи, сноуборд или снегоступы у нашего партнера и избегайте очередей. Ваш комплект будет ждать вас прямо в боксе к моменту прибытия.',
            action: 'Забронировать снаряжение'
        }
        : {
            title: 'Ski Box & Noleggio',
            heroLabel: 'Servizi Comodi & Sicuri',
            introTitle: 'Tutto cio di cui hai bisogno proprio qui in hotel.',
            introText: 'Per offrirti la massima comodita, abbiamo attivato collaborazioni con i migliori noleggi di Torgnon e mettiamo a tua disposizione una ski room riscaldata e sicura dove depositare la tua attrezzatura.',
            boxTitle: 'Ski Box Privati',
            boxText: 'Ogni camera ha il proprio box riservato nella nostra Ski Room ad accesso codificato. I box sono dotati di riscaldamento temporizzato per garantirti scarponi asciutti e caldi ogni mattina.',
            boxItems: ["Accesso diretto dall'esterno", 'Riscaldamento automatico', 'Videosorveglianza 24h'],
            rentalTitle: 'Noleggio Partner',
            rentalText: 'Prenota la tua attrezzatura (sci, snowboard, ciaspole) tramite il nostro partner ed eviterai code inutili. Troverai i tuoi sci direttamente nel tuo box al tuo arrivo in hotel.',
            action: 'Prenota Attrezzatura'
        });
</script>

<svelte:head>
    <title>{copy.title} | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div class="absolute inset-0">
        <img src="https://images.unsplash.com/photo-1551698618-1fed5d97530d?q=80&w=2000&auto=format&fit=crop" class="ken-burns h-full w-full object-cover opacity-60" alt="Noleggio Sci Torgnon" />
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
        <PackageCheck class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            {copy.introTitle}
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            {copy.introText}
        </p>
    </div>
</section>

<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20">
    <div class="bg-white p-12 border border-alpine-border fade-up-element h-full">
        <ShieldCheck class="w-8 h-8 text-alpine-gold mb-6 stroke-[1.5px]" />
        <h4 class="font-serif text-3xl text-alpine-text mb-6">{copy.boxTitle}</h4>
        <p class="text-sm text-alpine-muted font-light leading-relaxed mb-8">
            {copy.boxText}
        </p>
        <ul class="space-y-4 text-xs tracking-widest uppercase font-bold text-alpine-gold">
            {#each copy.boxItems as item (item)}
             <li>- {item}</li>
            {/each}
        </ul>
    </div>
    <div class="bg-white p-12 border border-alpine-border fade-up-element h-full">
        <Snowflake class="w-8 h-8 text-alpine-gold mb-6 stroke-[1.5px]" />
        <h4 class="font-serif text-3xl text-alpine-text mb-6">{copy.rentalTitle}</h4>
        <p class="text-sm text-alpine-muted font-light leading-relaxed mb-8">
            {copy.rentalText}
        </p>
        <button class="inline-block border border-alpine-text text-alpine-text px-8 py-3 text-[10px] tracking-[0.2em] uppercase hover:bg-alpine-text hover:text-white transition-all font-bold">
            {copy.action} <ArrowRight class="w-4 h-4 ml-2 inline" />
        </button>
    </div>
</section>
