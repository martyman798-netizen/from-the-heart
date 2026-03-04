from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.data import ORGANISATIONS, CATEGORIES, LAST_UPDATED

router = APIRouter(prefix="/api", tags=["organisasjoner"])


@router.get("/organisations")
def get_organisations(
    category: Optional[str] = Query(None, description="Filtrer på kategori"),
    search:   Optional[str] = Query(None, description="Søk i navn og beskrivelse"),
    sort:     Optional[str] = Query("score", description="Sorter på: score, rank, name")
):
    results = list(ORGANISATIONS)

    if category and category != "alle":
        results = [o for o in results if o["category"] == category]

    if search:
        q = search.lower()
        results = [o for o in results if q in o["name"].lower() or q in o["description"].lower()]

    if sort == "rank":
        results.sort(key=lambda o: (o.get("rank") or 99))
    elif sort == "name":
        results.sort(key=lambda o: o["name"])
    else:
        results.sort(key=lambda o: -(o.get("score") or 0))

    return {
        "count": len(results),
        "last_updated": LAST_UPDATED,
        "organisations": results
    }


@router.get("/organisations/{org_id}")
def get_organisation(org_id: int):
    for org in ORGANISATIONS:
        if org["id"] == org_id:
            return org
    raise HTTPException(status_code=404, detail="Organisasjon ikke funnet")


@router.get("/categories")
def get_categories():
    cats = []
    for c in CATEGORIES:
        count = sum(1 for o in ORGANISATIONS if o["category"] == c["id"])
        cats.append({**c, "count": count})
    return {"categories": cats, "total": len(ORGANISATIONS)}


@router.get("/stats")
def get_stats():
    scores  = [o["score"] for o in ORGANISATIONS if o["score"]]
    formals = [o["til_formal"] for o in ORGANISATIONS if o["til_formal"]]
    return {
        "total_organisations": len(ORGANISATIONS),
        "innsamling_approved": sum(1 for o in ORGANISATIONS if o["innsamling"]),
        "avg_score": round(sum(scores) / len(scores), 1) if scores else 0,
        "avg_til_formal": round(sum(formals) / len(formals), 1) if formals else 0,
        "last_updated": LAST_UPDATED
    }
