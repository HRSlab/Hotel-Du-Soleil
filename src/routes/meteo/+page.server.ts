import type { PageServerLoad } from './$types';

const TORGNON = {
	name: 'Torgnon',
	latitude: 45.844,
	longitude: 7.575,
	altitude: 1489
} as const;

type OpenMeteoResponse = {
	current?: {
		time?: string;
		temperature_2m?: number;
		relative_humidity_2m?: number;
		apparent_temperature?: number;
		is_day?: number;
		weather_code?: number;
		precipitation?: number;
		rain?: number;
		showers?: number;
		snowfall?: number;
		cloud_cover?: number;
		pressure_msl?: number;
		surface_pressure?: number;
		visibility?: number;
		wind_speed_10m?: number;
		wind_direction_10m?: number;
		wind_gusts_10m?: number;
	};
	hourly?: {
		time?: string[];
		temperature_80m?: number[];
		wind_speed_80m?: number[];
		wind_gusts_80m?: number[];
		wind_direction_80m?: number[];
		temperature_180m?: number[];
		wind_speed_180m?: number[];
		wind_gusts_180m?: number[];
		wind_direction_180m?: number[];
		freezing_level_height?: number[];
	};
	daily?: {
		time?: string[];
		weather_code?: number[];
		temperature_2m_max?: number[];
		temperature_2m_min?: number[];
		apparent_temperature_max?: number[];
		apparent_temperature_min?: number[];
		sunrise?: string[];
		sunset?: string[];
		daylight_duration?: number[];
		sunshine_duration?: number[];
		rain_sum?: number[];
		showers_sum?: number[];
		snowfall_sum?: number[];
		precipitation_sum?: number[];
		precipitation_hours?: number[];
		precipitation_probability_max?: number[];
		wind_speed_10m_max?: number[];
		wind_gusts_10m_max?: number[];
		wind_direction_10m_dominant?: number[];
		shortwave_radiation_sum?: number[];
		et0_fao_evapotranspiration?: number[];
	};
};

type NormalizedLayer = {
	code: number | null;
	description: string | null;
	icon: string | null;
	tempC: number | null;
	feelsLikeC: number | null;
	windKmh: number | null;
	windGustKmh: number | null;
	windDirection: string | null;
	humidityPct: number | null;
	dewpointC: number | null;
	pressureMb: number | null;
	freshSnowCm: number | null;
};

type NormalizedWeather = {
	date: string | null;
	time: string | null;
	isDay: boolean | null;
	weatherCode: number | null;
	cloudPct: number | null;
	humidityPct: number | null;
	dewpointC: number | null;
	pressureMslMb: number | null;
	pressureMb: number | null;
	precipMm: number | null;
	rainMm: number | null;
	showersMm: number | null;
	snowMm: number | null;
	freezingLevelM: number | null;
	visibilityKm: number | null;
	freshSnowCm: number | null;
	base: NormalizedLayer;
	mid: NormalizedLayer;
	upper: NormalizedLayer;
};

type NormalizedDailyForecast = {
	date: string;
	weatherCode: number | null;
	weatherDescription: string;
	maxTempC: number | null;
	minTempC: number | null;
	maxFeelsLikeC: number | null;
	minFeelsLikeC: number | null;
	sunrise: string | null;
	sunset: string | null;
	daylightDurationSec: number | null;
	sunshineDurationSec: number | null;
	rainSumMm: number | null;
	showersSumMm: number | null;
	snowfallSumCm: number | null;
	precipitationSumMm: number | null;
	precipitationHours: number | null;
	precipitationProbabilityMax: number | null;
	maxWindSpeedKmh: number | null;
	maxWindGustsKmh: number | null;
	dominantWindDirection: string | null;
	shortwaveRadiationSum: number | null;
	evapotranspirationEt0: number | null;
};

function toNumber(value: number | string | null | undefined): number | null {
	if (value === null || value === undefined || value === '') {
		return null;
	}

	const parsed = Number(value);
	return Number.isFinite(parsed) ? parsed : null;
}

function windDirectionFromDegrees(deg: number | null): string | null {
	if (deg === null) {
		return null;
	}

	const directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'];
	const index = Math.round(deg / 45) % 8;
	return directions[index];
}

function weatherDescription(code: number | null): string {
	if (code === null) return 'Condizioni non disponibili';
	if (code === 0) return 'Sereno';
	if (code <= 3) return 'Parzialmente nuvoloso';
	if (code <= 48) return 'Nebbia';
	if (code <= 67) return 'Pioggia';
	if (code <= 77) return 'Neve';
	if (code <= 86) return 'Rovesci neve';
	if (code <= 99) return 'Temporale';
	return 'Variabile';
}

