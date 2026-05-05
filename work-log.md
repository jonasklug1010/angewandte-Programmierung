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
Heute stand ein fundamentaler technologischer Umbruch auf dem Plan: Die Migration unserer API von einer lokalen JSON-Dateispeicherung hin zu einer relationalen Datenbank mit SQLite und dem Framework SQLModel. Bevor ich mich an die Haupt-API machte, habe ich mich intensiv mit dem Konzept der Query-Parameter beschäftigt und diese, wie in der Vorlesung empfohlen, zunächst isoliert an einer Test-Route (/queryparameters) ausprobiert, um das Filter-Verhalten praktisch zu verstehen.

Anschließend habe ich das Projekt architektonisch stark professionalisiert. Ich habe eine separate database.py angelegt und die Datenstrukturen in SQLModel-Klassen übersetzt, inklusive einer komplexen Many-to-Many-Beziehung (NoteTagLink) zwischen Notizen und Tags. Um den Code sauber zu halten, wurden die API-Modelle strikt in Eingabe- (NoteCreate), Ausgabe- (NoteResponse) und Update-Modelle (NoteUpdate) getrennt. Für eine saubere Kommunikation mit der Datenbank habe ich zudem eine FastAPI-Dependency (SessionDep) implementiert, die das Öffnen und Schließen von Datenbank-Sessions bei jedem Request automatisch handhabt. Darauf aufbauend habe ich die Endpunkte massiv erweitert: Die GET /notes-Route verfügt nun über komplexe Filter (nach Kategorie, Suchbegriff, Tags und Erstellungsdatum), ich habe eine PATCH-Route für teilweise Aktualisierungen programmiert und ein Skript geschrieben, das die alten JSON-Notizen automatisch in die neue Datenbank migriert.

---

#### 2. 🚧 What challenges did I face?
Die stark gestiegene Komplexität des Codes brachte im Entwickler-Alltag einige Hürden mit sich. Zunächst fiel mir auf, dass beim Öffnen der automatischen Dokumentation (/docs) im Terminal permanent die Warnung „Duplicate Operation ID“ erschien. Eine weitere große architektonische Schwierigkeit war die initiale Einrichtung der Many-to-Many-Beziehung in der Datenbank; es war anfangs schwer greifbar, wie diese Verknüpfungen funktionieren und wie man verwaiste Tags sauber aus dem System löscht.

Darüber hinaus stand ich bei der Implementierung der teilweisen Updates (PATCH) vor dem logischen Problem, wie die API erkennen soll, welche Werte tatsächlich geändert werden sollen und welche unverändert bleiben, wenn der Nutzer nicht das komplette Objekt mitsendet. Auch die neu eingebauten Datums-Filter (created_before) zeigten eine Schwachstelle: Übergab man ein einzelnes Datum wie 2026-05-02 (ohne exakte Uhrzeit), wurde nicht der gesamte Tag in der Suche berücksichtigt. Zuletzt stieß ich beim Testen im Browser auf einen 404-Fehler („Not Found“), als ich versuchte, Notizen über eine bestimmte Kategorie-URL abzurufen.

---

#### 3. 💡 How did I overcome them?
Um diese Vielzahl an Problemen effizient und systematisch zu bewältigen, habe ich verschiedene Lernstrategien und Hilfsmittel eingesetzt, allen voran gezielt KI-Tools zur Code-Analyse. Die KI half mir hervorragend dabei, die „Duplicate Operation ID“-Warnung zu entschlüsseln: Durch das Zusammenführen der Codes aus den ersten beiden Tagen sowie der Hausaufgaben hatte ich grundlegende Instanzen wie app = FastAPI() und bestimmte Routen versehentlich doppelt im Dokument stehen. Nachdem ich diese Duplikate entfernt hatte, lief der Server wieder absolut fehlerfrei. Auch die anspruchsvolle Syntax und Funktionsweise der Datenbankbeziehungen (Many-to-Many) habe ich mir von der KI nochmals zeilengenau und verständlich erklären lassen.

Um das Thema Query-Parameter über die Vorlesung hinaus tiefergehend zu durchdringen, habe ich mir ergänzend ein Tutorial-Video der „Tisfoulla Academy“ angesehen. Eine zentrale Erkenntnis daraus war, dass Parameter in FastAPI immer zwingend als Optional deklariert werden sollten, um Fehler zu vermeiden. Dieses Wissen konnte ich direkt auf mein PATCH-Problem anwenden: Ich erstellte ein eigenes Pydantic-Modell (NoteUpdate), bei dem alle Felder als optional markiert sind, was der API signalisiert, nur die explizit mitgesendeten Daten zu überschreiben. Den Datumsfilter habe ich programmatisch gelöst, indem ich den Code so anpasste, dass bei einer reinen Datumseingabe (Länge von 10 Zeichen) automatisch die Uhrzeit auf das Ende des Tages (time.max) gesetzt wird. Den 404-Fehler im Browser konnte ich letztlich selbst interpretieren und beheben, indem ich die passende, aber bis dato fehlende Route für die Kategorie-Suche im Code ergänzt habe.

