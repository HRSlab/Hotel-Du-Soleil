<script lang="ts">
    import { t } from '$lib/i18n';
    import { ShieldCheck, Car, Users, Camera } from 'lucide-svelte';
</script>

<svelte:head>
    <title>{$t('policy.title')} | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[40vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div class="absolute inset-0">
        <div class="absolute inset-0 bg-alpine-text opacity-90"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-16 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/60 uppercase md:text-xs fade-up-element">
            Hotel du Soleil — Torgnon
        </span>
        <h1 class="font-serif text-4xl md:text-6xl leading-tight font-light text-white fade-up-element">
            {$t('policy.title')}
        </h1>
    </div>
</header>

<section class="bg-alpine-bg px-6 py-20 lg:py-32 min-h-screen">
    <div class="fade-up-element mx-auto max-w-3xl">
        <div class="space-y-16 text-alpine-muted font-light leading-relaxed text-sm">

            <!-- Section 1: Camere e Suite -->
            <div>
                <div class="flex items-center gap-3 mb-6">
                    <ShieldCheck class="w-6 h-6 text-alpine-gold shrink-0" />
                    <h2 class="font-serif text-2xl md:text-3xl text-alpine-text">{$t('policy.rooms_title')}</h2>
                </div>
                <p class="mb-6">{$t('policy.rooms_intro')}</p>
                
                <h3 class="text-xs font-bold uppercase tracking-[0.2em] text-alpine-text mb-4">{$t('policy.included_title')}</h3>
                <ul class="space-y-3 mb-8">
                    {#each (Array.isArray($t('policy.included_items')) ? $t('policy.included_items') : []) as item, i (i)}
                        <li class="flex items-start gap-3">
                            <span class="mt-1.5 w-1.5 h-1.5 rounded-full bg-alpine-gold shrink-0"></span>
                            <span>{item}</span>
                        </li>
                    {/each}
                </ul>

                <div class="bg-white border border-alpine-border p-6 space-y-4">
                    <p>{$t('policy.tariffe_note')}</p>
                    <p>{$t('policy.colazione')}</p>
                    <p>{$t('policy.mezza_pensione')}</p>
                    <p class="font-medium text-alpine-text">{$t('policy.checkin_checkout')}</p>
                </div>
            </div>

            <!-- Section 2: Cancellazione -->
            <div>
                <div class="flex items-center gap-3 mb-6">
                    <ShieldCheck class="w-6 h-6 text-alpine-gold shrink-0" />
                    <h2 class="font-serif text-2xl md:text-3xl text-alpine-text">{$t('policy.cancel_title')}</h2>
                </div>
                <p class="mb-6">{$t('policy.cancel_intro')}</p>

                <div class="space-y-4">
                    {#each (Array.isArray($t('policy.cancel_rules')) ? $t('policy.cancel_rules') : []) as rule, i (i)}
                        <div class="bg-white border border-alpine-border p-6">
                            <h4 class="text-xs font-bold uppercase tracking-widest text-alpine-text mb-2">
                                {typeof rule === 'object' && rule !== null && 'label' in rule ? rule.label : ''}
                            </h4>
                            <p>
                                {typeof rule === 'object' && rule !== null && 'text' in rule ? rule.text : rule}
                            </p>
                        </div>
                    {/each}
                </div>
            </div>

            <!-- Section 3: Quadruple Familiari -->
            <div>
                <div class="flex items-center gap-3 mb-6">
                    <Users class="w-6 h-6 text-alpine-gold shrink-0" />
                    <h2 class="font-serif text-2xl md:text-3xl text-alpine-text">{$t('policy.family_title')}</h2>
                </div>
                <h3 class="text-xs font-bold uppercase tracking-[0.2em] text-alpine-text mb-4">{$t('policy.included_title')}</h3>
                <ul class="space-y-3">
                    {#each (Array.isArray($t('policy.family_items')) ? $t('policy.family_items') : []) as item, i (i)}
                        <li class="flex items-start gap-3">
                            <span class="mt-1.5 w-1.5 h-1.5 rounded-full bg-alpine-gold shrink-0"></span>
                            <span>{item}</span>
                        </li>
                    {/each}
                </ul>
            </div>

            <!-- Section 4: Gruppi -->
            <div>
                <div class="flex items-center gap-3 mb-6">
                    <Users class="w-6 h-6 text-alpine-gold shrink-0" />
                    <h2 class="font-serif text-2xl md:text-3xl text-alpine-text">{$t('policy.groups_title')}</h2>
                </div>
                <p>{$t('policy.groups_text')}</p>
            </div>

            <!-- Section 5: Logistica -->
            <div>
                <div class="flex items-center gap-3 mb-6">
                    <Car class="w-6 h-6 text-alpine-gold shrink-0" />
                    <h2 class="font-serif text-2xl md:text-3xl text-alpine-text">{$t('policy.parking_title')}</h2>
                </div>
                <p>{$t('policy.parking_text')}</p>
            </div>

            <!-- Section 6: Nota immagini -->
            <div>
                <div class="flex items-center gap-3 mb-6">
                    <Camera class="w-6 h-6 text-alpine-gold shrink-0" />
                    <h2 class="font-serif text-2xl md:text-3xl text-alpine-text">{$t('policy.images_title')}</h2>
                </div>
                <p>{$t('policy.images_text')}</p>
            </div>

            <div class="pt-12 border-t border-alpine-border">
                <p class="text-[10px] uppercase tracking-widest font-bold">{$t('policy.updated')}</p>
            </div>
        </div>
    </div>
</section>
