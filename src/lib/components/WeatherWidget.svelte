<script lang="ts">
	import { onMount } from 'svelte';
	import { Cloud, CloudRain, Eye, Snowflake, Sun, Thermometer, Wind } from 'lucide-svelte';

	type IconType = typeof Sun;

	type WeatherData = {
		temp: number;
		feelsLike: number;
		desc: string;
		wind: number;
		visibilityKm: number;
		precip: number;
		snow: number;
		icon: IconType;
	};

	let weather = $state<WeatherData | null>(null);

	function iconFromCode(code: number): IconType {
		if (code === 0) return Sun;
		if (code <= 3) return Cloud;
		if (code <= 67) return CloudRain;
		if (code <= 86) return Snowflake;
		return Cloud;
	}

	function descFromCode(code: number): string {
		if (code === 0) return 'Sereno';
		if (code <= 3) return 'Parzialmente nuvoloso';
		if (code <= 48) return 'Nebbia';
		if (code <= 67) return 'Pioggia';
		if (code <= 86) return 'Neve';
		return 'Variabile';
	}

	onMount(async () => {
		try {
			const endpoint = new URL('https://api.open-meteo.com/v1/forecast');
			endpoint.searchParams.set('latitude', '45.844');
			endpoint.searchParams.set('longitude', '7.575');
			endpoint.searchParams.set(
				'current',
				'temperature_2m,apparent_temperature,weather_code,wind_speed_10m,visibility,precipitation,snowfall'
			);
			endpoint.searchParams.set('timezone', 'Europe/Rome');

			const res = await fetch(endpoint);
			if (!res.ok) throw new Error('API Error');
			const data = await res.json();
			const current = data.current;

			if (!current) {
				weather = null;
				return;
			}

			const code = Number(current.weather_code ?? 3);

			weather = {
				temp: Number(current.temperature_2m ?? 0),
				feelsLike: Number(current.apparent_temperature ?? 0),
				desc: descFromCode(code),
				wind: Number(current.wind_speed_10m ?? 0),
				visibilityKm: Number(current.visibility ?? 0) / 1000,
				precip: Number(current.precipitation ?? 0),
				snow: Number(current.snowfall ?? 0),
				icon: iconFromCode(code)
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
		class="group block max-w-xl border border-alpine-border bg-white p-4 shadow-sm transition-colors hover:border-alpine-gold"
	>
		<div class="flex items-start justify-between gap-4">
			<div>
				<p class="text-[10px] font-bold tracking-[0.2em] text-alpine-muted uppercase">
					Weather Card
				</p>
				<p class="mt-1 text-sm font-semibold text-alpine-text">Torgnon</p>
			</div>
			<weather.icon class="h-5 w-5 text-alpine-gold" />
		</div>

		<div class="mt-4 flex items-end gap-3 border-b border-alpine-border/70 pb-4">
			<p class="font-serif text-4xl text-alpine-text">{weather.temp.toFixed(0)}°C</p>
			<p class="pb-1 text-xs text-alpine-muted">Feels {weather.feelsLike.toFixed(0)}°C</p>
		</div>

		<p class="mt-3 text-xs tracking-[0.12em] text-alpine-muted uppercase">{weather.desc}</p>

		<div class="mt-4 grid grid-cols-2 gap-3 text-xs text-alpine-text">
			<div class="flex items-center gap-1.5">
				<Snowflake class="h-3.5 w-3.5 text-alpine-gold" />
				<span>{weather.snow.toFixed(1)} mm neve</span>
			</div>
			<div class="flex items-center gap-1.5">
				<Wind class="h-3.5 w-3.5 text-alpine-gold" />
				<span>{weather.wind.toFixed(0)} km/h</span>
			</div>
			<div class="flex items-center gap-1.5">
				<CloudRain class="h-3.5 w-3.5 text-alpine-gold" />
				<span>{weather.precip.toFixed(1)} mm pioggia</span>
			</div>
			<div class="flex items-center gap-1.5">
				<Eye class="h-3.5 w-3.5 text-alpine-gold" />
				<span>{weather.visibilityKm.toFixed(1)} km visibilita</span>
			</div>
		</div>

		<div
			class="mt-3 flex items-center gap-1.5 text-[10px] tracking-[0.18em] text-alpine-muted uppercase group-hover:text-alpine-text"
		>
			<Thermometer class="h-3.5 w-3.5" />
			Apri forecast completo
		</div>
	</a>
{/if}
