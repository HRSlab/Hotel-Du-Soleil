/*
 * Copyright (c) 2026 Carlo Bello. All rights reserved.
 * Proprietary commercial software.
 * No modification is permitted without prior written consent.
 * Contact: carlo@hrslab.com
 */

import tailwindcss from '@tailwindcss/vite';
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({ plugins: [tailwindcss(), sveltekit()] });
