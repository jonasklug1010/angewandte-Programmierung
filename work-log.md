# Work Log

**Student Name:** 

Instructions: Fill out one log for each course day. Content to consider: Course Sessions + Assignment

## Template:

---

## 1. ✅ What did I accomplish?

_Reflect on the activities, exercises, and work you completed today._

**Guiding questions:**
- What topics or concepts did you work with?
- What exercises or projects did you complete?
- What tools or technologies did you use?
- What did you learn or practice?



---

## 2. 🚧 What challenges did I face?

_Describe any difficulties, obstacles, or confusing moments you encountered._

**Guiding questions:**
- What was difficult to understand?
- Where did you get stuck?
- What errors or problems did you face?
- What felt frustrating or confusing?




---

## 3. 💡 How did I overcome them?

_Explain how you overcame the challenges or what help you needed._

**Guiding questions:**
- What strategies did you try?
- Who or what helped you (instructor, classmates, documentation)?
- What did you learn from solving the problem?
- What questions do you still have?


---

## Week 1

### Day 1

#### 1. ✅ What did I accomplish?
Heute lag der Fokus auf der Einrichtung der Entwicklungsumgebung und der Einführung in die grundlegende Funktionsweise von APIs. Zunächst habe ich die erforderlichen Tools – Git, Visual Studio Code und den Python-Paketmanager uv – eingerichtet und das Kurs-Repository von GitHub geklont.
Anschließend habe ich mit dem Web-Framework FastAPI ein eigenes Projekt gestartet und die ersten Basis-Endpunkte implementiert (z. B. den Root-Endpunkt, der „Hello, World!“ zurückgibt). Sehr hilfreich war dabei das Kennenlernen der automatischen Dokumentationsebene unter dem Pfad /docs, über die sich die API direkt im Browser testen lässt. Als Transferleistung zu den Hausaufgaben, bei denen Berechnungen via Path-Parameter gefordert waren, habe ich eigenständig weitere, dynamische Endpunkte programmiert. Dazu gehören Endpunkte für die Verarbeitung eines Strings (/name/{name}) und eines Integers (/alter/{alter}). Als Erweiterung habe ich zudem einen komplexeren Endpunkt (/summe/{zahl1}/{zahl2}) entwickelt, der gleich zwei Integer-Werte als Path-Parameter entgegennimmt, diese addiert und das Ergebnis im JSON-Format ausgibt.

---

#### 2. 🚧 What challenges did I face?
Es gab zwei kleinere Hürden: Zum einen schienen Änderungen am Code beim lokalen Entwicklungsserver mit dem Startbefehl uv run fastapi dev anfangs nicht übernommen zu werden. Zum anderen geriet ich bei meiner eigenständigen Zusatzaufgabe (der Additions-Funktion) kurz ins Stocken, da mir die genaue Syntax für grundlegende mathematische Operationen und die korrekte Variablendeklaration (Typisierung) in Python in dem Moment nicht mehr komplett präsent war.

---

#### 3. 💡 How did I overcome them?
Das Problem mit dem Entwicklungsserver konnte ich schnell auf einen Flüchtigkeitsfehler zurückführen: Ich hatte meine letzten Änderungen im Dokument main.py schlichtweg noch nicht gespeichert. Da der Server nur beim Speichern der Datei neu lädt (Auto-Reload), war der Fehler danach sofort behoben. Das Problem bei der Summierung der Zahlen konnte ich lösen, indem ich die Python-Grundlagen für einfache Rechenoperationen noch einmal kurz nachgeschlagen habe. Dabei habe ich auch direkt angewendet, wie wichtig die Typisierung der Parameter in FastAPI ist (z. B. zahl1: int), damit das Framework die Eingaben automatisch validiert und weiß, dass es sich um Zahlen handelt, die mathematisch addiert werden sollen, und nicht um eine Verkettung von Strings.

---

### Day 2

