<script lang="ts">
  import './layout.css';
  import { locale, dir } from '$lib/i18n';
  import { page } from '$app/state';
  import Navbar from '$lib/components/Navbar.svelte';
  import Footer from '$lib/components/Footer.svelte';
  import CloudinaryRuntime from '$lib/components/CloudinaryRuntime.svelte';
  import SecurityGuard from '$lib/components/SecurityGuard.svelte';

  let { children } = $props();

  $effect(() => {
    if (typeof document !== 'undefined') {
      document.documentElement.lang = $locale;
      document.documentElement.dir = $dir;
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
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      }, observerOptions);

      const elements = document.querySelectorAll('.fade-up-element');
      elements.forEach(el => observer.observe(el));

      return () => observer.disconnect();
    }, 100);
  });
</script>

<SecurityGuard />
<CloudinaryRuntime />
<Navbar />

<main class="min-h-screen overflow-x-clip">
  {@render children()}
</main>

<Footer />
