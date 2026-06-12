<script lang="ts">
	import { AlertTriangle, Camera, Droplets, ExternalLink, Thermometer } from 'lucide-svelte';
	import { locale, t } from '$lib/i18n';
	import type { PageData } from './$types';

	let { data }: { data: PageData } = $props();

	function localeTag() {
		if ($locale === 'en') return 'en-GB';
		if ($locale === 'ru') return 'ru-RU';
		return 'it-IT';
	}

	function metric(value: number | null | undefined, unit = '', digits = 0) {
		if (value === null || value === undefined) {
			return 'n/d';
		}

		return `${value.toFixed(digits)}${unit}`;
	}

	function updatedLabel(value: string | null) {
		if (!value) {
			return 'n/d';
		}

		return new Intl.DateTimeFormat(localeTag(), {
			day: '2-digit',
			month: '2-digit',
			hour: '2-digit',
			minute: '2-digit'
		}).format(new Date(value));
	}

	function yesNo(value: boolean | null | undefined) {
		if (value === null || value === undefined) {
			return 'n/d';
		}

		return value ? $t('meteo.day') : $t('meteo.night');
	}

	function formatClock(value: string | null | undefined) {
		if (!value) {
			return 'n/d';
		}

		const date = new Date(value);
		if (Number.isNaN(date.getTime())) {
			return value;
		}

		return new Intl.DateTimeFormat(localeTag(), {
			hour: '2-digit',
			minute: '2-digit'
		}).format(date);
	}

	function formatDuration(seconds: number | null | undefined) {
		if (seconds === null || seconds === undefined) {
			return 'n/d';
		}

		const totalMinutes = Math.round(seconds / 60);
		const hours = Math.floor(totalMinutes / 60);
		const minutes = totalMinutes % 60;
		return `${hours}h ${minutes}m`;
	}

	function formatDateLabel(date: string) {
		const d = new Date(`${date}T00:00:00`);
		if (Number.isNaN(d.getTime())) {
			return date;
		}

		return new Intl.DateTimeFormat(localeTag(), {
			weekday: 'short',
			day: '2-digit',
			month: '2-digit'
		}).format(d);
	}
</script>

<svelte:head>
	<title>{$t('meteo.title')} | Chalet du Soleil</title>
</svelte:head>