---

## Week 2

### Day 4

#### 1. ✅ What did I accomplish?
Heute stand ein essenzielles Thema der Softwareentwicklung im Mittelpunkt: das automatisierte Testen von APIs. Mir wurde grundlegend klar, warum Testabdeckungen bei eigenen Projekten so wichtig sind – nicht nur um Fehler präventiv zu finden, sondern auch um bei späteren Code-Änderungen sofort überprüfen zu können, ob bestehende Funktionen weiterhin reibungslos laufen.

Im ersten Schritt habe ich mich mit den Basis-Endpunkten des Tages (main-day4.py) beschäftigt und die dazugehörige Testdatei (test-day4.py) stark erweitert. Mithilfe der Bibliotheken pytest, requests und Faker (zur Generierung zufälliger Testdaten) habe ich acht zusätzliche Tests geschrieben. Dabei habe ich bewusst Extrem- und Grenzfälle für die Altersprüfung abgedeckt, wie zum Beispiel die Werte 0, 17, 18, 120 und 999. Ebenso habe ich Fehlerfälle getestet, etwa negative Zahlen oder falsche Datentypen, bei denen die API korrekterweise mit einem 400er- oder 422er-Statuscode antworten muss.
Als Hauptaufgabe habe ich anschließend eine komplett neue, sehr umfangreiche Testdatei (test-main.py) für unser Hauptprojekt erstellt. Diese umfasst exakt 40 Tests und sichert alle bisherigen Funktionen ab: von den alten Tag-1-Routen über die Fehlerbehandlung (z. B. wenn Buchstaben statt Zahlen übergeben werden) bis hin zu den komplexen Datenbank-Routen der Notes-API. Es wird nun automatisch geprüft, ob Notizen korrekt angelegt, bearbeitet (PUT/PATCH), gelöscht und gefiltert (nach Kategorie, Datum oder Suchbegriff) werden. Zudem testen die Skripte, ob die Logik bei den Tags funktioniert, also ob leere Tags ignoriert, doppelte entfernt und alle Eingaben systematisch kleingeschrieben werden.

---

#### 2. 🚧 What challenges did I face?
Beim Aufbau dieser großen Testinfrastruktur bin ich auf mehrere praktische und konzeptionelle Hürden gestoßen. Die erste große Schwierigkeit bestand darin, dass unsere Tests über die requests-Bibliothek echte HTTP-Anfragen an die API senden. Das bedeutet, dass die Tests direkte Auswirkungen auf unsere echte notes.db SQLite-Datenbank haben. Wenn viele Tests nacheinander echte Notizen erstellen, verfälscht das nicht nur die Datenbank, sondern die Tests könnten sich gegenseitig stören (beispielsweise wenn ein Test eine Notiz löscht, die ein anderer Test gerade abrufen will).
Eine weitere Herausforderung war es, exakt 40 sinnvolle und unterschiedliche Tests zu konzipieren, ohne Inhalte einfach nur redundant zu überschreiben oder zu wiederholen.
Auf technischer Ebene gab es zudem Startschwierigkeiten mit dem Test-Framework selbst: Als ich versuchte, die Tests auszuführen, wurde pytest über den regulären python3-Befehl im Terminal nicht erkannt oder war nicht direkt verfügbar. Außerdem scheiterten die Anfragen anfangs komplett, wenn ich vergessen hatte, den FastAPI-Server parallel auf 127.0.0.1:8000 laufen zu lassen.

---

#### 3. 💡 How did I overcome them?
Um das kritische Problem mit der Datenbank und den sich gegenseitig störenden Tests zu lösen, habe ich die uuid-Bibliothek in mein Testskript integriert. Damit generiere ich nun für jeden Testdurchlauf einzigartige Testdaten (wie Titel, Kategorien oder Tags) mit einem dynamischen Hash-Wert. So kommen sich die Tests nicht in die Quere und die Datenbank bleibt strukturiert.
Das technische Problem mit pytest konnte ich durch die Nutzung unseres Paketmanagers uv umgehen. Mit dem Befehl uv run pytest --collect-only -q test-main.py konnte ich zunächst sauber verifizieren, ob alle 40 Tests vom System korrekt erkannt werden, bevor ich sie durchlaufen ließ. Dass der lokale Server für die requests nebenbei laufen muss, habe ich als feste Regel in meinen Workflow übernommen.

Der für mich wichtigste und lehrreichste Schritt heute war jedoch mein Umgang mit KI: Da der Test-Code extrem lang und komplex wurde, habe ich mir fest vorgenommen, nichts blind zu kopieren. Ich habe Gemini gezielt beim Erstellen der Tests genutzt und mir absolut jede einzelne Code-Zeile, die ich durchgegangen bin, detailliert erklären lassen. Diese Vorgehensweise hat mir enorm geholfen, die Logik hinter den Assertions, den Statuscodes und der Faker-Bibliothek wirklich tiefgreifend zu verstehen, sodass ich den Code nicht einfach nur sinnlos eingefügt habe, sondern das Konzept des Testens nun eigenständig anwenden kann.

