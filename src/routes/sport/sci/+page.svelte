<script lang="ts">
	import { Snowflake, ShieldCheck, Sparkles, Mountain } from 'lucide-svelte';

	// Svelte 5 reactivity for scroll-based animations
	let scrollY = $state(0);
	let activeGalleryIndex = $state(0);
	let heroRef: HTMLElement;
	let galleryViewport: HTMLElement;
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

	function syncGalleryIndex() {
		if (!galleryViewport) {
			return;
		}

		const cards = Array.from(galleryViewport.querySelectorAll<HTMLElement>('[data-gallery-card]'));
		if (cards.length === 0) {
			return;
		}

		const viewportCenter = galleryViewport.scrollLeft + galleryViewport.clientWidth / 2;
		let nearestIndex = 0;
		let nearestDistance = Number.POSITIVE_INFINITY;

		cards.forEach((card, index) => {
			const cardCenter = card.offsetLeft + card.offsetWidth / 2;
			const distance = Math.abs(cardCenter - viewportCenter);

			if (distance < nearestDistance) {
				nearestDistance = distance;
				nearestIndex = index;
			}
		});

		activeGalleryIndex = nearestIndex;
	}

	function scrollGalleryTo(index: number, behavior: ScrollBehavior = 'smooth') {
		if (!galleryViewport) {
			return;
		}

		const cards = Array.from(galleryViewport.querySelectorAll<HTMLElement>('[data-gallery-card]'));
		const clampedIndex = Math.max(0, Math.min(index, cards.length - 1));
		const targetCard = cards[clampedIndex];

		if (!targetCard) {
			return;
		}

		galleryViewport.scrollTo({
			left: targetCard.offsetLeft,
			behavior
		});
		activeGalleryIndex = clampedIndex;
	}

	function previousGalleryImage() {
		scrollGalleryTo(activeGalleryIndex - 1);
	}

	function nextGalleryImage() {
		scrollGalleryTo(activeGalleryIndex + 1);
	}

	function handleGalleryWheel(event: WheelEvent) {
		if (!galleryViewport || window.innerWidth < 1024) {
			return;
		}

		const hasHorizontalOverflow = galleryViewport.scrollWidth > galleryViewport.clientWidth;
		if (!hasHorizontalOverflow) {
			return;
		}

		if (Math.abs(event.deltaY) <= Math.abs(event.deltaX)) {
			return;
		}

		event.preventDefault();
		galleryViewport.scrollBy({
			left: event.deltaY,
			behavior: 'auto'
		});
		syncGalleryIndex();
	}
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

		<div class="mb-8 flex items-end justify-between gap-6">
			<p class="max-w-md text-sm font-light text-alpine-muted">
				Swipe on mobile or use your mouse wheel and arrows on desktop to move through the gallery.
			</p>
			<div class="hidden items-center gap-3 lg:flex">
				<button
					type="button"
					onclick={previousGalleryImage}
					class="flex h-12 w-12 items-center justify-center rounded-full border border-alpine-border bg-white text-alpine-text transition-colors hover:border-alpine-gold hover:text-alpine-gold disabled:cursor-not-allowed disabled:opacity-35"
					disabled={activeGalleryIndex === 0}
					aria-label="Show previous ski gallery image"
				>
					←
				</button>
				<button
					type="button"
					onclick={nextGalleryImage}
					class="flex h-12 w-12 items-center justify-center rounded-full border border-alpine-border bg-white text-alpine-text transition-colors hover:border-alpine-gold hover:text-alpine-gold disabled:cursor-not-allowed disabled:opacity-35"
					disabled={activeGalleryIndex === galleryImages.length - 1}
					aria-label="Show next ski gallery image"
				>
					→
				</button>
			</div>
		</div>

		<div
			bind:this={galleryViewport}
			class="scrollbar-hide -mx-6 overflow-x-auto px-6 pb-8 scroll-smooth snap-x snap-mandatory overscroll-x-contain [scrollbar-gutter:stable]"
			onscroll={syncGalleryIndex}
			onwheel={handleGalleryWheel}
		>
			<div class="flex w-max items-stretch gap-5 py-3 lg:gap-8">
				{#each galleryImages as item (item.src)}
					<div
						data-gallery-card
						class="group relative h-[54svh] min-w-[86vw] snap-center overflow-hidden rounded-4xl border border-alpine-border bg-[#0b0b0b] shadow-2xl sm:min-w-[72vw] md:min-w-[56vw] lg:min-w-[38vw] xl:min-w-[32vw]"
					>
						<img
							src={item.src}
							alt={item.alt}
							class="h-full w-full object-cover transition-transform duration-700 group-hover:scale-105"
							loading="lazy"
						/>
						<div class="absolute inset-0 bg-linear-to-t from-black/75 via-black/10 to-transparent"></div>
						<div class="absolute inset-x-0 bottom-0 p-6 md:p-8">
							<p class="mb-2 text-[10px] font-bold tracking-[0.32em] text-white/65 uppercase">
								Torgnon
							</p>
							<h3 class="font-serif text-2xl font-light text-white md:text-3xl">{item.alt}</h3>
						</div>
					</div>
				{/each}
			</div>
		</div>

		<div class="fade-up-element mt-12 text-center">
			<p class="mx-auto max-w-md text-sm font-light text-alpine-muted">
				Explore our winter wonderland through alpine photography curated for touch and desktop browsing.
			</p>
			<div class="mt-6 flex justify-center">
				<div class="flex flex-wrap justify-center gap-2">
					{#each galleryImages as _, index (index)}
						<button
							type="button"
							onclick={() => scrollGalleryTo(index)}
							class={`h-2 rounded-full transition-all duration-300 ${activeGalleryIndex === index ? 'w-8 bg-alpine-gold' : 'w-2 bg-alpine-gold/30 hover:bg-alpine-gold/60'}`}
							aria-label={`Go to ski gallery image ${index + 1}`}
						></button>
					{/each}
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
