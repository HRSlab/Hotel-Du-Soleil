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
    onSelect = () => {} 
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

<div class="calendar-component p-4 bg-white select-none lg:p-8">
  <div class="flex items-center justify-between mb-4 lg:mb-8">
    <button onclick={prevMonth} type="button" class="p-1 hover:bg-alpine-bg rounded-full transition-colors">
      <ArrowLeft class="w-4 h-4 text-alpine-muted" />
    </button>
    <span class="text-xs font-bold uppercase tracking-widest text-alpine-text lg:text-sm">
      {monthNames[viewDate.getMonth()]} {viewDate.getFullYear()}
    </span>
    <button onclick={nextMonth} type="button" class="p-1 hover:bg-alpine-bg rounded-full transition-colors">
      <ArrowRight class="w-4 h-4 text-alpine-muted" />
    </button>
  </div>

  <div class="grid grid-cols-7 gap-2 text-center mb-2">
    {#each ['L', 'M', 'M', 'G', 'V', 'S', 'D'] as day, i (i)}
      <span class="text-[10px] font-bold text-alpine-muted/60 uppercase lg:text-xs">{day}</span>
    {/each}
  </div>

  <div class="grid grid-cols-7 gap-1 lg:gap-2">
    {#each days() as date, i (i)}
      {#if date}
        <button 
          type="button"
          onclick={() => selectDate(date)}
          disabled={date < today}
          class={cn(
            "aspect-square text-[13px] font-medium flex items-center justify-center transition-all relative z-10 lg:text-base",
            date < today ? "text-alpine-muted/30 cursor-not-allowed" : "text-alpine-text hover:bg-alpine-gold/10",
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
