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

		const camereObj = [
			{
				adulti: adults.toString(),
				bambini: [children.toString()]
			}
		];
		params.set('camere', JSON.stringify(camereObj));

		return `${base}?${params.toString()}`;
	});
</script>

<div class="fade-up-element sticky top-32 border border-alpine-border bg-white p-8 shadow-sm">
	<h3 class="mb-8 font-serif text-2xl font-light text-alpine-text italic">
		Prenota il tuo soggiorno
	</h3>

	<div class="space-y-8">
		<!-- Inline Calendar -->
		<div class="calendar-container">
			<Calendar bind:arrival bind:departure />
		</div>

		<!-- Selection Summary -->
		<div class="grid grid-cols-2 gap-4 border-t border-alpine-border pt-8">
			<div class="space-y-1">
				<span class="text-[9px] font-bold tracking-widest text-alpine-muted uppercase">Arrivo</span>
				<p class="font-serif text-sm">{arrival || 'Seleziona'}</p>
			</div>
			<div class="space-y-1">
				<span class="text-[9px] font-bold tracking-widest text-alpine-muted uppercase"
					>Partenza</span
				>
				<p class="font-serif text-sm">{departure || 'Seleziona'}</p>
			</div>
		</div>

		<!-- Guests -->
		<div class="space-y-4 border-t border-alpine-border pt-8">
			<div class="flex items-center justify-between">
				<span class="text-[10px] font-bold tracking-widest text-alpine-muted uppercase">Adulti</span
				>
				<div class="flex items-center gap-4 bg-alpine-bg px-4 py-2">
					<button onclick={() => (adults = Math.max(1, adults - 1))} class="text-lg">-</button>
					<span class="w-4 text-center text-sm font-bold">{adults}</span>
					<button onclick={() => (adults = Math.min(4, adults + 1))} class="text-lg">+</button>
				</div>
			</div>
			<div class="flex items-center justify-between">
				<span class="text-[10px] font-bold tracking-widest text-alpine-muted uppercase"
					>Bambini</span
				>
				<div class="flex items-center gap-4 bg-alpine-bg px-4 py-2">
					<button onclick={() => (children = Math.max(0, children - 1))} class="text-lg">-</button>
					<span class="w-4 text-center text-sm font-bold">{children}</span>
					<button onclick={() => (children = Math.min(3, children + 1))} class="text-lg">+</button>
				</div>
			</div>
		</div>

		<!-- CTA -->
		<div class="pt-4">
			<a
				href={bookingUrl()}
				target="_blank"
				class={cn(
					'group flex w-full items-center justify-center gap-3 py-6 text-[11px] font-bold tracking-[0.2em] uppercase transition-all',
					arrival && departure
						? 'bg-alpine-text text-white hover:bg-alpine-gold'
						: 'pointer-events-none cursor-not-allowed bg-alpine-border text-alpine-muted'
				)}
			>
				<span>Prenota Ora</span>
				<ArrowRight class="h-4 w-4 transition-transform group-hover:translate-x-1" />
			</a>
			<p class="mt-4 text-center text-[9px] tracking-widest text-alpine-muted uppercase opacity-60">
				Miglior Tariffa Garantita
			</p>
		</div>
	</div>
</div>
