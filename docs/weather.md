# Weather feature

The site shows live mountain weather for **Torgnon** (the hotel's location) in two
places: small widgets on marketing pages, and a full `/meteo` forecast page.

Coordinates used: lat `45.844`, lon `7.575`, altitude `1489 m`.

## `/meteo` page (server-rendered, Open-Meteo)

[`src/routes/meteo/+page.server.ts`](../src/routes/meteo/+page.server.ts) loads the
forecast **on the server** and passes normalized data to
[`src/routes/meteo/+page.svelte`](../src/routes/meteo/+page.svelte).

- **Source:** [Open-Meteo](https://open-meteo.com) `https://api.open-meteo.com/v1/forecast`.
- **Requested data:** a rich set of `current`, `hourly` (incl. 80 m / 180 m layers and
  freezing-level height), and `daily` fields; `forecast_days=7`, `timezone=Europe/Rome`.
- **Resilience:** the fetch is wrapped in an `AbortController` with a **4.5 s timeout**.
  On any error/timeout it returns a safe payload with `weather: null` and a status
  message rather than failing the page.
- **Caching:** sets `cache-control: public, max-age=600, s-maxage=600, stale-while-revalidate=1200`
  (10-minute cache).

### Returned `data` shape

```ts
{
  resortName: 'Torgnon',
  lastUpdated: string | null,          // ISO timestamp
  weather: NormalizedWeather | null,   // current conditions + base/mid/upper layers
  dailyForecast: NormalizedDailyForecast[],  // up to 7 days
  officialLinks: { title, label, url }[],    // Torgnon ski area + Panomax webcam
  status: { configured, liveForecast, liveOperations, message }
}
```

### Normalization helpers (in `+page.server.ts`)

- `toNumber()` — safe numeric coercion (returns `null` for empty/non-finite).
- `windDirectionFromDegrees()` — degrees → `N/NE/E/.../NW`.
- `weatherDescription()` / `weatherIcon()` — map WMO `weather_code` to an Italian
  description and an icon key (`sun`, `partly-cloudy`, `fog`, `rain`, `snow`,
  `snow-showers`, `thunderstorm`, ...).
- `normalizeForecast()` — builds current conditions plus three altitude **layers**
  (`base` from surface, `mid` from 80 m hourly, `upper` from 180 m hourly).
- `normalizeDailyForecast()` — maps the daily arrays to a typed per-day list.

> Snowfall is reported by Open-Meteo in mm; the loader converts it to cm
> (`freshSnowCm = snowMm / 10`).

## Home & section widgets (client-side)

These fetch directly from the browser on mount:

| Component                                                                    | Source                              | Notes                                                                                                      |
| ---------------------------------------------------------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| [`HomeWeatherWidget.svelte`](../src/lib/components/HomeWeatherWidget.svelte) | `https://wttr.in/Torgnon?format=j1` | Compact current conditions on the home page.                                                               |
| [`WeatherWidget.svelte`](../src/lib/components/WeatherWidget.svelte)         | (weather-code based)                | Richer widget with temp, feels-like, wind, visibility, precipitation, snow; has an `iconFromCode` mapping. |

> Note there are **two weather data sources** in the codebase: the `/meteo` page uses
> **Open-Meteo** (server-side, full forecast), while `HomeWeatherWidget` uses
> **wttr.in** (client-side, quick current conditions). Keep this in mind when
> changing providers.

## External references shown on `/meteo`

- **Torgnon Ski Area** — piste/lift status: https://www.torgnon.net/inverno/
- **Panomax Torgnon** — live 360° webcam: https://torgnon-skiarea.panomax.com/

`liveOperations` is hard-coded `false` — lift/piste status is **not** scraped; the
page links out to the official sources instead.
