<script lang="ts">
  import { t, locale } from '$lib/i18n';
  import Calendar from '$lib/components/Calendar.svelte';
  import { Users, Calendar as CalendarIcon, ChevronDown } from 'lucide-svelte';
  import { clickOutside } from '$lib/utils/clickOutside';
  import { SvelteURLSearchParams } from 'svelte/reactivity';

  let arrival = $state('');
  let departure = $state('');
  let adults = $state(2);
  let children = $state(0);

  let showCalendar = $state(false);
  let showGuests = $state(false);

  const bookingUrl = $derived(() => {
    const base = 'https://booking.passepartout.cloud/booking';
    const params = new SvelteURLSearchParams({
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

<div class="relative z-20 -mt-16 max-w-6xl mx-auto px-6 fade-up-element">
  <div class="bg-white shadow-2xl flex flex-col md:flex-row items-stretch justify-between border border-alpine-border overflow-visible">
    
    <div class="flex-1 flex flex-col md:flex-row w-full divide-y md:divide-y-0 md:divide-x divide-alpine-border">
      
      <div 
        role="button"
        tabindex="0"
        onclick={toggleCalendar}
        onkeydown={(e) => e.key === 'Enter' && toggleCalendar()}
        class="flex-1 px-8 py-6 md:py-8 text-left hover:bg-alpine-bg transition-colors relative cursor-pointer outline-none group"
        use:clickOutside={() => showCalendar = false}
        aria-label={$t('booking.select_dates')}
      >
        <span class="block text-[11px] text-alpine-muted uppercase tracking-[0.2em] mb-3 font-bold">Check-in / Check-out</span>
        <div class="flex items-center justify-between">
          <span class="text-base md:text-lg font-medium text-alpine-text group-hover:text-alpine-gold transition-colors">
            {arrival ? `${arrival} — ${departure || '...'}` : ($t('booking.select_dates') || 'Seleziona Date')}
          </span>
          <CalendarIcon class="w-5 h-5 text-alpine-gold opacity-80" />
        </div>

        {#if showCalendar}
          <div 
            onclick={(e) => e.stopPropagation()}
            onkeydown={(e) => e.stopPropagation()}
            role="presentation"
            class="absolute top-full mt-4 w-[90vw] max-w-[340px] md:w-[340px] bg-white shadow-2xl border border-alpine-border z-50 animate-in fade-in slide-in-from-top-2 duration-300 left-1/2 -translate-x-1/2 md:left-0 md:translate-x-0"
          >
            <Calendar bind:arrival bind:departure onSelect={handleDateSelect} />
          </div>
        {/if}
      </div>

      <div 
        role="button"
        tabindex="0"
        onclick={toggleGuests}
        onkeydown={(e) => e.key === 'Enter' && toggleGuests()}
        class="flex-1 px-8 py-6 md:py-8 text-left hover:bg-alpine-bg transition-colors relative cursor-pointer outline-none group"
        use:clickOutside={() => showGuests = false}
        aria-label={$t('booking.guests_label')}
      >
        <span class="block text-[11px] text-alpine-muted uppercase tracking-[0.2em] mb-3 font-bold">{$t('booking.guests_label') || "Ospiti"}</span>
        <div class="flex items-center justify-between">
          <span class="text-base md:text-lg font-medium text-alpine-text group-hover:text-alpine-gold transition-colors">
            {adults} {$t('booking.adults')}, {children} {$t('booking.children')}
          </span>
          <Users class="w-5 h-5 text-alpine-gold opacity-80" />
        </div>

        {#if showGuests}
          <div 
            onclick={(e) => e.stopPropagation()}
            onkeydown={(e) => e.stopPropagation()}
            role="presentation"
            class="absolute top-full mt-4 w-[90vw] max-w-[340px] md:w-full bg-white shadow-2xl border border-alpine-border p-8 z-50 animate-in fade-in slide-in-from-top-2 duration-300 left-1/2 -translate-x-1/2 md:left-0 md:translate-x-0 space-y-8"
          >
            <div class="flex items-center justify-between">
              <span class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">{$t('booking.adults')}</span>
              <div class="flex items-center gap-5 bg-alpine-bg px-4 py-2">
                <button type="button" onclick={() => adults = Math.max(1, adults - 1)} class="text-xl hover:text-alpine-gold transition-colors">-</button>
                <span class="text-sm font-bold w-5 text-center">{adults}</span>
                <button type="button" onclick={() => adults = Math.min(4, adults + 1)} class="text-xl hover:text-alpine-gold transition-colors">+</button>
              </div>
            </div>
            <div class="flex items-center justify-between">
              <span class="text-[11px] uppercase tracking-widest text-alpine-muted font-bold">{$t('booking.children')}</span>
              <div class="flex items-center gap-5 bg-alpine-bg px-4 py-2">
                <button type="button" onclick={() => children = Math.max(0, children - 1)} class="text-xl hover:text-alpine-gold transition-colors">-</button>
                <span class="text-sm font-bold w-5 text-center">{children}</span>
                <button type="button" onclick={() => children = Math.min(3, children + 1)} class="text-xl hover:text-alpine-gold transition-colors">+</button>
              </div>
            </div>
          </div>
        {/if}
      </div>
    </div>

    <a 
      href={bookingUrl()} 
      target="_blank"
      class="w-full md:w-auto bg-alpine-text text-white px-14 py-6 md:py-8 text-xs md:text-sm font-bold tracking-[0.2em] uppercase hover:bg-alpine-gold transition-all text-center flex items-center justify-center gap-3 group"
    >
      <span>{$t('booking.check') || "Verifica"}</span>
      <ChevronDown class="w-5 h-5 -rotate-90 group-hover:translate-x-1 transition-transform" />
    </a>
  </div>
</div>