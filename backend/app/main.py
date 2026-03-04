from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from supabase import create_client, Client
from pydantic import BaseModel
from typing import Optional, List
import os
import secrets

app = FastAPI(title="From the Heart API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "changeme")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
security = HTTPBasic()

def verify_admin(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, ADMIN_USERNAME)
    correct_password = secrets.compare_digest(credentials.password, ADMIN_PASSWORD)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Feil brukernavn eller passord",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

class OrgCreate(BaseModel):
    id: int
    name: str
    emoji: Optional[str] = ""
    category: str
    rank: int
    description: Optional[str] = ""
    til_formal: int
    admin: int
    score: int
    openness: str
    innsamling: bool
    verdict_type: str
    verdict: Optional[str] = ""
    url: Optional[str] = ""
    sources: Optional[list] = []

@app.get("/")
def root():
    return {"status": "ok", "message": "From the Heart API"}

@app.get("/api/organisations")
def get_organisations():
    result = supabase.table("organisations").select("*").order("score", desc=True).execute()
    return result.data

@app.get("/api/organisations/{org_id}")
def get_organisation(org_id: int):
    result = supabase.table("organisations").select("*").eq("id", org_id).execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="Ikke funnet")
    return result.data[0]

@app.get("/api/categories")
def get_categories():
    return [
        {"id": "humanitaer", "label": "Humanitær", "emoji": "🌍"},
        {"id": "barn", "label": "Barn", "emoji": "🧒"},
        {"id": "helse", "label": "Helse", "emoji": "⚕️"},
        {"id": "miljoe", "label": "Miljø", "emoji": "🌿"},
        {"id": "dyr", "label": "Dyr", "emoji": "🐾"},
        {"id": "sosial", "label": "Sosial", "emoji": "❤️"},
    ]

# --- ADMIN ENDPOINTS ---

@app.post("/api/admin/organisations", dependencies=[Depends(verify_admin)])
def create_organisation(org: OrgCreate):
    result = supabase.table("organisations").insert(org.dict()).execute()
    return result.data[0]

@app.put("/api/admin/organisations/{org_id}", dependencies=[Depends(verify_admin)])
def update_organisation(org_id: int, org: OrgCreate):
    result = supabase.table("organisations").update(org.dict()).eq("id", org_id).execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="Ikke funnet")
    return result.data[0]

@app.delete("/api/admin/organisations/{org_id}", dependencies=[Depends(verify_admin)])
def delete_organisation(org_id: int, _=Depends(verify_admin)):
    result = supabase.table("organisations").delete().eq("id", org_id).execute()
    return {"message": "Slettet"}
