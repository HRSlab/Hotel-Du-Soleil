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
	import { trackEvent, trackPageView, isBookingUrl, classifyContactHref } from '$lib/analytics';

	let { children } = $props();
	const scrollMilestonesSent = new Set<number>();
	let lastTrackedPath = '';

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

	onMount(() => {
		if (typeof window === 'undefined' || typeof document === 'undefined') return;

		const milestones = [25, 50, 75, 90];

		const handleScroll = () => {
			const doc = document.documentElement;
			const maxScrollable = doc.scrollHeight - window.innerHeight;
			if (maxScrollable <= 0) return;

			const percent = Math.round((window.scrollY / maxScrollable) * 100);
			for (const milestone of milestones) {
				if (percent >= milestone && !scrollMilestonesSent.has(milestone)) {
					scrollMilestonesSent.add(milestone);
					trackEvent('scroll_depth', {
						percent_scrolled: milestone,
						page_path: page.url.pathname
					});
				}
			}
		};

		const handleDocumentClick = (event: MouseEvent) => {
			const target = event.target as Element | null;
			const anchor = target?.closest('a[href]') as HTMLAnchorElement | null;
			if (!anchor) return;

			const rawHref = anchor.getAttribute('href') ?? '';
			const contactType = classifyContactHref(rawHref);
			if (contactType) {
				trackEvent('contact_click', {
					contact_type: contactType,
					link_url: rawHref,
					page_path: page.url.pathname
				});
				return;
			}

			let url: URL;
			try {
				url = new URL(rawHref, window.location.origin);
			} catch {
				return;
			}

			if (isBookingUrl(url)) {
				trackEvent('begin_checkout', {
					currency: 'EUR',
					link_url: url.toString(),
					page_path: page.url.pathname
				});
				return;
			}

			if (/^\/offerte\/[^/]+$/.test(url.pathname)) {
				trackEvent('select_promotion', {
					promotion_id: url.pathname.split('/').pop() ?? 'unknown',
					page_path: page.url.pathname
				});
			}

			if (url.origin !== window.location.origin) {
				trackEvent('outbound_click', {
					link_url: url.toString(),
					link_domain: url.hostname,
					page_path: page.url.pathname
				});
			}
		};

		document.addEventListener('click', handleDocumentClick, true);
		window.addEventListener('scroll', handleScroll, { passive: true });

		return () => {
			document.removeEventListener('click', handleDocumentClick, true);
			window.removeEventListener('scroll', handleScroll);
		};
	});

	$effect(() => {
		if (typeof document !== 'undefined') {
			document.documentElement.lang = $locale;
			document.documentElement.dir = $dir;
			document.documentElement.classList.add('animations-enabled');
		}
	});

	$effect(() => {
		if (typeof document === 'undefined') return;

		const currentPath = page.url.pathname + page.url.search;
		if (currentPath === lastTrackedPath) return;

		lastTrackedPath = currentPath;
		scrollMilestonesSent.clear();
		trackPageView(currentPath, document.title);
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
