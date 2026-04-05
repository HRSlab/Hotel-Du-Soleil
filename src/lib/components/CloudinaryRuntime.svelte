<script lang="ts">
	import { browser } from '$app/environment';
	import { onMount } from 'svelte';
	import { isCloudinaryDeliveryEnabled, resolveCloudinaryUrl } from '$lib';

	function rewriteAttr(element: Element, attribute: 'src' | 'poster'): void {
		const currentValue = element.getAttribute(attribute);

		if (!currentValue) {
			return;
		}

		const resolvedValue = resolveCloudinaryUrl(currentValue);

		if (resolvedValue !== currentValue) {
			element.setAttribute(attribute, resolvedValue);
		}
	}

	function rewriteNode(node: ParentNode): void {
		if (node instanceof Element) {
			if (node.matches('img[src], source[src]')) {
				rewriteAttr(node, 'src');
			}

			if (node.matches('video[poster]')) {
				rewriteAttr(node, 'poster');
			}
		}

		node.querySelectorAll('img[src], source[src]').forEach((element) => rewriteAttr(element, 'src'));
		node.querySelectorAll('video[poster]').forEach((element) => rewriteAttr(element, 'poster'));
	}

	onMount(() => {
		if (!browser || !isCloudinaryDeliveryEnabled) {
			return;
		}

		rewriteNode(document);

		const observer = new MutationObserver((mutations) => {
			for (const mutation of mutations) {
				if (mutation.type === 'attributes' && mutation.target instanceof Element) {
					const attributeName = mutation.attributeName;

					if (attributeName === 'src' || attributeName === 'poster') {
						rewriteAttr(mutation.target, attributeName);
					}
				}

				mutation.addedNodes.forEach((addedNode) => {
					if (addedNode instanceof Element) {
						rewriteNode(addedNode);
					}
				});
			}
		});

		observer.observe(document.body, {
			attributes: true,
			attributeFilter: ['src', 'poster'],
			childList: true,
			subtree: true
		});

		return () => observer.disconnect();
	});
</script>