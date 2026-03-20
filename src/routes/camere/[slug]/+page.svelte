<script lang="ts">
  import { page } from '$app/state';
  import { rooms } from '$lib/rooms';
  import { t } from '$lib/i18n';
  import { ChevronLeft, Check } from 'lucide-svelte';
  import RoomBookingWidget from '$lib/components/RoomBookingWidget.svelte';

  const slug = $derived(page.params.slug);
  const room = $derived(rooms[slug as keyof typeof rooms]);
  const title = $derived(room ? `${room.name} | Hotel du Soleil` : 'Camera non trovata');
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
        alt={room.name} 
        class="w-full h-full object-cover ken-burns opacity-70"
      >
      <div class="absolute inset-0 bg-gradient-to-b from-black/40 via-transparent to-alpine-bg"></div>
    </div>
    <div class="absolute inset-0 flex flex-col items-center justify-center px-6 text-center z-10 pt-20">
      <h1 class="font-serif text-5xl md:text-7xl text-white font-light tracking-tight">{room.name}</h1>
    </div>
  </div>

  <div class="pb-24 px-6 bg-alpine-bg min-h-screen">
    <div class="max-w-7xl mx-auto">
      
      <!-- Back Link -->
      <a href="/camere" class="inline-flex items-center gap-2 text-alpine-muted text-[10px] uppercase font-bold tracking-widest my-12 hover:text-alpine-gold transition-colors">
        <ChevronLeft class="w-4 h-4" />
        Tutte le sistemazioni
      </a>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-16 items-start">
        
        <!-- Main Content (Info) -->
        <div class="lg:col-span-2 fade-up-element">
          <h2 class="font-serif text-4xl text-alpine-text mb-8">Descrizione</h2>
          <p class="text-alpine-muted leading-relaxed text-lg mb-12 font-light whitespace-pre-line">
            {room.description}
          </p>

          <div class="mb-12 border-t border-alpine-border pt-12">
            <h4 class="text-[10px] uppercase tracking-widest text-alpine-text font-bold mb-8">Servizi inclusi</h4>
            <ul class="grid grid-cols-1 md:grid-cols-2 gap-y-4 gap-x-8">
              {#each room.amenities as amenity}
                <li class="flex items-center gap-3 text-sm text-alpine-muted border-b border-alpine-border/30 pb-3">
                  <Check class="w-3 h-3 text-alpine-gold" />
                  {amenity}
                </li>
              {/each}
            </ul>
          </div>
        </div>

        <!-- Sticky Sidebar (Booking Widget) -->
        <div class="lg:col-span-1">
          <RoomBookingWidget />
        </div>

      </div>

      <!-- Full Width Gallery -->
      <div class="mt-24 pt-24 border-t border-alpine-border">
        <h4 class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold mb-12 text-center">Galleria Fotografica</h4>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 fade-up-element">
          {#each room.gallery as img}
            <div class="aspect-[16/10] overflow-hidden bg-stone-200 shadow-sm">
              <img src={img} alt={room.name} class="w-full h-full object-cover img-elegant hover:scale-105 transition-transform duration-[1.5s]" />
            </div>
          {/each}
        </div>
      </div>

    </div>
  </div>
{:else}
  <div class="h-screen flex items-center justify-center">
    <p>Camera non trovata.</p>
  </div>
{/if}
