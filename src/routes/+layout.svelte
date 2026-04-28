<script lang="ts">
	import './layout.css';
	import { onMount } from 'svelte';
	import { locale, dir, t } from '$lib/i18n';
	import { page } from '$app/state';
	import Navbar from '$lib/components/Navbar.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import CloudinaryRuntime from '$lib/components/CloudinaryRuntime.svelte';
	import SecurityGuard from '$lib/components/SecurityGuard.svelte';
	import PromoCarousel from '$lib/components/PromoCarousel.svelte';

	let { children } = $props();

	onMount(() => {
		if (typeof window === 'undefined' || typeof document === 'undefined') return;
		if (document.getElementById('CanaryChatWidget')) return;

		(function (w: any, d: Document, o: string, f: string) {
			w[o] =
				w[o] ||
				function () {
					(w[o].q = w[o].q || []).push(arguments);
				};

			const js = d.createElement('script') as HTMLScriptElement;
			const fjs = d.getElementsByTagName('script')[0];
			js.id = o;
			js.src = f;
			js.async = true;
			fjs.parentNode?.insertBefore(js, fjs);
		})(
			window as any,
			document,
			'CanaryChatWidget',
			'https://static.cdn.canarytechnologies.com/dist/web-chat-loader.js'
		);

		(window as any).CanaryChatWidget?.(
			'init',
			{
				slug: 'hotel-du-soleil-torgnon83',
				chat_button_bottom_offset: 20,
				chat_button_color: '#B89872',
				chat_button_background_color: '#B89872',
				chat_button_text_color: '#2C3333'
			},
			'https://eu.canarytechnologies.com'
		);
	});

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
<PromoCarousel />
<Navbar />

<main class="min-h-screen overflow-x-clip">
	{@render children()}
</main>

<Footer />
