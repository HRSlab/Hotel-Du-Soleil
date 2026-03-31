<script lang="ts">
	import { locale } from '$lib/i18n';
	import {
		PackageCheck,
		ShieldCheck,
		Snowflake,
		ArrowRight,
		X,
		Thermometer,
		Lock,
		Eye,
		Mail
	} from 'lucide-svelte';
	import { fade, fly } from 'svelte/transition';
	import { clickOutside } from '$lib/utils/clickOutside';

	let scrollY = $state(0);
	let showRentalForm = $state(false);

	let formName = $state('');
	let formEmail = $state('');
	let formPhone = $state('');
	let formArrival = $state('');
	let formDeparture = $state('');
	let formAdults = $state(1);
	let formChildren = $state(0);
	let formEquipment = $state('sci');
	let formLevel = $state('intermedio');
	let formBootSizeAdult = $state('');
	let formBootSizeChild = $state('');
	let formHelmet = $state(true);
	let formNotes = $state('');
	let formSubmitted = $state(false);

	const content = {
		it: {
			metaTitle: 'Ski Box & Noleggio | Chalet du Soleil',
			metaDescription:
				'Ski box condivisi all’esterno e deposito scarponi riscaldato vicino alla reception a Torgnon. Servizio noleggio attrezzatura con partner locale.',
			heroLabel: 'Deposito & Attrezzatura · Torgnon',
			heroTitle: 'Ski Box & Noleggio',
			heroText:
				'Ski box condivisi all’esterno e deposito scarponi riscaldato vicino alla reception.',
			introTitle: 'Tutto ciò di cui hai bisogno, proprio qui in hotel.',
			introText:
				'Per offrirti la massima comodità, mettiamo a disposizione ski box condivisi all’esterno dell’hotel per sci e snowboard, oltre a un deposito scarponi condiviso in una stanza riscaldata vicino alla reception. L’ambiente è riscaldato ma non dispone di asciugascarponi. Grazie alla collaborazione con il nostro partner noleggio, puoi prenotare l’attrezzatura prima del tuo arrivo e trovarla pronta in hotel.',
			storageLabel: 'Deposito Attrezzatura',
			storageTitle1: 'Ski Box',
			storageTitle2: 'Condivisi',
			storageText1:
				'Gli ski box si trovano all’esterno dell’hotel, in un’area dedicata accanto alla reception. I box sono condivisi e non riscaldati, ma sono pratici per lasciare sci e snowboard tra una sciata e l’altra.',
			storageText2:
				'La posizione, a pochi passi dall’ingresso e dalla pista, ti consente di recuperare rapidamente l’attrezzatura e partire verso gli impianti senza passaggi inutili.',
			storageFeature1: 'Box condivisi',
			storageFeature2: 'Area esterna',
			bootsLabel: 'Scarponi',
			bootsTitle1: 'Deposito Scarponi',
			bootsTitle2: 'Riscaldato',
			bootsText1:
				'Gli scarponi vengono riposti in un deposito condiviso, situato in una stanza dedicata vicino alla reception.',
			bootsText2:
				'La stanza è riscaldata, così al mattino trovi scarponi meno freddi e più confortevoli da indossare. Non è presente un asciugascarponi, ma lo spazio dedicato aiuta a tenerli in ordine e al riparo.',
			bootsFeature1: 'Stanza riscaldata',
			bootsFeature2: 'Vicino alla reception',
			stats: [
				{ value: 'Condivisi', label: 'Ski box' },
				{ value: 'Outdoor', label: 'Posizione' },
				{ value: 'Riscaldato', label: 'Deposito scarponi' },
				{ value: '50m', label: 'Dalla pista' }
			],
			rentalTitle: 'Noleggio Attrezzatura',
			rentalSubtitle: 'In collaborazione con il nostro partner locale',
			rentalCards: [
				{
					title: 'Sci & Snowboard',
					subtitle: 'Attrezzatura completa',
					text: 'Sci alpino, snowboard, scarponi, bastoncini e casco. Attrezzatura regolata e preparata in base al tuo livello e alle tue esigenze.'
				},
				{
					title: 'Pronta in Hotel',
					subtitle: 'Zero code, zero stress',
					text: 'Prenota prima del tuo arrivo e organizzeremo tutto con il partner locale, così la tua attrezzatura sarà pronta in hotel senza attese inutili.'
				},
				{
					title: 'Assistenza Dedicata',
					subtitle: 'Supporto durante il soggiorno',
					text: 'Problemi con gli attacchi? Scarponi scomodi? Il nostro partner è a disposizione per sostituzioni e regolazioni durante il soggiorno.'
				}
			],
			ctaButton: 'Prenota Attrezzatura',
			howTitle: 'Come Funziona',
			howSubtitle: 'In 4 semplici passi',
			steps: [
				{
					title: 'Prenota Online',
					text: 'Compila il modulo con le tue preferenze e le date del soggiorno.'
				},
				{
					title: 'Conferma',
					text: 'Il nostro partner ti contatterà per confermare disponibilità e prezzi.'
				},
				{
					title: 'Preparazione',
					text: 'L’attrezzatura viene preparata prima del tuo arrivo e resa disponibile in hotel.'
				},
				{
					title: 'In Pista',
					text: 'Ritira l’attrezzatura e sei pronto per iniziare la giornata sulla neve.'
				}
			],
			finalTitle: 'Pronto a sciare?',
			finalText:
				'Prenota la tua attrezzatura adesso e goditi la vacanza senza pensieri. Il nostro partner si occuperà della preparazione prima del tuo arrivo.',
			form: {
				successTitle: 'Richiesta inviata!',
				successText:
					'Il tuo client email si è aperto con tutti i dettagli. Invia l’email per completare la richiesta.',
				headerTitle: 'Prenota Attrezzatura',
				headerText: 'Compila il modulo e invia la richiesta al nostro partner',
				personalInfo: 'Dati Personali',
				fullName: 'Nome e Cognome *',
				email: 'Email *',
				phone: 'Telefono',
				stay: 'Soggiorno',
				arrival: 'Arrivo *',
				departure: 'Partenza *',
				adults: 'Adulti *',
				children: 'Bambini',
				equipment: 'Attrezzatura',
				type: 'Tipo *',
				level: 'Livello *',
				adultBoot: 'Taglia scarponi (adulto)',
				childBoot: 'Taglia scarponi (bambino)',
				includeHelmet: 'Includi casco (consigliato)',
				notes: 'Note Aggiuntive',
				notesPlaceholder: 'Esigenze particolari, taglie per più persone, ecc.',
				submit: 'Invia Richiesta al Partner',
				submitHelp: 'Si aprirà il tuo client email con tutti i dettagli già compilati',
				emailSubjectPrefix: 'Prenotazione Noleggio',
				emailHeading: 'RICHIESTA NOLEGGIO ATTREZZATURA',
				guestData: 'DATI OSPITE',
				period: 'PERIODO',
				equipmentSection: 'ATTREZZATURA',
				notesSection: 'NOTE',
				nameLabel: 'Nome',
				emailLabel: 'Email',
				phoneLabel: 'Telefono',
				notProvided: 'Non indicato',
				arrivalLabel: 'Arrivo',
				departureLabel: 'Partenza',
				adultsLabel: 'Adulti',
				childrenLabel: 'Bambini',
				typeLabel: 'Tipo',
				levelLabel: 'Livello',
				adultBootLabel: 'Taglia scarponi adulto',
				childBootLabel: 'Taglia scarponi bambino',
				toDefine: 'Da definire',
				helmetLabel: 'Casco',
				yesIncluded: 'Sì, incluso',
				no: 'No',
				sentFromSite: 'Inviato tramite il sito Chalet du Soleil',
				placeholderName: 'Mario Rossi',
				placeholderEmail: 'mario@email.com',
				placeholderPhone: '+39 333 1234567',
				placeholderAdultBoot: 'es. 42, 43.5',
				placeholderChildBoot: 'es. 32, 35'
			},
			equipmentLabels: {
				sci: 'Sci alpino',
				snowboard: 'Snowboard',
				ciaspole: 'Ciaspole',
				fondo: 'Sci di fondo'
			},
			levelLabels: {
				principiante: 'Principiante',
				intermedio: 'Intermedio',
				esperto: 'Esperto'
			}
		},
		en: {
			metaTitle: 'Ski Box & Rental | Chalet du Soleil',
			metaDescription:
				'Shared outdoor ski boxes and a heated boot room near reception in Torgnon. Equipment rental service with our local partner.',
			heroLabel: 'Storage & Equipment · Torgnon',
			heroTitle: 'Ski Box & Rental',
			heroText: 'Shared outdoor ski boxes and a heated boot room near reception.',
			introTitle: 'Everything you need, right here at the hotel.',
			introText:
				'For maximum convenience, we provide shared outdoor ski boxes for skis and snowboards, plus a shared boot storage room in a heated space near reception. The room is heated, but there is no boot dryer. Thanks to our local rental partner, you can book your equipment before arrival and have everything ready at the hotel.',
			storageLabel: 'Equipment Storage',
			storageTitle1: 'Shared',
			storageTitle2: 'Ski Boxes',
			storageText1:
				'The ski boxes are located outside the hotel, in a dedicated area next to reception. They are shared and not heated, but practical for leaving skis and snowboards between runs.',
			storageText2:
				'Their location, just a few steps from the entrance and the slope, makes it easy to pick up your gear and head straight to the lifts.',
			storageFeature1: 'Shared boxes',
			storageFeature2: 'Outdoor area',
			bootsLabel: 'Boot Storage',
			bootsTitle1: 'Heated',
			bootsTitle2: 'Boot Room',
			bootsText1:
				'Ski boots are stored in a shared boot room located in a dedicated heated room near reception.',
			bootsText2:
				'The room is heated, so your boots feel less cold and more comfortable in the morning. There is no boot dryer, but the dedicated space keeps everything organized and protected.',
			bootsFeature1: 'Heated room',
			bootsFeature2: 'Near reception',
			stats: [
				{ value: 'Shared', label: 'Ski boxes' },
				{ value: 'Outdoor', label: 'Location' },
				{ value: 'Heated', label: 'Boot room' },
				{ value: '50m', label: 'From the slope' }
			],
			rentalTitle: 'Equipment Rental',
			rentalSubtitle: 'In partnership with our local rental partner',
			rentalCards: [
				{
					title: 'Skis & Snowboards',
					subtitle: 'Complete equipment',
					text: 'Alpine skis, snowboard, boots, poles and helmet. Equipment prepared and adjusted to your level and needs.'
				},
				{
					title: 'Ready at the Hotel',
					subtitle: 'No queues, no stress',
					text: 'Book before your arrival and we will organize everything with our local partner, so your equipment is ready for you at the hotel.'
				},
				{
					title: 'Dedicated Support',
					subtitle: 'Help during your stay',
					text: 'Issues with bindings? Uncomfortable boots? Our partner is available for adjustments and replacements during your stay.'
				}
			],
			ctaButton: 'Book Equipment',
			howTitle: 'How It Works',
			howSubtitle: 'In 4 simple steps',
			steps: [
				{
					title: 'Book Online',
					text: 'Fill in the form with your preferences and stay dates.'
				},
				{
					title: 'Confirmation',
					text: 'Our partner will contact you to confirm availability and pricing.'
				},
				{
					title: 'Preparation',
					text: 'Your equipment is prepared before arrival and made available at the hotel.'
				},
				{
					title: 'Hit the Slopes',
					text: 'Pick up your gear and start your day on the snow right away.'
				}
			],
			finalTitle: 'Ready to ski?',
			finalText:
				'Book your equipment now and enjoy a smoother holiday. Our partner will take care of the preparation before you arrive.',
			form: {
				successTitle: 'Request sent!',
				successText:
					'Your email client opened with all the details. Send the email to complete your request.',
				headerTitle: 'Book Equipment',
				headerText: 'Fill in the form and send your request to our partner',
				personalInfo: 'Personal Details',
				fullName: 'Full Name *',
				email: 'Email *',
				phone: 'Phone',
				stay: 'Stay',
				arrival: 'Arrival *',
				departure: 'Departure *',
				adults: 'Adults *',
				children: 'Children',
				equipment: 'Equipment',
				type: 'Type *',
				level: 'Level *',
				adultBoot: 'Boot size (adult)',
				childBoot: 'Boot size (child)',
				includeHelmet: 'Include helmet (recommended)',
				notes: 'Additional Notes',
				notesPlaceholder: 'Special requests, sizes for multiple people, etc.',
				submit: 'Send Request to Partner',
				submitHelp: 'Your email client will open with all details already filled in',
				emailSubjectPrefix: 'Rental Request',
				emailHeading: 'EQUIPMENT RENTAL REQUEST',
				guestData: 'GUEST DETAILS',
				period: 'STAY',
				equipmentSection: 'EQUIPMENT',
				notesSection: 'NOTES',
				nameLabel: 'Name',
				emailLabel: 'Email',
				phoneLabel: 'Phone',
				notProvided: 'Not provided',
				arrivalLabel: 'Arrival',
				departureLabel: 'Departure',
				adultsLabel: 'Adults',
				childrenLabel: 'Children',
				typeLabel: 'Type',
				levelLabel: 'Level',
				adultBootLabel: 'Adult boot size',
				childBootLabel: 'Child boot size',
				toDefine: 'To be defined',
				helmetLabel: 'Helmet',
				yesIncluded: 'Yes, included',
				no: 'No',
				sentFromSite: 'Sent via the Chalet du Soleil website',
				placeholderName: 'John Smith',
				placeholderEmail: 'john@email.com',
				placeholderPhone: '+44 1234 567890',
				placeholderAdultBoot: 'e.g. 42, 43.5',
				placeholderChildBoot: 'e.g. 32, 35'
			},
			equipmentLabels: {
				sci: 'Alpine skis',
				snowboard: 'Snowboard',
				ciaspole: 'Snowshoes',
				fondo: 'Cross-country skis'
			},
			levelLabels: {
				principiante: 'Beginner',
				intermedio: 'Intermediate',
				esperto: 'Advanced'
			}
		}
	} as const;

	const PARTNER_EMAIL = 'bellocarlo@gmail.com';

	function currentCopy() {
		return content[$locale as keyof typeof content] ?? content.it;
	}

	function equipmentLabel() {
		return (
			currentCopy().equipmentLabels[formEquipment as keyof typeof content.it.equipmentLabels] ??
			formEquipment
		);
	}

	function levelLabel() {
		return currentCopy().levelLabels[formLevel as keyof typeof content.it.levelLabels] ?? formLevel;
	}

	function handleSubmit(e: Event) {
		e.preventDefault();

		const copy = currentCopy();
		const subject = encodeURIComponent(
			`${copy.form.emailSubjectPrefix} – Chalet du Soleil – ${formName}`
		);

		let body = `${copy.form.emailHeading}\n`;
		body += `Chalet du Soleil – Torgnon\n`;
		body += `${'─'.repeat(40)}\n\n`;
		body += `${copy.form.guestData}\n`;
		body += `${copy.form.nameLabel}: ${formName}\n`;
		body += `${copy.form.emailLabel}: ${formEmail}\n`;
		body += `${copy.form.phoneLabel}: ${formPhone || copy.form.notProvided}\n\n`;
		body += `${copy.form.period}\n`;
		body += `${copy.form.arrivalLabel}: ${formArrival}\n`;
		body += `${copy.form.departureLabel}: ${formDeparture}\n`;
		body += `${copy.form.adultsLabel}: ${formAdults}\n`;
		body += `${copy.form.childrenLabel}: ${formChildren}\n\n`;
		body += `${copy.form.equipmentSection}\n`;
		body += `${copy.form.typeLabel}: ${equipmentLabel()}\n`;
		body += `${copy.form.levelLabel}: ${levelLabel()}\n`;
		body += `${copy.form.adultBootLabel}: ${formBootSizeAdult || copy.form.toDefine}\n`;
		if (formChildren > 0) {
			body += `${copy.form.childBootLabel}: ${formBootSizeChild || copy.form.toDefine}\n`;
		}
		body += `${copy.form.helmetLabel}: ${formHelmet ? copy.form.yesIncluded : copy.form.no}\n`;
		if (formNotes) {
			body += `\n${copy.form.notesSection}\n${formNotes}\n`;
		}
		body += `\n${'─'.repeat(40)}\n`;
		body += copy.form.sentFromSite;

		const mailtoUrl = `mailto:${PARTNER_EMAIL}?subject=${subject}&body=${encodeURIComponent(body)}`;
		const link = document.createElement('a');
		link.href = mailtoUrl;
		link.click();

		setTimeout(() => {
			formSubmitted = true;
			setTimeout(() => {
				formSubmitted = false;
				showRentalForm = false;
			}, 3000);
		}, 500);
	}
