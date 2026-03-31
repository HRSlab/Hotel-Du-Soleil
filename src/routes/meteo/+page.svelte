<script lang="ts">
	import { onMount } from 'svelte';
	import { Sun, Cloud, Snowflake, Map, Camera, ExternalLink } from 'lucide-svelte';
	import { t } from '$lib/i18n';
	import type { ComponentType } from 'svelte';

	type WeatherData = {
		temp: string;
		feelsLike: string;
		desc: string;
		wind: string;
		visibility: string;
		uv: string;
		precip: string;
		snow: string;
		chanceSnow: string;
		icon: ComponentType;
	};

	let weather = $state<WeatherData | null>(null);

	let skiStats = $state({
		slopes: { open: 18, total: 18, details: { blue: 5, red: 11, black: 2 } },
		lifts: { open: 5, total: 6 },
		snowDepth: { base: '30cm', top: '50cm' },
		lastSnowfall: '14/03/2026',
		snowQuality: 'Hard packed / Spring'
	});

	onMount(async () => {
		try {
			const res = await fetch('https://wttr.in/Torgnon?format=j1');
			if (!res.ok) throw new Error('API Error');
			const data = await res.json();
			const current = data.current_condition[0];
			const today = data.weather[0];

			weather = {
				temp: current.temp_C,
				feelsLike: current.FeelsLikeC,
				desc: current.lang_it?.[0]?.value || current.weatherDesc[0].value,
				wind: current.windspeedKmph,
				visibility: current.visibility,
				uv: current.uvIndex,
				precip: current.precipMM,
				snow: today.totalSnow_cm || '0',
				chanceSnow: today.hourly[0].chanceofsnow || '0',
				icon: parseInt(current.weatherCode) < 116 ? Sun : Cloud
			};

			// Updates for "Bollettino Neve" from Live Data
			if (parseFloat(weather.snow) > 0) {
				skiStats.snowQuality = 'Neve Fresca / Polverosa';
				skiStats.lastSnowfall = 'Oggi';
			} else if (parseInt(weather.temp) > 3) {
				skiStats.snowQuality = 'Trasformata / Primaverile';
			}

			// Check current and forecast for last snowfall in current data array
			const allSnowEvents = data.weather.filter(
				(w: { totalSnow_cm: string }) => parseFloat(w.totalSnow_cm) > 0
			);
			if (allSnowEvents.length > 0) {
				// Sort by date descending to find the most recent one
				const sortedEvents = allSnowEvents.sort((a: { date: string }, b: { date: string }) =>
					b.date.localeCompare(a.date)
				);
				skiStats.lastSnowfall = new Date(sortedEvents[0].date).toLocaleDateString('it-IT');
			}

			// Sync Lift/Slopes - ensuring reactive state is used in HTML
			// (The UI already binds to skiStats, so updating it here triggers the update)
		} catch (e) {
			console.error('Weather fetch error:', e);
		}
	});
</script>

<svelte:head>
	<title>{$t('meteo.title')} | Chalet du Soleil</title>
</svelte:head>

