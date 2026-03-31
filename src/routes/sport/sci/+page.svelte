<script lang="ts">
	import { Snowflake, ShieldCheck, Sparkles, Mountain } from 'lucide-svelte';

	// Svelte 5 reactivity for scroll-based animations
	let scrollY = $state(0);
	let heroRef: HTMLElement;
	let observer: IntersectionObserver;

	// Remove complex gallery state and animation code
	// Keeping only essential scroll and observer

	// Gallery images - simplified premium horizontal scroll
	let galleryImages = $state([
		{ src: '/imgs/skier-torgnon.webp', alt: 'Skier in Torgnon' },
		{ src: '/imgs/Ski_slope.webp', alt: 'Slopes From Torgnon' },
		{ src: '/imgs/ski-gondola-view.webp', alt: 'View from the gondola' },
		{ src: '/imgs/slope-torgnon.webp', alt: 'Torgnon slope' },
		{ src: '/imgs/ski-ome-activities.webp', alt: 'Winter activities' },
		{ src: '/imgs/ski-sport-hero.webp', alt: 'Winter sports' },
		{ src: '/imgs/torgnon-view.webp', alt: 'Torgnon view' }
	]);

	// Remove lerp and animate functions - using simple scroll

	// Intersection Observer for fade-ups
	$effect(() => {
		observer = new IntersectionObserver(
			(entries) => {
				entries.forEach((entry) => {
					if (entry.isIntersecting) {
						entry.target.classList.add('animate-fade-up');
					}
				});
			},
			{ threshold: 0.1, rootMargin: '0px 0px -100px 0px' }
		);

		const fadeElements = document.querySelectorAll('.fade-up-element');
		fadeElements.forEach((el) => observer.observe(el));

		return () => {
			if (observer) {
				observer.disconnect();
			}
		};
	});

	// Scroll handler for parallax
	$effect(() => {
		const handleScroll = () => {
			scrollY = window.scrollY;
		};

		window.addEventListener('scroll', handleScroll);

		return () => {
			window.removeEventListener('scroll', handleScroll);
		};
	});
</script>

<svelte:head>
	<title>Ski & Snowboard | Chalet du Soleil</title>
</svelte:head>

<!-- Hero Section with Parallax -->
<header
	bind:this={heroRef}
	class="relative h-[80vh] w-full overflow-hidden bg-[#1a1a1a]"
	style="transform: scale({1 + scrollY * 0.0002})"
>
	<div class="absolute inset-0">
		<img
			src="/imgs/torgnon-view.webp"
			class="h-full w-full object-cover"
			alt="Ski in Torgnon"
			style="transform: scale({1 + scrollY * 0.0001})"
		/>
		<div class="absolute inset-0 bg-linear-to-b from-black/90 via-black/50 to-alpine-bg"></div>
	</div>

	<div class="absolute inset-0 z-10 flex flex-col justify-end px-6 pb-32 md:pb-40">
		<div class="max-w-4xl">
			<span
				class="fade-up-element mb-6 block text-[10px] font-bold tracking-[0.4em] text-white/70 uppercase"
			>
				SKI-IN SKI-OUT
			</span>
			<h1
				class="fade-up-element mb-8 font-serif text-6xl leading-none font-light text-white md:text-8xl"
			>
				Ski &<br />Snowboard
			</h1>
			<p class="fade-up-element max-w-lg text-lg leading-relaxed font-light text-white/80">
				Just 50 meters from the Torgnon ski lifts. Experience world-class slopes in the shadow of
				the Matterhorn.
			</p>
		</div>
	</div>
</header>

<!-- Asymmetrical Content Section -->
<section class="relative bg-alpine-bg px-6 py-32">
	<div class="mx-auto max-w-7xl">
		<!-- Overlapping layout -->
		<div class="relative">
			<div class="fade-up-element md:absolute md:top-0 md:right-0 md:w-2/5">
				<div class="border border-alpine-border bg-white p-12 shadow-2xl">
					<Snowflake class="mb-6 h-8 w-8 text-alpine-gold" strokeWidth={1} />
					<h3 class="mb-4 font-serif text-2xl text-alpine-text italic">Sun-Kissed Slopes</h3>
					<p class="text-sm leading-relaxed font-light text-alpine-muted">
						Torgnon's ski area offers perfectly groomed pistes for all levels, surrounded by
						breathtaking views from the Matterhorn to Monte Rosa.
					</p>
				</div>
			</div>

			<div class="fade-up-element md:mt-24 md:w-3/5 md:pr-24">
				<div class="mb-16">
					<span
						class="mb-8 block text-[10px] font-bold tracking-[0.3em] text-alpine-gold uppercase"
					>
						THE EXPERIENCE
					</span>
					<h2
						class="mb-12 font-serif text-5xl leading-tight font-light text-alpine-text md:text-6xl"
					>
						Pure Alpine<br />Adventure
					</h2>
				</div>

				<div class="space-y-12">
					<div class="border-l-2 border-alpine-gold pl-8">
						<h4 class="mb-4 font-serif text-2xl text-alpine-text italic">Slopes for Every Level</h4>
						<p class="leading-relaxed font-light text-alpine-muted">
							From gentle beginner trails to challenging black runs, our ski area caters to all
							abilities with professional instruction available.
						</p>
					</div>

					<div class="border-l-2 border-alpine-gold pl-8">
						<h4 class="mb-4 font-serif text-2xl text-alpine-text italic">Guided Off-Piste</h4>
						<p class="leading-relaxed font-light text-alpine-muted">
							Explore fresh powder with our certified guides for safe and unforgettable backcountry
							experiences.
						</p>
					</div>

					<div class="border-l-2 border-alpine-gold pl-8">
						<h4 class="mb-4 font-serif text-2xl text-alpine-text italic">Snow Park Excellence</h4>
						<p class="leading-relaxed font-light text-alpine-muted">
							State-of-the-art snow park with jumps, rails, and halfpipe for freestyle skiing and
							snowboarding.
						</p>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>

