<script lang="ts">
  import { t, locale } from '$lib/i18n';
  import { ArrowRight } from 'lucide-svelte';
  import Calendar from '$lib/components/Calendar.svelte';
  import { clsx, type ClassValue } from 'clsx';
  import { twMerge } from 'tailwind-merge';

  function cn(...inputs: ClassValue[]) {
    return twMerge(clsx(inputs));
  }

  let arrival = $state('');
  let departure = $state('');
  let adults = $state(2);
  let children = $state(0);

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
</script>

<div class="bg-white border border-alpine-border p-8 shadow-sm fade-up-element sticky top-32">
  <h3 class="font-serif text-2xl mb-8 text-alpine-text font-light italic">Prenota il tuo soggiorno</h3>
  
  <div class="space-y-8">
    
    <!-- Inline Calendar -->
    <div class="calendar-container">
      <Calendar bind:arrival bind:departure />
    </div>

    <!-- Selection Summary -->
    <div class="grid grid-cols-2 gap-4 border-t border-alpine-border pt-8">
      <div class="space-y-1">
        <span class="text-[9px] uppercase tracking-widest text-alpine-muted font-bold">Arrivo</span>
        <p class="text-sm font-serif">{arrival || 'Seleziona'}</p>
      </div>
      <div class="space-y-1">
        <span class="text-[9px] uppercase tracking-widest text-alpine-muted font-bold">Partenza</span>
        <p class="text-sm font-serif">{departure || 'Seleziona'}</p>
      </div>
    </div>

    <!-- Guests -->
    <div class="space-y-4 border-t border-alpine-border pt-8">
      <div class="flex items-center justify-between">
        <span class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">Adulti</span>
        <div class="flex items-center gap-4 bg-alpine-bg px-4 py-2">
          <button onclick={() => adults = Math.max(1, adults - 1)} class="text-lg">-</button>
          <span class="text-sm font-bold w-4 text-center">{adults}</span>
          <button onclick={() => adults = Math.min(4, adults + 1)} class="text-lg">+</button>
        </div>
      </div>
      <div class="flex items-center justify-between">
        <span class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold">Bambini</span>
        <div class="flex items-center gap-4 bg-alpine-bg px-4 py-2">
          <button onclick={() => children = Math.max(0, children - 1)} class="text-lg">-</button>
          <span class="text-sm font-bold w-4 text-center">{children}</span>
          <button onclick={() => children = Math.min(3, children + 1)} class="text-lg">+</button>
        </div>
      </div>
    </div>

    <!-- CTA -->
    <div class="pt-4">
      <a 
        href={bookingUrl()} 
        target="_blank" 
        class={cn(
          "w-full py-6 flex items-center justify-center gap-3 text-[11px] font-bold uppercase tracking-[0.2em] transition-all group",
          arrival && departure ? "bg-alpine-text text-white hover:bg-alpine-gold" : "bg-alpine-border text-alpine-muted cursor-not-allowed pointer-events-none"
        )}
      >
        <span>Prenota Ora</span>
        <ArrowRight class="w-4 h-4 transition-transform group-hover:translate-x-1" />
      </a>
      <p class="text-[9px] text-center mt-4 text-alpine-muted uppercase tracking-widest opacity-60">
        Reindirizzamento al motore sicuro
      </p>
    </div>
  </div>
</div>
