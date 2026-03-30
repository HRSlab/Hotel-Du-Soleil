#!/usr/bin/env python3
"""Replace hardcoded Italian text in yoga page with i18n $t() calls."""

with open('src/routes/esperienze/yoga/+page.svelte', 'r') as f:
    c = f.read()

# Add import
c = c.replace(
    "import { Flower, Wind, Sparkles, Sun, Moon, Mountain, Clock, Users, ShieldCheck, Star, Heart, ArrowRight, Sunrise, CloudSun, TreePine, Leaf } from 'lucide-svelte';",
    "import { Flower, Wind, Sparkles, Sun, Moon, Mountain, Clock, Users, ShieldCheck, Star, Heart, ArrowRight, Sunrise, CloudSun, TreePine, Leaf } from 'lucide-svelte';\n    import { t } from '$lib/i18n';",
    1
)

replacements = [
    # Head
    (">Yoga in Quota | Chalet Du Soleil<", ">{$t('yoga_page.meta_title')}<"),
    ('content="Yoga in quota a Torgnon, Valle d\u2019Aosta. Sessioni all\u2019alba e al tramonto a 1.500 metri, meditazione alpina, pranayama e retreats settimanali con vista sul Cervino."', "content={$t('yoga_page.meta_description')}"),

    # Hero
    ("Equilibrio Interiore \u00b7 1.500m", "{$t('yoga_page.hero_label')}"),
    (">Yoga in Quota<", ">{$t('yoga_page.hero_title')}<"),
    ("Dove il respiro incontra l\u2019aria sottile delle Alpi", "{$t('yoga_page.hero_subtitle')}"),

    # Intro
    ("Il respiro si fonde con l\u2019aria sottile dei 1.500 metri.", "{$t('yoga_page.intro_title')}"),
    ("Lo yoga in montagna \u00e8 un\u2019esperienza che va oltre la pratica. \n            A 1.500 metri, l\u2019aria \u00e8 pi\u00f9 pura, i suoni della natura sostituiscono il rumore della citt\u00e0 \n            e il corpo risponde con una profondit\u00e0 diversa. Le nostre sessioni si svolgono \n            all\u2019alba e al tramonto, nella cornice delle Alpi valdostane, \n            dove ogni posizione diventa un dialogo tra te e la montagna.", "{$t('yoga_page.intro_text')}"),

    # Experience
    (">L\u2019Esperienza<", ">{$t('yoga_page.experience_label')}<"),
    ("Pratica tra<br/>Cielo e Terra", "{$t('yoga_page.experience_title')}"),
    ("Le nostre sessioni si tengono sulla terrazza panoramica dell\u2019hotel, affacciata \n            sulla valle e sulle vette del Cervino. In estate, quando il tempo lo permette, \n            ci spostiamo nel prato alpino adiacente, dove l\u2019erba diventa il tuo tappetino \n            e il cielo il tuo soffitto.", "{$t('yoga_page.experience_text1')}"),
    ("La nostra insegnante certificata adatta ogni lezione al gruppo presente: \n            dal principiante assoluto al praticante avanzato. \n            Non serve esperienza, solo la voglia di fermarsi e ascoltarsi.", "{$t('yoga_page.experience_text2')}"),
    (">Tutti i livelli<", ">{$t('yoga_page.experience_badge_levels')}<"),
    (">Vista Cervino<", ">{$t('yoga_page.experience_badge_view')}<"),

    # Stats
    (">Di altitudine<", ">{$t('yoga_page.stats_altitude')}<"),
    (">Per sessione<", ">{$t('yoga_page.stats_session')}<"),
    (">Giorni a settimana<", ">{$t('yoga_page.stats_days')}<"),
    (">Posti per sessione<", ">{$t('yoga_page.stats_places')}<"),

    # Sessions title
    (">Le Sessioni<", ">{$t('yoga_page.sessions_title')}<"),
    (">Tre momenti, tre energie diverse<", ">{$t('yoga_page.sessions_subtitle')}<"),

    # Dawn session
    (">Ore 07:00<", ">{$t('yoga_page.session_dawn_time')}<"),
    (">Saluto al Sole</h4>", ">{$t('yoga_page.session_dawn_name')}</h4>"),
    (">Hatha Yoga \u00b7 60 min<", ">{$t('yoga_page.session_dawn_type')}<"),
    ("Risveglia il corpo con una sequenza dolce e fluida mentre il sole \n                        illumina le vette. Posizioni classiche, respirazione consapevole \n                        e un\u2019energia che ti accompagner\u00e0 per tutta la giornata.", "{$t('yoga_page.session_dawn_text')}"),

    # Afternoon session
    (">Ore 15:00<", ">{$t('yoga_page.session_afternoon_time')}<"),
    (">Pranayama Alpino</h4>", ">{$t('yoga_page.session_afternoon_name')}</h4>"),
    (">Breathwork \u00b7 60 min<", ">{$t('yoga_page.session_afternoon_type')}<"),
    ("Tecniche di respirazione avanzate nell\u2019aria pura d\u2019alta quota. \n                        L\u2019ossigeno rarefatto amplifica ogni respiro, portando \n                        una chiarezza mentale che in pianura \u00e8 difficile raggiungere.", "{$t('yoga_page.session_afternoon_text')}"),

    # Sunset session
    (">Ore 18:30<", ">{$t('yoga_page.session_sunset_time')}<"),
    (">Meditazione al Tramonto</h4>", ">{$t('yoga_page.session_sunset_name')}</h4>"),
    (">Yin Yoga & Meditazione \u00b7 60 min<", ">{$t('yoga_page.session_sunset_type')}<"),
    ("Posizioni tenute a lungo, rilascio profondo delle tensioni \n                        e meditazione guidata mentre il sole tinge le vette di rosa. \n                        Il modo perfetto per chiudere la giornata e prepararsi a una notte di sonno ristoratore.", "{$t('yoga_page.session_sunset_text')}"),

    # Retreat
    (">Immersione Totale<", ">{$t('yoga_page.retreat_label')}<"),
    ("Retreat<br/>Settimanale", "{$t('yoga_page.retreat_title')}"),
    ("Per chi desidera un\u2019esperienza pi\u00f9 profonda, organizziamo retreats settimanali \n            che combinano yoga, meditazione, escursioni consapevoli e alimentazione naturale. \n            Sette giorni per disconnettersi completamente e ritrovare l\u2019equilibrio.", "{$t('yoga_page.retreat_text')}"),
    (">7 giorni<", ">{$t('yoga_page.retreat_badge_days')}<"),
    (">Max 8 persone<", ">{$t('yoga_page.retreat_badge_places')}<"),

    # Benefits
    (">Perch\u00e9 Yoga in Montagna<", ">{$t('yoga_page.benefits_title')}<"),
    (">I benefici dell\u2019alta quota sulla pratica<", ">{$t('yoga_page.benefits_subtitle')}<"),
    (">Aria Purissima<", ">{$t('yoga_page.benefit_air_title')}<"),
    ("L\u2019aria d\u2019alta quota \u00e8 priva di inquinamento. Ogni respiro \u00e8 pi\u00f9 profondo e consapevole.", "{$t('yoga_page.benefit_air_text')}"),
    (">Silenzio Totale<", ">{$t('yoga_page.benefit_silence_title')}<"),
    ("Nessun rumore urbano. Solo il vento, gli uccelli e il tuo respiro. La meditazione diventa naturale.", "{$t('yoga_page.benefit_silence_text')}"),
    (">Connessione Naturale<", ">{$t('yoga_page.benefit_nature_title')}<"),
    ("Praticare circondati dalla natura amplifica la sensazione di radicamento e presenza.", "{$t('yoga_page.benefit_nature_text')}"),
    (">Recupero Muscolare<", ">{$t('yoga_page.benefit_recovery_title')}<"),
    ("Dopo una giornata di sci o trekking, lo yoga rilascia le tensioni e accelera il recupero.", "{$t('yoga_page.benefit_recovery_text')}"),

    # Teacher
    (">La Tua Guida<", ">{$t('yoga_page.teacher_title')}<"),
    (">Professionalit\u00e0 e passione<", ">{$t('yoga_page.teacher_subtitle')}<"),
    ("\u201cLa montagna ti insegna ci\u00f2 che nessun maestro pu\u00f2: \n                    che sei piccolo, che sei forte, e che il silenzio \n                    \u00e8 il suono pi\u00f9 potente che esista.\u201d", "{$t('yoga_page.teacher_quote')}"),
    ("La nostra insegnante \u00e8 certificata Yoga Alliance RYT-500 con specializzazione \n                    in yoga di montagna e meditazione mindfulness. Anni di pratica nelle Alpi \n                    le hanno insegnato ad adattare ogni sessione all\u2019altitudine, al clima \n                    e all\u2019energia del gruppo. Ogni lezione \u00e8 unica, proprio come ogni giornata in montagna.", "{$t('yoga_page.teacher_text')}"),

    # Info section
    (">Info Pratiche</h2>", ">{$t('yoga_page.info_title')}</h2>"),
    (">Tutto quello che devi sapere<", ">{$t('yoga_page.info_subtitle')}<"),
    ("Orari & Sessioni", "{$t('yoga_page.info_schedule_title')}"),
    ("<span>Saluto al Sole</span>", "<span>{$t('yoga_page.info_schedule_sun')}</span>"),
    ("<span>Pranayama Alpino</span>", "<span>{$t('yoga_page.info_schedule_pranayama')}</span>"),
    ("<span>Meditazione al Tramonto</span>", "<span>{$t('yoga_page.info_schedule_sunset')}</span>"),
    ("<span>Disponibilit\u00e0</span>", "<span>{$t('yoga_page.info_schedule_availability')}</span>"),
    (">Tutti i giorni<", ">{$t('yoga_page.info_schedule_everyday')}<"),
    ("Da Sapere", "{$t('yoga_page.info_know_title')}"),
    ("<span>Livello richiesto</span>", "<span>{$t('yoga_page.info_level')}</span>"),
    (">Nessuno<", ">{$t('yoga_page.info_level_value')}<"),
    ("<span>Tappetino</span>", "<span>{$t('yoga_page.info_mat')}</span>"),
    (">Fornito dall\u2019hotel<", ">{$t('yoga_page.info_mat_value')}<"),
    ("<span>Prenotazione</span>", "<span>{$t('yoga_page.info_booking')}</span>"),
    (">Alla reception (entro sera prima)<", ">{$t('yoga_page.info_booking_value')}<"),
    ("<span>Costo</span>", "<span>{$t('yoga_page.info_cost')}</span>"),
    (">Incluso nel soggiorno<", ">{$t('yoga_page.info_cost_value')}<"),

    # CTA
    (">Trova il Tuo Equilibrio<", ">{$t('yoga_page.cta_title')}<"),
    ("L\u2019aria sottile, il silenzio delle vette, il primo raggio di sole sulle Alpi. \n                Non \u00e8 solo yoga, \u00e8 un\u2019esperienza che ti cambia.", "{$t('yoga_page.cta_text')}"),
    ("Scopri il Wellness", "{$t('yoga_page.cta_wellness')}"),
    ("Massaggi Post-Yoga", "{$t('yoga_page.cta_massage')}"),
]

