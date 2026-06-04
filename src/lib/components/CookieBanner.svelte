<script lang="ts">
	import { onMount } from 'svelte';
	import { t } from '$lib/i18n';
	import {
		acceptAllConsent,
		initConsentFromStorage,
		rejectAllConsent,
		saveCustomConsent
	} from '$lib/consent';

	let showBanner = $state(false);
	let showDetails = $state(false);
	let functional = $state(false);
	let analytics = $state(false);
	let marketing = $state(false);

	function syncFromStoredConsent(): void {
		const stored = initConsentFromStorage();
		if (!stored) {
			showBanner = true;
			return;
		}

		functional = stored.functional;
		analytics = stored.analytics;
		marketing = stored.marketing;
		showBanner = false;
	}

	function acceptAll(): void {
		acceptAllConsent();
		functional = true;
		analytics = true;
		marketing = true;
		showBanner = false;
		showDetails = false;
	}

	function rejectAll(): void {
		rejectAllConsent();
		functional = false;
		analytics = false;
		marketing = false;
		showBanner = false;
		showDetails = false;
	}

	function savePreferences(): void {
		saveCustomConsent({ functional, analytics, marketing });
		showBanner = false;
		showDetails = false;
	}

	function openSettings(): void {
		showBanner = true;
		showDetails = true;
	}

	onMount(() => {
		syncFromStoredConsent();

		const onConsentUpdated = (event: Event) => {
			const customEvent = event as CustomEvent<{
				functional: boolean;
				analytics: boolean;
				marketing: boolean;
			}>;
			if (!customEvent.detail) return;

			functional = customEvent.detail.functional;
			analytics = customEvent.detail.analytics;
			marketing = customEvent.detail.marketing;
		};

		window.addEventListener('cookie-consent-updated', onConsentUpdated as EventListener);

		return () => {
			window.removeEventListener('cookie-consent-updated', onConsentUpdated as EventListener);
		};
	});
</script>

{#if showBanner}
	<div
		class="fixed right-4 bottom-4 left-4 z-60 mx-auto w-full max-w-3xl rounded-2xl border border-alpine-border bg-white/95 p-4 shadow-[0_18px_40px_rgba(44,51,51,0.12)] backdrop-blur-sm md:p-5"
		role="dialog"
		aria-live="polite"
		aria-label="Cookie preferences"
	>
		<div class="space-y-3">
			<div>
				<p class="text-sm font-semibold text-alpine-text">{$t('cookie_banner.title')}</p>
				<p class="mt-1 text-xs leading-relaxed text-alpine-muted">
					{$t('cookie_banner.description')}
				</p>
			</div>

			{#if showDetails}
				<div
					class="space-y-2 rounded-xl border border-alpine-border/80 bg-alpine-bg/60 p-3 text-xs text-alpine-muted"
				>
					<label class="flex items-start justify-between gap-3">
						<span>
							<span class="block font-medium text-alpine-text">{$t('cookie_banner.necessary')}</span
							>
							<span>{$t('cookie_banner.necessary_desc')}</span>
						</span>
						<input type="checkbox" checked disabled class="mt-0.5" />
					</label>

					<label class="flex items-start justify-between gap-3">
						<span>
							<span class="block font-medium text-alpine-text"
								>{$t('cookie_banner.functional')}</span
							>
							<span>{$t('cookie_banner.functional_desc')}</span>
						</span>
						<input type="checkbox" bind:checked={functional} class="mt-0.5" />
					</label>

					<label class="flex items-start justify-between gap-3">
						<span>
							<span class="block font-medium text-alpine-text">{$t('cookie_banner.analytics')}</span
							>
							<span>{$t('cookie_banner.analytics_desc')}</span>
						</span>
						<input type="checkbox" bind:checked={analytics} class="mt-0.5" />
					</label>

					<label class="flex items-start justify-between gap-3">
						<span>
							<span class="block font-medium text-alpine-text">{$t('cookie_banner.marketing')}</span
							>
							<span>{$t('cookie_banner.marketing_desc')}</span>
						</span>
						<input type="checkbox" bind:checked={marketing} class="mt-0.5" />
					</label>
				</div>
			{/if}

			<p class="text-[11px] text-alpine-muted">
				{$t('cookie_banner.detail')}
				<a
					href="/cookie-policy"
					class="underline decoration-alpine-gold/70 underline-offset-2 hover:text-alpine-text"
					>{$t('cookie_banner.policy_link')}</a
				>
				·
				<a
					href="/policy"
					class="underline decoration-alpine-gold/70 underline-offset-2 hover:text-alpine-text"
					>{$t('cookie_banner.privacy_link')}</a
				>
			</p>

			<div class="flex flex-wrap items-center gap-2 pt-1">
				<button
					type="button"
					onclick={rejectAll}
					class="rounded-full border border-alpine-border px-3 py-1.5 text-xs font-medium text-alpine-text transition hover:bg-alpine-bg"
				>
					{$t('cookie_banner.reject_all')}
				</button>

				<button
					type="button"
					onclick={acceptAll}
					class="rounded-full bg-alpine-text px-3 py-1.5 text-xs font-medium text-white transition hover:opacity-90"
				>
					{$t('cookie_banner.accept_all')}
				</button>

				{#if showDetails}
					<button
						type="button"
						onclick={savePreferences}
						class="rounded-full border border-alpine-gold/70 px-3 py-1.5 text-xs font-medium text-alpine-text transition hover:bg-alpine-bg"
					>
						{$t('cookie_banner.save_preferences')}
					</button>
				{:else}
					<button
						type="button"
						onclick={() => (showDetails = true)}
						class="rounded-full border border-alpine-gold/70 px-3 py-1.5 text-xs font-medium text-alpine-text transition hover:bg-alpine-bg"
					>
						{$t('cookie_banner.customize')}
					</button>
				{/if}
			</div>
		</div>
	</div>
{:else}
	<button
		type="button"
		onclick={openSettings}
		class="fixed right-4 bottom-4 z-50 rounded-full border border-alpine-border bg-white/90 px-3 py-1.5 text-[11px] font-medium text-alpine-text shadow-sm backdrop-blur-sm transition hover:bg-white"
	>
		{$t('cookie_banner.manage')}
	</button>
{/if}