function weatherIcon(code: number | null): string {
	if (code === null) return 'na';
	if (code === 0) return 'sun';
	if (code <= 3) return 'partly-cloudy';
	if (code <= 48) return 'fog';
	if (code <= 67) return 'rain';
	if (code <= 77) return 'snow';
	if (code <= 86) return 'snow-showers';
	if (code <= 99) return 'thunderstorm';
	return 'mixed';
}

function layerFromBase(payload: OpenMeteoResponse): NormalizedLayer {
	const current = payload.current;
	const code = toNumber(current?.weather_code);

	return {
		code,
		description: weatherDescription(code),
		icon: weatherIcon(code),
		tempC: toNumber(current?.temperature_2m),
		feelsLikeC: toNumber(current?.apparent_temperature),
		windKmh: toNumber(current?.wind_speed_10m),
		windGustKmh: toNumber(current?.wind_gusts_10m),
		windDirection: windDirectionFromDegrees(toNumber(current?.wind_direction_10m)),
		humidityPct: toNumber(current?.relative_humidity_2m),
		dewpointC: toNumber(current?.dew_point_2m),
		pressureMb: toNumber(current?.surface_pressure),
		freshSnowCm: null
	};
}

function layerFromHourly(
	tempSeries?: number[],
	windSeries?: number[],
	gustSeries?: number[],
	directionSeries?: number[],
	time?: string | null
): NormalizedLayer {
	const idx = 0;
	return {
		code: null,
		description: time ? `Strato ${time}` : 'Strato',
		icon: null,
		tempC: toNumber(tempSeries?.[idx]),
		feelsLikeC: toNumber(tempSeries?.[idx]),
		windKmh: toNumber(windSeries?.[idx]),
		windGustKmh: toNumber(gustSeries?.[idx]),
		windDirection: windDirectionFromDegrees(toNumber(directionSeries?.[idx])),
		humidityPct: null,
		dewpointC: null,
		pressureMb: null,
		freshSnowCm: null
	};
}

function normalizeForecast(payload: OpenMeteoResponse): NormalizedWeather | null {
	if (!payload.current) {
		return null;
	}

	const hourly = payload.hourly;
	const base = layerFromBase(payload);
	const mid = layerFromHourly(
		hourly?.temperature_80m,
		hourly?.wind_speed_80m,
		hourly?.wind_gusts_80m,
		hourly?.wind_direction_80m,
		hourly?.time?.[0] ?? null
	);
	const upper = layerFromHourly(
		hourly?.temperature_180m,
		hourly?.wind_speed_180m,
		hourly?.wind_gusts_180m,
		hourly?.wind_direction_180m,
		hourly?.time?.[0] ?? null
	);

	const snowMm = toNumber(payload.current.snowfall);
	const freshSnowCm = snowMm === null ? null : snowMm / 10;

	return {
		date: payload.current.time?.split('T')[0] ?? null,
		time: payload.current.time?.split('T')[1] ?? null,
		isDay:
			payload.current.is_day === undefined || payload.current.is_day === null
				? null
				: payload.current.is_day === 1,
		weatherCode: toNumber(payload.current.weather_code),
		cloudPct: toNumber(payload.current.cloud_cover),
		humidityPct: toNumber(payload.current.relative_humidity_2m),
		dewpointC: toNumber(payload.current.dew_point_2m),
		pressureMslMb: toNumber(payload.current.pressure_msl),
		pressureMb: toNumber(payload.current.surface_pressure),
		precipMm: toNumber(payload.current.precipitation),
		rainMm: toNumber(payload.current.rain),
		showersMm: toNumber(payload.current.showers),
		snowMm,
		freezingLevelM: toNumber(hourly?.freezing_level_height?.[0]),
		visibilityKm:
			toNumber(payload.current.visibility) === null
				? null
				: Number(payload.current.visibility) / 1000,
		freshSnowCm,
		base,
		mid,
		upper
	};
}

function normalizeDailyForecast(payload: OpenMeteoResponse): NormalizedDailyForecast[] {
	const daily = payload.daily;
	const dates = daily?.time ?? [];

	return dates.slice(0, 7).map((date, idx) => {
		const code = toNumber(daily?.weather_code?.[idx]);

		return {
			date,
			weatherCode: code,
			weatherDescription: weatherDescription(code),
			maxTempC: toNumber(daily?.temperature_2m_max?.[idx]),
			minTempC: toNumber(daily?.temperature_2m_min?.[idx]),
			maxFeelsLikeC: toNumber(daily?.apparent_temperature_max?.[idx]),
			minFeelsLikeC: toNumber(daily?.apparent_temperature_min?.[idx]),
			sunrise: daily?.sunrise?.[idx] ?? null,
			sunset: daily?.sunset?.[idx] ?? null,
			daylightDurationSec: toNumber(daily?.daylight_duration?.[idx]),
			sunshineDurationSec: toNumber(daily?.sunshine_duration?.[idx]),
			rainSumMm: toNumber(daily?.rain_sum?.[idx]),
			showersSumMm: toNumber(daily?.showers_sum?.[idx]),
			snowfallSumCm: toNumber(daily?.snowfall_sum?.[idx]),
			precipitationSumMm: toNumber(daily?.precipitation_sum?.[idx]),
			precipitationHours: toNumber(daily?.precipitation_hours?.[idx]),
			precipitationProbabilityMax: toNumber(daily?.precipitation_probability_max?.[idx]),
			maxWindSpeedKmh: toNumber(daily?.wind_speed_10m_max?.[idx]),
			maxWindGustsKmh: toNumber(daily?.wind_gusts_10m_max?.[idx]),
			dominantWindDirection: windDirectionFromDegrees(
				toNumber(daily?.wind_direction_10m_dominant?.[idx])
			),
			shortwaveRadiationSum: toNumber(daily?.shortwave_radiation_sum?.[idx]),
			evapotranspirationEt0: toNumber(daily?.et0_fao_evapotranspiration?.[idx])
		};
	});
}

