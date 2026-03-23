<script lang="ts">
    import { t, locale } from '$lib/i18n';
    import { X, Phone, MessageCircle, Mail, Calendar as CalendarIcon, Users, ChevronRight } from 'lucide-svelte';
    import { fade, fly } from 'svelte/transition';
    import Calendar from '$lib/components/Calendar.svelte';
    import { SvelteURLSearchParams } from 'svelte/reactivity';
    import { clsx, type ClassValue } from 'clsx';
    import { twMerge } from 'tailwind-merge';

    function cn(...inputs: ClassValue[]) {
        return twMerge(clsx(inputs));
    }

    let { isOpen = $bindable(false) } = $props();

    let arrival = $state('');
    let departure = $state('');
    let adults = $state(2);
    let children = $state(0);

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

    let activeTab = $state<'online' | 'assisted'>('online');

    function close() {
        isOpen = false;
    }
    
    $effect(() => {
        if (isOpen) {
            document.body.classList.add('drawer-open');
            document.body.style.overflow = 'hidden';
        } else {
            document.body.classList.remove('drawer-open');
            document.body.style.overflow = '';
        }
    });
</script>

{#if isOpen}
    <div
        transition:fade={{ duration: 300 }}
        class="fixed inset-0 z-[100] bg-black/60 backdrop-blur-sm"
        onclick={close}
        onkeydown={(e) => e.key === 'Escape' && close()}
        role="button"
        tabindex="-1"
        aria-label="Close booking menu"
    ></div>

    <div
        transition:fly={{ x: 800, duration: 500, opacity: 1 }}
        class="fixed top-0 right-0 z-[101] h-full w-[95vw] lg:w-[80vw] border-l border-alpine-border bg-white shadow-2xl overflow-hidden flex flex-col"
    >
        <div class="flex items-center justify-between border-b border-alpine-border p-4 lg:p-6 flex-none bg-alpine-bg">
            <h2 class="font-serif text-2xl text-alpine-text lg:text-3xl">{$t('nav.book') || "Prenota"}</h2>
            <button
                onclick={close}
                class="rounded-full p-2 transition-colors hover:bg-alpine-border"
                aria-label="Chiudi"
            >
                <X class="h-6 w-6 text-alpine-text" />
            </button>
        </div>

        <div class="grid grid-cols-2 border-b border-alpine-border lg:hidden flex-none">
            <button 
                onclick={() => activeTab = 'online'}
                class={cn("py-4 text-[10px] font-bold uppercase tracking-widest transition-colors", activeTab === 'online' ? "bg-alpine-text text-white" : "bg-white text-alpine-muted hover:bg-alpine-bg")}
            >Online</button>
            <button 
                onclick={() => activeTab = 'assisted'}
                class={cn("py-4 text-[10px] font-bold uppercase tracking-widest transition-colors", activeTab === 'assisted' ? "bg-alpine-text text-white" : "bg-white text-alpine-muted hover:bg-alpine-bg")}
            >Diretta</button>
        </div>

        <div class="flex-1 overflow-y-auto lg:overflow-hidden p-4 lg:p-8">
            
            <div class="h-full lg:grid lg:grid-cols-[1.3fr_1fr] lg:gap-10">
                
                <section class={cn("flex flex-col h-full", activeTab !== 'online' && "hidden lg:flex")}>
                    <div class="mb-4 flex items-center gap-3 flex-none">
                        <div class="h-px flex-1 bg-alpine-border"></div>
                        <span class="text-[10px] font-bold tracking-[0.2em] text-alpine-muted uppercase lg:text-xs">
                            Seleziona Date
                        </span>
                        <div class="h-px flex-1 bg-alpine-border"></div>
                    </div>
                    
                    <div class="flex-1 min-h-0 border border-alpine-border bg-alpine-bg p-2 focus-within:border-alpine-gold transition-all overflow-hidden flex flex-col">
                        <Calendar bind:arrival bind:departure />
                    </div>
                </section>

                <section class={cn("flex flex-col h-full mt-8 lg:mt-0 justify-between", activeTab !== 'assisted' && "hidden lg:flex")}>
                    
                    <div class="flex flex-col gap-4">
                        <div class="mb-2 flex items-center gap-3 flex-none">
                            <div class="h-px flex-1 bg-alpine-border"></div>
                            <span class="text-[10px] font-bold tracking-[0.2em] text-alpine-muted uppercase lg:text-xs">
                                Ospiti & Prenotazione
                            </span>
                            <div class="h-px flex-1 bg-alpine-border"></div>
                        </div>

                        <div class="grid grid-cols-2 gap-4">
                            <div class="flex flex-col gap-1 border border-alpine-border bg-alpine-bg px-3 py-2">
                                <span class="text-[9px] text-alpine-muted uppercase tracking-widest font-bold">Adulti</span>
                                <div class="flex items-center justify-between">
                                    <button onclick={() => adults = Math.max(1, adults - 1)} class="text-xl hover:text-alpine-gold transition-colors leading-none">-</button>
                                    <span class="text-[14px] font-bold">{adults}</span>
                                    <button onclick={() => adults = Math.min(4, adults + 1)} class="text-xl hover:text-alpine-gold transition-colors leading-none">+</button>
                                </div>
                            </div>
                            <div class="flex flex-col gap-1 border border-alpine-border bg-alpine-bg px-3 py-2">
                                <span class="text-[9px] text-alpine-muted uppercase tracking-widest font-bold">Bambini</span>
                                <div class="flex items-center justify-between">
                                    <button onclick={() => children = Math.max(0, children - 1)} class="text-xl hover:text-alpine-gold transition-colors leading-none">-</button>
                                    <span class="text-[14px] font-bold">{children}</span>
                                    <button onclick={() => children = Math.min(3, children + 1)} class="text-xl hover:text-alpine-gold transition-colors leading-none">+</button>
                                </div>
                            </div>
                        </div>

                        <a
                            href={bookingUrl()}
                            target="_blank"
                            class="group flex w-full items-center justify-center gap-3 bg-alpine-text py-4 lg:py-5 text-xs lg:text-sm font-bold tracking-[0.2em] text-white uppercase transition-all hover:bg-alpine-gold"
                        >
                            {$t('booking.check') || "Verifica Disponibilità"}
                            <ChevronRight class="h-5 w-5 transition-transform group-hover:translate-x-1" />
                        </a>
                    </div>

                    <div class="flex flex-col gap-3 mt-8 lg:mt-4 flex-none">
                        <div class="mb-1 flex items-center gap-3">
                            <div class="h-px flex-1 bg-alpine-border"></div>
                            <span class="text-[10px] font-bold tracking-[0.2em] text-alpine-muted uppercase">
                                Assistenza Diretta
                            </span>
                            <div class="h-px flex-1 bg-alpine-border"></div>
                        </div>

                        <a href="tel:+393793357713" class="flex items-center justify-between border border-alpine-border bg-alpine-bg p-3 transition-all hover:border-alpine-gold group">
                            <div class="flex items-center gap-4">
                                <div class="flex h-8 w-8 items-center justify-center rounded-full bg-white shadow-sm transition-colors group-hover:bg-alpine-gold/10 shrink-0">
                                    <Phone class="h-4 w-4 text-alpine-gold" />
                                </div>
                                <div class="text-left leading-tight">
                                    <span class="block text-[9px] font-bold tracking-widest text-alpine-muted uppercase">Chiamaci</span>
                                    <span class="text-xs font-medium text-alpine-text">+39 379 335 7713</span>
                                </div>
                            </div>
                            <ChevronRight class="h-4 w-4 text-alpine-border transition-transform group-hover:translate-x-1 group-hover:text-alpine-gold" />
                        </a>

                        <a href="https://wa.me/393793357713" target="_blank" class="flex items-center justify-between border border-alpine-border bg-alpine-bg p-3 transition-all hover:border-[#25D366] group">
                            <div class="flex items-center gap-4">
                                <div class="flex h-8 w-8 items-center justify-center rounded-full bg-white shadow-sm transition-colors group-hover:bg-[#25D366]/10 shrink-0">
                                    <MessageCircle class="h-4 w-4 text-[#25D366]" />
                                </div>
                                <div class="text-left leading-tight">
                                    <span class="block text-[9px] font-bold tracking-widest text-alpine-muted uppercase">WhatsApp</span>
                                    <span class="text-xs font-medium text-alpine-text">Messaggio Rapido</span>
                                </div>
                            </div>
                            <ChevronRight class="h-4 w-4 text-alpine-border transition-transform group-hover:translate-x-1 group-hover:text-[#25D366]" />
                        </a>

                        <a href="mailto:booking@hotel-du-soleil.it" class="flex items-center justify-between border border-alpine-border bg-alpine-bg p-3 transition-all hover:border-blue-400 group">
                            <div class="flex items-center gap-4">
                                <div class="flex h-8 w-8 items-center justify-center rounded-full bg-white shadow-sm transition-colors group-hover:bg-blue-400/10 shrink-0">
                                    <Mail class="h-4 w-4 text-blue-400" />
                                </div>
                                <div class="text-left leading-tight">
                                    <span class="block text-[9px] font-bold tracking-widest text-alpine-muted uppercase">Email</span>
                                    <span class="text-xs font-medium text-alpine-text truncate">Scrivici</span>
                                </div>
                            </div>
                            <ChevronRight class="h-4 w-4 text-alpine-border transition-transform group-hover:translate-x-1 group-hover:text-blue-400" />
                        </a>
                    </div>

                </section>
            </div>
        </div>

        <div class="flex-none bg-alpine-bg border-t border-alpine-border p-3 text-center">
            <p class="text-[9px] uppercase tracking-[0.2em] text-alpine-muted font-bold lg:text-[10px]">
                Miglior Prezzo Garantito sul nostro sito
            </p>
        </div>
    </div>
{/if}

<style>
    :global(body) {
        overflow: hidden !important;
    }
    :global(body:not(.drawer-open)) {
        overflow: auto !important;
    }
</style>