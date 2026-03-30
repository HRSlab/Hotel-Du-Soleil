<script lang="ts">
    import { t } from '$lib/i18n';
    import { Cookie, Shield, Settings } from 'lucide-svelte';
</script>

<svelte:head>
    <title>{$t('cookie_policy.title')} | Chalet du Soleil</title>
</svelte:head>

<header class="relative h-[40vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div class="absolute inset-0">
        <div class="absolute inset-0 bg-alpine-text opacity-90"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-16 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/60 uppercase md:text-xs fade-up-element">
            Chalet du Soleil — Torgnon
        </span>
        <h1 class="font-serif text-4xl md:text-6xl leading-tight font-light text-white fade-up-element">
            {$t('cookie_policy.title')}
        </h1>
    </div>
</header>

<section class="bg-alpine-bg px-6 py-20 lg:py-32 min-h-screen">
    <div class="fade-up-element mx-auto max-w-3xl">
        <div class="space-y-16 text-alpine-muted font-light leading-relaxed text-sm">

            <!-- Introduction -->
            <div>
                <div class="flex items-center gap-3 mb-6">
                    <Cookie class="w-6 h-6 text-alpine-gold shrink-0" />
                    <h2 class="font-serif text-2xl md:text-3xl text-alpine-text">{$t('cookie_policy.intro_title')}</h2>
                </div>
                <p class="mb-6">{$t('cookie_policy.intro_text')}</p>
            </div>

            <!-- What are cookies -->
            <div>
                <div class="flex items-center gap-3 mb-6">
                    <Settings class="w-6 h-6 text-alpine-gold shrink-0" />
                    <h2 class="font-serif text-2xl md:text-3xl text-alpine-text">{$t('cookie_policy.what_title')}</h2>
                </div>
                <p class="mb-6">{$t('cookie_policy.what_text')}</p>
            </div>

            <!-- Types of cookies -->
            <div>
                <div class="flex items-center gap-3 mb-6">
                    <Shield class="w-6 h-6 text-alpine-gold shrink-0" />
                    <h2 class="font-serif text-2xl md:text-3xl text-alpine-text">{$t('cookie_policy.types_title')}</h2>
                </div>

                <div class="space-y-8">
                    <div>
                        <h3 class="text-lg font-semibold text-alpine-text mb-4">{$t('cookie_policy.essential_title')}</h3>
                        <p>{$t('cookie_policy.essential_text')}</p>
                    </div>

                    <div>
                        <h3 class="text-lg font-semibold text-alpine-text mb-4">{$t('cookie_policy.analytics_title')}</h3>
                        <p>{$t('cookie_policy.analytics_text')}</p>
                    </div>

                    <div>
                        <h3 class="text-lg font-semibold text-alpine-text mb-4">{$t('cookie_policy.functional_title')}</h3>
                        <p>{$t('cookie_policy.functional_text')}</p>
                    </div>
                </div>
            </div>

            <!-- How to manage cookies -->
            <div>
                <h2 class="font-serif text-2xl md:text-3xl text-alpine-text mb-6">{$t('cookie_policy.manage_title')}</h2>
                <p class="mb-6">{$t('cookie_policy.manage_text')}</p>

                <div class="bg-white border border-alpine-border p-6 space-y-4">
                    <h3 class="text-lg font-semibold text-alpine-text">{$t('cookie_policy.browser_title')}</h3>
                    <p>{$t('cookie_policy.browser_text')}</p>
                </div>
            </div>

            <!-- Contact -->
            <div>
                <h2 class="font-serif text-2xl md:text-3xl text-alpine-text mb-6">{$t('cookie_policy.contact_title')}</h2>
                <p class="mb-6">{$t('cookie_policy.contact_text')}</p>
                <p class="text-alpine-text font-medium">info@hotel-du-soleil.it</p>
            </div>

            <!-- Last updated -->
            <div class="text-center text-alpine-muted/60 text-xs">
                {$t('cookie_policy.last_updated')}
            </div>

        </div>
    </div>
</section>