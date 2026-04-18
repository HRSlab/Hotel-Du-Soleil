export const commonAmenities = [
	'Letti matrimoniali e singoli',
	'TV satellitare',
	'Canali via cavo',
	'Telefono con centralino',
	'Armadio e cassettiera',
	'Riscaldamento',
	'Prodotti da bagno',
	'Doccia o vasca',
	'Asciugamani',
	'Pantofole',
	'Asciugacapelli',
	'Bidet',
	'Wi-Fi gratuita',
	'Servizio di mezza pensione',
	'Ski Box',
	'Parcheggio coperto e gratuito'
];

export const rooms: Record<string, any> = {
	matrimoniale: {
		name: 'Camera Matrimoniale',
		slug: 'matrimoniale',
		description:
			"La nostra camera doppia a Torgnon offre un rifugio semplice, caldo e funzionale, perfetto per le coppie o gli sciatori che desiderano un soggiorno pratico in Valle d’Aosta. Caratterizzate dall'arredamento tradizionale in legno massiccio, queste stanze fondono il calore del design classico con una vista aperta sul territorio circostante.\n\nIl valore aggiunto delle nostre doppie è l'affaccio sull'esterno: alcune camere guardano verso le piste, altre verso il paese.\n\nArredate nello stile classico dell'hotel con copriletti rossi e dettagli tradizionali, le stanze offrono dotazioni essenziali e affidabili: configurazione flessibile con letto matrimoniale o due singoli in legno, Wi-Fi gratuito e TV a schermo piatto.",
		price: 'da €120 / notte',
		size: '18-20 mq',
		occupancy: '2 ospiti',
		bedType: 'Matrimoniale o Twin',
		highlight: 'Affaccio esterno, verso le piste o verso il paese',
		image: '/imgs/Rooms/doppia-superior-1.webp',
		amenities: [...commonAmenities],
		gallery: [
			'/imgs/Rooms/matrimoniale-classic-hero-1.webp',
			'/imgs/Rooms/matrimoniale-classic-1-1.webp',
			'/imgs/Rooms/matrimoniale-superior-hero-1.webp',
			'/imgs/Rooms/matrimoniale-twin-1.webp',
			'/imgs/Rooms/bagno-standard-1-1.webp'
		]
	},
	tripla: {
		name: 'Camera Tripla',
		slug: 'tripla',
		description:
			'La nostra camera tripla a Torgnon è la soluzione ideale per chi cerca una vacanza in montagna in Valle d’Aosta senza rinunciare allo spazio. Con una superficie che arriva fino a 20mq, queste stanze offrono un’atmosfera di quiete e un layout versatile, perfetto per piccoli gruppi di amici o famiglie con un bambino.\n\nLa flessibilità è la nostra firma. Potete scegliere la configurazione che meglio si adatta alle vostre necessità: tre letti singoli separati o un letto matrimoniale e un letto singolo.\n\nL’arredo essenziale in stile alpino garantisce tutto ciò che serve per un soggiorno rigenerante: Wi-Fi Fibra gratuita, TV LED Satellitare, ampi armadi e bagno privato con doccia, linea di cortesia ricercata e morbide pantofole incluse.',
		price: 'da €160 / notte',
		size: '20 mq',
		occupancy: '3 ospiti',
		bedType: 'Matrimoniale + singolo o 3 singoli',
		highlight: 'Layout flessibile per famiglie e piccoli gruppi',
		image: '/imgs/Rooms/tripla-alcova-1.webp',
		amenities: [...commonAmenities],
		gallery: [
			'/imgs/Rooms/tripla-alcova-1.webp',
			'/imgs/Rooms/tripla-alcova-matrimoniale-1.webp',
			'/imgs/Rooms/tripla-alcova-dettaglio-1.webp',
			'/imgs/Rooms/tripla-letto-a-castello-1.webp',
			'/imgs/Rooms/tripla-dettaglio-1-1.webp',
			'/imgs/Rooms/bagno-standard-2-1.webp'
		]
	},
	quadrupla_standard: {
		name: 'Quadrupla Standard',
		slug: 'quadrupla_standard',
		description:
			'Camera Quadrupla a Torgnon: Lo Spazio Ideale per la tua Famiglia. Se stai pianificando una vacanza in famiglia in Valle d’Aosta, le nostre camere quadruple a Torgnon offrono il rifugio perfetto. Progettate per accogliere fino a quattro persone in un unico ambiente generoso e luminoso, queste stanze eliminano lo stress degli spazi ristretti, permettendovi di godere appieno della quota.\n\nOgni camera è pensata per garantire il giusto equilibrio tra condivisione e comfort individuale: Configurazione Flex con quattro letti singoli reali o un letto matrimoniale accompagnato da due letti singoli. Ampia metratura fino a 24mq di superficie per muoversi in totale libertà.',
		price: 'da €190 / notte',
		size: '24 mq',
		occupancy: '4 ospiti',
		bedType: '4 singoli o matrimoniale + 2 singoli',
		highlight: 'Spazio comodo per la vacanza in famiglia',
		image: '/imgs/Rooms/quadrupla-letto-a-castello-1.webp',
		amenities: [...commonAmenities],
		gallery: [
			'/imgs/Rooms/quadrupla-letto-a-castello-1.webp',
			'/imgs/Rooms/bagno-standard-2-1.webp'
		]
	},
	familiare: {
		name: 'Quadrupla Familiare',
		slug: 'familiare',
		description:
			"L'alloggio più esclusivo, pensato per il massimo comfort della famiglia in montagna. Spazi ampi e finiture premium.",
		price: 'da €220 / notte',
		size: '28-32 mq',
		occupancy: '4 ospiti',
		bedType: 'Matrimoniale + letti singoli',
		highlight: "L'opzione più ampia e premium della struttura",
		image: '/imgs/Rooms/familiare-suite-ingresso-1.webp',
		amenities: [...commonAmenities],
		gallery: [
			'/imgs/Rooms/familiare-suite-ingresso-1.webp',
			'/imgs/Rooms/matrimoniale-twin-1.webp',
			'/imgs/Rooms/matrimoniale-classic-1-1.webp',
			'/imgs/Rooms/bagno-standard-1-1.webp'
		]
	}
};
