# ❤️ From the Heart – Veldedighet Norge

En åpen og uavhengig oversikt over norske veldedighetsorganisasjoner med rangeringer basert på åpenhet, administrasjonskostnader og andel til formål.

## Prosjektstruktur

```
from-the-heart/
├── backend/          # FastAPI Python-backend
│   ├── app/
│   │   ├── main.py           # App-inngangspunkt
│   │   ├── data.py           # Organisasjonsdata
│   │   └── routers/
│   │       └── orgs.py       # API-ruter for organisasjoner
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/         # Statisk HTML/CSS/JS frontend
│   ├── public/
│   │   └── index.html        # Nettsiden
│   └── src/
│       └── app.js            # Frontend-logikk
├── .gitignore
└── README.md
```

## Kom i gang lokalt

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```
API kjører på: http://localhost:8000
Dokumentasjon: http://localhost:8000/docs

### Frontend
Åpne `frontend/public/index.html` direkte i nettleseren,
eller kjør en lokal server:
```bash
cd frontend/public
python -m http.server 3000
```

## Deployment
- **Backend:** Railway eller Render (gratis tier)
- **Frontend:** Vercel eller Netlify (gratis)

## Datakilder
- [Innsamlingskontrollen](https://www.innsamlingskontrollen.no)
- [Gi Effektivt](https://gieffektivt.no)
- [Skatteetaten – gavefradragsliste](https://www.skatteetaten.no/person/skatt/hjelp-til-riktig-skatt/gave-og-arv/gave-til-frivillige-organisasjoner/liste/)
- Organisasjonenes egne årsrapporter
