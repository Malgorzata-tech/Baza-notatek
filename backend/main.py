# Prosty backend do przechowywania i wyszukiwania dokumentów
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import sqlite3
import os

app = FastAPI()

# CORS (ważne dla Reacta)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_PATH = os.path.join(os.path.dirname(__file__), "data.db")


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
        """)
    conn.commit()
    conn.close()


@app.on_event("startup")
def startup_event():
    init_db()


@app.get("/")
def read_root():
    return {"message": "Backend działa"}


@app.get("/hello")
def hello():
    return {"message": "Hello z FastAPI"}


class DocumentIn(BaseModel):
    title: str
    content: str


class DocumentOut(DocumentIn):
    id: int




@app.post(
    "/documents", response_model=DocumentOut
)  # endpoint do tworzenia dokumentów, z walidacją i usuwaniem białych znaków
def create_document(doc: DocumentIn):
    # Prosta walidacja — blokuje puste lub białe znaki
    if not doc.title or not doc.title.strip():  #
        raise HTTPException(status_code=400, detail="Tytuł nie może być pusty")
    if not doc.content or not doc.content.strip():
        raise HTTPException(status_code=400, detail="Treść nie może być pusta")

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO documents (title, content) VALUES (?, ?)",
        (
            doc.title.strip(),
            doc.content.strip(),
        ),  # usuwam białe znaki z tytułu i treści
    )
    conn.commit()
    doc_id = cur.lastrowid  # pobieram ID nowo dodanego dokumentu
    conn.close()
    return {"id": doc_id, "title": doc.title.strip(), "content": doc.content.strip()}


@app.get(
    "/documents", response_model=List[DocumentOut]
)  # zwracam listę dokumentów, posortowaną od najnowszych do najstarszych
def list_documents():
    conn = sqlite3.connect(DB_PATH)  # łącze się z bazą danych
    cur = conn.cursor()  # tworze kursor do wykonywania zapytań SQL
    cur.execute("SELECT id, title, content FROM documents ORDER BY id DESC")
    rows = (
        cur.fetchall()
    )  # pobieramy wszystkie dokumenty, posortowane od najnowszych do najstarszych
    conn.close()
    return [{"id": r[0], "title": r[1], "content": r[2]} for r in rows]


@app.get(
    "/search", response_model=List[DocumentOut]
)  # endpoint do wyszukiwania dokumentów po tytule lub treści, z obsługą wielkości liter
def search(q: str = ""):
    q_like = (
        f"%{q}%"  # przygotowujemy wzorzec do wyszukiwania, z obsługą wielkości liter
    )
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "SELECT id, title, content FROM documents WHERE title LIKE ? COLLATE NOCASE OR content LIKE ? COLLATE NOCASE ORDER BY id DESC",
        (
            q_like,
            q_like,
        ),  # wyszukujemy dokumenty, gdzie tytuł lub treść zawiera zapytanie, z obsługą wielkości liter
    )
    rows = cur.fetchall()
    conn.close()
    return [{"id": r[0], "title": r[1], "content": r[2]} for r in rows]


@app.delete("/documents")
def delete_documents(q: str = ""):
    # Usuwa dokumenty, których tytuł lub treść pasuje do zapytania LIKE
    if not q or not q.strip():
        raise HTTPException(status_code=400, detail="Parametr q jest wymagany do usunięcia dokumentów")

    q_like = f"%{q}%"
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM documents WHERE title LIKE ? COLLATE NOCASE OR content LIKE ? COLLATE NOCASE",
        (q_like, q_like),
    )
    deleted = cur.rowcount
    conn.commit()
    conn.close()
    return {"deleted": deleted}
