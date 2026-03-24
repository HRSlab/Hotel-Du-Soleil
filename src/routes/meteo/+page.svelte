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
    snowDepth: { base: "30cm", top: "50cm" },
    lastSnowfall: "14/03/2026",
    snowQuality: "Hard packed / Spring"
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
        snow: today.totalSnow_cm || "0",
        chanceSnow: today.hourly[0].chanceofsnow || "0",
        icon: parseInt(current.weatherCode) < 116 ? Sun : Cloud
      };

      // Updates for "Bollettino Neve" from Live Data
      if (parseFloat(weather.snow) > 0) {
        skiStats.snowQuality = "Neve Fresca / Polverosa";
        skiStats.lastSnowfall = "Oggi";
      } else if (parseInt(weather.temp) > 3) {
        skiStats.snowQuality = "Trasformata / Primaverile";
      }

      // Check current and forecast for last snowfall in current data array
      const allSnowEvents = data.weather.filter((w: { totalSnow_cm: string }) => parseFloat(w.totalSnow_cm) > 0);
      if (allSnowEvents.length > 0) {
        // Sort by date descending to find the most recent one
        const sortedEvents = allSnowEvents.sort((a: {date: string}, b: {date: string}) => b.date.localeCompare(a.date));
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
  <title>{$t('meteo.title')} | Hotel du Soleil</title>
</svelte:head>

<main class="min-h-screen bg-alpine-bg pt-32 pb-24">
  <div class="max-w-7xl mx-auto px-6">
    
    <!-- Title & Status -->
    <div class="flex flex-col md:flex-row justify-between items-end mb-16 border-b border-alpine-border pb-8">
      <div>
        <h1 class="font-serif text-5xl text-alpine-text mb-4">{$t('meteo.title')}</h1>
        <p class="text-xs uppercase tracking-[0.3em] text-alpine-muted">{$t('meteo.subtitle')}</p>
      </div>
      <div class="mt-8 md:mt-0 flex items-center gap-4 bg-white px-6 py-3 border border-alpine-border">
        <div class="w-2 h-2 rounded-full bg-green-500 animate-pulse"></div>
        <span class="text-[10px] font-bold uppercase tracking-widest text-alpine-text">{$t('meteo.status_open')}</span>
      </div>
    </div>

    <!-- Main Dashboard Grid -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 mb-12">
      
      <!-- Left: Real Time Weather -->
      <div class="lg:col-span-4 space-y-8">
        <div class="bg-white p-8 border border-alpine-border shadow-sm h-full">
          <h2 class="text-[11px] uppercase tracking-[0.2em] text-alpine-muted font-bold mb-10 flex items-center gap-2">
            <Sun class="w-4 h-4 text-alpine-gold" /> {$t('meteo.current_conditions')}
          </h2>
          
          {#if weather}
            <div class="space-y-10">
              <div class="flex items-center gap-6">
                <weather.icon class="w-16 h-16 text-alpine-gold" />
                <div>
                  <div class="text-6xl font-light text-alpine-text">{weather.temp}°</div>
                  <div class="text-xs uppercase tracking-widest text-alpine-muted mt-2 font-medium">{weather.desc}</div>
                </div>
              </div>

              <div class="grid grid-cols-2 gap-8 border-t border-alpine-border/50 pt-8">
                <div class="space-y-2">
                  <span class="text-[9px] uppercase tracking-widest text-alpine-muted">{$t('meteo.feels_like')}</span>
                  <p class="text-lg font-serif italic text-alpine-text">{weather.feelsLike}°C</p>
                </div>
                <div class="space-y-2">
                  <span class="text-[9px] uppercase tracking-widest text-alpine-muted">{$t('meteo.wind')}</span>
                  <p class="text-lg font-serif italic text-alpine-text">{weather.wind} <span class="text-xs font-sans not-italic font-bold">km/h</span></p>
                </div>
                <div class="space-y-2">
                  <span class="text-[9px] uppercase tracking-widest text-alpine-muted">{$t('meteo.visibility')}</span>
                  <p class="text-lg font-serif italic text-alpine-text">{weather.visibility} <span class="text-xs font-sans not-italic font-bold">km</span></p>
                </div>
                <div class="space-y-2">
                  <span class="text-[9px] uppercase tracking-widest text-alpine-muted">{$t('meteo.uv_index')}</span>
                  <p class="text-lg font-serif italic text-alpine-text">{weather.uv}</p>
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
      <div class="lg:col-span-8 space-y-8">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 h-full">
          
          <!-- Snow Depth -->
          <div class="bg-alpine-text text-white p-8 border border-alpine-text/10 shadow-xl overflow-hidden relative">
            <Snowflake class="absolute -right-8 -top-8 w-48 h-48 opacity-10" />
            <h2 class="text-[11px] uppercase tracking-[0.2em] text-white/60 font-bold mb-10 flex items-center gap-2">
               {$t('meteo.snow_report')}
            </h2>
            <div class="space-y-12 relative z-10">
              <div class="flex justify-between items-end border-b border-white/20 pb-4">
                <span class="text-sm font-light italic">{$t('meteo.snow_depth_base')}</span>
                <span class="text-4xl font-serif">{skiStats.snowDepth.base}</span>
              </div>
              <div class="flex justify-between items-end border-b border-white/20 pb-4">
                <span class="text-sm font-light italic">{$t('meteo.snow_depth_top')}</span>
                <span class="text-4xl font-serif">{skiStats.snowDepth.top}</span>
              </div>
              <div class="grid grid-cols-2 gap-4">
                <div class="p-4 bg-white/10">
                  <span class="block text-[9px] uppercase tracking-widest text-white/50 mb-1">{$t('meteo.snow_quality')}</span>
                  <p class="text-xs font-bold">{skiStats.snowQuality}</p>
                </div>
                <div class="p-4 bg-white/10">
                  <span class="block text-[9px] uppercase tracking-widest text-white/50 mb-1">{$t('meteo.last_snowfall')}</span>
                  <p class="text-xs font-bold">{skiStats.lastSnowfall}</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Slopes Status -->
          <div class="bg-white p-8 border border-alpine-border shadow-sm">
            <h2 class="text-[11px] uppercase tracking-[0.2em] text-alpine-muted font-bold mb-10 flex items-center gap-2">
              <Map class="w-4 h-4 text-alpine-gold" /> {$t('meteo.slopes_lifts')}
            </h2>
            <div class="space-y-10">
              <div class="flex gap-4 items-center">
                <div class="text-6xl font-serif text-alpine-text">{skiStats.slopes.open} <span class="text-2xl text-alpine-muted">/ {skiStats.slopes.total}</span></div>
                <div class="text-[10px] uppercase tracking-widest text-alpine-muted font-bold leading-tight">{$t('meteo.slopes_open')}</div>
              </div>
              
              <div class="grid grid-cols-3 gap-2">
                <div class="bg-blue-500 h-1" style="width: 100%"></div>
                <div class="bg-red-500 h-1" style="width: 100%"></div>
                <div class="bg-black h-1" style="width: 100%"></div>
              </div>

              <div class="space-y-6 pt-6 border-t border-alpine-border/50">
                <div class="flex justify-between items-center">
                  <span class="text-xs font-medium text-alpine-muted uppercase tracking-widest">{$t('meteo.lifts_running')}</span>
                  <span class="text-lg font-serif text-alpine-text">{skiStats.lifts.open} / {skiStats.lifts.total}</span>
                </div>
                <div class="bg-alpine-bg h-1.5 w-full overflow-hidden">
                  <div class="bg-alpine-gold h-full" style="width: {(skiStats.lifts.open / skiStats.lifts.total) * 100}%"></div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>

    <!-- Webcams Section -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
      <div class="lg:col-span-12">
        <div class="bg-white border border-alpine-border shadow-sm overflow-hidden">
          <div class="p-8 border-b border-alpine-border flex justify-between items-center">
            <h2 class="text-[11px] uppercase tracking-[0.2em] text-alpine-muted font-bold flex items-center gap-2">
              <Camera class="w-4 h-4 text-alpine-gold" /> {$t('meteo.webcam_title')}
            </h2>
            <a href="https://torgnon-skiarea.panomax.com/" target="_blank" class="text-[10px] uppercase tracking-widest font-bold flex items-center gap-2 hover:text-alpine-gold transition-colors">
              {$t('meteo.fullscreen')} <ExternalLink class="w-3.5 h-3.5" />
            </a>
          </div>
          <div class="aspect-21/9 bg-alpine-bg relative group">
             <img 
               src="https://www.hotel-du-soleil.it/Resources/hotel-du-soleil/gallery/gallery06.jpg" 
               alt="Torgnon Webcam Preview"
               class="w-full h-full object-cover opacity-80" 
             />
             <div class="absolute inset-0 flex items-center justify-center bg-black/10 transition-colors group-hover:bg-black/20">
                <a href="https://torgnon-skiarea.panomax.com/" target="_blank" class="bg-white px-10 py-5 text-[11px] font-bold uppercase tracking-[0.3em] shadow-2xl hover:bg-alpine-text hover:text-white transition-all transform hover:scale-105">
                  {$t('meteo.activate_stream')}
                </a>
             </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</main>
