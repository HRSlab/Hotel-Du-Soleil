#!/usr/bin/env python3
"""Replace hardcoded Italian text in ciaspolate page with i18n $t() calls."""

with open('src/routes/esperienze/ciaspolate/+page.svelte', 'r') as f:
    c = f.read()

replacements = [
    # Experience section
    ("L\u2019Esperienza", "{$t('ciaspolate_page.experience_label')}"),
    ("Quando il Bosco <br/>si Addormenta", "{$t('ciaspolate_page.experience_title')}"),
    ("La partenza avviene al tramonto dall\u2019hotel. Le guide vi equipaggiano con racchette da neve, bastoncini e lampade frontali, poi si parte lungo sentieri battuti che si inoltrano nei boschi di larici secolari sopra Torgnon.", "{$t('ciaspolate_page.experience_text1')}"),
    ("Man mano che la luce del giorno svanisce, il paesaggio si trasforma: il silenzio diventa totale, la neve brilla sotto le stelle e ogni passo scricchiola nel bianco. Niente telefoni, niente fretta \u2014 solo il respiro e la montagna.", "{$t('ciaspolate_page.experience_text2')}"),
    (">Lampade frontali<", ">{$t('ciaspolate_page.experience_badge_lamps')}<"),
    (">Guide certificate<", ">{$t('ciaspolate_page.experience_badge_guides')}<"),

    # 3 Highlights
    (">Percorso Magico<", ">{$t('ciaspolate_page.highlight_trail_title')}<"),
    ("Attraversiamo boschi di larici e radure silenziose, con la neve fresca che attutisce ogni suono e le stelle come unica compagnia.", "{$t('ciaspolate_page.highlight_trail_text')}"),
    (">Cena in Rifugio</h4>", ">{$t('ciaspolate_page.highlight_dinner_title')}</h4>"),
    ("Arrivo in baita per gustare polenta concia alla valdostana, carbonada, Fontina DOP fusa e dolci della tradizione, accanto al camino.", "{$t('ciaspolate_page.highlight_dinner_text')}"),
    (">Rientro sotto le Stelle<", ">{$t('ciaspolate_page.highlight_return_title')}<"),
    ("Dopo la cena, il ritorno a piedi attraverso il bosco innevato \u00e8 il momento pi\u00f9 magico: il cielo di Torgnon, lontano dalle luci, rivela migliaia di stelle.", "{$t('ciaspolate_page.highlight_return_text')}"),

    # Stats
    (">Durata escursione<", ">{$t('ciaspolate_page.stats_duration')}<"),
    (">Dislivello massimo<", ">{$t('ciaspolate_page.stats_elevation')}<"),
    (">Stagione<", ">{$t('ciaspolate_page.stats_season')}<"),
    (">Partecipanti per gruppo<", ">{$t('ciaspolate_page.stats_group')}<"),

    # Trails section
    (">I Percorsi<", ">{$t('ciaspolate_page.trails_title')}<"),
    (">Tre itinerari per ogni livello di esperienza<", ">{$t('ciaspolate_page.trails_subtitle')}<"),
    (">Bosco dei Larici<", ">{$t('ciaspolate_page.trail_easy_name')}<"),
    (">Facile \u00b7 1,5h \u00b7 150m dislivello<", ">{$t('ciaspolate_page.trail_easy_level')}<"),
    ("L\u2019itinerario ideale per chi si avvicina per la prima volta alle ciaspolate. Un anello dolce attraverso il bosco di larici sopra Torgnon, con panorama finale sulla vallata. Adatto anche ai bambini dai 10 anni.", "{$t('ciaspolate_page.trail_easy_text')}"),
    (">Sentiero della Luna<", ">{$t('ciaspolate_page.trail_medium_name')}<"),
    (">Medio \u00b7 3h \u00b7 300m dislivello<", ">{$t('ciaspolate_page.trail_medium_level')}<"),
    ("Il percorso classico della ciaspolata notturna con cena in rifugio. Si sale attraverso radure e boschi fino alla baita, dove vi attende una cena completa. Il rientro sotto il cielo stellato \u00e8 indimenticabile.", "{$t('ciaspolate_page.trail_medium_text')}"),
    (">Cresta del Cervino<", ">{$t('ciaspolate_page.trail_hard_name')}<"),
    (">Impegnativo \u00b7 4h \u00b7 500m dislivello<", ">{$t('ciaspolate_page.trail_hard_level')}<"),
    ("Per escursionisti esperti. Un itinerario diurno che sale fino al belvedere con vista impareggiabile sul Cervino e la catena del Monte Rosa. Neve profonda, panorami sterminati, silenzio assoluto.", "{$t('ciaspolate_page.trail_hard_text')}"),

    # Dinner section
    (">Il Cuore dell\u2019Esperienza<", ">{$t('ciaspolate_page.dinner_label')}<"),
    ("La Cena <br/>in Rifugio", "{$t('ciaspolate_page.dinner_title')}"),
    ("Dopo un\u2019ora e mezza di cammino nella neve, arrivare in una baita calda e illuminata dal fuoco del camino \u00e8 un\u2019emozione che non si dimentica.\n            I rifugisti vi accolgono con un bombardino caldo \u2014 la tradizionale bevanda delle Alpi a base di zabaione e brandy \u2014 prima di servire una cena autentica.", "{$t('ciaspolate_page.dinner_text1')}"),
    ("Il men\u00f9 cambia con le stagioni ma segue sempre la tradizione valdostana: zuppa alla valpellinentze con fontina e verza, polenta concia con Fontina DOP fusa, carbonada con polenta, e per finire tegole e dolci alle castagne. Il tutto accompagnato da vini rossi della Valle d\u2019Aosta.", "{$t('ciaspolate_page.dinner_text2')}"),
    (">Men\u00f9 completo<", ">{$t('ciaspolate_page.dinner_badge_menu')}<"),
    (">Vini valdostani<", ">{$t('ciaspolate_page.dinner_badge_wine')}<"),

    # Daytime section
    (">Anche di Giorno<", ">{$t('ciaspolate_page.daytime_label')}<"),
    ("Ciaspolate <br/>Diurne", "{$t('ciaspolate_page.daytime_title')}"),
    ("Per chi preferisce la luce del sole o viaggia con bambini, organizziamo ciaspolate mattutine e pomeridiane lungo gli stessi sentieri incantati sopra Torgnon.\n                La vista diurna sulle vette \u00e8 spettacolare: il Cervino, il Gran Combin, la catena del Monte Rosa e tutta la valle che si apre ai vostri piedi.", "{$t('ciaspolate_page.daytime_text1')}"),
    ("Le escursioni diurne sono ideali anche per chi non ha mai provato le racchette da neve. I nostri accompagnatori adattano il ritmo e il percorso al gruppo, fermandosi per ammirare i panorami, osservare le tracce degli animali nel bosco e raccontare la storia del territorio.", "{$t('ciaspolate_page.daytime_text2')}"),
    (">Partenza ore 10:00<", ">{$t('ciaspolate_page.daytime_badge_departure')}<"),
    (">Adatto a famiglie<", ">{$t('ciaspolate_page.daytime_badge_families')}<"),

    # Includes section
    (">Cosa Include<", ">{$t('ciaspolate_page.includes_title')}<"),
    (">Tutto il necessario per un\u2019esperienza senza pensieri<", ">{$t('ciaspolate_page.includes_subtitle')}<"),
    (">Attrezzatura<", ">{$t('ciaspolate_page.includes_gear_title')}<"),
    ("Racchette da neve, bastoncini telescopici e lampade frontali fornite dall\u2019hotel. Voi portate solo scarponi caldi e voglia di avventura.", "{$t('ciaspolate_page.includes_gear_text')}"),
    (">Guida Alpina<", ">{$t('ciaspolate_page.includes_guide_title')}<"),
    ("Accompagnatore di media montagna certificato, con conoscenza perfetta dei sentieri e delle condizioni meteo e nivologiche del territorio.", "{$t('ciaspolate_page.includes_guide_text')}"),
    (">Cena Completa<", ">{$t('ciaspolate_page.includes_dinner_title')}<"),
    ("Inclusa nell\u2019escursione notturna: antipasto, primo, secondo, dolce e una bevanda. Piatti della tradizione valdostana preparati nel rifugio.", "{$t('ciaspolate_page.includes_dinner_text')}"),
    (">Flessibilit\u00e0<", ">{$t('ciaspolate_page.includes_flex_title')}<"),
    ("Partenza direttamente dall\u2019hotel. Escursioni programmate ogni mercoled\u00ec e sabato, o su richiesta per gruppi privati a partire da 4 persone.", "{$t('ciaspolate_page.includes_flex_text')}"),

    # Info section
    (">Informazioni Pratiche<", ">{$t('ciaspolate_page.info_title')}<"),
    ("Ciaspolata Notturna + Cena", "{$t('ciaspolate_page.info_night_title')}"),
    ("Ciaspolata Diurna\n                </h4>", "{$t('ciaspolate_page.info_day_title')}\n                </h4>"),
]