<!-- Services Section -->
<section class="bg-[#050505] px-6 py-32">
	<div class="mx-auto max-w-6xl">
		<div class="fade-up-element mb-20 text-center">
			<span class="mb-6 block text-[10px] font-bold tracking-[0.3em] text-alpine-gold uppercase">
				PREMIUM SERVICES
			</span>
			<h2 class="font-serif text-4xl font-light text-white md:text-5xl">Ski Club Amenities</h2>
		</div>

		<div class="grid grid-cols-1 gap-8 md:grid-cols-3">
			<div class="fade-up-element border border-white/10 bg-white/5 p-8 backdrop-blur-sm">
				<ShieldCheck class="mb-6 h-6 w-6 text-alpine-gold" />
				<h4 class="mb-4 font-serif text-lg text-white">Secure Ski Storage</h4>
				<p class="text-sm leading-relaxed font-light text-white/70">
					CCTV-monitored ski room with individual lockers and boot warming area.
				</p>
			</div>

			<div class="fade-up-element border border-white/10 bg-white/5 p-8 backdrop-blur-sm md:mt-12">
				<Sparkles class="mb-6 h-6 w-6 text-alpine-gold" />
				<h4 class="mb-4 font-serif text-lg text-white">Equipment Services</h4>
				<p class="text-sm leading-relaxed font-light text-white/70">
					Professional ski tuning, waxing, and on-site rental equipment.
				</p>
			</div>

			<div class="fade-up-element border border-white/10 bg-white/5 p-8 backdrop-blur-sm md:mt-24">
				<Mountain class="mb-6 h-6 w-6 text-alpine-gold" />
				<h4 class="mb-4 font-serif text-lg text-white">Certified Instruction</h4>
				<p class="text-sm leading-relaxed font-light text-white/70">
					Partnered with certified ski schools for private and group lessons.
				</p>
			</div>
		</div>
	</div>
</section>

<!-- Premium Horizontal Scroll Gallery -->
<section class="relative overflow-hidden bg-alpine-bg px-6 py-32">
	<div class="mx-auto max-w-7xl">
		<div class="fade-up-element mb-20">
			<span class="mb-6 block text-[10px] font-bold tracking-[0.3em] text-alpine-gold uppercase">
				VISUAL JOURNEY
			</span>
			<h2 class="font-serif text-5xl leading-tight font-light text-alpine-text md:text-6xl">
				Live the<br />Snow
			</h2>
		</div>

		<!-- Horizontal scroll container with smooth scrolling -->
		<div class="scrollbar-hide w-full max-w-full overflow-x-auto px-2 pb-8">
			<div class="inline-flex w-max items-stretch gap-8 py-4">
				{#each galleryImages as item (item.src)}
					<div
						class="h-[42vh] min-w-[82vw] overflow-hidden rounded-3xl border border-alpine-border bg-[#0b0b0b] shadow-2xl sm:h-[50vh] sm:min-w-[72vw] md:h-[55vh] md:min-w-[42vw] lg:min-w-[34vw] xl:min-w-[28vw]"
					>
						<img
							src={item.src}
							alt={item.alt}
							class="h-full w-full object-contain p-2 transition-transform duration-700 md:object-cover md:p-0 md:hover:scale-105"
							loading="lazy"
						/>
					</div>
				{/each}
			</div>
		</div>

		<div class="fade-up-element mt-12 text-center">
			<p class="mx-auto max-w-md text-sm font-light text-alpine-muted">
				Scroll horizontally to explore our winter wonderland through stunning alpine photography
			</p>
			<!-- Scroll indicator -->
			<div class="mt-6 flex justify-center">
				<div class="flex space-x-2">
					<div class="h-2 w-2 animate-pulse rounded-full bg-alpine-gold"></div>
					<div class="h-2 w-2 rounded-full bg-alpine-gold/50"></div>
					<div class="h-2 w-2 rounded-full bg-alpine-gold/30"></div>
				</div>
			</div>
		</div>
	</div>
</section>

<style>
	:global(.animate-fade-up) {
		animation: fadeUp 1s ease-out forwards;
	}

	@keyframes fadeUp {
		from {
			opacity: 0;
			transform: translateY(30px);
		}
		to {
			opacity: 1;
			transform: translateY(0);
		}
	}

	/* Hide scrollbar for horizontal scroll gallery */
	.scrollbar-hide {
		-ms-overflow-style: none;
		scrollbar-width: none;
	}
	.scrollbar-hide::-webkit-scrollbar {
		display: none;
	}
</style>
