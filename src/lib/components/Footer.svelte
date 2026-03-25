<script lang="ts">
  import { t } from '$lib/i18n';
</script>

<footer class="bg-alpine-text text-white/70 pt-24 pb-12 px-6">
  <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-16 mb-20">
    
    <div class="md:col-span-2">
      <h2 class="font-serif text-3xl text-white mb-6 uppercase tracking-widest">Hotel du Soleil</h2>
      <p class="font-light text-sm leading-relaxed max-w-sm mb-8 opacity-80">
        {$t('footer.description')}
      </p>
      <div class="flex gap-6">
        <a href="https://www.instagram.com/hotel_du_soleil_?igsh=MWI4NjJ3d2t3anR2OQ%3D%3D" class="text-white hover:text-alpine-gold transition-colors text-sm uppercase tracking-widest font-semibold">Instagram</a>
        <a href="https://www.facebook.com/share/1D9sq5H7nA/" class="text-white hover:text-alpine-gold transition-colors text-sm uppercase tracking-widest font-semibold">Facebook</a>
      </div>
    </div>

    <div>
      <h4 class="text-[10px] uppercase tracking-widest text-white/40 mb-6 font-bold">{$t('footer.contacts_title')}</h4>
      <ul class="space-y-4 text-sm font-light opacity-90">
        <li>Piazza Frutaz 30, Torgnon (AO)</li>
        <li>+39 3793357713</li>
        <li>info@hotel-du-soleil.it</li>
      </ul>
    </div>

    <div>
      <h4 class="text-[10px] uppercase tracking-widest text-white/40 mb-6 font-bold">{$t('footer.explore_title')}</h4>
      <ul class="space-y-4 text-sm font-light opacity-90">
        <li><a href="/struttura" class="hover:text-white transition-colors">{$t('footer.links.structure')}</a></li>
        <li><a href="/camere" class="hover:text-white transition-colors">{$t('footer.links.rooms')}</a></li>
        <li><a href="/ristorante" class="hover:text-white transition-colors">{$t('footer.links.restaurant')}</a></li>
        <li><a href="/termini" class="hover:text-white transition-colors">{$t('footer.links.terms')}</a></li>
        <li><a href="/policy" class="hover:text-white transition-colors">{$t('footer.links.policy') || 'Policy'}</a></li>
      </ul>
    </div>

  </div>

  <div class="max-w-7xl mx-auto border-t border-white/10 pt-8 flex flex-col md:flex-row justify-between items-center text-[10px] uppercase tracking-widest opacity-60">
    <p>{$t('footer.rights')}</p>
    <p class="mt-4 md:mt-0">{$t('footer.made_by')}</p>
  </div>
</footer>
