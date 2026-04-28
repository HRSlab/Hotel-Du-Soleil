<script lang="ts">
	import { t } from '$lib/i18n';

	type Props = {
		title: string;
		subtitle: string;
		notesPlaceholder?: string;
		submitLabel?: string;
		successTitle?: string;
		successText?: string;
	};

	let {
		title,
		subtitle,
		notesPlaceholder: _notesPlaceholder,
		submitLabel: _submitLabel,
		successTitle: _successTitle,
		successText: _successText
	}: Props = $props();

	const bookingPhoneHref = 'tel:+393793357713';
	const bookingPhoneLabel = '+39 379 335 7713';
	const bookingEmail = 'booking@hotel-du-soleil.it';
	const bookingEmailHref = `mailto:${bookingEmail}`;
	const bookingWhatsappHref = 'https://wa.me/393793357713';

	const faqs = $derived([
		{
			question: $t('offer_lead_form.faq_1_question'),
			answer: $t('offer_lead_form.faq_1_answer')
		},
		{
			question: $t('offer_lead_form.faq_2_question'),
			answer: $t('offer_lead_form.faq_2_answer')
		},
		{
			question: $t('offer_lead_form.faq_3_question'),
			answer: $t('offer_lead_form.faq_3_answer')
		}
	]);

	const trustSignals = $derived([
		$t('offer_lead_form.trust_1'),
		$t('offer_lead_form.trust_2'),
		$t('offer_lead_form.trust_3'),
		$t('offer_lead_form.trust_4')
	]);
</script>

<section class="border-y border-alpine-border bg-white px-6 py-24">
	<div class="mx-auto max-w-6xl space-y-10">
		<div class="mb-10 text-center">
			<h2 class="font-serif text-4xl text-alpine-text md:text-5xl">{title}</h2>
			<p class="mx-auto mt-4 max-w-2xl text-sm font-light text-alpine-muted md:text-base">
				{subtitle}
			</p>
		</div>

		<div class="grid grid-cols-1 gap-6 md:grid-cols-3">
			<a
				href={bookingWhatsappHref}
				target="_blank"
				rel="noopener noreferrer"
				class="border border-[#25D366]/40 bg-[#25D366]/5 px-6 py-5 text-center transition-colors hover:bg-[#25D366]/10"
			>
				<p class="text-[10px] font-bold tracking-[0.18em] text-[#1f8f47] uppercase">WhatsApp</p>
				<p class="mt-2 font-serif text-2xl text-alpine-text">
					{$t('offer_lead_form.whatsapp_title')}
				</p>
				<p class="mt-2 text-xs text-alpine-muted">{$t('offer_lead_form.whatsapp_text')}</p>
			</a>

			<a
				href={bookingPhoneHref}
				class="border border-alpine-border bg-alpine-bg px-6 py-5 text-center transition-colors hover:border-alpine-gold"
			>
				<p class="text-[10px] font-bold tracking-[0.18em] text-alpine-muted uppercase">
					{$t('offer_lead_form.phone_label')}
				</p>
				<p class="mt-2 font-serif text-2xl text-alpine-text">{bookingPhoneLabel}</p>
				<p class="mt-2 text-xs text-alpine-muted">{$t('offer_lead_form.phone_text')}</p>
			</a>

			<a
				href={bookingEmailHref}
				class="border border-blue-300/60 bg-blue-50/35 px-6 py-5 text-center transition-colors hover:bg-blue-50"
			>
				<p class="text-[10px] font-bold tracking-[0.18em] text-blue-700 uppercase">
					{$t('offer_lead_form.email_label')}
				</p>
				<p class="mt-2 font-serif text-2xl break-all text-alpine-text">{bookingEmail}</p>
				<p class="mt-2 text-xs text-alpine-muted">{$t('offer_lead_form.email_text')}</p>
			</a>
		</div>

		<div class="grid grid-cols-1 gap-8 lg:grid-cols-2">
			<article class="border border-alpine-border bg-alpine-bg p-7">
				<h3 class="font-serif text-3xl text-alpine-text">{$t('offer_lead_form.faq_title')}</h3>
				<div class="mt-5 space-y-4">
					{#each faqs as faq}
						<div class="border-b border-alpine-border/70 pb-4 last:border-b-0 last:pb-0">
							<h4 class="text-sm font-semibold text-alpine-text">{faq.question}</h4>
							<p class="mt-2 text-sm font-light text-alpine-muted">{faq.answer}</p>
						</div>
					{/each}
				</div>
			</article>

			<article class="border border-alpine-border bg-white p-7">
				<h3 class="font-serif text-3xl text-alpine-text">{$t('offer_lead_form.trust_title')}</h3>
				<ul class="mt-5 space-y-3 text-sm font-light text-alpine-muted">
					{#each trustSignals as item}
						<li class="flex items-start gap-3">
							<span class="mt-1.25 inline-block h-2 w-2 rounded-full bg-alpine-gold"></span>
							<span>{item}</span>
						</li>
					{/each}
				</ul>
			</article>
		</div>

		<div class="border border-alpine-gold/40 bg-alpine-gold/10 px-6 py-5 text-center">
			<p class="text-[10px] font-bold tracking-[0.18em] text-alpine-text uppercase">
				{$t('offer_lead_form.contact_title')}
			</p>
			<p class="mt-2 text-sm text-alpine-muted">
				{$t('offer_lead_form.contact_text')}
			</p>
		</div>
	</div>
</section>
