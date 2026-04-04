<script lang="ts">
    import { locale } from '$lib/i18n';
    import { ShieldCheck, Mountain, Users } from 'lucide-svelte';

    const copy = $derived($locale === 'ru'
        ? {
            title: 'Партнерские горные гиды',
            heroLabel: 'Эксперты гор',
            introTitle: 'Ваша безопасность для нас абсолютный приоритет.',
            introText: 'Мы сотрудничаем с лучшими горными гидами Валле-д’Аоста, чтобы предложить вам безопасные и вдохновляющие маршруты. Наши профессионалы знают здесь каждый склон и проведут вас к местам, скрытым от большинства гостей.',
            cards: [
                { title: 'Альпинизм и freeride', text: 'Бронируйте высокогорное восхождение или безопасный выход за пределы трасс, чтобы почувствовать настоящий freeride на свежем снегу.', label: 'По предварительному бронированию' },
                { title: 'Групповые экскурсии', text: 'Присоединяйтесь к ежедневным прогулкам с гидом, чтобы открыть местную флору и фауну вместе с другими гостями отеля.', label: 'Включено для клиентов Premium' }
            ]
        }
        : {
            title: 'Guide Alpine Partner',
            heroLabel: 'Esperti della Montagna',
            introTitle: 'La vostra sicurezza e per noi una priorita assoluta.',
            introText: 'Collaboriamo con le migliori guide alpine della Valle d\'Aosta per offrirvi escursioni sicure ed emozionanti. I nostri professionisti conoscono ogni anfratto di queste montagne e vi condurranno a scoprire luoghi invisibili ai piu.',
            cards: [
                { title: 'Alpinismo & Freeride', text: 'Prenotate un\'uscita di alpinismo d\'alta quota o fatevi accompagnare in sicurezza fuori dalle piste battute per sperimentare il vero freeride sulla neve fresca.', label: 'Servizio su prenotazione' },
                { title: 'Escursioni di Gruppo', text: 'Unitevi alle nostre escursioni guidate giornaliere per scoprire la fauna e la flora locali in compagnia di altri ospiti dell\'hotel.', label: 'Incluso per i clienti Premium' }
            ]
        });
</script>

<svelte:head>
    <title>{copy.title} | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div class="absolute inset-0">
        <img src="https://images.unsplash.com/photo-1544450531-64d7fa39b400?q=80&w=2000&auto=format&fit=crop" class="ken-burns h-full w-full object-cover opacity-80" alt="Guide Alpine" />
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
        <ShieldCheck class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            {copy.introTitle}
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            {copy.introText}
        </p>
    </div>
</section>

<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20">
    <div class="bg-white p-12 border border-alpine-border shadow-sm flex flex-col h-full fade-up-element">
         <Mountain class="w-8 h-8 text-alpine-gold mb-6 stroke-[1.5px]" />
            <h4 class="font-serif text-3xl text-alpine-text mb-6">{copy.cards[0].title}</h4>
            <p class="text-sm text-alpine-muted font-light leading-relaxed mb-8 grow">{copy.cards[0].text}</p>
         <div class="pt-6 border-t border-alpine-border">
                <span class="text-[10px] uppercase tracking-widest font-bold text-alpine-muted italic">{copy.cards[0].label}</span>
         </div>
    </div>
    <div class="bg-white p-12 border border-alpine-border shadow-sm flex flex-col h-full fade-up-element">
         <Users class="w-8 h-8 text-alpine-gold mb-6 stroke-[1.5px]" />
            <h4 class="font-serif text-3xl text-alpine-text mb-6">{copy.cards[1].title}</h4>
            <p class="text-sm text-alpine-muted font-light leading-relaxed mb-8 grow">{copy.cards[1].text}</p>
         <div class="pt-6 border-t border-alpine-border">
                <span class="text-[10px] uppercase tracking-widest font-bold text-alpine-muted italic">{copy.cards[1].label}</span>
         </div>
    </div>
</section>
