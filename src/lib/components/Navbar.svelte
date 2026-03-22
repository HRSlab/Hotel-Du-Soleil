<script lang="ts">
	import { t, locale, locales } from '$lib/i18n';
	import { onMount } from 'svelte';
	import { Menu, X, Minus, ArrowRight } from 'lucide-svelte';
	import { page } from '$app/state';
	import { clsx, type ClassValue } from 'clsx';
	import { twMerge } from 'tailwind-merge';

	function cn(...inputs: ClassValue[]) {
		return twMerge(clsx(inputs));
	}

	let isScrolled = $state(false);
	let isMobileMenuOpen = $state(false);

	const darkHeroRoutes = ['/', '/camere'];
	const isDarkHero = $derived(
		darkHeroRoutes.includes(page.url.pathname) || page.url.pathname.startsWith('/camere/')
	);

	const images: Record<string, string> = {
		overview: '/imgs/Winter_entrance_hero.png',
		rooms: '/imgs/room_view_menu.png',
		restaurant: '/imgs/deer_dish_hero.webp',
		wellness:
			'https://images.unsplash.com/photo-1544161515-4ab6ce6db874?q=80&w=1000&auto=format&fit=crop',
		sport:
			'https://images.unsplash.com/photo-1518602164578-cd0074062767?q=80&w=1000&auto=format&fit=crop',
		experiences: '/imgs/yoga-in-the-snow.png'
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
		{ key: 'sport', href: '/sport' },
		{ key: 'experiences', href: '/esperienze' }
	];
</script>

<nav
	id="navbar"
	class={cn(
		'fixed z-50 w-full transition-all duration-500',
		isScrolled
			? 'bg-alpine-bg py-4 text-alpine-text shadow-sm'
			: isDarkHero
				? 'bg-transparent py-6 text-white'
				: 'border-b border-alpine-border bg-alpine-bg py-6 text-alpine-text shadow-sm'
	)}
>
	<div class="mx-auto flex max-w-screen-2xl items-center justify-between px-6">
		<!-- Logo -->
		<a href="/" class="z-20 flex flex-col items-end flex-shrink-0 cursor-pointer text-left">
			<h1 class="font-serif text-2xl tracking-widest uppercase md:text-3xl">Hotel du Soleil</h1>
			<span class="font-['Great_Vibes'] text-3xl text-alpine-gold -mt-3 pr-2 opacity-90 tracking-wide" style="text-transform: none;">by Futuro</span>
		</a>

		<!-- Desktop Menu -->
		<ul
			class="z-20 hidden h-full items-center gap-8 text-[11px] font-semibold tracking-[0.15em] uppercase lg:flex"
		>
			{#each navItems as item}
				<li class="group py-6">
					<a href={item.href} class="nav-item-link relative inline-block">{$t(`nav.${item.key}`)}</a
					>

					<!-- MEGA MENU CONTENT -->
					<div
						class="mega-menu-content cursor-default border-t border-alpine-border bg-white text-alpine-text shadow-2xl"
					>
						<div class="mx-auto grid max-w-screen-2xl grid-cols-12 gap-12 px-6 py-12 text-left">
							<div class="col-span-3">
								<h4 class="mb-6 font-serif text-3xl tracking-normal text-alpine-text capitalize">
									{$t(`megamenu.${item.key}.title`)}
								</h4>
								<ul class="space-y-4 text-sm font-normal tracking-normal normal-case">
									{#each $t(`megamenu.${item.key}.links`) as link}
										<li>
											<a
												href={typeof link === 'object' ? link.href : item.href}
												class="flex items-center gap-2 transition-colors hover:text-alpine-gold"
											>
												<Minus class="h-4 w-4 text-alpine-gold" />
												{typeof link === 'object' ? link.name : link}
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
									{$t(`megamenu.${item.key}.featured_label`)}
								</span>
								<p class="mb-6 text-sm leading-relaxed text-alpine-muted">
									{$t(`megamenu.${item.key}.featured_text`)}
								</p>
								<a
									href={item.href}
									class="flex items-center gap-2 text-xs font-bold tracking-widest text-alpine-text uppercase transition-colors hover:text-alpine-gold"
								>
									{$t(`megamenu.${item.key}.featured_cta`)}
									<ArrowRight class="h-4 w-4" />
								</a>
							</div>
							<div
								class="group/img bg-fossil relative col-span-5 aspect-[16/9] cursor-pointer overflow-hidden"
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

			<!-- Locale Switcher -->
			<li class="ml-4 flex items-center gap-2">
				{#each locales as l, i}
					<button
						onclick={() => ($locale = l)}
						class={cn(
							'text-[10px] uppercase transition-colors hover:text-alpine-gold focus:outline-none',
							$locale === l ? 'font-bold text-alpine-gold' : 'font-normal opacity-60'
						)}
					>
						{l}
					</button>
					{#if i < locales.length - 1}
						<span class="text-[8px] opacity-20">|</span>
					{/if}
				{/each}
			</li>
		</ul>

		<!-- Book & Mobile Toggle -->
		<div class="z-20 flex items-center gap-6">
			<a
				href="https://booking.passepartout.cloud/booking?oidPortale=17552&lingua={$locale}"
				target="_blank"
				class={cn(
					'hidden px-8 py-3 text-[10px] tracking-[0.2em] uppercase transition-colors md:block',
					isScrolled || !isDarkHero
						? 'bg-alpine-text text-white hover:bg-alpine-gold'
						: 'bg-white text-alpine-text hover:bg-alpine-gold hover:text-white'
				)}
			>
				{$t('nav.book')}
			</a>
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

<!-- Mobile Menu -->
<div
	class={cn(
		'fixed inset-0 z-40 flex flex-col justify-center gap-6 overflow-y-auto bg-alpine-bg p-8 text-alpine-text transition-all duration-500',
		isMobileMenuOpen
			? 'translate-y-0 opacity-100'
			: 'pointer-events-none -translate-y-full opacity-0'
	)}
>
	<nav class="mt-10 flex flex-col gap-6 text-center">
		{#each navItems as item}
			<a href={item.href} class="font-serif text-3xl" onclick={() => (isMobileMenuOpen = false)}
				>{$t(`nav.${item.key}`)}</a
			>
		{/each}
		<div class="mt-8">
			<a
				href="https://booking.passepartout.cloud/booking?oidPortale=17552&lingua={$locale}"
				class="block w-full bg-alpine-text px-10 py-4 text-xs tracking-[0.2em] text-white uppercase"
				>{$t('nav.book')}</a
			>
		</div>

		<div class="mt-8 flex flex-wrap justify-center gap-4">
			{#each locales as l}
				<button
					onclick={() => {
						$locale = l;
						isMobileMenuOpen = false;
					}}
					class={cn(
						'text-xs uppercase',
						$locale === l ? 'font-bold text-alpine-gold' : 'opacity-50'
					)}
				>
					{l}
				</button>
			{/each}
		</div>
	</nav>
</div>
