<script lang="ts">
	import { page } from '$app/state';
	import { rooms } from '$lib/rooms';
	import { t } from '$lib/i18n';
	import { ChevronLeft, Check } from 'lucide-svelte';
	import RoomBookingWidget from '$lib/components/RoomBookingWidget.svelte';

	const amenityKeyByLabel: Record<string, string> = {
		'Letti matrimoniali e singoli': 'beds_double_single',
		'TV satellitare': 'tv_satellite',
		'Canali via cavo': 'cable_channels',
		'Telefono con centralino': 'phone',
		'Armadio e cassettiera': 'wardrobe_drawers',
		Riscaldamento: 'heating',
		'Prodotti da bagno': 'toiletries',
		'Doccia o vasca': 'shower_or_bathtub',
		Asciugamani: 'towels',
		Pantofole: 'slippers',
		Asciugacapelli: 'hairdryer',
		Bidet: 'bidet',
		'Wi-Fi gratuita': 'wifi_free',
		'Servizio di mezza pensione': 'half_board',
		'Ski Box': 'ski_box',
		'Parcheggio coperto e gratuito': 'parking_covered_free'
	};

	function amenityText(label: string): string {
		const key = amenityKeyByLabel[label];
		if (!key) return label;
		return ($t(`rooms_amenities.${key}`) as string) || label;
	}

	const slug = $derived(page.params.slug);
	const room = $derived(rooms[slug as keyof typeof rooms]);
	const title = $derived(
		room ? `${$t(`rooms_data.${slug}.name`)} | Chalet du Soleil` : $t('errors.not_found')
	);
</script>

<svelte:head>
	<title>{title}</title>
</svelte:head>

