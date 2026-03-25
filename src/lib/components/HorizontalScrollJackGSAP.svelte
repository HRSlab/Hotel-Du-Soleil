/* eslint-disable svelte/require-each-key */
<script lang="ts">
	interface ImageItem {
		src: string;
		alt: string;
	}

	interface Props {
		images: ImageItem[];
	}

	let { images }: Props = $props();
</script>

<div class="w-full max-w-7xl mx-auto px-6">
	<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
		{#each images as image, i}
			<div class="group relative aspect-[4/3] overflow-hidden rounded-lg bg-gray-100">
				<img
					src={image.src}
					alt={image.alt}
					class="w-full h-full object-cover transition-transform duration-300 group-hover:scale-105"
					loading="lazy"
				/>

				<!-- Overlay -->
				<div class="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition-colors duration-300"></div>

				<!-- Title -->
				<div class="absolute bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-black/80 to-transparent">
					<h3 class="text-white font-serif text-lg font-light">
						{image.alt}
					</h3>
				</div>
			</div>
		{/each}
	</div>
</div>