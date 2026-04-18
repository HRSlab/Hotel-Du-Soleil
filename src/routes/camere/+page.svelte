<script lang="ts">
	import { rooms } from '$lib/rooms';
	import { ArrowRight } from 'lucide-svelte';
	import { t } from '$lib/i18n';
</script>

<svelte:head>
	<title>{$t('rooms.title')} | Chalet du Soleil</title>
</svelte:head>

<div class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
	<div class="absolute inset-0">
		<img
			src="/imgs/Rooms/matrimoniale-superior-hero-1.webp"
			alt="Sistemazioni Hero"
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
			{$t('rooms.main_title') || 'Le Nostre Camere'}
		</h1>
		<p
			class="fade-up-element mt-6 text-[10px] font-bold tracking-[0.4em] text-white/80 uppercase md:text-xs"
		>
			{$t('home.rooms_subtitle')}
		</p>
	</div>
</div>

<div class="min-h-screen bg-alpine-bg px-6 py-24">
	<div class="mx-auto max-w-7xl">
		<div class="mb-14 border-b border-alpine-border pb-8 text-center md:text-left">
			<p class="text-[10px] font-bold tracking-[0.24em] text-alpine-muted uppercase">
				{$t('rooms.collection_label') || 'Suite Collection'}
			</p>
			<p
				class="mx-auto mt-4 max-w-3xl text-sm leading-relaxed font-light text-alpine-muted md:mx-0 md:text-base"
			>
				{$t('rooms.collection_text') ||
					'Ogni camera interpreta lo stesso linguaggio: materiali naturali, comfort essenziale e una relazione diretta con il paesaggio alpino.'}
			</p>
		</div>

		<div class="grid grid-cols-1 gap-16 md:grid-cols-2 lg:gap-20">
			{#each Object.entries(rooms) as [key, room], i}
				<a
					href="/camere/{key}"
					class="group fade-up-element cursor-pointer {i % 2 === 1 ? 'md:mt-24' : ''}"
				>
					<div class="aspect-4/5 overflow-hidden bg-alpine-border shadow-sm">
						<img
							src={room.image}
							alt={$t(`rooms_data.${key}.name`)}
							class="img-elegant h-full w-full object-cover transition-transform duration-1000 group-hover:scale-105"
						/>
					</div>
					<div class="border border-t-0 border-alpine-border bg-white px-7 py-7">
						<div class="flex items-start justify-between gap-4">
							<div>
								<h3 class="font-serif text-3xl text-alpine-text">{$t(`rooms_data.${key}.name`)}</h3>
								<p class="mt-1 text-xs font-bold tracking-[0.2em] text-alpine-muted uppercase">
									{room.price}
								</p>
							</div>
							<div
								class="flex h-10 w-10 items-center justify-center rounded-full border border-alpine-border transition-all group-hover:bg-alpine-text group-hover:text-white"
							>
								<ArrowRight class="h-4 w-4" />
							</div>
						</div>

						<p class="mt-4 line-clamp-3 text-sm leading-relaxed font-light text-alpine-muted">
							{$t(`rooms_data.${key}.description`)}
						</p>

						<div class="mt-5 grid grid-cols-3 gap-3 border-t border-alpine-border pt-5 text-center">
							<div>
								<p class="text-[10px] font-bold tracking-[0.18em] text-alpine-muted uppercase">
									{$t('rooms.size_label') || 'Size'}
								</p>
								<p class="mt-1 text-xs text-alpine-text">
									{$t(`rooms_specs.${key}.size`) || room.size}
								</p>
							</div>
							<div>
								<p class="text-[10px] font-bold tracking-[0.18em] text-alpine-muted uppercase">
									{$t('rooms.occupancy_label') || 'Guests'}
								</p>
								<p class="mt-1 text-xs text-alpine-text">
									{$t(`rooms_specs.${key}.occupancy`) || room.occupancy}
								</p>
							</div>
							<div>
								<p class="text-[10px] font-bold tracking-[0.18em] text-alpine-muted uppercase">
									{$t('rooms.beds_label') || 'Beds'}
								</p>
								<p class="mt-1 text-xs text-alpine-text">
									{$t(`rooms_specs.${key}.beds`) || room.bedType}
								</p>
							</div>
						</div>
					</div>
				</a>
			{/each}
		</div>
	</div>
</div>