<main class="min-h-screen bg-alpine-bg pt-32 pb-24">
	<div class="mx-auto max-w-7xl px-6">
		<!-- Title & Status -->
		<div
			class="mb-16 flex flex-col items-end justify-between border-b border-alpine-border pb-8 md:flex-row"
		>
			<div>
				<h1 class="mb-4 font-serif text-5xl text-alpine-text">{$t('meteo.title')}</h1>
				<p class="text-xs tracking-[0.3em] text-alpine-muted uppercase">{$t('meteo.subtitle')}</p>
			</div>
			<div
				class="mt-8 flex items-center gap-4 border border-alpine-border bg-white px-6 py-3 md:mt-0"
			>
				<div class="h-2 w-2 animate-pulse rounded-full bg-green-500"></div>
				<span class="text-[10px] font-bold tracking-widest text-alpine-text uppercase"
					>{$t('meteo.status_open')}</span
				>
			</div>
		</div>

		<!-- Main Dashboard Grid -->
		<div class="mb-12 grid grid-cols-1 gap-8 lg:grid-cols-12">
			<!-- Left: Real Time Weather -->
			<div class="space-y-8 lg:col-span-4">
				<div class="h-full border border-alpine-border bg-white p-8 shadow-sm">
					<h2
						class="mb-10 flex items-center gap-2 text-[11px] font-bold tracking-[0.2em] text-alpine-muted uppercase"
					>
						<Sun class="h-4 w-4 text-alpine-gold" />
						{$t('meteo.current_conditions')}
					</h2>

					{#if weather}
						<div class="space-y-10">
							<div class="flex items-center gap-6">
								<weather.icon class="h-16 w-16 text-alpine-gold" />
								<div>
									<div class="text-6xl font-light text-alpine-text">{weather.temp}°</div>
									<div class="mt-2 text-xs font-medium tracking-widest text-alpine-muted uppercase">
										{weather.desc}
									</div>
								</div>
							</div>

							<div class="grid grid-cols-2 gap-8 border-t border-alpine-border/50 pt-8">
								<div class="space-y-2">
									<span class="text-[9px] tracking-widest text-alpine-muted uppercase"
										>{$t('meteo.feels_like')}</span
									>
									<p class="font-serif text-lg text-alpine-text italic">{weather.feelsLike}°C</p>
								</div>
								<div class="space-y-2">
									<span class="text-[9px] tracking-widest text-alpine-muted uppercase"
										>{$t('meteo.wind')}</span
									>
									<p class="font-serif text-lg text-alpine-text italic">
										{weather.wind} <span class="font-sans text-xs font-bold not-italic">km/h</span>
									</p>
								</div>
								<div class="space-y-2">
									<span class="text-[9px] tracking-widest text-alpine-muted uppercase"
										>{$t('meteo.visibility')}</span
									>
									<p class="font-serif text-lg text-alpine-text italic">
										{weather.visibility}
										<span class="font-sans text-xs font-bold not-italic">km</span>
									</p>
								</div>
								<div class="space-y-2">
									<span class="text-[9px] tracking-widest text-alpine-muted uppercase"
										>{$t('meteo.uv_index')}</span
									>
									<p class="font-serif text-lg text-alpine-text italic">{weather.uv}</p>
								</div>
							</div>
						</div>
					{:else}
						<div class="animate-pulse space-y-4">
							<div class="h-20 bg-alpine-bg"></div>
							<div class="h-40 bg-alpine-bg"></div>
						</div>
					{/if}
				</div>
			</div>

			<!-- Center: Snow & Slopes -->
			<div class="space-y-8 lg:col-span-8">
				<div class="grid h-full grid-cols-1 gap-8 md:grid-cols-2">
					<!-- Snow Depth -->
					<div
						class="relative overflow-hidden border border-alpine-text/10 bg-alpine-text p-8 text-white shadow-xl"
					>
						<Snowflake class="absolute -top-8 -right-8 h-48 w-48 opacity-10" />
						<h2
							class="mb-10 flex items-center gap-2 text-[11px] font-bold tracking-[0.2em] text-white/60 uppercase"
						>
							{$t('meteo.snow_report')}
						</h2>
						<div class="relative z-10 space-y-12">
							<div class="flex items-end justify-between border-b border-white/20 pb-4">
								<span class="text-sm font-light italic">{$t('meteo.snow_depth_base')}</span>
								<span class="font-serif text-4xl">{skiStats.snowDepth.base}</span>
							</div>
							<div class="flex items-end justify-between border-b border-white/20 pb-4">
								<span class="text-sm font-light italic">{$t('meteo.snow_depth_top')}</span>
								<span class="font-serif text-4xl">{skiStats.snowDepth.top}</span>
							</div>
							<div class="grid grid-cols-2 gap-4">
								<div class="bg-white/10 p-4">
									<span class="mb-1 block text-[9px] tracking-widest text-white/50 uppercase"
										>{$t('meteo.snow_quality')}</span
									>
									<p class="text-xs font-bold">{skiStats.snowQuality}</p>
								</div>
								<div class="bg-white/10 p-4">
									<span class="mb-1 block text-[9px] tracking-widest text-white/50 uppercase"
										>{$t('meteo.last_snowfall')}</span
									>
									<p class="text-xs font-bold">{skiStats.lastSnowfall}</p>
								</div>
							</div>
						</div>
					</div>

					<!-- Slopes Status -->
					<div class="border border-alpine-border bg-white p-8 shadow-sm">
						<h2
							class="mb-10 flex items-center gap-2 text-[11px] font-bold tracking-[0.2em] text-alpine-muted uppercase"
						>
							<Map class="h-4 w-4 text-alpine-gold" />
							{$t('meteo.slopes_lifts')}
						</h2>
						<div class="space-y-10">
							<div class="flex items-center gap-4">
								<div class="font-serif text-6xl text-alpine-text">
									{skiStats.slopes.open}
									<span class="text-2xl text-alpine-muted">/ {skiStats.slopes.total}</span>
								</div>
								<div
									class="text-[10px] leading-tight font-bold tracking-widest text-alpine-muted uppercase"
								>
									{$t('meteo.slopes_open')}
								</div>
							</div>

							<div class="grid grid-cols-3 gap-2">
								<div class="h-1 bg-blue-500" style="width: 100%"></div>
								<div class="h-1 bg-red-500" style="width: 100%"></div>
								<div class="h-1 bg-black" style="width: 100%"></div>
							</div>

							<div class="space-y-6 border-t border-alpine-border/50 pt-6">
								<div class="flex items-center justify-between">
									<span class="text-xs font-medium tracking-widest text-alpine-muted uppercase"
										>{$t('meteo.lifts_running')}</span
									>
									<span class="font-serif text-lg text-alpine-text"
										>{skiStats.lifts.open} / {skiStats.lifts.total}</span
									>
								</div>
								<div class="h-1.5 w-full overflow-hidden bg-alpine-bg">
									<div
										class="h-full bg-alpine-gold"
										style="width: {(skiStats.lifts.open / skiStats.lifts.total) * 100}%"
									></div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>

		<!-- Webcams Section -->
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