---

### Day 5

#### 1. ✅ What did I accomplish?
Heute lag der Schwerpunkt auf tiefgreifendem Code-Refactoring und der Implementierung einer strengen Datenvalidierung. Zu Beginn habe ich die main.py strukturell komplett aufgeräumt. Zuvor war der Code unübersichtlich gewachsen – so wurde die FastAPI()-Instanz anfangs doppelt erstellt und manche Routen wurden später unbeabsichtigt erneut registriert. Jetzt ist die Datei in klare, kommentierte logische Bereiche gegliedert (App-Setup, Validierungs-Hilfsfunktionen, API-Modelle, Datenbank und Endpunkte), was die Lesbarkeit und Wartbarkeit enorm erhöht.

Fachlich habe ich die Notes-API durch Pydantic-Validierungen auf ein professionelles, sehr robustes Niveau gehoben. Ziel war es, fehlerhafte Benutzereingaben direkt beim Request abzufangen, noch bevor sie die Datenbanklogik erreichen. Dazu wurden die Modelle NoteCreate und NoteUpdate stark erweitert: Kategorien sind nun auf ein festes Set (wie "work", "personal", "school") limitiert, Tags werden über Regex-Muster validiert, und zusätzliche, nicht im Modell definierte Felder im Request werden durch die Pydantic-Konfiguration (extra="forbid") strikt blockiert. Um diese neuen Regeln abzusichern, habe ich eine neue Testdatei test_validation.py geschrieben. Diese nutzt FastAPIs TestClient, um gezielt Fehlerfälle (wie zu kurze Titel oder unbekannte Kategorien) zu provozieren und sicherzustellen, dass die API korrekterweise mit einem 422-Statuscode antwortet. Ergänzend habe ich ein Testskript einer Kommilitonin auf meinem Mac ausgeführt und erfolgreich verifiziert, dass unsere Systeme und Tests reibungslos miteinander kompatibel sind.

---

#### 2. 🚧 What challenges did I face?
Die größte Herausforderung des Tages war eine direkte Konsequenz meiner eigenen Optimierungen: Durch die Einführung der strengen Validierungsregeln fielen plötzlich viele meiner bereits bestehenden Tests aus den vorherigen Tagen durch. Das lag daran, dass ich in den alten Tests Tools wie uuid4 genutzt hatte, um zufällige, einzigartige Kategorienamen (z. B. "Testing-8a2f...") zu generieren. Da die neue API nun aber explizit nur noch feste Werte aus dem Set ALLOWED_CATEGORIES zulässt, wurden all diese automatisierten Test-Requests plötzlich mit einem Validierungsfehler (HTTP 422) abgelehnt.

Eine weitere Hürde war die korrekte Implementierung der Pydantic-Validatoren selbst. Es war konzeptionell anspruchsvoll zu verstehen, wann Daten vor der eigentlichen Überprüfung bereinigt werden müssen (z. B. Whitespaces entfernen oder Strings in Kleinbuchstaben umwandeln) und wie man komplexe, feldübergreifende Abhängigkeiten prüft – wie etwa die neue Regel, dass eine Notiz der Kategorie "work" zwingend auch den Tag "work" enthalten muss.

---

#### 3. 💡 How did I overcome them?
Das Problem mit den fehlgeschlagenen Tests konnte ich systematisch beheben, indem ich die Logik der Testdaten-Generierung anpasste. Statt komplett zufälliger Strings für die Kategorien übergebe ich nun bei den betroffenen automatisierten Tests validen Dummy-Content (wie "general" oder "work"). Die Einzigartigkeit der Test-Notizen stelle ich nun ausschließlich über den Titel oder den Inhalt sicher, wodurch alle Tests wieder erfolgreich durchlaufen.

Um die komplexe Syntax und Funktionsweise der Pydantic-Validatoren zu meistern, habe ich auch heute wieder gezielt KI-Unterstützung genutzt. Ich habe mir von der KI detailliert erklären lassen, wie der Datenfluss innerhalb von Pydantic funktioniert und wie genau sich die Dekoratoren @field_validator(mode="before") und @model_validator(mode="after") unterscheiden. Durch diesen interaktiven Erklärprozess habe ich nicht nur gelernt, wie man Eingaben normalisiert, bevor das System sie ablehnt, sondern auch verstanden, wie man feldübergreifende Logikprüfungen sauber programmiert. Dieser Schritt war entscheidend, um den Code nicht nur blind aus einem Tutorial zu übernehmen, sondern die tieferliegende Mechanik von Datenvalidierung in Python wirklich zu verinnerlichen.

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













