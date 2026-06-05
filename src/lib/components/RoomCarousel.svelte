<script lang="ts">
	import { rooms } from '$lib/rooms';
	import { ArrowLeft, ArrowRight } from 'lucide-svelte';
	import { fade, fly } from 'svelte/transition';
	import { t } from '$lib/i18n';

	const roomList = Object.entries(rooms);
	let currentIndex = $state(0);

	function next() {
		currentIndex = (currentIndex + 1) % roomList.length;
	}

	function prev() {
		currentIndex = (currentIndex - 1 + roomList.length) % roomList.length;
	}

	const currentRoomKey = $derived(roomList[currentIndex][0]);
	const currentRoomData = $derived(roomList[currentIndex][1]);
</script>

<div class="relative w-full overflow-hidden py-12">
	<div class="mx-auto max-w-7xl px-6">
		<div class="grid grid-cols-1 items-center gap-12 lg:grid-cols-12">
			<!-- Image Column -->
			<div class="group relative lg:col-span-7">
				<div class="relative aspect-16/10 overflow-hidden bg-stone-200 shadow-sm">
					{#key currentIndex}
						<div in:fade={{ duration: 800 }} out:fade={{ duration: 400 }} class="absolute inset-0">
							<img
								src={currentRoomData.image}
								alt={$t(`rooms_data.${currentRoomKey}.name`)}
								class="img-elegant h-full w-full scale-100 transform object-cover transition-transform duration-[2s] group-hover:scale-105"
							/>
						</div>
					{/key}

					<!-- Overlay Controls (Mobile) -->
					<div class="absolute right-0 bottom-0 flex bg-white/90 backdrop-blur-md lg:hidden">
						<button
							onclick={prev}
							aria-label={$t('common.prev') || 'Precedente'}
							class="p-6 transition-colors hover:bg-alpine-text hover:text-white"
						>
							<ArrowLeft class="h-5 w-5" />
						</button>
						<button
							onclick={next}
							aria-label={$t('common.next') || 'Successiva'}
							class="p-6 transition-colors hover:bg-alpine-text hover:text-white"
						>
							<ArrowRight class="h-5 w-5" />
						</button>
					</div>
				</div>
			</div>

			<!-- Info Column -->
			<div class="flex flex-col justify-center lg:col-span-5">
				{#key currentIndex}
					<div in:fly={{ x: 20, duration: 800, delay: 200 }} class="space-y-6">
						<div class="flex items-center gap-3 text-alpine-gold">
							<span class="text-[10px] font-bold tracking-[0.3em] uppercase"
								>0{currentIndex + 1} / 0{roomList.length}</span
							>
							<div class="h-px w-8 bg-alpine-gold/30"></div>
						</div>

						<h3 class="font-serif text-5xl leading-tight font-light text-alpine-text md:text-6xl">
							{$t(`rooms_data.${currentRoomKey}.name`)}
						</h3>

						<p
							class="line-clamp-3 text-sm leading-relaxed font-light text-alpine-muted md:text-base"
						>
							{$t(`rooms_data.${currentRoomKey}.description`)}
						</p>

						<div class="pt-6">
							<a href="/camere/{currentRoomKey}" class="group/btn inline-flex items-center gap-4">
								<span class="mt-1 text-[11px] font-bold tracking-[0.2em] text-alpine-text uppercase"
									>{$t('home.rooms_cta') || 'Esplora Dettagli'}</span
								>
								<div
									class="flex h-12 w-12 items-center justify-center rounded-full border border-alpine-border transition-all duration-500 group-hover/btn:bg-alpine-text group-hover/btn:text-white"
								>
									<ArrowRight class="h-4 w-4" />
								</div>
							</a>
						</div>
					</div>
				{/key}

				<!-- Controls (Desktop) -->
				<div class="mt-16 hidden items-center gap-8 border-t border-alpine-border pt-8 lg:flex">
					<div class="flex gap-4">
						<button
							onclick={prev}
							aria-label={$t('common.prev') || 'Precedente'}
							class="flex h-14 w-14 items-center justify-center rounded-full border border-alpine-border transition-all duration-500 hover:bg-alpine-text hover:text-white"
						>
							<ArrowLeft class="h-5 w-5" />
						</button>
						<button
							onclick={next}
							aria-label={$t('common.next') || 'Successiva'}
							class="flex h-14 w-14 items-center justify-center rounded-full border border-alpine-border transition-all duration-500 hover:bg-alpine-text hover:text-white"
						>
							<ArrowRight class="h-5 w-5" />
						</button>
					</div>

					<!-- Indicators -->
					<div class="flex gap-2">
						{#each roomList as _, i}
							<button
								onclick={() => (currentIndex = i)}
								aria-label="Room {i + 1}"
								class="h-1 transition-all duration-500 {currentIndex === i
									? 'w-12 bg-alpine-gold'
									: 'w-4 bg-alpine-border hover:bg-alpine-muted'}"
							></button>
						{/each}
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
