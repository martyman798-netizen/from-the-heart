"""
Organisasjonsdata – dette er grunnlaget for API-et.
Scores og metadata kan oppdateres her manuelt,
eller automatisk via update_scores() (fremtidig funksjon).
"""

from datetime import date

LAST_UPDATED = str(date.today())

ORGANISATIONS = [
    {
        "id": 1, "name": "Røde Kors Norge", "emoji": "🔴", "category": "humanitaer", "rank": 1,
        "description": "Verdens største humanitære nettverk. Hjelper mennesker i krise – nasjonalt og internasjonalt.",
        "til_formal": 90, "admin": 4, "score": 88, "openness": "A", "innsamling": True,
        "verdict_type": "good",
        "verdict": "Svært godt. Over 90 % av midlene går til formålet og kun 4 % til administrasjon. Stor og veldokumentert effekt. Godkjent av Innsamlingskontrollen.",
        "url": "https://www.rodekors.no",
        "sources": [
            {"icon": "📄", "title": "Røde Kors Årsrapport 2023", "url": "https://www.rodekors.no/globalassets/_rapporter/_arsrapporter-rode-kors/2023_rk_arsrapport_no_versjon2.pdf"},
            {"icon": "✅", "title": "Innsamlingskontrollen", "url": "https://www.innsamlingskontrollen.no"},
            {"icon": "🏛️", "title": "Skatteetaten – gavefradragsliste", "url": "https://www.skatteetaten.no/person/skatt/hjelp-til-riktig-skatt/gave-og-arv/gave-til-frivillige-organisasjoner/liste/"}
        ]
    },
    {
        "id": 2, "name": "Flyktninghjelpen", "emoji": "🌍", "category": "humanitaer", "rank": 2,
        "description": "Beskytter rettighetene til flyktninger og internt fordrevne over hele verden.",
        "til_formal": 88, "admin": 5, "score": 84, "openness": "A", "innsamling": True,
        "verdict_type": "good",
        "verdict": "Meget bra. Ca. 88 % til formålet og høy åpenhet. En av Norges mest effektive internasjonale organisasjoner.",
        "url": "https://www.flyktninghjelpen.no",
        "sources": [
            {"icon": "📄", "title": "Flyktninghjelpen årsrapport", "url": "https://www.flyktninghjelpen.no/om-flyktninghjelpen/rapporter/"},
            {"icon": "✅", "title": "Innsamlingskontrollen", "url": "https://www.innsamlingskontrollen.no"}
        ]
    },
    {
        "id": 3, "name": "Norsk Folkehjelp", "emoji": "🤲", "category": "humanitaer", "rank": 3,
        "description": "Solidaritetsorganisasjon som driver humanitært arbeid og bistand globalt.",
        "til_formal": 82, "admin": 7, "score": 78, "openness": "B", "innsamling": True,
        "verdict_type": "good",
        "verdict": "Bra. 82 % til formålet. God åpenhet og veldokumentert arbeid med minerydding og nødhjelp.",
        "url": "https://www.folkehjelp.no",
        "sources": [
            {"icon": "📄", "title": "Norsk Folkehjelp årsrapport", "url": "https://www.folkehjelp.no/om-oss/rapporter/"},
            {"icon": "✅", "title": "Innsamlingskontrollen", "url": "https://www.innsamlingskontrollen.no"}
        ]
    },
    {
        "id": 4, "name": "Kirkens Nødhjelp", "emoji": "✝️", "category": "humanitaer", "rank": 4,
        "description": "Kristen hjelpeorganisasjon som bekjemper fattigdom og urettferdighet globalt.",
        "til_formal": 80, "admin": 8, "score": 75, "openness": "B", "innsamling": True,
        "verdict_type": "ok",
        "verdict": "OK. Rundt 80 % til formålet. Generelt solid og godkjent av Innsamlingskontrollen.",
        "url": "https://www.kirkensnodhjelp.no",
        "sources": [
            {"icon": "📄", "title": "Kirkens Nødhjelp årsrapport", "url": "https://www.kirkensnodhjelp.no/om-oss/styring-og-kontroll/"},
            {"icon": "✅", "title": "Innsamlingskontrollen", "url": "https://www.innsamlingskontrollen.no"}
        ]
    },
    {
        "id": 5, "name": "Amnesty International Norge", "emoji": "🕯️", "category": "humanitaer", "rank": 5,
        "description": "Forsvarer menneskerettigheter globalt gjennom kampanjer, forskning og aktivisme.",
        "til_formal": 72, "admin": 12, "score": 68, "openness": "B", "innsamling": True,
        "verdict_type": "ok",
        "verdict": "Moderat. Ca. 72 % til formålet. Mye av arbeidet er lobbyvirksomhet som er vanskelig å måle direkte.",
        "url": "https://www.amnesty.no",
        "sources": [
            {"icon": "📄", "title": "Amnesty Norge årsrapport", "url": "https://www.amnesty.no/om-amnesty/"},
            {"icon": "✅", "title": "Innsamlingskontrollen", "url": "https://www.innsamlingskontrollen.no"}
        ]
    },
    {
        "id": 6, "name": "CARE Norge", "emoji": "📦", "category": "humanitaer", "rank": 6,
        "description": "Bekjemper fattigdom og fremmer likestilling – særlig fokus på kvinner og jenter.",
        "til_formal": 76, "admin": 10, "score": 70, "openness": "B", "innsamling": True,
        "verdict_type": "ok",
        "verdict": "OK. 76 % til formålet. Seriøs og godkjent organisasjon.",
        "url": "https://www.care.no",
        "sources": [
            {"icon": "📄", "title": "CARE Norge årsrapport", "url": "https://www.care.no/om-care/"},
            {"icon": "✅", "title": "Innsamlingskontrollen", "url": "https://www.innsamlingskontrollen.no"}
        ]
    },
    {
        "id": 7, "name": "Strømmestiftelsen", "emoji": "💧", "category": "humanitaer", "rank": 7,
        "description": "Norsk utviklingsorganisasjon som arbeider med bærekraftig utvikling i fattige land.",
        "til_formal": 78, "admin": 9, "score": 72, "openness": "B", "innsamling": True,
        "verdict_type": "ok",
        "verdict": "OK. Ca. 78 % til formålet. Godkjent av Innsamlingskontrollen.",
        "url": "https://www.strommestiftelsen.no",
        "sources": [
            {"icon": "📄", "title": "Strømmestiftelsen årsrapport", "url": "https://www.strommestiftelsen.no/om-oss/"},
            {"icon": "✅", "title": "Innsamlingskontrollen", "url": "https://www.innsamlingskontrollen.no"}
        ]
    },
    {
        "id": 8, "name": "UNICEF Norge", "emoji": "🧒", "category": "barn", "rank": 1,
        "description": "Arbeider for barns rettigheter og velferd i over 190 land.",
        "til_formal": 87, "admin": 5, "score": 86, "openness": "A", "innsamling": True,
        "verdict_type": "good",
        "verdict": "Svært godt. 87 % til formålet. Sterk åpenhet og systematisk effektdokumentasjon.",
        "url": "https://www.unicef.no",
        "sources": [
            {"icon": "📄", "title": "UNICEF Norge årsrapport", "url": "https://www.unicef.no/om-unicef/arsrapport/"},
            {"icon": "✅", "title": "Innsamlingskontrollen", "url": "https://www.innsamlingskontrollen.no"},
            {"icon": "🔍", "title": "Gi Effektivt – toppliste", "url": "https://gieffektivt.no/topplista"}
        ]
    },
    {
        "id": 9, "name": "Redd Barna Norge", "emoji": "🤝", "category": "barn", "rank": 2,
        "description": "Kjemper for barns rettigheter og mot fattigdom, vold og diskriminering.",
        "til_formal": 83, "admin": 7, "score": 80, "openness": "A", "innsamling": True,
        "verdict_type": "good",
        "verdict": "Meget bra. Over 83 % til formålet og lave administrasjonskostnader. Anbefalt.",
        "url": "https://www.reddbarna.no",
        "sources": [
            {"icon": "📄", "title": "Redd Barna årsrapport", "url": "https://www.reddbarna.no/om-redd-barna/"},
            {"icon": "✅", "title": "Innsamlingskontrollen", "url": "https://www.innsamlingskontrollen.no"}
        ]
    },
    {
        "id": 10, "name": "SOS Barnebyer Norge", "emoji": "🏠", "category": "barn", "rank": 3,
        "description": "Gir foreldreløse og sårbare barn et trygt hjem og en meningsfull fremtid.",
        "til_formal": 79, "admin": 9, "score": 74, "openness": "B", "innsamling": True,
        "verdict_type": "ok",
        "verdict": "OK. Ca. 79 % til formålet. Noe kritikk for at fadderpenger ikke alltid øremerkes ett spesifikt barn.",
        "url": "https://www.sos-barnebyer.no",
        "sources": [
            {"icon": "📄", "title": "SOS Barnebyer årsrapport", "url": "https://www.sos-barnebyer.no/om-oss/"},
            {"icon": "✅", "title": "Innsamlingskontrollen", "url": "https://www.innsamlingskontrollen.no"}
        ]
    },
    {
        "id": 11, "name": "Plan International Norge", "emoji": "🌐", "category": "barn", "rank": 4,
        "description": "Kjemper for barns rettigheter og likestilling – særlig jenters rettigheter.",
        "til_formal": 77, "admin": 10, "score": 71, "openness": "B", "innsamling": True,
        "verdict_type": "ok",
        "verdict": "OK. Ca. 77 % til formålet. Innsamlingskostnadene er noe høye.",
        "url": "https://www.plan-norge.no",
        "sources": [
            {"icon": "📄", "title": "Plan International årsrapport", "url": "https://www.plan-norge.no/om-plan/"},
            {"icon": "✅", "title": "Innsamlingskontrollen", "url": "https://www.innsamlingskontrollen.no"}
        ]
    },
    {
        "id": 12, "name": "Norsk Luftambulanse", "emoji": "🚁", "category": "helse", "rank": 1,
        "description": "Driver luftambulanse og akuttmedisin for å redde liv i kritiske situasjoner.",
        "til_formal": 91, "admin": 3, "score": 90, "openness": "A", "innsamling": True,
        "verdict_type": "good",
        "verdict": "Topp. 91 % til formålet og kun 3 % administrasjon. Målbar effekt med dokumentert antall reddede liv.",
        "url": "https://www.norskluftambulanse.no",
        "sources": [
            {"icon": "📄", "title": "Norsk Luftambulanse årsrapport", "url": "https://www.norskluftambulanse.no/om-oss/"},
            {"icon": "✅", "title": "Innsamlingskontrollen", "url": "https://www.innsamlingskontrollen.no"},
            {"icon": "🏛️", "title": "Skatteetaten – gavefradragsliste", "url": "https://www.skatteetaten.no/person/skatt/hjelp-til-riktig-skatt/gave-og-arv/gave-til-frivillige-organisasjoner/liste/"}
        ]
    },
    {
        "id": 13, "name": "Leger Uten Grenser", "emoji": "⚕️", "category": "helse", "rank": 2,
        "description": "Gir medisinsk nødhjelp til ofre for konflikter, epidemier og naturkatastrofer.",
        "til_formal": 86, "admin": 5, "score": 85, "openness": "A", "innsamling": True,
        "verdict_type": "good",
        "verdict": "Svært godt. 86 % til formålet. Globalt anerkjent med høy åpenhet og uavhengighet.",
        "url": "https://www.legerutengrenser.no",
        "sources": [
            {"icon": "📄", "title": "Leger Uten Grenser årsrapport", "url": "https://www.legerutengrenser.no/om-oss/"},
            {"icon": "✅", "title": "Innsamlingskontrollen", "url": "https://www.innsamlingskontrollen.no"}
        ]
    },
    {
        "id": 14, "name": "Kreftforeningen", "emoji": "🎗️", "category": "helse", "rank": 3,
        "description": "Norges største frivillige kreftorganisasjon – forskning, støtte og forebygging.",
        "til_formal": 85, "admin": 6, "score": 83, "openness": "A", "innsamling": True,
        "verdict_type": "good",
        "verdict": "Svært godt. 85 % til formålet. Finansierer konkret forskning og pasientstøtte.",
        "url": "https://www.kreftforeningen.no",
        "sources": [
            {"icon": "📄", "title": "Kreftforeningen årsrapport", "url": "https://www.kreftforeningen.no/om-kreftforeningen/"},
            {"icon": "✅", "title": "Innsamlingskontrollen", "url": "https://www.innsamlingskontrollen.no"}
        ]
    },
    {
        "id": 15, "name": "Mental Helse", "emoji": "🧠", "category": "helse", "rank": 4,
        "description": "Arbeider for økt åpenhet om psykisk helse og bedre helsetilbud i Norge.",
        "til_formal": 74, "admin": 11, "score": 65, "openness": "B", "innsamling": False,
        "verdict_type": "ok",
        "verdict": "Moderat. Ca. 74 % til formålet. Viktig arbeid, men begrenset uavhengig effektdokumentasjon.",
        "url": "https://www.mentalhelse.no",
        "sources": [
            {"icon": "📄", "title": "Mental Helse årsrapport", "url": "https://www.mentalhelse.no/om-oss/"},
            {"icon": "🏛️", "title": "Skatteetaten – gavefradragsliste", "url": "https://www.skatteetaten.no/person/skatt/hjelp-til-riktig-skatt/gave-og-arv/gave-til-frivillige-organisasjoner/liste/"}
        ]
    },
    {
        "id": 16, "name": "Norges Naturvernforbund", "emoji": "🌿", "category": "miljoe", "rank": 1,
        "description": "Norges eldste natur- og miljøvernorganisasjon, grunnlagt i 1914.",
        "til_formal": 84, "admin": 7, "score": 80, "openness": "A", "innsamling": True,
        "verdict_type": "good",
        "verdict": "Meget bra. 84 % til formålet og god påvirkningshistorikk.",
        "url": "https://www.naturvernforbundet.no",
        "sources": [
            {"icon": "📄", "title": "Naturvernforbundet årsrapport", "url": "https://www.naturvernforbundet.no/om-oss/"},
            {"icon": "✅", "title": "Innsamlingskontrollen", "url": "https://www.innsamlingskontrollen.no"}
        ]
    },
    {
        "id": 17, "name": "WWF Norge", "emoji": "🐼", "category": "miljoe", "rank": 2,
        "description": "Jobber for å bevare naturmangfoldet og sikre en bærekraftig fremtid for planeten.",
        "til_formal": 82, "admin": 8, "score": 77, "openness": "A", "innsamling": True,
        "verdict_type": "good",
        "verdict": "Bra. 82 % til formålet og globalt nettverk med stor effekt.",
        "url": "https://www.wwf.no",
        "sources": [
            {"icon": "📄", "title": "WWF Norge årsrapport", "url": "https://www.wwf.no/om-wwf/"},
            {"icon": "✅", "title": "Innsamlingskontrollen", "url": "https://www.innsamlingskontrollen.no"}
        ]
    },
    {
        "id": 18, "name": "Bellona", "emoji": "☀️", "category": "miljoe", "rank": 3,
        "description": "Miljøstiftelse som jobber med klimaløsninger – særlig karbonfangst og ren energi.",
        "til_formal": 78, "admin": 10, "score": 72, "openness": "B", "innsamling": False,
        "verdict_type": "ok",
        "verdict": "Moderat. Finansieres delvis av næringslivet. Ikke godkjent av Innsamlingskontrollen.",
        "url": "https://www.bellona.no",
        "sources": [
            {"icon": "📄", "title": "Bellona årsrapport", "url": "https://www.bellona.no/om-bellona/"},
            {"icon": "⚠️", "title": "Ikke godkjent av Innsamlingskontrollen", "url": "https://www.innsamlingskontrollen.no"}
        ]
    },
    {
        "id": 19, "name": "Greenpeace Norge", "emoji": "🌊", "category": "miljoe", "rank": 4,
        "description": "Internasjonal miljøorganisasjon som bekjemper klimaendringer og miljøødeleggelser.",
        "til_formal": 76, "admin": 11, "score": 68, "openness": "B", "innsamling": False,
        "verdict_type": "ok",
        "verdict": "Moderat. Ikke med i Innsamlingskontrollen. Mye ressurser til kampanjer.",
        "url": "https://www.greenpeace.org/norway",
        "sources": [
            {"icon": "📄", "title": "Greenpeace International årsrapport", "url": "https://www.greenpeace.org/international/publication/"},
            {"icon": "⚠️", "title": "Ikke godkjent av Innsamlingskontrollen", "url": "https://www.innsamlingskontrollen.no"}
        ]
    },
    {
        "id": 20, "name": "Dyrebeskyttelsen Norge", "emoji": "🐾", "category": "dyr", "rank": 1,
        "description": "Norges eldste dyrevernorganisasjon – kjemper for alle dyrs rettigheter og velferd.",
        "til_formal": 81, "admin": 8, "score": 77, "openness": "B", "innsamling": True,
        "verdict_type": "good",
        "verdict": "Bra. 81 % til formålet. Godt dokumentert arbeid. Godkjent av Innsamlingskontrollen.",
        "url": "https://www.dyrebeskyttelsen.no",
        "sources": [
            {"icon": "📄", "title": "Dyrebeskyttelsen årsrapport", "url": "https://www.dyrebeskyttelsen.no/om-oss/"},
            {"icon": "✅", "title": "Innsamlingskontrollen", "url": "https://www.innsamlingskontrollen.no"}
        ]
    },
    {
        "id": 21, "name": "NOAH – for dyrs rettigheter", "emoji": "🐇", "category": "dyr", "rank": 2,
        "description": "Jobber aktivt mot dyremishandling og fremmer dyrs interesser juridisk og politisk.",
        "til_formal": 75, "admin": 12, "score": 65, "openness": "B", "innsamling": False,
        "verdict_type": "ok",
        "verdict": "Moderat. Ca. 75 % til formålet. Ikke del av Innsamlingskontrollen.",
        "url": "https://www.dyrsrettigheter.no",
        "sources": [
            {"icon": "📄", "title": "NOAH årsrapport", "url": "https://www.dyrsrettigheter.no/om-noah/"},
            {"icon": "⚠️", "title": "Ikke godkjent av Innsamlingskontrollen", "url": "https://www.innsamlingskontrollen.no"}
        ]
    },
    {
        "id": 22, "name": "Kirkens Bymisjon", "emoji": "❤️", "category": "sosial", "rank": 1,
        "description": "Hjelper marginaliserte og sårbare mennesker i norske byer med omsorg og fellesskap.",
        "til_formal": 85, "admin": 6, "score": 82, "openness": "A", "innsamling": True,
        "verdict_type": "good",
        "verdict": "Svært godt. 85 % til formålet. Tydelig og veldokumentert effekt. Høy tillit.",
        "url": "https://www.bymisjon.no",
        "sources": [
            {"icon": "📄", "title": "Kirkens Bymisjon årsrapport", "url": "https://www.bymisjon.no/om-oss/"},
            {"icon": "✅", "title": "Innsamlingskontrollen", "url": "https://www.innsamlingskontrollen.no"}
        ]
    },
    {
        "id": 23, "name": "Frelsesarmeen Norge", "emoji": "🎺", "category": "sosial", "rank": 2,
        "description": "Kristen hjelpeorganisasjon med fokus på fattigdomsbekjempelse og sosial rettferdighet.",
        "til_formal": 80, "admin": 9, "score": 74, "openness": "B", "innsamling": True,
        "verdict_type": "good",
        "verdict": "Bra. 80 % til formålet og god effektrapportering.",
        "url": "https://www.frelsesarmeen.no",
        "sources": [
            {"icon": "📄", "title": "Frelsesarmeen årsrapport", "url": "https://www.frelsesarmeen.no/om-oss/"},
            {"icon": "✅", "title": "Innsamlingskontrollen", "url": "https://www.innsamlingskontrollen.no"}
        ]
    },
    {
        "id": 24, "name": "Blå Kors Norge", "emoji": "💙", "category": "sosial", "rank": 3,
        "description": "Hjelper mennesker rammet av rusproblemer og avhengighet til et bedre liv.",
        "til_formal": 77, "admin": 10, "score": 70, "openness": "B", "innsamling": True,
        "verdict_type": "ok",
        "verdict": "OK. 77 % til formålet. Seriøs organisasjon med viktig formål.",
        "url": "https://www.blakors.no",
        "sources": [
            {"icon": "📄", "title": "Blå Kors årsrapport", "url": "https://www.blakors.no/om-oss/"},
            {"icon": "✅", "title": "Innsamlingskontrollen", "url": "https://www.innsamlingskontrollen.no"}
        ]
    },
]

CATEGORIES = [
    {"id": "humanitaer", "label": "Humanitær",  "emoji": "🌍"},
    {"id": "barn",       "label": "Barn",        "emoji": "🧒"},
    {"id": "helse",      "label": "Helse",       "emoji": "⚕️"},
    {"id": "miljoe",     "label": "Miljø",       "emoji": "🌿"},
    {"id": "dyr",        "label": "Dyr",         "emoji": "🐾"},
    {"id": "sosial",     "label": "Sosial",      "emoji": "❤️"},
]
