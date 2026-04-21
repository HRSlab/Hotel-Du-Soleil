<script lang="ts">
	import { t, locale } from '$lib/i18n';
	import {
		X,
		Phone,
		MessageCircle,
		Mail,
		Calendar as CalendarIcon,
		Users,
		ChevronRight
	} from 'lucide-svelte';
	import { fade, fly } from 'svelte/transition';
	import Calendar from '$lib/components/Calendar.svelte';
	import { clsx, type ClassValue } from 'clsx';
	import { twMerge } from 'tailwind-merge';
	import { getBookingEngineUrl } from '$lib/config/booking';

	function cn(...inputs: ClassValue[]) {
		return twMerge(clsx(inputs));
	}

	let { isOpen = $bindable(false) } = $props();

	let arrival = $state('');
	let departure = $state('');
	let adults = $state(2);
	let children = $state(0);

	const bookingUrl = $derived(getBookingEngineUrl('booking_drawer'));

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
		class="fixed inset-0 z-100 bg-black/60 backdrop-blur-sm"
		onclick={close}
		onkeydown={(e) => e.key === 'Escape' && close()}
		role="button"
		tabindex="-1"
		aria-label="Close booking menu"
	></div>

	<div
		transition:fly={{ x: 800, duration: 500, opacity: 1 }}
		class="fixed top-0 right-0 z-101 flex h-full w-[95vw] flex-col overflow-hidden border-l border-alpine-border bg-white shadow-2xl lg:w-[80vw]"
	>
		<div
			class="flex flex-none items-center justify-between border-b border-alpine-border bg-alpine-bg p-4 lg:p-6"
		>
			<h2 class="font-serif text-2xl text-alpine-text lg:text-3xl">
				{$t('nav.book') || 'Prenota'}
			</h2>
			<button
				onclick={close}
				class="rounded-full p-2 transition-colors hover:bg-alpine-border"
				aria-label="Chiudi"
			>
				<X class="h-6 w-6 text-alpine-text" />
			</button>
		</div>

		<div class="grid flex-none grid-cols-2 border-b border-alpine-border lg:hidden">
			<button
				onclick={() => (activeTab = 'online')}
				class={cn(
					'py-4 text-[10px] font-bold tracking-widest uppercase transition-colors',
					activeTab === 'online'
						? 'bg-alpine-text text-white'
						: 'bg-white text-alpine-muted hover:bg-alpine-bg'
				)}>Online</button
			>
			<button
				onclick={() => (activeTab = 'assisted')}
				class={cn(
					'py-4 text-[10px] font-bold tracking-widest uppercase transition-colors',
					activeTab === 'assisted'
						? 'bg-alpine-text text-white'
						: 'bg-white text-alpine-muted hover:bg-alpine-bg'
				)}>Contattaci</button
			>
		</div>

		<div class="flex-1 overflow-y-auto p-4 lg:overflow-hidden lg:p-8">
			<div class="h-full lg:grid lg:grid-cols-[1.3fr_1fr] lg:gap-10">
				<section class={cn('flex h-full flex-col', activeTab !== 'online' && 'hidden lg:flex')}>
					<div class="mb-4 flex flex-none items-center gap-3">
						<div class="h-px flex-1 bg-alpine-border"></div>
						<span
							class="text-[10px] font-bold tracking-[0.2em] text-alpine-muted uppercase lg:text-xs"
						>
							Seleziona Date
						</span>
						<div class="h-px flex-1 bg-alpine-border"></div>
					</div>

					<div
						class="flex min-h-0 flex-1 flex-col overflow-hidden border border-alpine-border bg-alpine-bg p-2 transition-all focus-within:border-alpine-gold"
					>
						<Calendar bind:arrival bind:departure />
					</div>

					<div class="mt-6 flex flex-col gap-4 lg:hidden">
						<div class="mb-2 flex flex-none items-center gap-3">
							<div class="h-px flex-1 bg-alpine-border"></div>
							<span class="text-[10px] font-bold tracking-[0.2em] text-alpine-muted uppercase">
								Ospiti & Prenotazione
							</span>
							<div class="h-px flex-1 bg-alpine-border"></div>
						</div>

						<div class="grid grid-cols-2 gap-4">
							<div class="flex flex-col gap-1 border border-alpine-border bg-alpine-bg px-3 py-2">
								<span class="text-[9px] font-bold tracking-widest text-alpine-muted uppercase"
									>Adulti</span
								>
								<div class="flex items-center justify-between">
									<button
										onclick={() => (adults = Math.max(1, adults - 1))}
										class="text-xl leading-none transition-colors hover:text-alpine-gold">-</button
									>
									<span class="text-[14px] font-bold">{adults}</span>
									<button
										onclick={() => (adults = Math.min(4, adults + 1))}
										class="text-xl leading-none transition-colors hover:text-alpine-gold">+</button
									>
								</div>
							</div>
							<div class="flex flex-col gap-1 border border-alpine-border bg-alpine-bg px-3 py-2">
								<span class="text-[9px] font-bold tracking-widest text-alpine-muted uppercase"
									>Bambini</span
								>
								<div class="flex items-center justify-between">
									<button
										onclick={() => (children = Math.max(0, children - 1))}
										class="text-xl leading-none transition-colors hover:text-alpine-gold">-</button
									>
									<span class="text-[14px] font-bold">{children}</span>
									<button
										onclick={() => (children = Math.min(3, children + 1))}
										class="text-xl leading-none transition-colors hover:text-alpine-gold">+</button
									>
								</div>
							</div>
						</div>

						<a
							href={bookingUrl}
							target="_blank"
							class="group flex w-full items-center justify-center gap-3 bg-alpine-text py-4 text-xs font-bold tracking-[0.2em] text-white uppercase transition-all hover:bg-alpine-gold"
						>
							{$t('booking.check') || 'Verifica Disponibilità'}
							<ChevronRight class="h-5 w-5 transition-transform group-hover:translate-x-1" />
						</a>
					</div>
				</section>

				<section
					class={cn(
						'mt-8 flex h-full flex-col justify-between lg:mt-0',
						activeTab !== 'assisted' && 'hidden lg:flex'
					)}
				>
					<div class="hidden flex-col gap-4 lg:flex">
						<div class="mb-2 flex flex-none items-center gap-3">
							<div class="h-px flex-1 bg-alpine-border"></div>
							<span
								class="text-[10px] font-bold tracking-[0.2em] text-alpine-muted uppercase lg:text-xs"
							>
								Ospiti & Prenotazione
							</span>
							<div class="h-px flex-1 bg-alpine-border"></div>
						</div>

						<div class="grid grid-cols-2 gap-4">
							<div class="flex flex-col gap-1 border border-alpine-border bg-alpine-bg px-3 py-2">
								<span class="text-[9px] font-bold tracking-widest text-alpine-muted uppercase"
									>Adulti</span
								>
								<div class="flex items-center justify-between">
									<button
										onclick={() => (adults = Math.max(1, adults - 1))}
										class="text-xl leading-none transition-colors hover:text-alpine-gold">-</button
									>
									<span class="text-[14px] font-bold">{adults}</span>
									<button
										onclick={() => (adults = Math.min(4, adults + 1))}
										class="text-xl leading-none transition-colors hover:text-alpine-gold">+</button
									>
								</div>
							</div>
							<div class="flex flex-col gap-1 border border-alpine-border bg-alpine-bg px-3 py-2">
								<span class="text-[9px] font-bold tracking-widest text-alpine-muted uppercase"
									>Bambini</span
								>
								<div class="flex items-center justify-between">
									<button
										onclick={() => (children = Math.max(0, children - 1))}
										class="text-xl leading-none transition-colors hover:text-alpine-gold">-</button
									>
									<span class="text-[14px] font-bold">{children}</span>
									<button
										onclick={() => (children = Math.min(3, children + 1))}
										class="text-xl leading-none transition-colors hover:text-alpine-gold">+</button
									>
								</div>
							</div>
						</div>

						<a
							href={bookingUrl}
							target="_blank"
							class="group flex w-full items-center justify-center gap-3 bg-alpine-text py-4 text-xs font-bold tracking-[0.2em] text-white uppercase transition-all hover:bg-alpine-gold lg:py-5 lg:text-sm"
						>
							{$t('booking.check') || 'Verifica Disponibilità'}
							<ChevronRight class="h-5 w-5 transition-transform group-hover:translate-x-1" />
						</a>
					</div>

					<div class="mt-8 flex flex-none flex-col gap-3 lg:mt-4">
						<div class="mb-1 flex items-center gap-3">
							<div class="h-px flex-1 bg-alpine-border"></div>
							<span class="text-[10px] font-bold tracking-[0.2em] text-alpine-muted uppercase">
								Assistenza Diretta
							</span>
							<div class="h-px flex-1 bg-alpine-border"></div>
						</div>

						<a
							href="tel:+393793357713"
							class="group flex items-center justify-between border border-alpine-border bg-alpine-bg p-3 transition-all hover:border-alpine-gold"
						>
							<div class="flex items-center gap-4">
								<div
									class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-white shadow-sm transition-colors group-hover:bg-alpine-gold/10"
								>
									<Phone class="h-4 w-4 text-alpine-gold" />
								</div>
								<div class="text-left leading-tight">
									<span
										class="block text-[9px] font-bold tracking-widest text-alpine-muted uppercase"
										>Chiamaci</span
									>
									<span class="text-xs font-medium text-alpine-text">+39 379 335 7713</span>
								</div>
							</div>
							<ChevronRight
								class="h-4 w-4 text-alpine-border transition-transform group-hover:translate-x-1 group-hover:text-alpine-gold"
							/>
						</a>

						<a
							href="https://wa.me/393793357713"
							target="_blank"
							class="group flex items-center justify-between border border-alpine-border bg-alpine-bg p-3 transition-all hover:border-[#25D366]"
						>
							<div class="flex items-center gap-4">
								<div
									class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-white shadow-sm transition-colors group-hover:bg-[#25D366]/10"
								>
									<MessageCircle class="h-4 w-4 text-[#25D366]" />
								</div>
								<div class="text-left leading-tight">
									<span
										class="block text-[9px] font-bold tracking-widest text-alpine-muted uppercase"
										>WhatsApp</span
									>
									<span class="text-xs font-medium text-alpine-text">Messaggio Rapido</span>
								</div>
							</div>
							<ChevronRight
								class="h-4 w-4 text-alpine-border transition-transform group-hover:translate-x-1 group-hover:text-[#25D366]"
							/>
						</a>

						<a
							href="mailto:booking@hotel-du-soleil.it"
							class="group flex items-center justify-between border border-alpine-border bg-alpine-bg p-3 transition-all hover:border-blue-400"
						>
							<div class="flex items-center gap-4">
								<div
									class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-white shadow-sm transition-colors group-hover:bg-blue-400/10"
								>
									<Mail class="h-4 w-4 text-blue-400" />
								</div>
								<div class="text-left leading-tight">
									<span
										class="block text-[9px] font-bold tracking-widest text-alpine-muted uppercase"
										>Email</span
									>
									<span class="truncate text-xs font-medium text-alpine-text">Scrivici</span>
								</div>
							</div>
							<ChevronRight
								class="h-4 w-4 text-alpine-border transition-transform group-hover:translate-x-1 group-hover:text-blue-400"
							/>
						</a>
					</div>
				</section>
			</div>
		</div>

		<div class="flex-none border-t border-alpine-border bg-alpine-bg p-3 text-center">
			<p class="text-[9px] font-bold tracking-[0.2em] text-alpine-muted uppercase lg:text-[10px]">
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
