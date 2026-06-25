import os
import shutil
import sqlite3
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "data.db")

def backup_db(path):
    if not os.path.exists(path):
        print("Brak pliku bazy danych do backupu.")
        return None
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = path + f".bak_{ts}"
    shutil.copy2(path, dest)
    print(f"Utworzono kopię zapasową: {dest}")
    return dest


def recreate_empty_db(path):
    if os.path.exists(path):
        try:
            os.remove(path)
            print(f"Usunięto plik: {path}")
        except Exception as e:
            print(f"Nie można usunąć pliku {path}: {e}")
            return False

    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print(f"Utworzono pustą bazę: {path}")
    return True


if __name__ == '__main__':
    print("Backup i czyszczenie bazy danych backend/data.db")
    backup_db(DB_PATH)
    ok = recreate_empty_db(DB_PATH)
    if ok:
        print("Baza została wyczyszczona.")
    else:
        print("Wystąpił błąd podczas czyszczenia bazy.")
