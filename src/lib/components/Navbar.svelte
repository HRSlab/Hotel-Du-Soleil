<script lang="ts">
	/* eslint-disable @typescript-eslint/no-explicit-any */
	import { t, locale, locales } from '$lib/i18n';

	import { onMount } from 'svelte';
	import { Menu, X, Minus, ArrowRight, Globe, ChevronDown, Phone, Mail } from 'lucide-svelte';
	import { page } from '$app/state';
	import { clsx, type ClassValue } from 'clsx';
	import { twMerge } from 'tailwind-merge';
	import BookingDrawer from '$lib/components/BookingDrawer.svelte';
	import { clickOutside } from '$lib/utils/clickOutside';

	function cn(...inputs: ClassValue[]) {
		return twMerge(clsx(inputs));
	}

	const langLabels: Record<string, string> = {
		it: 'Italiano',
		en: 'English',
		fr: 'Français',
		ru: 'Русский',
		de: 'Deutsch',
		es: 'Español',
		ar: 'العربية',
		zh: '中文'
	};

	let isScrolled = $state(false);
	let isMobileMenuOpen = $state(false);
	let isBookingMenuOpen = $state(false);
	let isLangOpen = $state(false);
	let isMobileLangOpen = $state(false);

	const darkHeroRoutes = ['/', '/camere', '/struttura', '/wellness', '/offerte'];
	const isDarkHero = $derived(
		darkHeroRoutes.includes(page.url.pathname) ||
			page.url.pathname.startsWith('/camere/') ||
			page.url.pathname.startsWith('/wellness/') ||
			page.url.pathname.startsWith('/offerte/')
	);

	const images: Record<string, string> = {
		overview: '/imgs/winter-entrance-hero.webp',
		rooms: '/imgs/room-view-menu.webp',
		restaurant: '/imgs/deer-dish-hero.webp',
		wellness: '/imgs/jacuzzi-spa-hds-2026.webp',
		offers: '/imgs/exterior-snow-back-2026.webp'
	};

	onMount(() => {
		const handleScroll = () => {
			isScrolled = window.scrollY > 50;
		};
		window.addEventListener('scroll', handleScroll);
		return () => window.removeEventListener('scroll', handleScroll);
	});

	const navItems = [
		{ key: 'overview', href: '/' },
		{ key: 'rooms', href: '/camere' },
		{ key: 'restaurant', href: '/ristorante' },
		{ key: 'wellness', href: '/wellness' },
		{ key: 'offers', href: '/offerte' }
	];

	function getLinkHref(link: unknown, fallbackHref: string): string {
		if (typeof link === 'object' && link !== null && 'href' in link) {
			const href = (link as { href?: unknown }).href;
			if (typeof href === 'string') return href;
		}
		return fallbackHref;
	}

	function isHiddenSectionHref(href: string): boolean {
		return href === '/posizione' || href === '/sport' || href.startsWith('/sport/');
	}

	function isInactiveOfferHref(href: string): boolean {
		return href.startsWith('/offerte/') && href !== '/offerte/restart';
	}

	function getVisibleMegaLinks(itemKey: string, fallbackHref: string): unknown[] {
		const links = $t('megamenu.' + itemKey + '.links');
		if (!Array.isArray(links)) return [];
		return links.filter((link) => {
			const href = getLinkHref(link, fallbackHref);
			return !isHiddenSectionHref(href) && !(itemKey === 'offers' && isInactiveOfferHref(href));
		});
	}

	const bookingPhoneHref = 'tel:+393793357713';
	const bookingPhoneLabel = '+39 379 335 7713';
	const bookingEmail = 'booking@hotel-du-soleil.it';
	const bookingEmailHref = `mailto:${bookingEmail}`;
</script>

