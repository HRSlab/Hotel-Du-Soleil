import { writable, derived } from 'svelte/store';
import it from './locales/it.json';
import en from './locales/en.json';
import ru from './locales/ru.json';
import fr from './locales/fr.json';
import de from './locales/de.json';
import es from './locales/es.json';
import ar from './locales/ar.json';
import zh from './locales/zh.json';

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const translations: Record<string, any> = { it, en, ru, fr, de, es, ar, zh };

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

export const dir = derived(locale, ($locale) => {
  return $locale === 'ar' ? 'rtl' : 'ltr';
});

export const locales = ['it', 'en'];