<main class="min-h-screen bg-alpine-bg pt-32 pb-24">
	<div class="mx-auto max-w-7xl px-6">
		<div class="mb-10 border-b border-alpine-border pb-8">
			<div class="flex flex-wrap items-end justify-between gap-6">
				<div>
					<p class="text-xs tracking-[0.3em] text-alpine-muted uppercase">{$t('meteo.subtitle')}</p>
					<h1 class="mt-3 font-serif text-5xl text-alpine-text">{$t('meteo.title')}</h1>
					<p class="mt-4 max-w-3xl text-sm leading-relaxed text-alpine-muted">
						{$t('meteo.live_intro')}
					</p>
				</div>
				<div class="space-y-2">
					<p class="text-[11px] tracking-[0.18em] text-alpine-muted uppercase">
						{$t('meteo.updated_label')}: {updatedLabel(data.lastUpdated)}
					</p>
				</div>
			</div>
		</div>

		<div class="mb-10 grid grid-cols-1 gap-8 lg:grid-cols-12">
			<div class="lg:col-span-8">
				<div class="border border-alpine-border bg-white p-8 shadow-sm">
					<div class="mb-7 flex flex-wrap items-center justify-between gap-4">
						<h2
							class="flex items-center gap-2 text-[11px] font-bold tracking-[0.2em] text-alpine-muted uppercase"
						>
							<Thermometer class="h-4 w-4 text-alpine-gold" />
							{$t('meteo.live_data_title')}
						</h2>
						<p class="text-[10px] tracking-[0.18em] text-alpine-muted uppercase">
							{$t('meteo.updated_label')}: {updatedLabel(data.lastUpdated)}
						</p>
					</div>

					{#if data.weather}
						<div class="grid grid-cols-1 gap-4 md:grid-cols-2 xl:grid-cols-3">
							<div class="border border-alpine-border/70 p-4">
								<p class="text-[9px] tracking-widest text-alpine-muted uppercase">{$t('meteo.condition')}</p>
								<p class="mt-2 font-serif text-2xl text-alpine-text">{data.weather.base.description ?? 'n/d'}</p>
							</div>
							<div class="border border-alpine-border/70 p-4">
								<p class="text-[9px] tracking-widest text-alpine-muted uppercase">{$t('meteo.temperature')}</p>
								<p class="mt-2 font-serif text-2xl text-alpine-text">{metric(data.weather.base.tempC, '°C')}</p>
							</div>
							<div class="border border-alpine-border/70 p-4">
								<p class="text-[9px] tracking-widest text-alpine-muted uppercase">{$t('meteo.feels_like_full')}</p>
								<p class="mt-2 font-serif text-2xl text-alpine-text">{metric(data.weather.base.feelsLikeC, '°C')}</p>
							</div>
							<div class="border border-alpine-border/70 p-4">
								<p class="text-[9px] tracking-widest text-alpine-muted uppercase">{$t('meteo.day')}</p>
								<p class="mt-2 font-serif text-2xl text-alpine-text">{yesNo(data.weather.isDay)}</p>
							</div>
							<div class="border border-alpine-border/70 p-4">
								<p class="text-[9px] tracking-widest text-alpine-muted uppercase">{$t('meteo.humidity')}</p>
								<p class="mt-2 font-serif text-2xl text-alpine-text">{metric(data.weather.humidityPct, '%')}</p>
							</div>
							<div class="border border-alpine-border/70 p-4">
								<p class="text-[9px] tracking-widest text-alpine-muted uppercase">{$t('meteo.precipitation')}</p>
								<p class="mt-2 font-serif text-2xl text-alpine-text">{metric(data.weather.precipMm, ' mm', 1)}</p>
							</div>
							<div class="border border-alpine-border/70 p-4">
								<p class="text-[9px] tracking-widest text-alpine-muted uppercase">{$t('meteo.cloud_cover')}</p>
								<p class="mt-2 font-serif text-2xl text-alpine-text">{metric(data.weather.cloudPct, '%')}</p>
							</div>
							<div class="border border-alpine-border/70 p-4">
								<p class="text-[9px] tracking-widest text-alpine-muted uppercase">{$t('meteo.wind_speed')}</p>
								<p class="mt-2 font-serif text-2xl text-alpine-text">{metric(data.weather.base.windKmh, ' km/h')}</p>
							</div>
							<div class="border border-alpine-border/70 p-4">
								<p class="text-[9px] tracking-widest text-alpine-muted uppercase">{$t('meteo.wind_gusts')}</p>
								<p class="mt-2 font-serif text-2xl text-alpine-text">{metric(data.weather.base.windGustKmh, ' km/h')}</p>
							</div>
						</div>
					{:else}
						<div class="rounded-sm border border-amber-200 bg-amber-50 p-4">
							<p class="text-sm text-alpine-text">{$t('meteo.not_available_current')}</p>
						</div>
					{/if}
				</div>
			</div>
			<div class="lg:col-span-4">
				<div class="border border-alpine-border bg-white p-8 shadow-sm">
					<h2
						class="mb-7 flex items-center gap-2 text-[11px] font-bold tracking-[0.2em] text-alpine-muted uppercase"
					>
						<AlertTriangle class="h-4 w-4 text-alpine-gold" />
						Piste e impianti
					</h2>
					<div class="space-y-3">
						{#each data.officialLinks as link}
							<a
								href={link.url}
								target="_blank"
								rel="noreferrer"
								class="flex items-center justify-between border border-alpine-border p-4 transition-colors hover:border-alpine-gold hover:bg-alpine-bg/60"
							>
								<div>
									<p class="text-sm font-semibold text-alpine-text">{link.title}</p>
									<p class="text-[10px] tracking-[0.16em] text-alpine-muted uppercase">{link.label}</p>
								</div>
								<ExternalLink class="h-4 w-4 text-alpine-muted" />
							</a>
						{/each}
					</div>
				</div>
			</div>
		</div>

		<div class="mb-10 border border-alpine-border bg-white p-8 shadow-sm">
			<h2 class="mb-6 flex items-center gap-2 text-[11px] font-bold tracking-[0.2em] text-alpine-muted uppercase">
				<Droplets class="h-4 w-4 text-alpine-gold" />
				{$t('meteo.weekly_forecast_title')}
			</h2>

			{#if data.dailyForecast && data.dailyForecast.length > 0}
				<div class="grid grid-cols-1 gap-4 md:grid-cols-2 xl:grid-cols-3">
					{#each data.dailyForecast as day}
						<div class="border border-alpine-border/70 p-5">
							<div class="mb-4 border-b border-alpine-border/60 pb-3">
								<p class="font-serif text-2xl text-alpine-text">{formatDateLabel(day.date)}</p>
								<p class="mt-1 text-xs tracking-[0.14em] text-alpine-muted uppercase">{day.weatherDescription}</p>
							</div>

							<div class="mb-4 flex items-end justify-between gap-3">
								<div>
									<p class="text-[10px] tracking-[0.15em] text-alpine-muted uppercase">{$t('meteo.max_temp')}</p>
									<p class="font-serif text-3xl text-alpine-text">{metric(day.maxTempC, '°C')}</p>
								</div>
								<div class="text-right">
									<p class="text-[10px] tracking-[0.15em] text-alpine-muted uppercase">{$t('meteo.min_temp')}</p>
									<p class="font-serif text-2xl text-alpine-muted">{metric(day.minTempC, '°C')}</p>
								</div>
							</div>

							<div class="grid grid-cols-2 gap-2 text-xs">
								<div class="border border-alpine-border/60 p-2">
									<p class="tracking-wide text-alpine-muted uppercase">{$t('meteo.sunrise')}</p>
									<p class="mt-1 text-alpine-text">{formatClock(day.sunrise)}</p>
								</div>
								<div class="border border-alpine-border/60 p-2">
									<p class="tracking-wide text-alpine-muted uppercase">{$t('meteo.sunset')}</p>
									<p class="mt-1 text-alpine-text">{formatClock(day.sunset)}</p>
								</div>
								<div class="border border-alpine-border/60 p-2">
									<p class="tracking-wide text-alpine-muted uppercase">{$t('meteo.precip_probability')}</p>
									<p class="mt-1 text-alpine-text">{metric(day.precipitationProbabilityMax, '%')}</p>
								</div>
								<div class="border border-alpine-border/60 p-2">
									<p class="tracking-wide text-alpine-muted uppercase">{$t('meteo.daily_rain')}</p>
									<p class="mt-1 text-alpine-text">{metric(day.rainSumMm, ' mm', 1)}</p>
								</div>
								<div class="border border-alpine-border/60 p-2">
									<p class="tracking-wide text-alpine-muted uppercase">{$t('meteo.daily_snow')}</p>
									<p class="mt-1 text-alpine-text">{metric(day.snowfallSumCm, ' cm', 1)}</p>
								</div>
								<div class="border border-alpine-border/60 p-2">
									<p class="tracking-wide text-alpine-muted uppercase">{$t('meteo.max_wind')}</p>
									<p class="mt-1 text-alpine-text">{metric(day.maxWindSpeedKmh, ' km/h')}</p>
								</div>
							</div>
						</div>
					{/each}
				</div>
			{:else}
				<div class="rounded-sm border border-amber-200 bg-amber-50 p-4">
					<p class="text-sm text-alpine-text">{$t('meteo.not_available_daily')}</p>
				</div>
			{/if}
		</div>

		<div class="grid grid-cols-1 gap-8 lg:grid-cols-12">
			<div class="lg:col-span-12">
				<div class="overflow-hidden border border-alpine-border bg-white shadow-sm">
					<div class="flex items-center justify-between border-b border-alpine-border p-8">
						<h2
							class="flex items-center gap-2 text-[11px] font-bold tracking-[0.2em] text-alpine-muted uppercase"
						>
							<Camera class="h-4 w-4 text-alpine-gold" />
							{$t('meteo.webcam_title')}
						</h2>
						<a
							href="https://torgnon-skiarea.panomax.com/"
							target="_blank"
							rel="noreferrer"
							class="flex items-center gap-2 text-[10px] font-bold tracking-widest uppercase transition-colors hover:text-alpine-gold"
						>
							{$t('meteo.fullscreen')}
							<ExternalLink class="h-3.5 w-3.5" />
						</a>
					</div>
					<div class="group relative aspect-21/9 bg-alpine-bg">
						<img
							src="/imgs/torgnon-view.webp"
							alt="Torgnon Webcam Preview"
							class="h-full w-full object-cover opacity-80"
						/>
						<div
							class="absolute inset-0 flex items-center justify-center bg-black/10 transition-colors group-hover:bg-black/20"
						>
							<a
								href="https://torgnon-skiarea.panomax.com/"
								target="_blank"
								rel="noreferrer"
								class="transform bg-white px-10 py-5 text-[11px] font-bold tracking-[0.3em] uppercase shadow-2xl transition-all hover:scale-105 hover:bg-alpine-text hover:text-white"
							>
								{$t('meteo.activate_stream')}
							</a>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</main>
