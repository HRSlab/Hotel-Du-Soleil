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

		const camereObj = [
			{
				adulti: adults.toString(),
				bambini: [children.toString()]
			}
		];
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
			setTimeout(() => (showCalendar = false), 300);
		}
	}

	const copy = $derived(
		$locale === 'ru'
			? { dateLabel: 'Заезд / Выезд', emptyDates: 'Выберите даты', action: 'Проверить' }
			: { dateLabel: 'Check-in / Check-out', emptyDates: 'Seleziona Date', action: 'Verifica' }
	);
</script>

<div class="fade-up-element relative z-20 mx-auto -mt-16 max-w-6xl px-6">
	<div
		class="flex flex-col items-stretch justify-between overflow-visible border border-alpine-border bg-white shadow-2xl md:flex-row"
	>
		<div
			class="flex w-full flex-1 flex-col divide-y divide-alpine-border md:flex-row md:divide-x md:divide-y-0"
		>
			<div
				role="button"
				tabindex="0"
				onclick={toggleCalendar}
				onkeydown={(e) => e.key === 'Enter' && toggleCalendar()}
				class="group relative flex-1 cursor-pointer px-8 py-6 text-left transition-colors outline-none hover:bg-alpine-bg md:py-8"
				use:clickOutside={() => (showCalendar = false)}
				aria-label={$t('booking.select_dates')}
			>
				<span class="mb-3 block text-[11px] font-bold tracking-[0.2em] text-alpine-muted uppercase"
					>{copy.dateLabel}</span
				>
				<div class="flex items-center justify-between">
					<span
						class="text-base font-medium text-alpine-text transition-colors group-hover:text-alpine-gold md:text-lg"
					>
						{arrival
							? `${arrival} — ${departure || '...'}`
							: $t('booking.select_dates') || copy.emptyDates}
					</span>
					<CalendarIcon class="h-5 w-5 text-alpine-gold opacity-80" />
				</div>

				{#if showCalendar}
					<div
						onclick={(e) => e.stopPropagation()}
						onkeydown={(e) => e.stopPropagation()}
						role="presentation"
						class="animate-in fade-in slide-in-from-top-2 absolute top-full left-1/2 z-50 mt-4 w-[90vw] max-w-[340px] -translate-x-1/2 border border-alpine-border bg-white shadow-2xl duration-300 md:left-0 md:w-[340px] md:translate-x-0"
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
				class="group relative flex-1 cursor-pointer px-8 py-6 text-left transition-colors outline-none hover:bg-alpine-bg md:py-8"
				use:clickOutside={() => (showGuests = false)}
				aria-label={$t('booking.guests_label')}
			>
				<span class="mb-3 block text-[11px] font-bold tracking-[0.2em] text-alpine-muted uppercase"
					>{$t('booking.guests_label') || 'Ospiti'}</span
				>
				<div class="flex items-center justify-between">
					<span
						class="text-base font-medium text-alpine-text transition-colors group-hover:text-alpine-gold md:text-lg"
					>
						{adults}
						{$t('booking.adults')}, {children}
						{$t('booking.children')}
					</span>
					<Users class="h-5 w-5 text-alpine-gold opacity-80" />
				</div>

				{#if showGuests}
					<div
						onclick={(e) => e.stopPropagation()}
						onkeydown={(e) => e.stopPropagation()}
						role="presentation"
						class="animate-in fade-in slide-in-from-top-2 absolute top-full left-1/2 z-50 mt-4 w-[90vw] max-w-[340px] -translate-x-1/2 space-y-8 border border-alpine-border bg-white p-8 shadow-2xl duration-300 md:left-0 md:w-full md:translate-x-0"
					>
						<div class="flex items-center justify-between">
							<span class="text-[11px] font-bold tracking-widest text-alpine-muted uppercase"
								>{$t('booking.adults')}</span
							>
							<div class="flex items-center gap-5 bg-alpine-bg px-4 py-2">
								<button
									type="button"
									onclick={() => (adults = Math.max(1, adults - 1))}
									class="text-xl transition-colors hover:text-alpine-gold">-</button
								>
								<span class="w-5 text-center text-sm font-bold">{adults}</span>
								<button
									type="button"
									onclick={() => (adults = Math.min(4, adults + 1))}
									class="text-xl transition-colors hover:text-alpine-gold">+</button
								>
							</div>
						</div>
						<div class="flex items-center justify-between">
							<span class="text-[11px] font-bold tracking-widest text-alpine-muted uppercase"
								>{$t('booking.children')}</span
							>
							<div class="flex items-center gap-5 bg-alpine-bg px-4 py-2">
								<button
									type="button"
									onclick={() => (children = Math.max(0, children - 1))}
									class="text-xl transition-colors hover:text-alpine-gold">-</button
								>
								<span class="w-5 text-center text-sm font-bold">{children}</span>
								<button
									type="button"
									onclick={() => (children = Math.min(3, children + 1))}
									class="text-xl transition-colors hover:text-alpine-gold">+</button
								>
							</div>
						</div>
					</div>
				{/if}
			</div>
		</div>

		<a
			href={bookingUrl()}
			target="_blank"
			class="group flex w-full items-center justify-center gap-3 bg-alpine-text px-14 py-6 text-center text-xs font-bold tracking-[0.2em] text-white uppercase transition-all hover:bg-alpine-gold md:w-auto md:py-8 md:text-sm"
		>
			<span>{$t('booking.check') || copy.action}</span>
			<ChevronDown class="h-5 w-5 -rotate-90 transition-transform group-hover:translate-x-1" />
		</a>
	</div>
</div>