#### 1. ✅ What did I accomplish?
Heute lag der Fokus auf der Vertiefung der Python-Basics und dem Ausbau unserer API zu einer funktionsfähigen "Note Management API" mit echter Datenspeicherung. Zu Beginn haben wir eine .gitignore-Datei angelegt, um dem System mitzuteilen, welche lokalen Dateien (wie z. B. virtuelle Umgebungen) nicht in die Versionskontrolle hochgeladen werden sollen.
Programmiertechnisch haben wir einen großen Sprung gemacht: Wir haben Pydantic (BaseModel) eingeführt, um Datenstrukturen (wie NoteCreate und Note) professionell zu definieren und eingehende Daten automatisch validieren zu lassen. Ein zentraler Meilenstein war die Persistenz der Daten: Die Notizen werden nun über die Funktionen load_notes und save_notes in einer lokalen JSON-Datei gespeichert und geladen. Für die Hausaufgabe habe ich dieses Fundament stark erweitert und verschiedene neue Endpunkte programmiert. Dazu gehören GET-Routen für das Abrufen von Notiz-Statistiken (/notes/stats), das Filtern nach Kategorien (/notes/category/{category}) sowie das Abrufen spezifischer Notizen via ID (/notes/{note_id}) inklusive Error-Handling (HTTPException). Abschließend habe ich erfolgreich einen DELETE-Endpunkt zum Löschen einzelner Notizen implementiert.

---

#### 2. 🚧 What challenges did I face?
Der heutige Tag war sehr anspruchsvoll und erforderte durch das viele und komplexe Programmieren höchste Konzentration. Theoretisch waren mir anfangs die grundlegenden HTTP-Konzepte noch etwas unklar und zu abstrakt.
In der Praxis zeigten sich ebenfalls einige Hürden: Ich stieß auf einen hartnäckigen Internal Server Error, der den gesamten Endpunkt lahmlegte. Zudem scheiterte das Skript zunächst daran, die fertigen Notizen abzuspeichern. Bei der Hausaufgabe war es extrem herausfordernd, den Überblick über die Datenkonvertierung zu behalten (wie man Pydantic-Objekte für die JSON-Datei in Dictionaries umwandelt und umgekehrt) und wie die globalen Variablen (notes_db, note_id_counter) innerhalb der verschiedenen Funktionen korrekt aktualisiert werden. Ohne ständige Fokussierung schlichen sich hier schnell Logik- oder Syntaxfehler ein.

---

#### 3. 💡 How did I overcome them?
Das theoretische Verständnis für HTTP habe ich nach der Vorlesung noch einmal intensiv nachgearbeitet, bis die Zusammenhänge für mich komplett logisch und greifbar wurden – das Thema ist tatsächlich sehr interessant, wenn man es einmal durchdrungen hat.
Den Server-Fehler beim Coden konnte ich als kleinen, aber fatalen Flüchtigkeitsfehler dank meines Professors identifizieren: Ich hatte mich bei zwei Variablen verschrieben (ich tippte titel statt title). Dadurch konnte das System die Daten nicht mehr dem Pydantic-Modell zuordnen. Nach der Korrektur lief es einwandfrei. Das Problem mit der Dateispeicherung ließ sich lösen, indem ich den benötigten data-Ordner im Verzeichnis manuell erstellte, auf den der Pfad (Path("data/notes.json")) zugreifen wollte. Um die hohe Komplexität bei der Hausaufgabe zu bewältigen, habe ich eine neue Lernstrategie angewandt: Ich habe mir immer mal wieder gezielt einzelne, komplexe Code-Passagen von einer KI detailliert erklären lassen. Zu verstehen, was genau in welcher Zeile passiert, hat mir enorm geholfen, die Logik (wie Listen-Durchläufe oder das Error-Handling) wirklich zu verinnerlichen und zu wissen, wie und wo ich solche Bausteine in Zukunft selbst einbauen muss. Letztendlich hat am Ende alles fehlerfrei funktioniert.

---

### Day 3

#### 1. ✅ What did I accomplish?






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






---

## Week 2

### Day 4

#### 1. ✅ What did I accomplish?






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






---

### Day 5

#### 1. ✅ What did I accomplish?






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






---

### Day 6

#### 1. ✅ What did I accomplish?






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






---

## Week 3

### Day 7

#### 1. ✅ What did I accomplish?






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






---

### Day 8

#### 1. ✅ What did I accomplish?






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






---

### Day 9

#### 1. ✅ What did I accomplish?






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






---


# 🎉 Congratulations! You did it! 🎓✨













