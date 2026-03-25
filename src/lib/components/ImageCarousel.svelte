<script lang="ts">
  import { ArrowLeft, ArrowRight } from 'lucide-svelte';
  import { fade } from 'svelte/transition';

  interface ImageItem {
    src: string;
    alt: string;
  }

  interface Props {
    images: ImageItem[];
    aspectRatio?: string;
    autoPlay?: boolean;
    autoPlayInterval?: number;
  }

  let {
    images,
    aspectRatio = 'aspect-[4/5]',
    autoPlay = false,
    autoPlayInterval = 5000
  }: Props = $props();

  let currentIndex = $state(0);
  let isAutoPlaying = $state(autoPlay);
  let autoPlayTimer: number | undefined;

  function next() {
    currentIndex = (currentIndex + 1) % images.length;
    resetAutoPlay();
  }

  function prev() {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    resetAutoPlay();
  }

  function goTo(index: number) {
    currentIndex = index;
    resetAutoPlay();
  }

  function resetAutoPlay() {
    if (isAutoPlaying) {
      clearInterval(autoPlayTimer);
      autoPlayTimer = setInterval(next, autoPlayInterval);
    }
  }

  function toggleAutoPlay() {
    isAutoPlaying = !isAutoPlaying;
    if (isAutoPlaying) {
      autoPlayTimer = setInterval(next, autoPlayInterval);
    } else {
      clearInterval(autoPlayTimer);
    }
  }

  // Handle touch/swipe
  let touchStartX = 0;
  let touchEndX = 0;

  function handleTouchStart(event: TouchEvent) {
    touchStartX = event.changedTouches[0].screenX;
  }

  function handleTouchEnd(event: TouchEvent) {
    touchEndX = event.changedTouches[0].screenX;
    handleSwipe();
  }

  function handleSwipe() {
    const swipeThreshold = 50;
    const diff = touchStartX - touchEndX;

    if (Math.abs(diff) > swipeThreshold) {
      if (diff > 0) {
        next();
      } else {
        prev();
      }
    }
  }

  // Initialize auto-play if enabled
  $effect(() => {
    if (autoPlay && isAutoPlaying) {
      autoPlayTimer = setInterval(next, autoPlayInterval);
    }

    return () => {
      if (autoPlayTimer) {
        clearInterval(autoPlayTimer);
      }
    };
  });
</script>

<div class="relative w-full overflow-hidden group">
  <!-- Main Image Container -->
  <div class="{aspectRatio} overflow-hidden bg-alpine-border relative shadow-lg hover:shadow-xl transition-shadow duration-700 cursor-pointer" role="button" tabindex="0"
       ontouchstart={handleTouchStart}
       ontouchend={handleTouchEnd}
       onclick={next}>
    {#key currentIndex}
      <div
        in:fade={{ duration: 800 }}
        out:fade={{ duration: 400 }}
        class="absolute inset-0"
      >
        <img
          src={images[currentIndex].src}
          alt={images[currentIndex].alt}
          class="w-full h-full object-cover img-elegant transform group-hover:scale-105 transition-transform duration-[3s] ease-out"
          loading="lazy"
        />
      </div>
    {/key}

    <!-- Navigation Arrows -->
    <button
      onclick={(e) => { e.stopPropagation(); prev(); }}
      aria-label="Previous image"
      class="absolute left-4 top-1/2 -translate-y-1/2 w-12 h-12 rounded-full bg-white/10 backdrop-blur-md border border-white/20 flex items-center justify-center text-white opacity-0 group-hover:opacity-100 hover:bg-white/20 hover:scale-110 transition-all duration-300 hover:shadow-lg"
    >
      <ArrowLeft class="w-5 h-5" />
    </button>

    <button
      onclick={(e) => { e.stopPropagation(); next(); }}
      aria-label="Next image"
      class="absolute right-4 top-1/2 -translate-y-1/2 w-12 h-12 rounded-full bg-white/10 backdrop-blur-md border border-white/20 flex items-center justify-center text-white opacity-0 group-hover:opacity-100 hover:bg-white/20 hover:scale-110 transition-all duration-300 hover:shadow-lg"
    >
      <ArrowRight class="w-5 h-5" />
    </button>

    <!-- Image Counter -->
    <div class="absolute top-4 right-4 bg-black/20 backdrop-blur-md rounded-full px-3 py-1 text-white text-xs font-medium opacity-0 group-hover:opacity-100 transition-opacity duration-300">
      {currentIndex + 1} / {images.length}
    </div>
  </div>

  <!-- Indicators -->
  <div class="flex justify-center gap-2 mt-6">
    {#each images as _, i}
      <button
        onclick={() => goTo(i)}
        aria-label="Go to image {i + 1}"
        class="h-1.5 rounded-full transition-all duration-500 hover:scale-125 {currentIndex === i ? 'w-8 bg-alpine-gold shadow-sm' : 'w-3 bg-alpine-border hover:bg-alpine-muted'}"
      ></button>
    {/each}
  </div>

  <!-- Auto-play Toggle (optional) -->
  {#if autoPlay}
    <button
      onclick={toggleAutoPlay}
      aria-label={isAutoPlaying ? "Pause auto-play" : "Start auto-play"}
      class="absolute bottom-4 left-4 w-8 h-8 rounded-full bg-black/20 backdrop-blur-md flex items-center justify-center text-white opacity-0 group-hover:opacity-100 hover:bg-black/30 transition-all duration-300"
    >
      {#if isAutoPlaying}
        <div class="w-3 h-3 rounded-sm bg-white"></div>
      {:else}
        <div class="w-0 h-0 border-l-3 border-l-white border-t-1.5 border-t-transparent border-b-1.5 border-b-transparent ml-0.5"></div>
      {/if}
    </button>
  {/if}
</div>