</script>

<svelte:window bind:scrollY />

<svelte:head>
	<title>{currentCopy().metaTitle}</title>
	<meta name="description" content={currentCopy().metaDescription} />
</svelte:head>

<header class="relative h-[85vh] w-full overflow-hidden bg-[#1a1a1a]">
	<div
		class="absolute inset-0 scale-110"
		style="transform: translateY({scrollY * 0.25}px) scale(1.1);"
	>
		<img
			src="https://images.unsplash.com/photo-1551698618-1fed5d97530d?q=80&w=2000&auto=format&fit=crop"
			class="h-full w-full object-cover opacity-60"
			alt="Noleggio sci Torgnon"
		/>
		<div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/30 to-alpine-bg"></div>
	</div>

	<div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-28 text-center">
		<span
			class="fade-up-element mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs"
		>
			{currentCopy().heroLabel}
		</span>
		<h1 class="fade-up-element font-serif text-5xl leading-tight font-light text-white md:text-8xl">
			{currentCopy().heroTitle}
		</h1>
		<p class="fade-up-element mt-6 max-w-md text-sm font-light text-white/50">
			{currentCopy().heroText}
		</p>
	</div>
</header>

<section class="bg-alpine-bg px-6 py-28">
	<div class="fade-up-element mx-auto max-w-3xl text-center">
		<PackageCheck class="mx-auto mb-10 h-10 w-10 text-alpine-gold" />
		<h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
			{currentCopy().introTitle}
		</h3>
		<p
			class="mx-auto mt-12 max-w-xl border-t border-alpine-border pt-12 text-sm leading-relaxed font-light text-alpine-muted md:text-base"
		>
			{currentCopy().introText}
		</p>
	</div>
