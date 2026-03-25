<script lang="ts">
  import { onMount } from 'svelte';

  interface ImageItem {
    src: string;
    alt: string;
  }

  interface Props {
    images: ImageItem[];
  }

  let { images }: Props = $props();

  let container: HTMLElement;
  let scrollContainer: HTMLElement;
  let isScrolling = false;
  let scrollX = $state(0);
  let targetScrollX = $state(0);
  let lerpFactor = 0.08; // Adjust for smoothness (0.01 = very smooth, 0.2 = responsive)

  // Parallax layers
  let backgroundLeft: HTMLElement;
  let backgroundRight: HTMLElement;
  let centerLayer: HTMLElement;

  // Scroll bounds
  let maxScrollX = 0;
  let sectionWidth = 0;

  function updateMaxScroll() {
    if (container && scrollContainer) {
      sectionWidth = container.offsetWidth;
      const totalWidth = images.length * sectionWidth;
      maxScrollX = Math.max(0, totalWidth - window.innerWidth);
    }
  }

  function handleWheel(event: WheelEvent) {
    event.preventDefault();

    // Convert vertical scroll to horizontal with momentum
    const deltaX = event.deltaY * 1.5; // Adjust multiplier for sensitivity
    targetScrollX = Math.max(0, Math.min(maxScrollX, targetScrollX + deltaX));

    if (!isScrolling) {
      isScrolling = true;
      requestAnimationFrame(animateScroll);
    }
  }

  function animateScroll() {
    // Enhanced lerp with easing
    const ease = 1 - Math.pow(1 - lerpFactor, 3); // Cubic ease-out
    scrollX += (targetScrollX - scrollX) * ease;

    // Apply transforms to parallax layers with different speeds
    const parallaxOffset = scrollX;
    if (backgroundLeft) {
      backgroundLeft.style.transform = `translateX(${-parallaxOffset * 0.2}px)`;
    }
    if (backgroundRight) {
      backgroundRight.style.transform = `translateX(${-parallaxOffset * 0.15}px)`;
    }
    if (centerLayer) {
      centerLayer.style.transform = `translateX(${-parallaxOffset}px)`;
    }

    // Continue animation if not close to target
    if (Math.abs(targetScrollX - scrollX) > 0.5) {
      requestAnimationFrame(animateScroll);
    } else {
      isScrolling = false;
    }
  }

  function handleResize() {
    updateMaxScroll();
  }

  onMount(() => {
    updateMaxScroll();

    // Add scroll-jack class to body
    document.body.classList.add('horizontal-scroll-jack-active');

    // Add event listeners
    window.addEventListener('wheel', handleWheel, { passive: false });
    window.addEventListener('resize', handleResize);

    return () => {
      // Remove scroll-jack class from body
      document.body.classList.remove('horizontal-scroll-jack-active');

      window.removeEventListener('wheel', handleWheel);
      window.removeEventListener('resize', handleResize);
    };
  });
</script>

<div bind:this={container} class="relative w-full h-screen overflow-hidden bg-black">
  <!-- Background Left Layer (slowest, blurred) -->
  <div bind:this={backgroundLeft} class="absolute inset-0 flex opacity-40">
    {#each images as image, i}
      <div class="flex-shrink-0 w-screen h-full relative">
        <img
          src={image.src}
          alt=""
          class="w-full h-full object-cover blur-sm scale-110 brightness-50"
          loading="lazy"
        />
      </div>
    {/each}
  </div>

  <!-- Background Right Layer (medium speed, more blurred) -->
  <div bind:this={backgroundRight} class="absolute inset-0 flex opacity-30">
    {#each images as image, i}
      <div class="flex-shrink-0 w-screen h-full relative">
        <img
          src={image.src}
          alt=""
          class="w-full h-full object-cover blur-md scale-125 brightness-25"
          loading="lazy"
        />
      </div>
    {/each}
  </div>

  <!-- Center Layer (main content, full speed) -->
  <div bind:this={centerLayer} class="absolute inset-0 flex">
    {#each images as image, i}
      <div class="flex-shrink-0 w-screen h-full relative flex items-center justify-center">
        <!-- Content Overlay -->
        <div class="relative z-20 text-center px-6 max-w-4xl mx-auto">
          <div class="bg-black/30 backdrop-blur-lg rounded-3xl p-12 border border-white/10 shadow-2xl">
            <h3 class="font-serif text-5xl md:text-7xl text-white mb-6 leading-tight font-light">
              {image.alt}
            </h3>
            <p class="text-white/70 text-xl leading-relaxed font-light max-w-2xl mx-auto">
              {#if i === 0}
                Scopri la bellezza delle nostre piste innevate
              {:else if i === 1}
                Vivi l'emozione dello sci in compagnia
              {:else if i === 2}
                Ammira panorami mozzafiato dalla gondola
              {:else if i === 3}
                Scivola su piste perfettamente preparate
              {:else if i === 4}
                Partecipa alle nostre attività sulla neve
              {:else if i === 5}
                Esplora tutti gli sport invernali disponibili
              {:else}
                L'esperienza completa del nostro comprensorio
              {/if}
            </p>
          </div>
        </div>

        <!-- Main Image -->
        <img
          src={image.src}
          alt={image.alt}
          class="absolute inset-0 w-full h-full object-cover"
          loading="lazy"
        />

        <!-- Vignette Effect -->
        <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-black/40"></div>
      </div>
    {/each}
  </div>

  <!-- Scroll Progress Indicator -->
  <div class="absolute bottom-12 left-1/2 -translate-x-1/2 z-30">
    <div class="bg-black/20 backdrop-blur-lg rounded-full px-6 py-3 border border-white/10">
      <div class="flex gap-3">
        {#each images as _, i}
          <div
            class="h-2 rounded-full transition-all duration-500 {Math.abs(scrollX - (i * sectionWidth)) < sectionWidth / 2 ? 'w-12 bg-white shadow-lg' : 'w-3 bg-white/40 hover:bg-white/60'}"
          ></div>
        {/each}
      </div>
    </div>
  </div>

  <!-- Scroll Hint -->
  <div class="absolute bottom-8 right-12 z-30">
    <div class="bg-black/20 backdrop-blur-lg rounded-full px-4 py-2 border border-white/10">
      <div class="flex items-center gap-3 text-white/80 text-sm font-light">
        <span>Scroll</span>
        <div class="w-5 h-5 border border-white/40 rounded-full flex items-center justify-center">
          <div class="w-1.5 h-1.5 border-r border-b border-white/40 rotate-45"></div>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
  /* Disable default scrolling for this component only */
  :global(.horizontal-scroll-jack-active) {
    overflow: hidden !important;
  }

  /* Smooth transitions for parallax layers */
  .parallax-layer {
    will-change: transform;
  }
</style>