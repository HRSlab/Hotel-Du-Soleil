<script lang="ts">
  import { onMount } from 'svelte';
  import { Cloud, Sun, CloudRain, Wind, Eye, SunDim } from 'lucide-svelte';
  import { t, locale } from '$lib/i18n';

  type WeatherData = {
    temp: string;
    feelsLike: string;
    desc: string;
    wind: string;
    visibility: string;
    uv: string;
    precip: string;
    icon: any;
  };

  let weather = $state<WeatherData | null>(null);

  onMount(async () => {
    try {
      const res = await fetch('https://wttr.in/Torgnon?format=j1');
      if (!res.ok) throw new Error('API Error');
      const data = await res.json();
      const current = data.current_condition[0];
      
      weather = {
        temp: current.temp_C,
        feelsLike: current.FeelsLikeC,
        desc: current.lang_it?.[0]?.value || current.weatherDesc[0].value,
        wind: current.windspeedKmph,
        visibility: current.visibility,
        uv: current.uvIndex,
        precip: current.precipMM,
        icon: parseInt(current.weatherCode) < 116 ? Sun : Cloud
      };
    } catch (e) {
      console.error('Weather fetch error:', e);
      weather = null;
    }
  });
</script>

{#if weather}
  <div class="flex flex-wrap items-center gap-x-6 gap-y-2 text-alpine-text/60 text-[9px] uppercase tracking-[0.15em] font-bold">
    <!-- Main -->
    <div class="flex items-center gap-2">
      <weather.icon class="w-3.5 h-3.5 text-alpine-gold" />
      <span class="text-alpine-text">Torgnon {weather.temp}°C</span>
      <span class="opacity-60 ml-1">({weather.desc})</span>
    </div>

    <!-- Outdoor Details -->
    <div class="flex items-center gap-4 opacity-80 border-l border-alpine-border pl-6">
      <div class="flex items-center gap-1.5" title="Vento">
        <Wind class="w-3 h-3" />
        <span>{weather.wind} km/h</span>
      </div>
      <div class="flex items-center gap-1.5" title="Visibilità">
        <Eye class="w-3 h-3" />
        <span>{weather.visibility} km</span>
      </div>
      <div class="flex items-center gap-1.5" title="Indice UV">
        <SunDim class="w-3 h-3" />
        <span>UV {weather.uv}</span>
      </div>
      {#if parseFloat(weather.precip) > 0}
        <div class="flex items-center gap-1.5 text-blue-500/70" title="Precipitazioni">
          <CloudRain class="w-3 h-3" />
          <span>{weather.precip} mm</span>
        </div>
      {/if}
    </div>
  </div>
{/if}