</section>

<section
	class="mx-auto grid max-w-7xl grid-cols-1 items-center gap-12 bg-alpine-bg px-6 pb-32 md:grid-cols-2 lg:gap-20"
>
	<div class="fade-up-element overflow-hidden bg-alpine-border shadow-xl">
		<img
			src="https://images.unsplash.com/photo-1565992441121-4367c2967103?q=80&w=1500&auto=format&fit=crop"
			alt="Ski box deposito sci"
			class="img-elegant aspect-4/3 h-full w-full object-cover brightness-90"
		/>
	</div>
	<div class="fade-up-element">
		<span class="mb-4 block text-[10px] font-bold tracking-[0.3em] text-alpine-gold uppercase"
			>{currentCopy().storageLabel}</span
		>
		<h2 class="mb-6 font-serif text-4xl text-alpine-text">
			{currentCopy().storageTitle1} <br />{currentCopy().storageTitle2}
		</h2>
		<p class="mb-6 text-sm leading-relaxed font-light text-alpine-muted">
			{currentCopy().storageText1}
		</p>
		<p class="mb-8 text-sm leading-relaxed font-light text-alpine-muted">
			{currentCopy().storageText2}
		</p>
		<div class="grid grid-cols-2 gap-6 border-t border-alpine-border pt-6">
			<div class="flex items-center gap-3">
				<Lock class="h-5 w-5 shrink-0 text-alpine-gold" />
				<span class="text-xs font-bold tracking-widest text-alpine-text uppercase"
					>{currentCopy().storageFeature1}</span
				>
			</div>
			<div class="flex items-center gap-3">
				<Eye class="h-5 w-5 shrink-0 text-alpine-gold" />
				<span class="text-xs font-bold tracking-widest text-alpine-text uppercase"
					>{currentCopy().storageFeature2}</span
				>
			</div>
		</div>
	</div>
