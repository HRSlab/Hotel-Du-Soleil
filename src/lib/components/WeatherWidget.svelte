<script lang="ts">
  import { onMount } from 'svelte';
  import { Cloud, Sun, CloudRain, Wind, Eye, SunDim, Snowflake, Activity } from 'lucide-svelte';
  import { t, locale } from '$lib/i18n';

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
    icon: any;
  };

  let weather = $state<WeatherData | null>(null);

  const copy = $derived($locale === 'ru'
    ? { stable: 'Свежо и стабильно', detail: 'Подробнее', snowTitle: 'Снег', windTitle: 'Ветер', estimatedSnow: 'Снег на земле (оценка)' }
    : { stable: 'Fresco & Stabile', detail: 'In-Depth', snowTitle: 'Neve', windTitle: 'Vento', estimatedSnow: 'Neve al suolo (stimata)' });

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
        snow: today.totalSnow_cm || "0",
        chanceSnow: today.hourly[0].chanceofsnow || "0",
        icon: parseInt(current.weatherCode) < 116 ? Sun : Cloud
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
    class="flex flex-wrap items-center gap-x-6 gap-y-2 text-alpine-text/60 text-[0.75em] uppercase tracking-[0.15em] font-bold hover:text-alpine-text transition-all group"
  >
    <!-- Main -->
    <div class="flex items-center gap-2">
      <weather.icon class="w-3.5 h-3.5 text-alpine-gold" />
      <span class="text-alpine-text">Torgnon {weather.temp}°C</span>
      <span class="opacity-60 ml-1">({weather.desc})</span>
    </div>

    <!-- Snow/Outdoor Details -->
    <div class="flex items-center gap-4 border-l border-alpine-border pl-6">
      
      <!-- Snow Depth / Forecast -->
      {#if parseFloat(weather.snow) > 0 || parseFloat(weather.chanceSnow) > 10}
        <div class="flex items-center gap-1.5 text-alpine-gold" title={copy.snowTitle}>
          <Snowflake class="w-3 h-3" />
          <span>{weather.snow} cm / {weather.chanceSnow}% Neve</span>
        </div>
      {:else}
        <div class="flex items-center gap-1.5 opacity-40" title={copy.estimatedSnow}>
          <Snowflake class="w-3 h-3" />
          <span>{copy.stable}</span>
        </div>
      {/if}

      <div class="flex items-center gap-1.5" title={copy.windTitle}>
        <Wind class="w-3 h-3" />
        <span>{weather.wind} km/h</span>
      </div>
      
      <div class="flex items-center gap-1.5 text-alpine-gold opacity-0 group-hover:opacity-100 transition-opacity ml-2">
        <span class="text-[8px]">{copy.detail}</span>
        <Activity class="w-3 h-3" />
      </div>
    </div>
  </a>
{/if}
