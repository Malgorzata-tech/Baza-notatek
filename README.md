Baza dokumentów i notatek
==============

Krótki opis
----------
Prosta aplikacja webowa do gromadzenia i wyszukiwania krótkich dokumentów tekstowych lub notatek. 
Składa się z backendu (FastAPI + SQLite) oraz frontendowego interfejsu (React + Vite).

Aplikacja służy do zapisywania dokumentów (tytuł + treść), wyszukiwania ich lub też usuwania. 
Ma prosty, responsywny interfejs użytkownika i lokalną bazę danych.


Jak go uruchomić?
------------------
Wymagania:
- Python 3.8+
- Node.js + npm (dla frontendu)

Backend (PowerShell):
1. Wejdź do katalogu projektu.
2. Zainstaluj zależności:
   pip install -r backend/requirements.txt
3. Uruchom serwer deweloperski:
   uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000

Frontend (PowerShell):
1. Przejdź do folderu frontend (ważne aby wejść najpierw w folder /frontend):
   cd frontend
2. Zainstaluj zależności i uruchom deweloperski server Vite:
   npm install
   npm run dev
3. Otwórz przeglądarkę pod adresem podanym przez Vite (domyślnie http://localhost:3000)


--------------------------------------------------------------

Plik bazy danych
----------------
- Baza SQLite znajduje się w backend/data.db i jest tworzona automatycznie przy pierwszym uruchomieniu backendu.
- Aby wykonać backup i wyczyścić bazę, można uruchomić skrypt:
  python .\backend\clear_db.py

Jakie technologie wykorzystuje?
-------------------------------
- Backend: Python, FastAPI, SQLite (sqlite3), uvicorn
- Frontend: React, Vite, vanilla CSS
- Narzędzia developerskie: npm, pip

Jakie funkcje już działają?
---------------------------
- Backend:
  - GET /hello — testowy endpoint
  - POST /documents — dodawanie dokumentu (walidacja pustego tytułu/treści)
  - GET /documents — lista dokumentów
  - GET /search?q=... — wyszukiwanie dokumentów po tytule/treści (LIKE, case-insensitive)
  - DELETE /documents?q=... — usuwanie dokumentów pasujących do zapytania (LIKE)

- Frontend:
  - Responsywny UI z formularzem dodawania dokumentu
  - Pole wyszukiwania i lista wyników
  - Przycisk „Usuń wyniki wyszukiwania" wywołujący DELETE do backendu
  - Stylizacja CSS dla profesjonalnego wyglądu