not_found = []
for old, new in replacements:
    if old in c:
        c = c.replace(old, new, 1)
    else:
        not_found.append(repr(old[:80]))

# Now replace the hardcoded bullet lists with {#each} loops
# Night info list
old_night_list = """<ul class="space-y-3 text-white/50 text-sm font-light">
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">\u2022</span> Partenza alle 17:30 dall\u2019hotel</li>
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">\u2022</span> Durata circa 3 ore (cena inclusa)</li>
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">\u2022</span> Difficolt\u00e0: facile/media</li>
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">\u2022</span> Et\u00e0 minima: 12 anni</li>
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">\u2022</span> Ogni mercoled\u00ec e sabato, Dic\u2013Mar</li>
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">\u2022</span> Min. 4 \u2014 Max. 15 partecipanti</li>
                </ul>"""

new_night_list = """<ul class="space-y-3 text-white/50 text-sm font-light">
                    {#each $t('ciaspolate_page.info_night_items') as item}
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">\u2022</span> {item}</li>
                    {/each}
                </ul>"""

if old_night_list in c:
    c = c.replace(old_night_list, new_night_list, 1)
else:
    not_found.append("Night list block")

# Day info list
old_day_list = """<ul class="space-y-3 text-white/50 text-sm font-light">
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">\u2022</span> Partenza alle 10:00 dall\u2019hotel</li>
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">\u2022</span> Durata 2\u20134 ore (a scelta)</li>
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">\u2022</span> Difficolt\u00e0: facile</li>
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">\u2022</span> Et\u00e0 minima: 8 anni</li>
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">\u2022</span> Su richiesta, tutti i giorni</li>
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">\u2022</span> Ideale per famiglie con bambini</li>
                </ul>"""

new_day_list = """<ul class="space-y-3 text-white/50 text-sm font-light">
                    {#each $t('ciaspolate_page.info_day_items') as item}
                    <li class="flex items-start gap-2"><span class="text-alpine-gold mt-1">\u2022</span> {item}</li>
                    {/each}
                </ul>"""

if old_day_list in c:
    c = c.replace(old_day_list, new_day_list, 1)
else:
    not_found.append("Day list block")

# Disclaimer
old_disclaimer = "Tutte le escursioni sono soggette a condizioni meteo e nivologiche favorevoli.\n                La reception \u00e8 a disposizione per informazioni, prenotazioni e per aiutarvi a scegliere il percorso pi\u00f9 adatto a voi."
new_disclaimer = "{$t('ciaspolate_page.info_disclaimer')}"
if old_disclaimer in c:
    c = c.replace(old_disclaimer, new_disclaimer, 1)
else:
    not_found.append("Disclaimer")

with open('src/routes/esperienze/ciaspolate/+page.svelte', 'w') as f:
    f.write(c)

if not_found:
    print(f"NOT FOUND ({len(not_found)}):")
    for nf in not_found:
        print(f"  - {nf}")
else:
    print("All replacements applied successfully!")
