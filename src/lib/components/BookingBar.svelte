<script lang="ts">
  import { t, locale } from '$lib/i18n';
  import Calendar from '$lib/components/Calendar.svelte';
  import { Users, Calendar as CalendarIcon, ChevronDown } from 'lucide-svelte';
  import { clickOutside } from '$lib/utils/clickOutside';

  let arrival = $state('');
  let departure = $state('');
  let adults = $state(2);
  let children = $state(0);

  let showCalendar = $state(false);
  let showGuests = $state(false);

  const bookingUrl = $derived(() => {
    const base = 'https://booking.passepartout.cloud/booking';
    const params = new URLSearchParams({
      oidPortale: '17552',
      lingua: $locale,
      arrivo: arrival || '',
      partenza: departure || '',
      adulti: adults.toString(),
      bambini: children.toString()
    });

    const camereObj = [{ 
      adulti: adults.toString(), 
      bambini: [children.toString()] 
    }];
    params.set('camere', JSON.stringify(camereObj));

    return `${base}?${params.toString()}`;
  });

  function toggleCalendar() {
    showCalendar = !showCalendar;
    showGuests = false;
  }

  function toggleGuests() {
    showGuests = !showGuests;
    showCalendar = false;
  }

  function handleDateSelect() {
    if (arrival && departure) {
      setTimeout(() => showCalendar = false, 300);
    }
  }
</script>

<div class="relative z-20 -mt-16 max-w-5xl mx-auto px-6 fade-up-element">
  <div class="bg-white shadow-2xl flex flex-col md:flex-row items-stretch justify-between border border-alpine-border overflow-visible">
    
    <div class="flex-1 flex flex-col md:flex-row w-full divide-y md:divide-y-0 md:divide-x divide-alpine-border">
      
      <!-- Date Picker Trigger -->
      <div 
        role="button"
        tabindex="0"
        onclick={toggleCalendar}
        onkeydown={(e) => e.key === 'Enter' && toggleCalendar()}
        class="flex-1 p-6 text-left hover:bg-alpine-bg transition-colors relative cursor-pointer outline-none"
        use:clickOutside={() => showCalendar = false}
        aria-label="Seleziona date di arrivo e partenza"
      >
        <span class="block text-[9px] text-alpine-muted uppercase tracking-[0.2em] mb-2 font-bold">Check-in / Check-out</span>
        <div class="flex items-center justify-between">
          <span class="text-sm font-medium text-alpine-text">
            {arrival ? `${arrival} — ${departure || '...'}` : 'Seleziona Date'}
          </span>
          <CalendarIcon class="w-4 h-4 text-alpine-gold" />
        </div>

        {#if showCalendar}
          <div 
            onclick={(e) => e.stopPropagation()}
            onkeydown={(e) => e.stopPropagation()}
            role="presentation"
            class="absolute top-full left-0 mt-2 w-[320px] bg-white shadow-2xl border border-alpine-border z-50 animate-in fade-in slide-in-from-top-2 duration-300"
          >
            <Calendar bind:arrival bind:departure onSelect={handleDateSelect} />
          </div>
        {/if}
      </div>

      <!-- Guest Picker Trigger -->
      <div 
        role="button"
        tabindex="0"
        onclick={toggleGuests}
        onkeydown={(e) => e.key === 'Enter' && toggleGuests()}
        class="flex-1 p-6 text-left hover:bg-alpine-bg transition-colors relative cursor-pointer outline-none"
        use:clickOutside={() => showGuests = false}
        aria-label="Seleziona numero di ospiti"
      >
        <span class="block text-[9px] text-alpine-muted uppercase tracking-[0.2em] mb-2 font-bold">Ospiti</span>
        <div class="flex items-center justify-between">
          <span class="text-sm font-medium text-alpine-text">
            {adults} Adulti, {children} Bambini
          </span>
          <Users class="w-4 h-4 text-alpine-gold" />
        </div>

        {#if showGuests}
          <div 
            onclick={(e) => e.stopPropagation()}
            onkeydown={(e) => e.stopPropagation()}
            role="presentation"
            class="absolute top-full left-0 mt-2 w-full min-w-[240px] bg-white shadow-2xl border border-alpine-border p-6 z-50 animate-in fade-in slide-in-from-top-2 duration-300 space-y-6"
          >
            <div class="flex items-center justify-between">
              <span class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">Adulti</span>
              <div class="flex items-center gap-4 bg-alpine-bg px-3 py-1">
                <button type="button" onclick={() => adults = Math.max(1, adults - 1)} class="text-lg hover:text-alpine-gold transition-colors">-</button>
                <span class="text-xs font-bold w-4 text-center">{adults}</span>
                <button type="button" onclick={() => adults = Math.min(4, adults + 1)} class="text-lg hover:text-alpine-gold transition-colors">+</button>
              </div>
            </div>
            <div class="flex items-center justify-between">
              <span class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">Bambini</span>
              <div class="flex items-center gap-4 bg-alpine-bg px-3 py-1">
                <button type="button" onclick={() => children = Math.max(0, children - 1)} class="text-lg hover:text-alpine-gold transition-colors">-</button>
                <span class="text-xs font-bold w-4 text-center">{children}</span>
                <button type="button" onclick={() => children = Math.min(3, children + 1)} class="text-lg hover:text-alpine-gold transition-colors">+</button>
              </div>
            </div>
          </div>
        {/if}
      </div>

    </div>

    <!-- CTA -->
    <a 
      href={bookingUrl()} 
      target="_blank"
      class="w-full md:w-auto bg-alpine-text text-white px-12 py-8 text-[11px] font-bold tracking-[0.2em] uppercase hover:bg-alpine-gold transition-all text-center flex items-center justify-center gap-2 group"
    >
      <span>{$t('booking.check')}</span>
      <ChevronDown class="w-4 h-4 -rotate-90 group-hover:translate-x-1 transition-transform" />
    </a>
  </div>
</div>