# Replace retreat items list
old_retreat_list = """<li class="flex items-start gap-3"><Star class="w-3.5 h-3.5 text-alpine-gold shrink-0 mt-0.5" /> 2 sessioni yoga al giorno (alba + tramonto)</li>
            <li class="flex items-start gap-3"><Star class="w-3.5 h-3.5 text-alpine-gold shrink-0 mt-0.5" /> Meditazione guidata quotidiana</li>
            <li class="flex items-start gap-3"><Star class="w-3.5 h-3.5 text-alpine-gold shrink-0 mt-0.5" /> Mindful hiking nei boschi di larici</li>
            <li class="flex items-start gap-3"><Star class="w-3.5 h-3.5 text-alpine-gold shrink-0 mt-0.5" /> Men\u00f9 vegetariano a km 0</li>
            <li class="flex items-start gap-3"><Star class="w-3.5 h-3.5 text-alpine-gold shrink-0 mt-0.5" /> 1 trattamento spa incluso</li>
            <li class="flex items-start gap-3"><Star class="w-3.5 h-3.5 text-alpine-gold shrink-0 mt-0.5" /> Digital detox (volontario)</li>"""

new_retreat_list = """{#each $t('yoga_page.retreat_items') as item}
            <li class="flex items-start gap-3"><Star class="w-3.5 h-3.5 text-alpine-gold shrink-0 mt-0.5" /> {item}</li>
            {/each}"""

not_found = []
for old, new in replacements:
    if old in c:
        c = c.replace(old, new, 1)
    else:
        not_found.append(repr(old[:80]))

if old_retreat_list in c:
    c = c.replace(old_retreat_list, new_retreat_list, 1)
else:
    not_found.append("Retreat items list")

with open('src/routes/esperienze/yoga/+page.svelte', 'w') as f:
    f.write(c)

if not_found:
    print(f"NOT FOUND ({len(not_found)}):")
    for nf in not_found:
        print(f"  - {nf}")
else:
    print("All replacements applied successfully!")
