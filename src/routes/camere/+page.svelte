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
      class="w-full h-full object-cover ken-burns opacity-70"
    >
    <div class="absolute inset-0 bg-linear-to-b from-black/40 via-transparent to-alpine-bg"></div>
  </div>
  <div class="absolute inset-0 flex flex-col items-center justify-end px-6 pb-24 text-center z-10 pt-20">
    <h1 class="font-serif text-5xl md:text-7xl text-white font-light tracking-tight fade-up-element">{$t('rooms.main_title') || "Le Nostre Camere"}</h1>
    <p class="mt-6 text-white/80 text-[10px] md:text-xs tracking-[0.4em] uppercase font-bold fade-up-element">{$t('home.rooms_subtitle')}</p>
  </div>
</div>

<div class="py-24 px-6 bg-alpine-bg min-h-screen">
  <div class="max-w-7xl mx-auto">
    
    <div class="grid grid-cols-1 md:grid-cols-2 gap-16 lg:gap-24">
      {#each Object.entries(rooms) as [key, room], i}
        <a 
          href="/camere/{key}" 
          class="group fade-up-element cursor-pointer {i % 2 === 1 ? 'md:mt-32' : ''}"
        >
          <div class="aspect-4/5 overflow-hidden bg-alpine-border mb-8 shadow-sm">
            <img 
              src={room.image} 
              alt={$t(`rooms_data.${key}.name`)} 
              class="w-full h-full object-cover img-elegant transition-transform duration-1000 group-hover:scale-105" 
            />
          </div>
          <div class="flex justify-between items-start">
            <div>
              <h3 class="font-serif text-3xl mb-2 text-alpine-text">{$t(`rooms_data.${key}.name`)}</h3>
              <p class="text-xs text-alpine-muted uppercase tracking-widest font-bold tracking-widest">{room.price}</p>
            </div>
            <div class="w-10 h-10 rounded-full border border-alpine-border flex items-center justify-center group-hover:bg-alpine-text group-hover:text-white transition-all">
              <ArrowRight class="w-4 h-4" />
            </div>
          </div>
        </a>
      {/each}
    </div>

  </div>
</div>