export const load: PageServerLoad = async ({ fetch, setHeaders }) => {
	setHeaders({
		'cache-control': 'public, max-age=600, s-maxage=600, stale-while-revalidate=1200'
	});

	const officialLinks = [
		{
			title: 'Torgnon Ski Area',
			label: 'Stato piste e impianti',
			url: 'https://www.torgnon.net/inverno/'
		},
		{
			title: 'Panomax Torgnon',
			label: 'Webcam live 360°',
			url: 'https://torgnon-skiarea.panomax.com/'
		}
	] as const;

	const endpoint = new URL('https://api.open-meteo.com/v1/forecast');
	endpoint.searchParams.set('latitude', String(TORGNON.latitude));
	endpoint.searchParams.set('longitude', String(TORGNON.longitude));
	endpoint.searchParams.set('elevation', String(TORGNON.altitude));
	endpoint.searchParams.set(
		'current',
		[
			'temperature_2m',
			'relative_humidity_2m',
			'apparent_temperature',
			'is_day',
			'precipitation',
			'rain',
			'showers',
			'snowfall',
			'weather_code',
			'cloud_cover',
			'pressure_msl',
			'surface_pressure',
			'visibility',
			'wind_speed_10m',
			'wind_direction_10m',
			'wind_gusts_10m'
		].join(',')
	);
	endpoint.searchParams.set(
		'hourly',
		[
			'temperature_80m',
			'wind_speed_80m',
			'wind_direction_80m',
			'temperature_180m',
			'wind_speed_180m',
			'wind_direction_180m',
			'freezing_level_height'
		].join(',')
	);
	endpoint.searchParams.set(
		'daily',
		[
			'weather_code',
			'temperature_2m_max',
			'temperature_2m_min',
			'apparent_temperature_max',
			'apparent_temperature_min',
			'sunrise',
			'sunset',
			'daylight_duration',
			'sunshine_duration',
			'rain_sum',
			'showers_sum',
			'snowfall_sum',
			'precipitation_sum',
			'precipitation_hours',
			'precipitation_probability_max',
			'wind_speed_10m_max',
			'wind_gusts_10m_max',
			'wind_direction_10m_dominant',
			'shortwave_radiation_sum',
			'et0_fao_evapotranspiration'
		].join(',')
	);
	endpoint.searchParams.set('forecast_hours', '1');
	endpoint.searchParams.set('forecast_days', '7');
	endpoint.searchParams.set('timezone', 'Europe/Rome');

	try {
		const controller = new AbortController();
		const timeout = setTimeout(() => controller.abort(), 4500);
		const response = await fetch(endpoint, {
			headers: { accept: 'application/json' },
			signal: controller.signal
		});
		clearTimeout(timeout);

		if (!response.ok) {
			throw new Error(`Forecast service error ${response.status}`);
		}

		const payload = (await response.json()) as OpenMeteoResponse;
		const weather = normalizeForecast(payload);
		const dailyForecast = normalizeDailyForecast(payload);

		return {
			resortName: TORGNON.name,
			lastUpdated: new Date().toISOString(),
			weather,
			dailyForecast,
			officialLinks,
			status: {
				configured: true,
				liveForecast: weather !== null,
				liveOperations: false,
				message: weather
					? 'Forecast aggiornato per Torgnon. Piste e impianti vanno verificati sulle fonti ufficiali.'
					: 'Il forecast non contiene dati aggiornati al momento.'
			}
		};
	} catch (error) {
		console.error('Failed to load ski forecast for /meteo:', error);

		return {
			resortName: TORGNON.name,
			lastUpdated: null,
			weather: null,
			dailyForecast: [],
			officialLinks,
			status: {
				configured: true,
				liveForecast: false,
				liveOperations: false,
				message: 'Il forecast non e raggiungibile in questo momento.'
			}
		};
	}
};
