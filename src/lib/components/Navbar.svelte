<script lang="ts">
  import { t, locale, locales } from '$lib/i18n';
  import { onMount } from 'svelte';
  import { Menu, X, Minus, ArrowRight } from 'lucide-svelte';
  import { clsx, type ClassValue } from 'clsx';
  import { twMerge } from 'tailwind-merge';

  function cn(...inputs: ClassValue[]) {
    return twMerge(clsx(inputs));
  }

  let isScrolled = $state(false);
  let isMobileMenuOpen = $state(false);

  const images: Record<string, string> = {
    overview: "https://images.unsplash.com/photo-1518602164578-cd0074062767?q=80&w=1000&auto=format&fit=crop",
    rooms: "https://images.unsplash.com/photo-1616594039964-ae9021a400a0?q=80&w=1000&auto=format&fit=crop",
    restaurant: "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?q=80&w=1000&auto=format&fit=crop",
    wellness: "https://images.unsplash.com/photo-1544161515-4ab6ce6db874?q=80&w=1000&auto=format&fit=crop",
    sport: "https://images.unsplash.com/photo-1518602164578-cd0074062767?q=80&w=1000&auto=format&fit=crop",
    experiences: "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=1000&auto=format&fit=crop"
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

<nav id="navbar" class={cn(
  "fixed w-full z-50 transition-all duration-500",
  isScrolled ? "bg-alpine-bg text-alpine-text py-4 shadow-sm" : "bg-transparent text-white py-6"
)}>
  <div class="max-w-screen-2xl mx-auto px-6 flex justify-between items-center">
    <!-- Logo -->
    <a href="/" class="text-left cursor-pointer z-20 flex-shrink-0">
      <h1 class="font-serif text-2xl md:text-3xl tracking-widest uppercase">
        Hotel du Soleil
      </h1>
    </a>

    <!-- Desktop Menu -->
    <ul class="hidden lg:flex gap-8 text-[11px] tracking-[0.15em] uppercase font-semibold h-full items-center z-20">
      {#each navItems as item}
        <li class="group py-6">
          <a href={item.href} class="nav-item-link relative inline-block">{$t(`nav.${item.key}`)}</a>
          
          <!-- MEGA MENU CONTENT -->
          <div class="mega-menu-content bg-white text-alpine-text shadow-2xl border-t border-alpine-border cursor-default">
            <div class="max-w-screen-2xl mx-auto px-6 py-12 grid grid-cols-12 gap-12 text-left">
              <div class="col-span-3">
                <h4 class="font-serif text-3xl mb-6 text-alpine-text capitalize tracking-normal">
                  {$t(`megamenu.${item.key}.title`)}
                </h4>
                <ul class="space-y-4 text-sm font-normal normal-case tracking-normal">
                  {#each $t(`megamenu.${item.key}.links`) as link}
                    <li>
                      <a href={typeof link === 'object' ? link.href : item.href} class="hover:text-alpine-gold transition-colors flex items-center gap-2">
                        <Minus class="w-4 h-4 text-alpine-gold" />
                        {typeof link === 'object' ? link.name : link}
                      </a>
                    </li>
                  {/each}
                </ul>
              </div>
              <div class="col-span-4 flex flex-col justify-center border-l border-alpine-border pl-12 pr-6">
                <span class="text-[10px] font-bold uppercase tracking-[0.2em] text-alpine-muted mb-4">
                  {$t(`megamenu.${item.key}.featured_label`)}
                </span>
                <p class="text-sm leading-relaxed text-alpine-muted mb-6">
                  {$t(`megamenu.${item.key}.featured_text`)}
                </p>
                <a href={item.href} class="text-xs font-bold uppercase tracking-widest text-alpine-text hover:text-alpine-gold transition-colors flex items-center gap-2">
                  {$t(`megamenu.${item.key}.featured_cta`)} <ArrowRight class="w-4 h-4" />
                </a>
              </div>
              <div class="col-span-5 relative group/img cursor-pointer overflow-hidden bg-fossil aspect-[16/9]">
                <img src={images[item.key]} alt={item.key} class="w-full h-full object-cover img-elegant" />
                <div class="absolute inset-0 bg-black/20 opacity-0 group-hover/img:opacity-100 transition-opacity flex items-center justify-center">
                  <span class="text-white font-bold tracking-widest uppercase text-xs border border-white px-4 py-2">Esplora</span>
                </div>
              </div>
            </div>
          </div>
        </li>
      {/each}
      
      <!-- Locale Switcher -->
      <li class="flex gap-2 ml-4 items-center">
        {#each locales as l, i}
          <button 
            onclick={() => $locale = l}
            class={cn(
              "text-[10px] uppercase transition-colors hover:text-alpine-gold focus:outline-none",
              $locale === l ? "text-alpine-gold font-bold" : "font-normal opacity-60"
            )}
          >
            {l}
          </button>
          {#if i < locales.length - 1}
            <span class="opacity-20 text-[8px]">|</span>
          {/if}
        {/each}
      </li>
    </ul>

    <!-- Book & Mobile Toggle -->
    <div class="flex items-center gap-6 z-20">
      <a href="https://booking.passepartout.cloud/booking?oidPortale=17552&lingua={$locale}" target="_blank" class={cn(
        "hidden md:block px-8 py-3 text-[10px] tracking-[0.2em] uppercase transition-colors",
        isScrolled ? "bg-alpine-text text-white hover:bg-alpine-gold" : "bg-white text-alpine-text hover:bg-alpine-gold hover:text-white"
      )}>
        {$t('nav.book')}
      </a>
      <button class="lg:hidden" onclick={() => isMobileMenuOpen = !isMobileMenuOpen}>
        {#if isMobileMenuOpen}
          <X class="w-6 h-6 text-alpine-text" />
        {:else}
          <Menu class={cn("w-6 h-6", isScrolled ? "text-alpine-text" : "text-white")} />
        {/if}
      </button>
    </div>
  </div>
</nav>

<!-- Mobile Menu -->
<div class={cn(
  "fixed inset-0 bg-alpine-bg z-40 flex flex-col justify-center p-8 gap-6 transition-all duration-500 text-alpine-text overflow-y-auto",
  isMobileMenuOpen ? "opacity-100 translate-y-0" : "opacity-0 -translate-y-full pointer-events-none"
)}>
  <nav class="flex flex-col gap-6 text-center mt-10">
    {#each navItems as item}
      <a href={item.href} class="font-serif text-3xl" onclick={() => isMobileMenuOpen = false}>{$t(`nav.${item.key}`)}</a>
    {/each}
    <div class="mt-8">
      <a href="https://booking.passepartout.cloud/booking?oidPortale=17552&lingua={$locale}" class="bg-alpine-text text-white px-10 py-4 text-xs tracking-[0.2em] uppercase block w-full">{$t('nav.book')}</a>
    </div>
    
    <div class="mt-8 flex justify-center flex-wrap gap-4">
      {#each locales as l}
        <button 
          onclick={() => { $locale = l; isMobileMenuOpen = false; }}
          class={cn(
            "text-xs uppercase",
            $locale === l ? "text-alpine-gold font-bold" : "opacity-50"
          )}
        >
          {l}
        </button>
      {/each}
    </div>
  </nav>
</div>
