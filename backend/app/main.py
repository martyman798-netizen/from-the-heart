from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.orgs import router as orgs_router

app = FastAPI(
    title="From the Heart API",
    description="API for norske veldedighetsorganisasjoner med rangeringer og åpenhetsvurderinger.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Bytt til din frontend-URL i produksjon
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(orgs_router)


@app.get("/")
def root():
    return {
        "app": "From the Heart API",
        "docs": "/docs",
        "endpoints": {
            "alle_organisasjoner": "/api/organisations",
            "kategorier": "/api/categories",
            "statistikk": "/api/stats",
            "én_organisasjon": "/api/organisations/{id}"
        }
    }