{#if room}
	<!-- Hero Section -->
	<div class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
		<div class="absolute inset-0">
			<img
				src={room.image}
				alt={$t(`rooms_data.${slug}.name`)}
				class="ken-burns h-full w-full object-cover opacity-70"
			/>
			<div class="absolute inset-0 bg-linear-to-b from-black/40 via-transparent to-alpine-bg"></div>
		</div>
		<div
			class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pt-20 pb-24 text-center"
		>
			<div class="fade-up-element">
				<span class="mb-4 block text-[10px] font-bold tracking-[0.32em] text-white/80 uppercase">
					{$t('rooms.detail_label') || 'Suite Details'}
				</span>
				<h1 class="font-serif text-5xl font-light tracking-tight text-white md:text-7xl">
					{$t(`rooms_data.${slug}.name`)}
				</h1>
			</div>
		</div>
	</div>

	<div class="min-h-screen bg-alpine-bg px-6 pb-24">
		<div class="mx-auto max-w-7xl">
			<!-- Back Link -->
			<a
				href="/camere"
				class="fade-up-element my-12 inline-flex items-center gap-2 text-[10px] font-bold tracking-[0.2em] text-alpine-muted uppercase transition-colors hover:text-alpine-gold"
			>
				<ChevronLeft class="h-4 w-4" />
				{$t('rooms.back_link') || 'Tutte le sistemazioni'}
			</a>

			<div class="grid grid-cols-1 gap-16 lg:grid-cols-12 lg:items-start">
				<div class="fade-up-element lg:col-span-8">
					<div class="border border-alpine-border bg-white p-8 md:p-10">
						<div class="grid grid-cols-1 gap-5 border-b border-alpine-border pb-7 sm:grid-cols-3">
							<div>
								<p class="text-[10px] font-bold tracking-[0.18em] text-alpine-muted uppercase">
									{$t('rooms.size_label') || 'Dimensione'}
								</p>
								<p class="mt-1 text-sm text-alpine-text">
									{$t(`rooms_specs.${slug}.size`) || room.size}
								</p>
							</div>
							<div>
								<p class="text-[10px] font-bold tracking-[0.18em] text-alpine-muted uppercase">
									{$t('rooms.occupancy_label') || 'Ospiti'}
								</p>
								<p class="mt-1 text-sm text-alpine-text">
									{$t(`rooms_specs.${slug}.occupancy`) || room.occupancy}
								</p>
							</div>
							<div>
								<p class="text-[10px] font-bold tracking-[0.18em] text-alpine-muted uppercase">
									{$t('rooms.beds_label') || 'Letti'}
								</p>
								<p class="mt-1 text-sm text-alpine-text">
									{$t(`rooms_specs.${slug}.beds`) || room.bedType}
								</p>
							</div>
						</div>

						<h2 class="mt-8 font-serif text-4xl text-alpine-text">
							{$t('rooms.description_label') || 'Descrizione'}
						</h2>
						<p
							class="mt-6 text-base leading-relaxed font-light whitespace-pre-line text-alpine-muted"
						>
							{$t(`rooms_data.${slug}.description`)}
						</p>

						<div class="mt-8 border-l-2 border-alpine-gold pl-4">
							<p class="text-sm leading-relaxed text-alpine-text">
								{room.highlight}
							</p>
						</div>

						<div class="mt-10 border-t border-alpine-border pt-8">
							<h4 class="text-[10px] font-bold tracking-[0.22em] text-alpine-text uppercase">
								{$t('rooms.amenities_label') || 'Servizi inclusi'}
							</h4>
							<ul class="mt-6 grid grid-cols-1 gap-x-8 gap-y-4 md:grid-cols-2">
								{#each room.amenities as amenity}
									<li
										class="flex items-center gap-3 border-b border-alpine-border/30 pb-3 text-sm font-light text-alpine-muted"
									>
										<Check class="h-3 w-3 text-alpine-gold" />
										{amenityText(amenity)}
									</li>
								{/each}
							</ul>
						</div>
					</div>

					<div class="mt-12 border-t border-alpine-border pt-10">
						<p class="font-serif text-2xl leading-snug text-alpine-text italic md:text-3xl">
							{$t('rooms.detail_tagline')}
						</p>
					</div>
				</div>

				<aside class="lg:col-span-4">
					<div class="sticky top-36.5 sm:top-33.5 lg:top-32">
						<RoomBookingWidget />
					</div>
				</aside>
			</div>

			<div class="mt-24 border-t border-alpine-border pt-20">
				<h4
					class="mb-10 text-center text-[10px] font-bold tracking-[0.24em] text-alpine-muted uppercase"
				>
					{$t('rooms.gallery_label') || 'Galleria Fotografica'}
				</h4>

				<div class="fade-up-element grid grid-cols-1 gap-8 md:grid-cols-12">
					{#each room.gallery as img, idx}
						<div
							class={idx === 0
								? 'aspect-16/10 overflow-hidden border border-alpine-border bg-stone-200 shadow-sm md:col-span-12'
								: 'aspect-16/10 overflow-hidden border border-alpine-border bg-stone-200 shadow-sm md:col-span-6'}
						>
							<img
								src={img}
								alt={$t(`rooms_data.${slug}.name`)}
								class="img-elegant h-full w-full object-cover transition-transform duration-[1.5s] hover:scale-105"
							/>
						</div>
					{/each}
				</div>
			</div>

			<div class="mt-16 border border-alpine-border bg-white p-8">
				<h4 class="text-[10px] font-bold tracking-[0.22em] text-alpine-muted uppercase">
					{$t('rooms.detail_notes_title') || 'Informazioni utili'}
				</h4>
				<div class="mt-5 space-y-3 text-sm leading-relaxed text-alpine-muted">
					<p>
						{$t('rooms.detail_note_1') ||
							"Le immagini rappresentano la categoria; distribuzione interna e arredi possono variare all'interno dello stesso standard."}
					</p>
					<p>
						{$t('rooms.detail_note_2') ||
							'Configurazioni letto e servizi speciali sono confermati in fase di prenotazione in base alla disponibilita.'}
					</p>
				</div>
			</div>
		</div>
	</div>
{:else}
	<div class="flex h-screen items-center justify-center">
		<p>{$t('errors.not_found')}</p>
	</div>
{/if}
