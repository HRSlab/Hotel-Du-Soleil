<script lang="ts">
    import { Moon, Snowflake, Sparkles, Map } from 'lucide-svelte';
</script>

<svelte:head>
    <title>Ciaspolate Notturne | Hotel du Soleil</title>
</svelte:head>

<header class="relative h-[60vh] w-full overflow-hidden bg-[#1a1a1a]">
    <div class="absolute inset-0">
        <img src="https://images.unsplash.com/photo-1544984243-ec57ea16fe75?q=80&w=2000&auto=format&fit=crop" class="ken-burns h-full w-full object-cover opacity-60 grayscale hover:grayscale-0 transition-all duration-700" alt="Ciaspolate Notturne" />
        <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/60 to-black"></div>
    </div>

    <div class="absolute inset-0 z-10 flex flex-col items-center justify-end px-6 pb-24 text-center">
        <span class="mb-4 block text-[10px] font-medium tracking-[0.4em] text-white/80 uppercase md:text-xs fade-up-element">
            La Magia della Notte
        </span>
        <h1 class="font-serif text-5xl md:text-7xl leading-tight font-light text-white fade-up-element">
            Ciaspolate Notturne
        </h1>
    </div>
</header>

<section class="bg-black text-white px-6 py-24">
    <div class="fade-up-element mx-auto max-w-3xl text-center">
        <Moon class="w-10 h-10 text-alpine-gold mx-auto mb-10" />
        <h3 class="mb-10 font-serif text-3xl leading-snug text-white md:text-4xl italic">
            "Sotto il chiarore lunare, la neve sussurra i suoi segreti."
        </h3>
        <p class="text-white/60 leading-relaxed font-light text-sm md:text-base border-t border-white/10 pt-12 mt-12 mx-auto max-w-xl">
            Un’escursione notturna con le racchette da neve è un’esperienza quasi mistica. Accompagnati dalle nostre guide, camminerete nel silenzio dei boschi innevati fino a raggiungere un rifugio dove vi attende una cena tipica valdostana.
        </p>
    </div>
</section>

<section class="bg-black pb-32 px-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
    <div class="bg-white/5 border border-white/10 p-12 fade-up-element">
         <Snowflake class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
         <h4 class="font-serif text-xl mb-4">Percorso Magico</h4>
         <p class="text-xs text-white/60 font-light leading-relaxed">Attraversiamo boschi di larici e radure silenziose sotto le stelle.</p>
    </div>
    <div class="bg-white/5 border border-white/10 p-12 fade-up-element">
         <Sparkles class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
         <h4 class="font-serif text-xl mb-4">Cena in Rifugio</h4>
         <p class="text-xs text-white/60 font-light leading-relaxed">Arrivo in baita per gustare polenta alla valdostana e piatti tipici.</p>
    </div>
    <div class="bg-white/5 border border-white/10 p-12 fade-up-element">
         <Map class="w-8 h-8 text-alpine-gold mx-auto mb-6" />
         <h4 class="font-serif text-xl mb-4">Escursione Guidata</h4>
         <p class="text-xs text-white/60 font-light leading-relaxed">Sempre accompagnati da professionisti della montagna in totale sicurezza.</p>
    </div>
</section>