</section>

<section
	class="mx-auto grid max-w-7xl grid-cols-1 items-center gap-12 bg-alpine-bg px-6 pb-32 md:grid-cols-2 lg:gap-20"
>
	<div class="fade-up-element order-2 md:order-1">
		<span class="mb-4 block text-[10px] font-bold tracking-[0.3em] text-alpine-gold uppercase"
			>{currentCopy().bootsLabel}</span
		>
		<h2 class="mb-6 font-serif text-4xl text-alpine-text">
			{currentCopy().bootsTitle1} <br />{currentCopy().bootsTitle2}
		</h2>
		<p class="mb-6 text-sm leading-relaxed font-light text-alpine-muted">
			{currentCopy().bootsText1}
		</p>
		<p class="mb-8 text-sm leading-relaxed font-light text-alpine-muted">
			{currentCopy().bootsText2}
		</p>
		<div class="grid grid-cols-2 gap-6 border-t border-alpine-border pt-6">
			<div class="flex items-center gap-3">
				<Thermometer class="h-5 w-5 shrink-0 text-alpine-gold" />
				<span class="text-xs font-bold tracking-widest text-alpine-text uppercase"
					>{currentCopy().bootsFeature1}</span
				>
			</div>
			<div class="flex items-center gap-3">
				<ShieldCheck class="h-5 w-5 shrink-0 text-alpine-gold" />
				<span class="text-xs font-bold tracking-widest text-alpine-text uppercase"
					>{currentCopy().bootsFeature2}</span
				>
			</div>
		</div>
	</div>
	<div class="fade-up-element order-1 overflow-hidden bg-alpine-border shadow-xl md:order-2">
		<img
			src="https://images.unsplash.com/photo-1605540436563-5bca919ae766?q=80&w=1500&auto=format&fit=crop"
			alt="Deposito scarponi riscaldato"
			class="img-elegant aspect-4/3 h-full w-full object-cover brightness-90"
		/>
	</div>
