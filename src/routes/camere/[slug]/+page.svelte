<script lang="ts">
	import { page } from '$app/state';
	import { rooms } from '$lib/rooms';
	import { t, locale } from '$lib/i18n';
	import { ChevronLeft, Check } from 'lucide-svelte';
	import RoomBookingWidget from '$lib/components/RoomBookingWidget.svelte';

	const slug = $derived(page.params.slug);
	const room = $derived(rooms[slug as keyof typeof rooms]);
	const title = $derived(
		room ? `${$t(`rooms_data.${slug}.name`)} | Hotel du Soleil` : $t('errors.not_found')
	);
	const copy = $derived(
		$locale === 'ru'
			? {
					tagline:
						'Всего в 20 метрах от склонов ваш номер становится не просто местом для сна, а вашим базовым лагерем в горах.',
					gallery: 'Фотогалерея'
				}
			: {
					tagline:
						'A soli 20 metri dalle piste da sci, la vostra stanza non e solo un letto: e il vostro Base Camp.',
					gallery: 'Galleria Fotografica'
				}
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
			<h1
				class="fade-up-element font-serif text-5xl font-light tracking-tight text-white md:text-7xl"
			>
				{$t(`rooms_data.${slug}.name`)}
			</h1>
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

			<div class="grid grid-cols-1 items-start gap-16 lg:grid-cols-3">
				<!-- Main Content (Info) -->
				<div class="fade-up-element lg:col-span-2">
					<h2 class="mb-8 font-serif text-4xl text-alpine-text">
						{$t('rooms.description_label') || 'Descrizione'}
					</h2>
					<p class="mb-12 text-lg leading-relaxed font-light whitespace-pre-line text-alpine-muted">
						{$t(`rooms_data.${slug}.description`)}
					</p>

					<div class="mb-12 border-t border-alpine-border pt-12">
						<h4
							class="mb-8 text-[10px] font-bold tracking-widest text-alpine-text uppercase italic"
						>
							{$t('rooms.amenities_label') || 'Servizi inclusi'}
						</h4>
						<ul class="grid grid-cols-1 gap-x-8 gap-y-4 md:grid-cols-2">
							{#each room.amenities as amenity}
								<li
									class="flex items-center gap-3 border-b border-alpine-border/30 pb-3 text-sm font-light text-alpine-muted"
								>
									<Check class="h-3 w-3 text-alpine-gold" />
									{amenity}
								</li>
							{/each}
						</ul>
					</div>

					<!-- Emotional Tagline -->
					<div class="mt-16 border-t border-alpine-border py-12">
						<p class="font-serif text-2xl leading-snug text-alpine-text italic md:text-3xl">
							{copy.tagline}
						</p>
					</div>
				</div>

				<!-- Sticky Sidebar (Booking Widget) -->
				<div class="lg:col-span-1">
					<RoomBookingWidget />
				</div>
			</div>

			<!-- Full Width Gallery -->
			<div class="mt-24 border-t border-alpine-border pt-24">
				<h4
					class="mb-12 text-center text-[10px] font-bold tracking-widest text-alpine-muted uppercase"
				>
					{copy.gallery}
				</h4>
				<div class="fade-up-element grid grid-cols-1 gap-8 md:grid-cols-2">
					{#each room.gallery as img}
						<div
							class="aspect-16/10 overflow-hidden border border-alpine-border bg-stone-200 shadow-sm"
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
		</div>
	</div>
{:else}
	<div class="flex h-screen items-center justify-center">
		<p>{$t('errors.not_found')}</p>
	</div>
{/if}
