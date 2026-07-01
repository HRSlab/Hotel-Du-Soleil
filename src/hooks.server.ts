/*
 * Copyright (c) 2026 Carlo Bello. All rights reserved.
 * Proprietary commercial software.
 * No modification is permitted without prior written consent.
 * Contact: carlo@hrslab.com
 */

import { redirect, type Handle } from '@sveltejs/kit';

function isHiddenSectionPath(pathname: string): boolean {
	return pathname === '/posizione' || pathname === '/sport' || pathname.startsWith('/sport/');
}

export const handle: Handle = async ({ event, resolve }) => {
	if (isHiddenSectionPath(event.url.pathname)) {
		throw redirect(307, '/');
	}

	return resolve(event);
};
