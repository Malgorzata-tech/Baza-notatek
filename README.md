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




Uruchomienie projektu za pomocą Dockera
------------------
Wymagania
- Docker
- Docker Compose

Sprawdź:
- docker --version
- docker compose version

Uruchomienie projektu
W głównym folderze projektu (tam gdzie docker-compose.yml) uruchom:    docker compose up --build

Dostęp do aplikacji - Po uruchomieniu wejdź na strony:
Frontend (React + Vite)    http://localhost:3000
Sprawdzenie działania Backendu (FastAPI)    http://localhost:8000
Dokumentacja API (Swagger)    http://localhost:8000/docs


Zatrzymanie aplikacji:    docker compose down

Reset (opcjonalnie) - Jeśli chcesz usunąć wszystkie kontenery i cache:
   docker compose down --volumes --rmi all



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


