import { writable, derived } from 'svelte/store';
import it from './locales/it.json';
import en from './locales/en.json';
import fr from './locales/fr.json';
import de from './locales/de.json';
import ru from './locales/ru.json';
import es from './locales/es.json';
import ar from './locales/ar.json';

const translations: any = { it, en, fr, de, ru, es, ar };

export const locale = writable('it');

export const t = derived(locale, ($locale) => {
  return (key: string) => {
    const keys = key.split('.');
    let value = translations[$locale] || translations['it'];
    for (const k of keys) {
      value = value?.[k];
    }
    return value || key;
  };
});

export const dir = derived(locale, ($locale) => {
  return $locale === 'ar' ? 'rtl' : 'ltr';
});

export const locales = ['it', 'en', 'fr', 'de', 'ru', 'es', 'ar'];
