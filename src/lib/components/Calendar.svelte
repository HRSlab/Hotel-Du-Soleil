<script lang="ts">
  import { ArrowLeft, ArrowRight } from 'lucide-svelte';
  import { clsx, type ClassValue } from 'clsx';
  import { twMerge } from 'tailwind-merge';

  function cn(...inputs: ClassValue[]) {
    return twMerge(clsx(inputs));
  }

  let { 
    arrival = $bindable(''), 
    departure = $bindable(''), 
    onSelect = (a: string, d: string) => {} 
  } = $props();

  let viewDate = $state(new Date());
  const today = new Date();
  today.setHours(0, 0, 0, 0);

  const monthNames = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno",
                    "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"];
  
  const days = $derived(() => {
    const year = viewDate.getFullYear();
    const month = viewDate.getMonth();
    const firstDay = new Date(year, month, 1).getDay();
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    const offset = firstDay === 0 ? 6 : firstDay - 1;
    const arr = [];
    for (let i = 0; i < offset; i++) arr.push(null);
    for (let i = 1; i <= daysInMonth; i++) arr.push(new Date(year, month, i));
    return arr;
  });

  function selectDate(date: Date) {
    if (date < today) return;
    const dateStr = date.toISOString().split('T')[0];
    if (!arrival || (arrival && departure)) {
      arrival = dateStr;
      departure = '';
    } else {
      if (dateStr < arrival) {
        arrival = dateStr;
      } else if (dateStr > arrival) {
        departure = dateStr;
      }
    }
    if (onSelect) onSelect(arrival, departure);
  }

  function isSelected(date: Date | null) {
    if (!date) return false;
    const d = date.toISOString().split('T')[0];
    return d === arrival || d === departure;
  }

  function isInRange(date: Date | null) {
    if (!date || !arrival || !departure) return false;
    const d = date.toISOString().split('T')[0];
    return d > arrival && d < departure;
  }

  function prevMonth() { viewDate = new Date(viewDate.getFullYear(), viewDate.getMonth() - 1, 1); }
  function nextMonth() { viewDate = new Date(viewDate.getFullYear(), viewDate.getMonth() + 1, 1); }
</script>

<div class="calendar-component p-4 bg-white select-none">
  <div class="flex items-center justify-between mb-4">
    <button onclick={prevMonth} type="button" class="p-2 hover:bg-alpine-bg rounded-full transition-colors">
      <ArrowLeft class="w-3 h-3 text-alpine-muted" />
    </button>
    <span class="text-[11px] font-bold uppercase tracking-widest text-alpine-text">
      {monthNames[viewDate.getMonth()]} {viewDate.getFullYear()}
    </span>
    <button onclick={nextMonth} type="button" class="p-2 hover:bg-alpine-bg rounded-full transition-colors">
      <ArrowRight class="w-3 h-3 text-alpine-muted" />
    </button>
  </div>

  <div class="grid grid-cols-7 gap-1 text-center mb-2">
    {#each ['L', 'M', 'M', 'G', 'V', 'S', 'D'] as day}
      <span class="text-[9px] font-bold text-alpine-muted/40 uppercase">{day}</span>
    {/each}
  </div>

  <div class="grid grid-cols-7 gap-1">
    {#each days() as date}
      {#if date}
        <button 
          type="button"
          onclick={() => selectDate(date)}
          disabled={date < today}
          class={cn(
            "aspect-square text-[10px] flex items-center justify-center transition-all relative z-10",
            date < today ? "text-alpine-muted/30 cursor-not-allowed" : "hover:bg-alpine-gold/10",
            isSelected(date) ? "bg-alpine-text text-white font-bold" : "",
            isInRange(date) ? "bg-alpine-gold/10" : ""
          )}
        >
          {date.getDate()}
        </button>
      {:else}
        <div class="aspect-square"></div>
      {/if}
    {/each}
  </div>
</div>
