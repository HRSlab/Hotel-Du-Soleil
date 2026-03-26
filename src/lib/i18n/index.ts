import { writable, derived } from 'svelte/store';
import it from './locales/it.json';
import en from './locales/en.json';
import ru from './locales/ru.json';
import fr from './locales/fr.json';

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const translations: Record<string, any> = { it, en, ru, fr };

export const locale = writable('it');

export const t = derived(locale, ($locale) => {
  return (key: string) => {
    const keys = key.split('.');
    
    // Try current locale
    let value = translations[$locale];
    for (const k of keys) {
      value = value?.[k];
    }
    
    // Fallback to 'it' if not found and current locale is not 'it'
    if (value === undefined && $locale !== 'it') {
      value = translations['it'];
      for (const k of keys) {
        value = value?.[k];
      }
    }
    
    return value;
  };
});

export const dir = derived(locale, () => {
  return 'ltr';
});

export const locales = ['it', 'en', 'fr', 'ru'];
