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
  <div class="max-w-7xl mx-auto px-6">
    
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
      
      <!-- Image Column -->
      <div class="lg:col-span-7 relative group">
        <div class="aspect-16/10 overflow-hidden bg-stone-200 relative shadow-sm">
          {#key currentIndex}
            <div 
              in:fade={{ duration: 800 }} 
              out:fade={{ duration: 400 }}
              class="absolute inset-0"
            >
              <img 
                src={currentRoomData.image} 
                alt={$t(`rooms_data.${currentRoomKey}.name`)} 
                class="w-full h-full object-cover img-elegant transform scale-100 group-hover:scale-105 transition-transform duration-[2s]"
              />
            </div>
          {/key}
          
          <!-- Overlay Controls (Mobile) -->
          <div class="absolute bottom-0 right-0 flex lg:hidden bg-white/90 backdrop-blur-md">
            <button onclick={prev} aria-label={$t('common.prev') || "Precedente"} class="p-6 hover:bg-alpine-text hover:text-white transition-colors">
              <ArrowLeft class="w-5 h-5" />
            </button>
            <button onclick={next} aria-label={$t('common.next') || "Successiva"} class="p-6 hover:bg-alpine-text hover:text-white transition-colors">
              <ArrowRight class="w-5 h-5" />
            </button>
          </div>
        </div>
      </div>

      <!-- Info Column -->
      <div class="lg:col-span-5 flex flex-col justify-center">
        {#key currentIndex}
          <div 
            in:fly={{ x: 20, duration: 800, delay: 200 }} 
            class="space-y-6"
          >
            <div class="flex items-center gap-3 text-alpine-gold">
              <span class="text-[10px] uppercase tracking-[0.3em] font-bold">0{currentIndex + 1} / 0{roomList.length}</span>
              <div class="h-[1px] w-8 bg-alpine-gold/30"></div>
            </div>
            
            <h3 class="font-serif text-5xl md:text-6xl text-alpine-text leading-tight font-light">
              {$t(`rooms_data.${currentRoomKey}.name`)}
            </h3>
            
            <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base line-clamp-3">
              {$t(`rooms_data.${currentRoomKey}.description`)}
            </p>

            <div class="pt-6">
              <a 
                href="/camere/{currentRoomKey}" 
                class="inline-flex items-center gap-4 group/btn"
              >
                <span class="text-[11px] uppercase tracking-[0.2em] font-bold text-alpine-text mt-1">{$t('home.rooms_cta') || "Esplora Dettagli"}</span>
                <div class="w-12 h-12 rounded-full border border-alpine-border flex items-center justify-center group-hover/btn:bg-alpine-text group-hover/btn:text-white transition-all duration-500">
                  <ArrowRight class="w-4 h-4" />
                </div>
              </a>
            </div>
          </div>
        {/key}

        <!-- Controls (Desktop) -->
        <div class="hidden lg:flex items-center gap-8 mt-16 border-t border-alpine-border pt-8">
          <div class="flex gap-4">
            <button 
              onclick={prev} 
              aria-label={$t('common.prev') || "Precedente"}
              class="w-14 h-14 rounded-full border border-alpine-border flex items-center justify-center hover:bg-alpine-text hover:text-white transition-all duration-500"
            >
              <ArrowLeft class="w-5 h-5" />
            </button>
            <button 
              onclick={next} 
              aria-label={$t('common.next') || "Successiva"}
              class="w-14 h-14 rounded-full border border-alpine-border flex items-center justify-center hover:bg-alpine-text hover:text-white transition-all duration-500"
            >
              <ArrowRight class="w-5 h-5" />
            </button>
          </div>
          
          <!-- Indicators -->
          <div class="flex gap-2">
            {#each roomList as _, i}
              <button 
                onclick={() => currentIndex = i}
                aria-label="Room {i + 1}"
                class="h-1 transition-all duration-500 {currentIndex === i ? 'w-12 bg-alpine-gold' : 'w-4 bg-alpine-border hover:bg-alpine-muted'}"
              ></button>
            {/each}
          </div>
        </div>
      </div>

    </div>

  </div>
</div>

<style>
  .line-clamp-3 {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    line-clamp: 3;
    overflow: hidden;
  }
</style>
