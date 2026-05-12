# Angewandte Programmierung

Dieses Repository enthaelt mein Projekt und meine Uebungen aus dem Modul **Angewandte Programmierung**. Der Schwerpunkt liegt auf einer Notes-API mit FastAPI, einer SQLite-Datenbank mit SQLModel, automatischen Tests mit pytest und einer kleinen Streamlit-Oberflaeche.

## Projektueberblick

Die Anwendung besteht aus mehreren Teilen:

- `main.py`: Hauptanwendung mit FastAPI und allen Notes-Endpunkten
- `database.py`: Datenbankmodelle mit SQLModel und SQLite-Verbindung
- `frontend.py`: Streamlit-App fuer die Notes-API
- `notes.db`: SQLite-Datenbank fuer gespeicherte Notizen
- `data/notes.json`: alte JSON-Daten, die in die Datenbank migriert werden koennen
- `checks/`: Testdateien fuer die API und einzelne Aufgaben
- `exploration/`: Beispiele und kleinere Uebungsdateien, zum Beispiel Day-4-Code und Decorator-Beispiele
- `presentations/`: Unterlagen und Notizen zu den einzelnen Kurstagen
- `work-log.md`: persoenliches Worklog zum Projektfortschritt

## Technologien

- Python
- FastAPI
- SQLModel
- SQLite
- Pydantic
- pytest
- requests
- Streamlit
- uv

## Funktionen der API

Die Hauptanwendung in `main.py` bietet unter anderem:

- einfache Day-1-Endpunkte wie `/`, `/name/{name}` und `/summe/{zahl1}/{zahl2}`
- Notizen erstellen, anzeigen, bearbeiten und loeschen
- Filter fuer Notizen nach Kategorie, Suchbegriff, Tag und Erstellungsdatum
- Statistik-Endpunkt fuer Anzahl der Notizen, Kategorien und haeufige Tags
- eigene Endpunkte fuer Kategorien und Tags
- Pydantic-Validierung fuer Eingabedaten
- Speicherung in `notes.db`

## Wichtige API-Endpunkte

| Methode | Endpunkt | Beschreibung |
| --- | --- | --- |
| `GET` | `/` | einfache Hello-World-Antwort |
| `GET` | `/name/{name}` | begruesst einen Namen |
| `GET` | `/summe/{zahl1}/{zahl2}` | addiert zwei Zahlen |
| `GET` | `/notes` | listet alle Notizen, optional mit Filtern |
| `POST` | `/notes` | erstellt eine neue Notiz |
| `GET` | `/notes/{note_id}` | zeigt eine bestimmte Notiz |
| `PUT` | `/notes/{note_id}` | ersetzt eine Notiz vollstaendig |
| `PATCH` | `/notes/{note_id}` | aktualisiert einzelne Felder einer Notiz |
| `DELETE` | `/notes/{note_id}` | loescht eine Notiz |
| `GET` | `/notes/stats` | zeigt Statistiken zu Notizen |
| `GET` | `/categories` | listet alle Kategorien |
| `GET` | `/categories/{category_name}/notes` | zeigt Notizen einer Kategorie |
| `GET` | `/tags` | listet alle Tags |
| `GET` | `/tags/{tag_name}/notes` | zeigt Notizen mit einem bestimmten Tag |

## Validierung

Neue Notizen werden durch Pydantic geprueft. Dabei gelten unter anderem diese Regeln:

- `title`: 3 bis 100 Zeichen
- `content`: 1 bis 10.000 Zeichen
- `category`: nur `work`, `personal`, `school`, `ideas`, `general`
- `tags`: maximal 10 Tags
- Tags werden bereinigt, kleingeschrieben und doppelte Tags werden entfernt
- ungueltige Felder werden abgelehnt

## Streamlit-Frontend

Die Datei `frontend.py` enthaelt eine kleine Streamlit-App. Sie kann:

- alle Notizen aus der API laden
- Notiztitel in einer Liste anzeigen
- Details einer ausgewaehlten Notiz anzeigen
- neue Notizen per Formular erstellen
- die Liste nach dem Erstellen aktualisieren

Dafuer muss die FastAPI parallel laufen, weil Streamlit die API ueber `http://127.0.0.1:8000` aufruft.

## Tests

Die Tests liegen im Ordner `checks/`. Einige wichtige Testdateien sind:

- `checks/test-main-martin.py`
- `checks/test-main-eigene.py`
- `checks/test-validation.py`
- `checks/test-main-day4.py`

Tests koennen mit pytest ausgefuehrt werden:

```bash
uv run pytest checks/
```

Eine einzelne Testdatei kann so gestartet werden:

```bash
uv run pytest checks/test-main-martin.py
```

## Projektstruktur

```text
angewandte-Programmierung/
├── __pycache__
├── .pytest_cache
├── .venv
├── .vscode
├── checks/
│   ├── test-main-eigene.py
│   ├── test-main-martin.py
│   └── test-validation.py
    └── ...
├── data/
│   └── notes.json
├── exploration/
│   ├── class-based-decorator.py
│   └── main-day4.py
├── presentations/
    └── ...
├── .gitignore
├── .python-version
├── database.py
├── frontend.py
├── main.py
├── notes.db
├── pyproject.toml
├── README.md
├── uv.lock
└── work-log.md
```

## Installation

Voraussetzung: `uv` sollte installiert sein.

Repository klonen:

```bash
git clone https://github.com/jonasklug1010/angewandte-Programmierung.git
```

In den Projektordner wechseln:

```bash
cd angewandte-Programmierung
```

Abhaengigkeiten installieren:

```bash
uv sync
```

## Anwendung starten

FastAPI starten:

```bash
uv run fastapi dev main.py
```

Danach ist die API erreichbar unter:

```text
http://127.0.0.1:8000
```

Die automatische Dokumentation findest du unter:

```text
http://127.0.0.1:8000/docs
```

Falls Port `8000` bereits belegt ist, kann ein anderer Port verwendet werden:

```bash
uv run fastapi dev main.py --port 8001
```

Streamlit-Frontend starten:

```bash
uv run streamlit run frontend.py
```

Danach ist die Streamlit-App normalerweise erreichbar unter:

```text
http://localhost:8501
```

## Beispiel: Neue Notiz per API erstellen

Wenn FastAPI laeuft, kann eine neue Notiz zum Beispiel so erstellt werden:

```bash
curl -X POST "http://127.0.0.1:8000/notes" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Team Meeting",
    "content": "Discuss Q2 goals",
    "category": "work",
    "tags": ["meeting", "urgent"]
  }'
```

Alle Notizen anzeigen:

```bash
curl "http://127.0.0.1:8000/notes"
```

## Autor

Erstellt von Jonas Klug.

GitHub: <https://github.com/jonasklug1010>

## Schnellstart Beispiel

So kannst du das Projekt lokal schnell starten:

```bash
# 1. Repository klonen
git clone https://github.com/jonasklug1010/angewandte-Programmierung.git

# 2. In den Projektordner wechseln
cd angewandte-Programmierung

# 3. Abhaengigkeiten installieren
uv sync

# 4. FastAPI starten
uv run fastapi dev main.py
```

Danach im Browser oeffnen:

```text
http://127.0.0.1:8000/docs
```

Optional kann in einem zweiten Terminal das Streamlit-Frontend gestartet werden:

```bash
uv run streamlit run frontend.py
```

Dann im Browser oeffnen:

```text
http://localhost:8501
```
