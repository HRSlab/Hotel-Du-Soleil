<script lang="ts">
    import { Leaf, Recycle, Sun, Droplet } from 'lucide-svelte';
</script>

<svelte:head>
    <title>Sostenibilità | Chalet du Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div class="absolute inset-0">
        <img src="https://images.unsplash.com/photo-1518173946687-a4c8892bbd9f?q=80&w=2000&auto=format&fit=crop" class="ken-burns h-full w-full object-cover opacity-80" alt="Sustainability at Chalet du Soleil" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/40 to-alpine-bg"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            In Armonia con l'Ambiente
        </span>
        <h1 class="font-serif text-5xl md:text-7xl leading-tight font-light text-white fade-up-element">
            Sostenibilità
        </h1>
    </div>
</header>

<section class="bg-alpine-bg px-6 py-24">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <Leaf class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-alpine-text md:text-4xl">
            Rispettiamo la montagna, curiamo il futuro.
        </h3>
        <p class="text-alpine-muted leading-relaxed font-light text-sm md:text-base border-t border-alpine-border pt-12 mt-12 mx-auto max-w-xl">
            Siamo custodi di un territorio prezioso e fragile. Per questo motivo adottiamo quotidianamente pratiche sostenibili che riducono il nostro impatto ambientale e promuovono l'economia locale.
        </p>
    </div>
</section>

<section class="bg-alpine-bg pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
    <div class="bg-white p-8 border border-alpine-border shadow-sm text-center fade-up-element">
        <Sun class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
        <h4 class="font-serif text-xl mb-4 italic">Energia Pulita</h4>
        <p class="text-xs text-alpine-muted font-light leading-relaxed">Pannelli solari per la produzione di acqua calda e illuminazione LED a basso consumo.</p>
    </div>
    <div class="bg-white p-8 border border-alpine-border shadow-sm text-center fade-up-element">
        <Recycle class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
        <h4 class="font-serif text-xl mb-4 italic">Zero Plastica</h4>
        <p class="text-xs text-alpine-muted font-light leading-relaxed">Abbiamo eliminato le monoporzioni di plastica in favore di dispenser e bottiglie di vetro.</p>
    </div>
    <div class="bg-white p-8 border border-alpine-border shadow-sm text-center fade-up-element">
        <Droplet class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
        <h4 class="font-serif text-xl mb-4 italic">Acqua di Fonte</h4>
        <p class="text-xs text-alpine-muted font-light leading-relaxed">Valorizziamo l'acqua purissima delle sorgenti di Torgnon, filtrata e servita al tavolo.</p>
    </div>
    <div class="bg-white p-8 border border-alpine-border shadow-sm text-center fade-up-element">
        <Leaf class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
        <h4 class="font-serif text-xl mb-4 italic">Km 0 & Biologico</h4>
        <p class="text-xs text-alpine-muted font-light leading-relaxed">Privilegiamo i produttori della valle per ridurre le emissioni legate ai trasporti.</p>
    </div>
</section>
