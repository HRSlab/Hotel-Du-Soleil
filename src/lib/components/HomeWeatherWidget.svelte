<script lang="ts">
	import { onMount } from 'svelte';
	import { Activity, Cloud, Snowflake, Sun, Wind } from 'lucide-svelte';

	type WeatherData = {
		temp: string;
		desc: string;
		wind: string;
		snow: string;
		chanceSnow: string;
		icon: typeof Sun;
	};

	let weather = $state<WeatherData | null>(null);

	onMount(async () => {
		try {
			const res = await fetch('https://wttr.in/Torgnon?format=j1');
			if (!res.ok) throw new Error('API Error');
			const data = await res.json();
			const current = data.current_condition?.[0];
			const today = data.weather?.[0];

			if (!current || !today) {
				weather = null;
				return;
			}

			weather = {
				temp: String(current.temp_C ?? '--'),
				desc: current.lang_it?.[0]?.value ?? current.weatherDesc?.[0]?.value ?? 'Variabile',
				wind: String(current.windspeedKmph ?? '--'),
				snow: String(today.totalSnow_cm ?? '0'),
				chanceSnow: String(today.hourly?.[0]?.chanceofsnow ?? '0'),
				icon: Number(current.weatherCode ?? 999) < 116 ? Sun : Cloud
			};
		} catch (e) {
			console.error('Weather fetch error:', e);
			weather = null;
		}
	});
</script>

{#if weather}
	<a
		href="/meteo"
		class="group flex flex-wrap items-center gap-x-6 gap-y-2 text-[0.75em] font-bold tracking-[0.15em] text-alpine-text/60 uppercase transition-all hover:text-alpine-text"
	>
		<div class="flex items-center gap-2">
			<weather.icon class="h-3.5 w-3.5 text-alpine-gold" />
			<span class="text-alpine-text">Torgnon {weather.temp}°C</span>
			<span class="ml-1 opacity-60">({weather.desc})</span>
		</div>

		<div class="flex items-center gap-4 border-l border-alpine-border pl-6">
			{#if Number.parseFloat(weather.snow) > 0 || Number.parseFloat(weather.chanceSnow) > 10}
				<div class="flex items-center gap-1.5 text-alpine-gold" title="Neve">
					<Snowflake class="h-3 w-3" />
					<span>{weather.snow} cm / {weather.chanceSnow}% Neve</span>
				</div>
			{:else}
				<div class="flex items-center gap-1.5 opacity-40" title="Neve al suolo (stimata)">
					<Snowflake class="h-3 w-3" />
					<span>Fresco & Stabile</span>
				</div>
			{/if}

			<div class="flex items-center gap-1.5" title="Vento">
				<Wind class="h-3 w-3" />
				<span>{weather.wind} km/h</span>
			</div>

			<div
				class="ml-2 flex items-center gap-1.5 text-alpine-gold opacity-0 transition-opacity group-hover:opacity-100"
			>
				<span class="text-[8px]">In-Depth</span>
				<Activity class="h-3 w-3" />
			</div>
		</div>
	</a>
{/if}