<nav
	id="navbar"
	class={cn(
		'fixed top-36.5 z-50 w-full transition-all duration-500 sm:top-33.5 lg:top-29.5',
		isScrolled
			? 'bg-alpine-bg py-4 text-alpine-text shadow-sm'
			: isDarkHero
				? 'bg-transparent py-6 text-white'
				: 'border-b border-alpine-border bg-alpine-bg py-6 text-alpine-text shadow-sm'
	)}
>
	<div class="mx-auto flex max-w-screen-2xl items-center justify-between px-6">
		<a
			href="/"
			class="z-20 flex shrink-0 cursor-pointer items-center gap-3 text-left transition-transform duration-300 hover:scale-105"
		>
			<img
				src="/imgs/logo.webp"
				alt="Logo Chalet du Soleil"
				class="h-10 w-auto object-contain drop-shadow-md md:h-12"
			/>

			<div class="flex flex-col items-start justify-center pt-1">
				<h1
					class="font-serif text-lg leading-none tracking-widest uppercase md:text-xl lg:text-2xl"
				>
					Chalet du Soleil
				</h1>
				<span
					class="mt-1 font-['Great_Vibes'] text-sm leading-none tracking-wide text-alpine-gold opacity-90 md:text-base"
					style="text-transform: none;">by Futuro</span
				>
			</div>
		</a>

		<ul
			class="z-20 hidden h-full items-center gap-8 text-[11px] font-semibold tracking-[0.15em] uppercase lg:flex"
		>
			{#each navItems as item (item.key)}
				<li class="group py-6">
					<!-- eslint-disable-next-line @typescript-eslint/no-explicit-any -->
					<a href={item.href as any} class="nav-item-link relative inline-block"
						>{$t('nav.' + item.key)}</a
					>

					<div
						class="mega-menu-content cursor-default border-t border-alpine-border bg-white text-alpine-text shadow-2xl"
					>
						<div class="mx-auto grid max-w-screen-2xl grid-cols-12 gap-12 px-6 py-12 text-left">
							<div class="col-span-3">
								<h4 class="mb-6 font-serif text-3xl tracking-normal text-alpine-text capitalize">
									{$t('megamenu.' + item.key + '.title')}
								</h4>
								<ul class="space-y-4 text-sm font-normal tracking-normal normal-case">
									{#each getVisibleMegaLinks(item.key, item.href) as link, i (i)}
										<li>
											<!-- eslint-disable-next-line @typescript-eslint/no-explicit-any -->
											<a
												href={(typeof link === 'object' && link !== null && 'href' in link
													? (link as any).href
													: item.href) as any}
												class="flex items-center gap-2 transition-colors hover:text-alpine-gold"
											>
												<Minus class="h-4 w-4 text-alpine-gold" />
												{typeof link === 'object' && link !== null && 'name' in link
													? (link as any).name
													: link}
											</a>
										</li>
									{/each}
								</ul>
							</div>
							<div
								class="col-span-4 flex flex-col justify-center border-l border-alpine-border pr-6 pl-12"
							>
								<span
									class="mb-4 text-[10px] font-bold tracking-[0.2em] text-alpine-muted uppercase"
								>
									{$t('megamenu.' + item.key + '.featured_label')}
								</span>
								<p class="mb-6 text-sm leading-relaxed text-alpine-muted">
									{$t('megamenu.' + item.key + '.featured_text')}
								</p>
								<!-- eslint-disable-next-line @typescript-eslint/no-explicit-any -->
								<a
									href={item.href as any}
									class="flex items-center gap-2 text-xs font-bold tracking-widest text-alpine-text uppercase transition-colors hover:text-alpine-gold"
								>
									{$t('megamenu.' + item.key + '.featured_cta')}
									<ArrowRight class="h-4 w-4" />
								</a>
							</div>
							<div
								class="group/img bg-fossil relative col-span-5 aspect-video cursor-pointer overflow-hidden"
							>
								<img
									src={images[item.key]}
									alt={item.key}
									class="img-elegant h-full w-full object-cover"
								/>
								<div
									class="absolute inset-0 flex items-center justify-center bg-black/20 opacity-0 transition-opacity group-hover/img:opacity-100"
								>
									<span
										class="border border-white px-4 py-2 text-xs font-bold tracking-widest text-white uppercase"
										>Esplora</span
									>
								</div>
							</div>
						</div>
					</div>
				</li>
			{/each}

			<li class="relative ml-4" use:clickOutside={() => (isLangOpen = false)}>
				<button
					onclick={() => (isLangOpen = !isLangOpen)}
					class="flex items-center gap-1.5 text-[10px] font-semibold tracking-[0.15em] uppercase transition-colors hover:text-alpine-gold focus:outline-none"
				>
					<Globe class="h-3.5 w-3.5" />
					{$locale.toUpperCase()}
					<ChevronDown class={cn('h-3 w-3 transition-transform', isLangOpen && 'rotate-180')} />
				</button>

				{#if isLangOpen}
					<div
						class="absolute top-full right-0 mt-3 min-w-40 border border-alpine-border bg-white py-2 shadow-xl"
					>
						{#each locales as l (l)}
							<button
								onclick={() => {
									$locale = l;
									isLangOpen = false;
								}}
								class={cn(
									'flex w-full items-center gap-3 px-5 py-2.5 text-left text-xs tracking-wide transition-colors hover:bg-alpine-bg',
									$locale === l ? 'font-bold text-alpine-gold' : 'text-alpine-text'
								)}
							>
								<span class="w-5 text-[10px] font-bold uppercase opacity-40">{l}</span>
								{langLabels[l] ?? l}
							</button>
						{/each}
					</div>
				{/if}
			</li>
		</ul>

		<div class="z-20 flex items-center gap-6">
			<div class="hidden flex-col items-end gap-1 text-right lg:flex">
				<a
					href={bookingPhoneHref}
					class={cn(
						'flex items-center gap-2 text-xs font-medium transition-colors',
						isScrolled || !isDarkHero
							? 'text-alpine-text/80 hover:text-alpine-gold'
							: 'text-white/85 hover:text-alpine-gold'
					)}
				>
					<Phone class="h-3.5 w-3.5" />
					<span>{bookingPhoneLabel}</span>
				</a>
				<a
					href={bookingEmailHref}
					class={cn(
						'flex items-center gap-2 text-xs font-medium transition-colors',
						isScrolled || !isDarkHero
							? 'text-alpine-text/80 hover:text-alpine-gold'
							: 'text-white/85 hover:text-alpine-gold'
					)}
				>
					<Mail class="h-3.5 w-3.5" />
					<span>{bookingEmail}</span>
				</a>
			</div>
			<button
				onclick={() => (isBookingMenuOpen = true)}
				class={cn(
					'hidden px-8 py-3 text-[10px] tracking-[0.2em] uppercase transition-colors md:block',
					isScrolled || !isDarkHero
						? 'bg-alpine-text text-white hover:bg-alpine-gold'
						: 'bg-white text-alpine-text hover:bg-alpine-gold hover:text-white'
				)}
			>
				{$t('nav.book')}
			</button>
			<button class="lg:hidden" onclick={() => (isMobileMenuOpen = !isMobileMenuOpen)}>
				{#if isMobileMenuOpen}
					<X class="h-6 w-6 text-alpine-text" />
				{:else}
					<Menu
						class={cn('h-6 w-6', isScrolled || !isDarkHero ? 'text-alpine-text' : 'text-white')}
					/>
				{/if}
			</button>
		</div>
	</div>
</nav>

<div
	class={cn(
		'fixed inset-0 z-40 flex flex-col justify-center gap-6 overflow-y-auto bg-alpine-bg p-8 text-alpine-text transition-all duration-500',
		isMobileMenuOpen
			? 'translate-y-0 opacity-100'
			: 'pointer-events-none -translate-y-full opacity-0'
	)}
>
	<div class="absolute top-8 left-8">
		<img src="/imgs/logo.webp" alt="Logo Chalet du Soleil" class="h-10 w-auto object-contain" />
	</div>

	<nav class="mt-20 flex flex-col gap-8 pb-20 text-center">
		{#each navItems as item (item.key)}
			<div class="flex flex-col gap-2">
				<a
					href={item.href as any}
					class="font-serif text-3xl text-alpine-text"
					onclick={() => (isMobileMenuOpen = false)}
				>
					{$t('nav.' + item.key)}
				</a>

				{#if getVisibleMegaLinks(item.key, item.href).length > 0}
					<div class="flex flex-wrap justify-center gap-x-4 gap-y-2 px-4 opacity-60">
						{#each getVisibleMegaLinks(item.key, item.href) as link, i (i)}
							<a
								href={(typeof link === 'object' && link !== null && 'href' in link
									? (link as any).href
									: item.href) as any}
								class="text-[10px] font-bold tracking-widest uppercase"
								onclick={() => (isMobileMenuOpen = false)}
							>
								{typeof link === 'object' && link !== null && 'name' in link
									? (link as any).name
									: link}
							</a>
						{/each}
					</div>
				{/if}
			</div>
		{/each}

		<div class="mt-4 px-6">
			<button
				onclick={() => {
					isMobileMenuOpen = false;
					isBookingMenuOpen = true;
				}}
				class="block w-full bg-alpine-text px-10 py-5 text-xs tracking-[0.2em] text-white uppercase shadow-lg"
				>{$t('nav.book')}</button
			>
		</div>

		<div class="mt-6 flex flex-col gap-3 px-6">
			<a
				href={bookingPhoneHref}
				class="flex items-center justify-center gap-3 border border-alpine-border px-6 py-4 text-xs font-semibold tracking-[0.15em] text-alpine-text uppercase transition-colors hover:border-alpine-gold hover:text-alpine-gold"
				onclick={() => (isMobileMenuOpen = false)}
			>
				<Phone class="h-4 w-4" />
				<span>{bookingPhoneLabel}</span>
			</a>
			<a
				href={bookingEmailHref}
				class="flex items-center justify-center gap-3 border border-alpine-border px-6 py-4 text-[11px] font-semibold tracking-[0.08em] text-alpine-text transition-colors hover:border-alpine-gold hover:text-alpine-gold"
				onclick={() => (isMobileMenuOpen = false)}
			>
				<Mail class="h-4 w-4" />
				<span>{bookingEmail}</span>
			</a>
		</div>

		<div class="mt-6 px-6" use:clickOutside={() => (isMobileLangOpen = false)}>
			<button
				onclick={() => (isMobileLangOpen = !isMobileLangOpen)}
				class="flex w-full items-center justify-center gap-2 border border-alpine-border px-6 py-4 text-[11px] font-semibold tracking-[0.15em] text-alpine-text uppercase transition-colors hover:border-alpine-gold hover:text-alpine-gold"
			>
				<Globe class="h-4 w-4" />
				<span>{langLabels[$locale] ?? $locale.toUpperCase()}</span>
				<ChevronDown class={cn('h-4 w-4 transition-transform', isMobileLangOpen && 'rotate-180')} />
			</button>

			{#if isMobileLangOpen}
				<div class="mt-3 border border-alpine-border bg-white py-2 shadow-xl">
					{#each locales as l (l)}
						<button
							onclick={() => {
								$locale = l;
								isMobileLangOpen = false;
								isMobileMenuOpen = false;
							}}
							class={cn(
								'flex w-full items-center justify-between px-5 py-3 text-left text-xs tracking-wide transition-colors hover:bg-alpine-bg',
								$locale === l ? 'font-bold text-alpine-gold' : 'text-alpine-text'
							)}
						>
							<span>{langLabels[l] ?? l}</span>
							<span class="text-[10px] uppercase opacity-40">{l}</span>
						</button>
					{/each}
				</div>
			{/if}
		</div>
	</nav>
</div>
<BookingDrawer bind:isOpen={isBookingMenuOpen} />
