<script lang="ts">
	import './layout.css';
	import { locale, dir, t } from '$lib/i18n';
	import { page } from '$app/state';
	import Navbar from '$lib/components/Navbar.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import CloudinaryRuntime from '$lib/components/CloudinaryRuntime.svelte';
	import SecurityGuard from '$lib/components/SecurityGuard.svelte';
	import { getRestartPromotionUrl } from '$lib/config/booking';

	let { children } = $props();
	const restartPromoUrl = getRestartPromotionUrl('global_restart_banner');

	$effect(() => {
		if (typeof document !== 'undefined') {
			document.documentElement.lang = $locale;
			document.documentElement.dir = $dir;
			document.documentElement.classList.add('animations-enabled');
		}
	});

	$effect(() => {
		// Re-run animation observer on every page change
		const path = page.url.pathname;

		// We wait a bit for the DOM to update
		setTimeout(() => {
			const observerOptions = {
				root: null,
				rootMargin: '0px 0px -50px 0px',
				threshold: 0.1
			};

			const observer = new IntersectionObserver((entries) => {
				entries.forEach((entry) => {
					if (entry.isIntersecting) {
						entry.target.classList.add('is-visible');
						observer.unobserve(entry.target);
					}
				});
			}, observerOptions);

			const elements = document.querySelectorAll('.fade-up-element');
			elements.forEach((el) => observer.observe(el));

			return () => observer.disconnect();
		}, 100);
	});
</script>

<SecurityGuard />
<CloudinaryRuntime />
<div
	class="fixed inset-x-0 top-0 z-60 border-b border-alpine-text/20 bg-alpine-gold text-alpine-text"
>
	<div class="mx-auto max-w-screen-2xl px-4 py-3 sm:px-6">
		<div class="flex flex-col gap-3 lg:flex-row lg:items-center lg:justify-between">
			<div class="text-center lg:text-left">
				<p class="text-xs font-extrabold tracking-[0.12em] uppercase">
					{$t('promo.restart_title')}
				</p>
				<p class="mt-1 text-sm leading-snug font-medium">{$t('promo.restart_subtitle')}</p>
				<p class="mt-1 text-[12px] leading-snug text-alpine-text/80">
					{$t('promo.restart_highlight')}
				</p>
			</div>

			<div class="flex shrink-0 flex-col items-center gap-1 lg:items-end">
				<div class="inline-flex items-center gap-2 rounded-sm bg-alpine-text px-3 py-1 text-white">
					<span class="text-[10px] font-bold tracking-[0.12em] uppercase"
						>{$t('promo.price_label')}</span
					>
					<span class="font-serif text-2xl leading-none">{$t('promo.price_value')}</span>
				</div>
				<a
					href={restartPromoUrl}
					target="_blank"
					rel="noopener noreferrer"
					class="inline-flex items-center border border-alpine-text bg-white px-4 py-1.5 text-[10px] font-bold tracking-[0.18em] uppercase transition-colors hover:bg-alpine-text hover:text-white"
				>
					{$t('promo.restart_cta')}
				</a>
				<p class="text-[11px] text-alpine-text/85">{$t('promo.restart_scarcity')}</p>
			</div>
		</div>
	</div>
</div>
<Navbar />

<main class="min-h-screen overflow-x-clip">
	{@render children()}
</main>

<Footer />
