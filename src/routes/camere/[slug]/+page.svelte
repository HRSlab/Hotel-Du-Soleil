<script lang="ts">
  import { page } from '$app/state';
  import { rooms } from '$lib/rooms';
  import { t } from '$lib/i18n';
  import { ChevronLeft, Check } from 'lucide-svelte';
  import RoomBookingWidget from '$lib/components/RoomBookingWidget.svelte';

  const slug = $derived(page.params.slug);
  const room = $derived(rooms[slug as keyof typeof rooms]);
  const title = $derived(room ? `${$t(`rooms_data.${slug}.name`)} | Chalet du Soleil` : $t('errors.not_found'));
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
        class="w-full h-full object-cover ken-burns opacity-70"
      >
      <div class="absolute inset-0 bg-linear-to-b from-black/40 via-transparent to-alpine-bg"></div>
    </div>
    <div class="absolute inset-0 flex flex-col items-center justify-end px-6 pb-24 text-center z-10 pt-20">
      <h1 class="font-serif text-5xl md:text-7xl text-white font-light tracking-tight fade-up-element">{$t(`rooms_data.${slug}.name`)}</h1>
    </div>
  </div>

  <div class="pb-24 px-6 bg-alpine-bg min-h-screen">
    <div class="max-w-7xl mx-auto">
      
      <!-- Back Link -->
      <a href="/camere" class="inline-flex items-center gap-2 text-alpine-muted text-[10px] uppercase font-bold tracking-[0.2em] my-12 hover:text-alpine-gold transition-colors fade-up-element">
        <ChevronLeft class="w-4 h-4" />
        {$t('rooms.back_link') || "Tutte le sistemazioni"}
      </a>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-16 items-start">
        
        <!-- Main Content (Info) -->
        <div class="lg:col-span-2 fade-up-element">
          <h2 class="font-serif text-4xl text-alpine-text mb-8">{$t('rooms.description_label') || "Descrizione"}</h2>
          <p class="text-alpine-muted leading-relaxed text-lg mb-12 font-light whitespace-pre-line">
            {$t(`rooms_data.${slug}.description`)}
          </p>

          <div class="mb-12 border-t border-alpine-border pt-12">
            <h4 class="text-[10px] uppercase tracking-widest text-alpine-text font-bold mb-8 italic">{$t('rooms.amenities_label') || "Servizi inclusi"}</h4>
            <ul class="grid grid-cols-1 md:grid-cols-2 gap-y-4 gap-x-8">
              {#each room.amenities as amenity}
                <li class="flex items-center gap-3 text-sm text-alpine-muted border-b border-alpine-border/30 pb-3 font-light">
                  <Check class="w-3 h-3 text-alpine-gold" />
                  {amenity}
                </li>
              {/each}
            </ul>
          </div>

          <!-- Emotional Tagline -->
          <div class="mt-16 py-12 border-t border-alpine-border">
            <p class="font-serif text-2xl md:text-3xl text-alpine-text italic leading-snug">
              "A soli <span class="text-alpine-gold">20 metri</span> dalle piste da sci, la vostra stanza non è solo un letto: è il vostro <span class="text-alpine-gold">Base Camp</span>."
            </p>
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
            <div class="aspect-16/10 overflow-hidden bg-stone-200 shadow-sm border border-alpine-border">
              <img src={img} alt={$t(`rooms_data.${slug}.name`)} class="w-full h-full object-cover img-elegant hover:scale-105 transition-transform duration-[1.5s]" />
            </div>
          {/each}
        </div>
      </div>

    </div>
  </div>
{:else}
  <div class="h-screen flex items-center justify-center">
    <p>{$t('errors.not_found')}</p>
  </div>
{/if}
