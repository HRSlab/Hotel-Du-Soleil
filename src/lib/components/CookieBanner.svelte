<script lang="ts">
	import { cookieConsent, setCookieConsent } from '$lib/consent';
	import { t } from '$lib/i18n';
</script>

{#if $cookieConsent === null}
	<div class="fixed inset-x-4 bottom-4 z-120 mx-auto max-w-4xl rounded-2xl border border-alpine-border bg-white/95 p-5 shadow-[0_20px_60px_rgba(44,51,51,0.2)] backdrop-blur-md md:inset-x-8 md:p-6">
		<div class="flex flex-col gap-4 md:flex-row md:items-end md:justify-between">
			<div class="max-w-2xl">
				<h2 class="font-serif text-2xl leading-tight text-alpine-text">{$t('cookie_banner.title')}</h2>
				<p class="mt-2 text-sm leading-relaxed text-alpine-muted">
					{$t('cookie_banner.description')}
					<a href="/cookie-policy" class="ml-1 underline decoration-alpine-gold underline-offset-4 hover:text-alpine-text">
						{$t('cookie_banner.policy_link')}
					</a>
				</p>
			</div>

			<div class="flex flex-col gap-2 sm:flex-row sm:items-center">
				<button
					type="button"
					on:click={() => setCookieConsent('rejected')}
					class="cursor-pointer rounded-full border border-alpine-text px-5 py-2 text-xs font-semibold tracking-[0.14em] text-alpine-text uppercase transition hover:bg-alpine-text hover:text-white"
				>
					{$t('cookie_banner.reject')}
				</button>
				<button
					type="button"
					on:click={() => setCookieConsent('accepted')}
					class="cursor-pointer rounded-full bg-alpine-gold px-5 py-2 text-xs font-semibold tracking-[0.14em] text-white uppercase transition hover:brightness-95"
				>
					{$t('cookie_banner.accept')}
				</button>
			</div>
		</div>
	</div>
{/if}