</section>

<section class="border-y border-alpine-border bg-white px-6 py-20">
	<div class="mx-auto grid max-w-6xl grid-cols-2 gap-12 text-center md:grid-cols-4">
		{#each currentCopy().stats as stat, i (i)}
			<div class="fade-up-element">
				<p class="mb-2 font-serif text-4xl text-alpine-text md:text-5xl">{stat.value}</p>
				<p class="text-[10px] font-bold tracking-[0.25em] text-alpine-muted uppercase">
					{stat.label}
				</p>
			</div>
		{/each}
	</div>
</section>

<section class="bg-alpine-bg px-6 py-32">
	<div class="mx-auto max-w-7xl">
		<div class="fade-up-element mx-auto mb-20 max-w-xl text-center">
			<h2 class="mb-5 font-serif text-4xl leading-tight text-alpine-text md:text-5xl">
				{currentCopy().rentalTitle}
			</h2>
			<p class="text-[11px] font-bold tracking-widest text-alpine-muted uppercase">
				{currentCopy().rentalSubtitle}
			</p>
		</div>

		<div class="grid grid-cols-1 gap-8 md:grid-cols-3 lg:gap-12">
			{#each currentCopy().rentalCards as card, i (i)}
				<div
					class="fade-up-element border border-alpine-border bg-white p-12 text-center transition-all duration-500 hover:border-alpine-gold hover:shadow-2xl md:p-14"
				>
					{#if i === 0}
						<Snowflake class="mx-auto mb-8 h-8 w-8 stroke-1 text-alpine-gold" />
					{:else if i === 1}
						<PackageCheck class="mx-auto mb-8 h-8 w-8 stroke-1 text-alpine-gold" />
					{:else}
						<ShieldCheck class="mx-auto mb-8 h-8 w-8 stroke-1 text-alpine-gold" />
					{/if}
					<h4 class="mb-2 font-serif text-2xl text-alpine-text">{card.title}</h4>
					<p class="mb-6 text-[10px] font-bold tracking-widest text-alpine-muted uppercase">
						{card.subtitle}
					</p>
					<p
						class="mx-auto max-w-xs text-xs leading-relaxed font-light text-alpine-muted lg:text-sm"
					>
						{card.text}
					</p>
				</div>
			{/each}
		</div>

		<div class="fade-up-element mt-16 text-center">
			<button
				onclick={() => (showRentalForm = true)}
				class="inline-flex cursor-pointer items-center gap-3 border-2 border-alpine-text px-10 py-4 text-[11px] font-bold tracking-[0.2em] text-alpine-text uppercase transition-all duration-300 hover:bg-alpine-text hover:text-white"
			>
				{currentCopy().ctaButton}
				<ArrowRight class="h-4 w-4" />
			</button>
		</div>
	</div>
</section>

<section class="border-y border-alpine-border bg-white px-6 py-32">
	<div class="mx-auto max-w-5xl">
		<div class="fade-up-element mx-auto mb-20 max-w-xl text-center">
			<h2 class="mb-5 font-serif text-4xl leading-tight text-alpine-text md:text-5xl">
				{currentCopy().howTitle}
			</h2>
			<p class="text-[11px] font-bold tracking-widest text-alpine-muted uppercase">
				{currentCopy().howSubtitle}
			</p>
		</div>

		<div class="grid grid-cols-1 gap-8 md:grid-cols-4">
			{#each currentCopy().steps as step, i (i)}
				<div class="fade-up-element text-center">
					<div
						class="mx-auto mb-6 flex h-12 w-12 items-center justify-center rounded-full border-2 border-alpine-gold"
					>
						<span class="font-serif text-xl text-alpine-gold">{i + 1}</span>
					</div>
					<h4 class="mb-3 font-serif text-lg text-alpine-text">{step.title}</h4>
					<p class="text-xs leading-relaxed font-light text-alpine-muted">
						{step.text}
					</p>
				</div>
			{/each}
		</div>
	</div>
</section>

<section class="bg-[#0a0a0a] px-6 py-32">
	<div class="mx-auto max-w-3xl text-center">
		<div class="fade-up-element">
			<h2 class="mb-6 font-serif text-4xl text-white">{currentCopy().finalTitle}</h2>
			<p class="mx-auto mb-12 max-w-lg text-sm leading-relaxed font-light text-white/50">
				{currentCopy().finalText}
			</p>
			<button
				onclick={() => (showRentalForm = true)}
				class="inline-flex cursor-pointer items-center gap-3 bg-alpine-gold px-10 py-4 text-[11px] font-bold tracking-[0.2em] text-white uppercase transition-all duration-300 hover:bg-alpine-gold/90"
			>
				{currentCopy().ctaButton}
				<ArrowRight class="h-4 w-4" />
			</button>
		</div>
	</div>
</section>

{#if showRentalForm}
	<div
		class="fixed inset-0 z-50 flex items-center justify-center p-4"
		transition:fade={{ duration: 200 }}
	>
		<button
			type="button"
			class="absolute inset-0 cursor-default bg-black/70 backdrop-blur-sm"
			onclick={() => (showRentalForm = false)}
			aria-label="Chiudi"
		></button>

		<div
			class="relative max-h-[90vh] w-full max-w-lg overflow-y-auto bg-white shadow-2xl"
			transition:fly={{ y: 40, duration: 300 }}
			use:clickOutside={() => (showRentalForm = false)}
		>
			{#if formSubmitted}
				<div class="p-16 text-center">
					<div
						class="mx-auto mb-6 flex h-16 w-16 items-center justify-center rounded-full bg-green-100"
					>
						<PackageCheck class="h-8 w-8 text-green-600" />
					</div>
					<h3 class="mb-4 font-serif text-2xl text-alpine-text">
						{currentCopy().form.successTitle}
					</h3>
					<p class="text-sm font-light text-alpine-muted">
						{currentCopy().form.successText}
					</p>
				</div>
			{:else}
				<div
					class="sticky top-0 z-10 flex items-center justify-between border-b border-alpine-border bg-white px-8 py-6"
				>
					<div>
						<h3 class="font-serif text-2xl text-alpine-text">{currentCopy().form.headerTitle}</h3>
						<p class="mt-1 text-xs font-light text-alpine-muted">{currentCopy().form.headerText}</p>
					</div>
					<button
						onclick={() => (showRentalForm = false)}
						class="cursor-pointer rounded p-2 transition-colors hover:bg-alpine-bg"
					>
						<X class="h-5 w-5 text-alpine-muted" />
					</button>
				</div>

				<form onsubmit={handleSubmit} class="space-y-6 p-8">
					<div class="space-y-4">
						<p class="text-[10px] font-bold tracking-[0.3em] text-alpine-gold uppercase">
							{currentCopy().form.personalInfo}
						</p>

						<div>
							<label for="rental-name" class="mb-1.5 block text-xs font-medium text-alpine-text"
								>{currentCopy().form.fullName}</label
							>
							<input
								id="rental-name"
								type="text"
								required
								bind:value={formName}
								class="w-full border border-alpine-border px-4 py-3 text-sm font-light transition-colors focus:border-alpine-gold focus:outline-none"
								placeholder={currentCopy().form.placeholderName}
							/>
						</div>

						<div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
							<div>
								<label for="rental-email" class="mb-1.5 block text-xs font-medium text-alpine-text"
									>{currentCopy().form.email}</label
								>
								<input
									id="rental-email"
									type="email"
									required
									bind:value={formEmail}
									class="w-full border border-alpine-border px-4 py-3 text-sm font-light transition-colors focus:border-alpine-gold focus:outline-none"
									placeholder={currentCopy().form.placeholderEmail}
								/>
							</div>
							<div>
								<label for="rental-phone" class="mb-1.5 block text-xs font-medium text-alpine-text"
									>{currentCopy().form.phone}</label
								>
								<input
									id="rental-phone"
									type="tel"
									bind:value={formPhone}
									class="w-full border border-alpine-border px-4 py-3 text-sm font-light transition-colors focus:border-alpine-gold focus:outline-none"
									placeholder={currentCopy().form.placeholderPhone}
								/>
							</div>
						</div>
					</div>

					<div class="space-y-4 border-t border-alpine-border pt-4">
						<p class="text-[10px] font-bold tracking-[0.3em] text-alpine-gold uppercase">
							{currentCopy().form.stay}
						</p>

						<div class="grid grid-cols-2 gap-4">
							<div>
								<label
									for="rental-arrival"
									class="mb-1.5 block text-xs font-medium text-alpine-text"
									>{currentCopy().form.arrival}</label
								>
								<input
									id="rental-arrival"
									type="date"
									required
									bind:value={formArrival}
									class="w-full border border-alpine-border px-4 py-3 text-sm font-light transition-colors focus:border-alpine-gold focus:outline-none"
								/>
							</div>
							<div>
								<label
									for="rental-departure"
									class="mb-1.5 block text-xs font-medium text-alpine-text"
									>{currentCopy().form.departure}</label
								>
								<input
									id="rental-departure"
									type="date"
									required
									bind:value={formDeparture}
									class="w-full border border-alpine-border px-4 py-3 text-sm font-light transition-colors focus:border-alpine-gold focus:outline-none"
								/>
							</div>
						</div>

						<div class="grid grid-cols-2 gap-4">
							<div>
								<label for="rental-adults" class="mb-1.5 block text-xs font-medium text-alpine-text"
									>{currentCopy().form.adults}</label
								>
								<select
									id="rental-adults"
									bind:value={formAdults}
									class="w-full cursor-pointer appearance-none border border-alpine-border bg-white px-4 py-3 text-sm font-light transition-colors focus:border-alpine-gold focus:outline-none"
								>
									{#each [1, 2, 3, 4, 5, 6] as n}
										<option value={n}>{n}</option>
									{/each}
								</select>
							</div>
							<div>
								<label
									for="rental-children"
									class="mb-1.5 block text-xs font-medium text-alpine-text"
									>{currentCopy().form.children}</label
								>
								<select
									id="rental-children"
									bind:value={formChildren}
									class="w-full cursor-pointer appearance-none border border-alpine-border bg-white px-4 py-3 text-sm font-light transition-colors focus:border-alpine-gold focus:outline-none"
								>
									{#each [0, 1, 2, 3, 4] as n}
										<option value={n}>{n}</option>
									{/each}
								</select>
							</div>
						</div>
					</div>

					<div class="space-y-4 border-t border-alpine-border pt-4">
						<p class="text-[10px] font-bold tracking-[0.3em] text-alpine-gold uppercase">
							{currentCopy().form.equipment}
						</p>

						<div class="grid grid-cols-2 gap-4">
							<div>
								<label
									for="rental-equipment"
									class="mb-1.5 block text-xs font-medium text-alpine-text"
									>{currentCopy().form.type}</label
								>
								<select
									id="rental-equipment"
									bind:value={formEquipment}
									class="w-full cursor-pointer appearance-none border border-alpine-border bg-white px-4 py-3 text-sm font-light transition-colors focus:border-alpine-gold focus:outline-none"
								>
									<option value="sci">{currentCopy().equipmentLabels.sci}</option>
									<option value="snowboard">{currentCopy().equipmentLabels.snowboard}</option>
									<option value="ciaspole">{currentCopy().equipmentLabels.ciaspole}</option>
									<option value="fondo">{currentCopy().equipmentLabels.fondo}</option>
								</select>
							</div>
							<div>
								<label for="rental-level" class="mb-1.5 block text-xs font-medium text-alpine-text"
									>{currentCopy().form.level}</label
								>
								<select
									id="rental-level"
									bind:value={formLevel}
									class="w-full cursor-pointer appearance-none border border-alpine-border bg-white px-4 py-3 text-sm font-light transition-colors focus:border-alpine-gold focus:outline-none"
								>
									<option value="principiante">{currentCopy().levelLabels.principiante}</option>
									<option value="intermedio">{currentCopy().levelLabels.intermedio}</option>
									<option value="esperto">{currentCopy().levelLabels.esperto}</option>
								</select>
							</div>
						</div>

						<div class="grid grid-cols-2 gap-4">
							<div>
								<label
									for="rental-boot-adult"
									class="mb-1.5 block text-xs font-medium text-alpine-text"
									>{currentCopy().form.adultBoot}</label
								>
								<input
									id="rental-boot-adult"
									type="text"
									bind:value={formBootSizeAdult}
									class="w-full border border-alpine-border px-4 py-3 text-sm font-light transition-colors focus:border-alpine-gold focus:outline-none"
									placeholder={currentCopy().form.placeholderAdultBoot}
								/>
							</div>
							{#if formChildren > 0}
								<div>
									<label
										for="rental-boot-child"
										class="mb-1.5 block text-xs font-medium text-alpine-text"
										>{currentCopy().form.childBoot}</label
									>
									<input
										id="rental-boot-child"
										type="text"
										bind:value={formBootSizeChild}
										class="w-full border border-alpine-border px-4 py-3 text-sm font-light transition-colors focus:border-alpine-gold focus:outline-none"
										placeholder={currentCopy().form.placeholderChildBoot}
									/>
								</div>
							{/if}
						</div>

						<label class="flex cursor-pointer items-center gap-3">
							<input type="checkbox" bind:checked={formHelmet} class="h-4 w-4 accent-alpine-gold" />
							<span class="text-sm font-light text-alpine-text"
								>{currentCopy().form.includeHelmet}</span
							>
						</label>
					</div>

					<div class="space-y-4 border-t border-alpine-border pt-4">
						<p class="text-[10px] font-bold tracking-[0.3em] text-alpine-gold uppercase">
							{currentCopy().form.notes}
						</p>
						<textarea
							bind:value={formNotes}
							rows="3"
							class="w-full resize-none border border-alpine-border px-4 py-3 text-sm font-light transition-colors focus:border-alpine-gold focus:outline-none"
							placeholder={currentCopy().form.notesPlaceholder}
						></textarea>
					</div>

					<div class="pt-4">
						<button
							type="submit"
							class="flex w-full cursor-pointer items-center justify-center gap-3 bg-alpine-text py-4 text-[11px] font-bold tracking-[0.2em] text-white uppercase transition-colors duration-300 hover:bg-alpine-gold"
						>
							<Mail class="h-4 w-4" />
							{currentCopy().form.submit}
						</button>
						<p class="mt-3 text-center text-[10px] font-light text-alpine-muted">
							{currentCopy().form.submitHelp}
						</p>
					</div>
				</form>
			{/if}
		</div>
	</div>
{/if}
