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
Am ersten Tag des Kurses lag mein primärer Fokus auf der Einrichtung einer sauberen, professionellen Entwicklungsumgebung sowie dem grundlegenden Verständnis von Web-APIs. Zunächst habe ich die essenziellen Werkzeuge für den Kurs konfiguriert: Dazu gehörte das Klonen des bereitgestellten Kurs-Repositories über Git, das Einrichten von Visual Studio Code als zentrale Entwicklungsumgebung und die Installation des modernen Python-Paketmanagers uv. Mit diesen Grundlagen konnte ich mein erstes eigenes Projekt initiieren und das Web-Framework FastAPI installieren.

Die praktische Programmierung begann mit der Implementierung eines simplen Root-Endpunkts (/), der über den Browser erfolgreich die klassische „Hello, World!“-Nachricht im JSON-Format zurückgab. Eine besonders wertvolle Erkenntnis an diesem Punkt war die Entdeckung der automatischen Dokumentationsebene von FastAPI unter dem Pfad /docs (Swagger UI), welche es ermöglicht, die API direkt und interaktiv im Browser zu testen, ohne externe Tools nutzen zu müssen. Im weiteren Verlauf der Vorlesung habe ich mich intensiv mit sogenannten Path-Parametern beschäftigt. Ich habe dynamische Endpunkte erstellt, die Variablen aus der URL auslesen und verarbeiten können, wie beispielsweise /name/{name} für Strings und /alter/{alter} für Integer-Werte. Um dieses theoretische Wissen sofort in die Praxis umzusetzen, habe ich eigenständig eine Transferleistung erbracht: Ich programmierte einen mathematischen Endpunkt (/summe/{zahl1}/{zahl2}), der gleich zwei Zahlen als Path-Parameter entgegennimmt, diese innerhalb der Python-Funktion addiert und das berechnete Ergebnis strukturiert zurückgibt. Rückblickend war meine größte und faszinierendste Erkenntnis des Tages, mit welch enormer Geschwindigkeit und Effizienz sich durch FastAPI ein voll funktionsfähiges, erweiterbares Grundgerüst für eine API aufbauen lässt.

---

#### 2. 🚧 What challenges did I face?
Trotz des schnellen Fortschritts stieß ich bei der praktischen Umsetzung auf erste technische und konzeptionelle Hürden. Das erste Problem betraf den lokalen Entwicklungsserver: Nachdem ich den Code für meine ersten Endpunkte geschrieben hatte, versuchte ich den Server über das Terminal mit dem Befehl uv run fastapi dev zu starten. Obwohl das Terminal anzeigte, dass der Server lief, wurden meine programmierten Endpunkte im Browser nicht gefunden (404 Not Found) oder es wurden keine meiner letzten Code-Ergänzungen übernommen. Das war in dem Moment sehr verwirrend, da ich davon ausging, dass das System durch den "dev"-Modus jede Änderung sofort live übernimmt.

Eine weitere Schwierigkeit zeigte sich bei meiner eigenständigen Zusatzaufgabe, der Additions-Funktion. Ich geriet beim Coden kurz ins Stocken, da mir die exakte Syntax für grundlegende mathematische Operationen und vor allem die korrekte Variablendeklaration in Python nicht mehr sofort präsent war. Zudem war es anfangs konzeptionell ungewohnt, in Python – einer Sprache, die normalerweise dynamisch typisiert ist – plötzlich strikte Datentypen (Type Hints wie int oder str) in die Funktionsparameter schreiben zu müssen, was mich zunächst verunsicherte.

---

#### 3. 💡 How did I overcome them?
Das frustrierende Problem mit dem nicht aktualisierenden Entwicklungsserver konnte ich nach einer kurzen Analyse mit meinem Professor als simplen, aber sehr lehrreichen Flüchtigkeitsfehler identifizieren: Ich hatte meine neu geschriebenen Zeilen in der Datei main.py schlichtweg noch nicht gespeichert. Daraus habe ich die wichtige Erkenntnis gezogen, dass der Auto-Reload-Mechanismus des FastAPI-Servers einen Speicher-Trigger (File-Save-Event) im Dateisystem benötigt, um den Server neu zu starten. Seitdem achte ich penibel darauf, Änderungen konsequent abzuspeichern, bevor ich in den Browser wechsle.

Um die Hürden bei der Additions-Funktion und der Typisierung zu überwinden, habe ich mir gezielt von einer KI helfen lassen. Ich ließ mir von der KI kurz die Syntax für mathematische Operationen in Python auffrischen und, was noch viel wichtiger war, den Grund für die strengen Type Hints in FastAPI erklären. Die KI veranschaulichte mir hervorragend, dass FastAPI diese Typisierungen (zahl1: int) zwingend benötigt, um eingehende Daten aus der URL automatisch zu validieren und umzuwandeln. Ohne das int hätte das Framework die Zahlen aus der URL als bloße Texte (Strings) interpretiert, was bei der Operation 1 + 1 nicht zur mathematischen Summe 2, sondern zur Textverkettung 11 geführt hätte. Durch diese KI-gestützte Erklärung habe ich das fundamentale Prinzip der Datenvalidierung in FastAPI sofort tiefgreifend verstanden und konnte den Endpunkt fehlerfrei fertigstellen.

---

### Day 2

#### 1. ✅ What did I accomplish?
Der heutige Kurstag war durch einen steilen Lernzuwachs geprägt, da wir den Übergang von simplen, statischen Endpunkten hin zu einer funktionalen "Note Management API" mit echter Datenpersistenz vollzogen haben. Zunächst haben wir grundlegende Best Practices der Softwareentwicklung angewandt, indem ich eine .gitignore-Datei angelegt habe. Dies war ein wichtiger Schritt, um dem Versionskontrollsystem mitzuteilen, welche lokalen und oft speicherintensiven Dateien (wie etwa virtuelle Python-Umgebungen .venv oder systemeigene Cache-Dateien) nicht in das GitHub-Repository hochgeladen werden sollen. Begleitend dazu haben wir wichtige Python-Basics aus der Präsentation wiederholt und vertieft.

Der programmiertechnische Durchbruch des Tages war die Einführung der Bibliothek Pydantic. Ich habe gelernt, wie man mittels BaseModel strukturierte und typensichere Datenklassen (Schemas) definiert. Um eine saubere Trennung zwischen Eingabe und Verarbeitung zu gewährleisten, habe ich ein NoteCreate-Modell (nur für Titel, Inhalt und Kategorie) und ein vollständiges Note-Modell (inklusive generierter ID und created_at-Zeitstempel via datetime) implementiert. Ein weiterer großer Meilenstein war die dauerhafte Speicherung der Notizen. Über das Modul json und pathlib habe ich die Funktionen load_notes() und save_notes() programmiert. Diese sorgen dafür, dass Pydantic-Objekte in Dictionaries umgewandelt (.dict()) und sicher in einer lokalen Datei (data/notes.json) abgelegt sowie beim Neustart des Servers wieder als Objekte geladen werden (Note(note)).

Als Hausaufgabe habe ich dieses solide Fundament massiv erweitert und fortgeschrittene Routen entwickelt. Ich habe einen Statistik-Endpunkt (GET /notes/stats) programmiert, der mithilfe von Schleifen und Dictionaries die Gesamtzahl der Notizen sowie deren Verteilung auf verschiedene Kategorien berechnet. Zudem habe ich Filter-Routen (GET /notes/category/{category}) und eine gezielte Einzelabfrage (GET /notes/{note_id}) implementiert. Bei Letzterer habe ich erstmals professionelles Error-Handling angewandt: Findet das System die ID nicht, wirft es über raise HTTPException(status_code=404) eine saubere Fehlermeldung. Den Abschluss bildete ein funktionsfähiger DELETE-Endpunkt, der Elemente über ihren Index aus der Datenbank-Liste entfernt.

---

#### 2. 🚧 What challenges did I face?
Aufgrund der hohen Dichte an neuen Konzepten war der heutige Tag mental sehr anspruchsvoll und erforderte höchste Konzentration. Auf theoretischer Ebene hatte ich anfangs große Schwierigkeiten, das zugrundeliegende HTTP-Protokoll in seiner Gänze zu begreifen. Die abstrakten Konzepte von zustandsloser Kommunikation, Request-Response-Zyklen und die genaue semantische Bedeutung der verschiedenen Statuscodes (z. B. der Unterschied zwischen 200 OK und 201 Created) waren mir zu Beginn der Vorlesung noch unklar.

In der praktischen Umsetzung traten ebenfalls mehrere Hürden auf. Beim Testen meiner Endpunkte stieß ich plötzlich auf einen hartnäckigen Internal Server Error (Status 500), der den gesamten Request lahmlegte. Zudem scheiterte das Skript in einer frühen Phase daran, die erstellten Notizen physisch abzuspeichern, da das System den Pfad zur Datei nicht auflösen konnte.

Besonders die Hausaufgabe entpuppte sich als komplexe Herausforderung. Es war extrem schwierig, beim Coden den Überblick über die Datentransformationen zu behalten – also exakt nachzuvollziehen, wann Daten als rohes JSON vorliegen, wann sie zu einem Python-Dictionary werden und wann sie als validiertes Pydantic-Objekt instanziiert sind. Auch der Umgang mit den globalen Variablen (notes_db und note_id_counter) innerhalb lokaler Funktionen (unter Nutzung des global-Keywords in Python) war eine Fehlerquelle, bei der man sich ohne strikten Fokus sofort die Logik zerschießen konnte.

---

#### 3. 💡 How did I overcome them?
Um das theoretische Defizit auszugleichen, habe ich mich nach der Vorlesung noch einmal intensiv und in Ruhe mit dem HTTP-Protokoll auseinandergesetzt. Ich habe die Konzepte eigenständig nachgelesen, bis ich die Logik hinter Headern, Bodys und Methoden (GET, POST, DELETE) wirklich durchdrungen hatte – eine nachträgliche Anstrengung, die das Thema für mich im Nachhinein sogar sehr interessant und greifbar gemacht hat.

Die technischen Fehler im Code konnte ich durch systematisches Debugging lösen. Den Internal Server Error konnte ich auf einen winzigen, aber fatalen Flüchtigkeitsfehler zurückführen: Ich hatte mich bei der Variablendeklaration schlichtweg verschrieben und das deutsche Wort titel anstelle des englischen title verwendet. Durch die strikte Validierung von Pydantic konnte das System den eingehenden JSON-Key nicht mehr dem Datenmodell zuordnen. Nach dieser Korrektur lief der Endpunkt. Das Problem mit der Dateispeicherung ließ sich lösen, als ich erkannte, dass die Datei notes.json in einen Ordner namens data geschrieben werden sollte, der auf meinem System noch gar nicht existierte. Nachdem ich diesen Ordner manuell angelegt hatte (bzw. das Skript über mkdir dazu befähigt hatte), funktionierte die Persistenz einwandfrei.

Die enorme Komplexität der Hausaufgabe habe ich durch eine gezielte, moderne Lernstrategie bewältigt: Ich habe eine KI (wie ChatGPT/Gemini) als interaktiven Tutor genutzt. Wann immer ich bei der Datenkonvertierung oder bei den Schleifendurchläufen (wie z. B. der Nutzung von enumerate() beim Löschen) den Faden verlor, ließ ich mir die entsprechenden Code-Zeilen von der KI Schritt für Schritt und im Detail erklären. Diese KI-gestützte Reflexion half mir extrem dabei, nicht nur funktionierenden Code zu produzieren, sondern die tiefere Logik zu verstehen, sodass ich genau weiß, wie und wo ich diese Code-Muster in Zukunft selbstständig einbauen muss.

---

### Day 3

#### 1. ✅ What did I accomplish?
Heute stand ein fundamentaler technologischer und architektonischer Umbruch in unserem Projekt auf dem Plan: Die vollständige Migration unserer API von einer simplen, lokalen JSON-Dateispeicherung hin zu einer professionellen, relationalen Datenbankumgebung unter Verwendung von SQLite und dem ORM-Framework SQLModel.

Bevor ich mich an den Umbau der Haupt-API machte, habe ich mich intensiv mit dem neuen Konzept der Query-Parameter beschäftigt. Um das Filter-Verhalten praktisch zu verstehen, habe ich diese zunächst isoliert an einer völlig neuen Test-Route (/queryparameters) ausprobiert. Dort habe ich eine simple Liste von Vornamen implementiert, die sich über URL-Parameter (wie ?param1=Jo) dynamisch filtern ließ.
Nachdem das Prinzip klar war, habe ich das gesamte Hauptprojekt strukturell professionalisiert. Ich habe die Datenbanklogik in eine separate Datei (database.py) ausgelagert und die bisherigen Pydantic-Modelle in echte SQLModel-Datenbankklassen übersetzt. Ein großer Meilenstein war hierbei die Implementierung einer komplexen Many-to-Many-Beziehung zwischen Notizen und Tags über eine sogenannte Verbindungstabelle (NoteTagLink).

Um den Code nach außen hin sauber zu halten, wurden die API-Modelle strikt nach ihrem Verwendungszweck getrennt: Es gibt nun ein dediziertes Eingabe-Modell (NoteCreate), ein Ausgabe-Modell (NoteResponse, welches das interne Datenbankobjekt in sauberes JSON umwandelt) und ein Update-Modell (NoteUpdate). Für eine effiziente und sichere Kommunikation mit der Datenbank habe ich zudem eine FastAPI-Dependency (SessionDep) implementiert, die das Öffnen und Schließen von Datenbank-Sessions bei jedem Request automatisch und ressourcenschonend handhabt.
Darauf aufbauend habe ich die Endpunkte massiv erweitert: Die GET /notes-Route verfügt nun über hochentwickelte Filtermechanismen, mit denen sich Notizen nach Kategorie, flexiblen Suchbegriffen (LIKE-Abfragen), spezifischen Tags und sogar nach Erstellungsdatum (created_after, created_before) filtern lassen. Zudem habe ich eine PATCH-Route für teilweise Aktualisierungen programmiert und – um keine Daten zu verlieren – ein Skript (migrate_json_notes_to_database()) geschrieben, das beim Serverstart automatisch alle alten JSON-Notizen in die neue relationale Datenbank übersetzt.

---

#### 2. 🚧 What challenges did I face?
Die stark gestiegene Komplexität des Codes und der Architektur brachte im Entwickler-Alltag einige unerwartete und tiefgreifende Hürden mit sich. Zunächst fiel mir auf, dass beim Öffnen der automatischen Dokumentation (/docs) im Browser permanent eine rote Warnung namens „Duplicate Operation ID“ im Terminal erschien. Der Server lief zwar, aber das System schien im Hintergrund verwirrt zu sein.

Eine weitere große architektonische Schwierigkeit war die initiale Einrichtung der Many-to-Many-Beziehung in der Datenbank. Es war anfangs extrem schwer greifbar, wie genau die Verknüpfungen zwischen den Tabellen funktionieren und vor allem, wie man sogenannte "verwaiste" Tags – also Tags, die nach dem Löschen oder Updaten einer Notiz nirgendwo mehr verwendet werden – sauber aus dem System entfernt, ohne die Datenbank auf Dauer zuzumüllen.

Darüber hinaus stand ich bei der Implementierung der teilweisen Updates (über die PATCH-Methode) vor einem konzeptionellen Logik-Problem: Wie soll die API sicher erkennen, welche Werte vom Nutzer tatsächlich geändert werden sollen und welche unverändert in der Datenbank bleiben müssen, wenn der Nutzer im Request-Body nicht das komplette Objekt mitsendet?
Auch die neu eingebauten Datums-Filter (created_before) zeigten in der Praxis eine Schwachstelle: Übergab man über die URL ein einzelnes, kurzes Datum wie 2026-05-02 (ohne exakte Uhrzeit), wurde nicht der gesamte Tag in der Suche berücksichtigt, sondern der Filter endete um exakt 00:00 Uhr, wodurch spätere Notizen desselben Tages fälschlicherweise ignoriert wurden. Zuletzt stieß ich beim manuellen Testen im Browser auf einen 404-Fehler („Not Found“), als ich versuchte, Notizen über eine bestimmte Kategorie-URL (/categories/work/notes) abzurufen.

---

#### 3. 💡 How did I overcome them?
Um diese Vielzahl an komplexen Problemen systematisch zu bewältigen, habe ich heute verstärkt auf verschiedene Hilfsmittel zurückgegriffen, allen voran auf gezielte KI-Tools zur Code-Analyse. Die KI half mir hervorragend dabei, die „Duplicate Operation ID“-Warnung zu entschlüsseln: Durch das unbedachte Zusammenführen der Codes aus den ersten beiden Tagen sowie der Hausaufgaben hatte ich grundlegende Instanzen wie app = FastAPI() und bestimmte Routen (wie POST /notes) versehentlich doppelt im Dokument stehen. FastAPI wusste daher nicht, welchen Endpunkt es ansteuern sollte. Nachdem ich diese Duplikate restlos entfernt hatte, lief der Server wieder absolut warnungsfrei. Auch die anspruchsvolle Syntax der Many-to-Many-Beziehungen und die Logik hinter der von mir eingebauten Hilfsfunktion delete_unused_tags() habe ich mir von der KI nochmals zeilengenau erklären lassen, was mein Verständnis für relationale Datenbankstrukturen enorm geschärft hat.

Um das Thema Query-Parameter über das Vorlesungsmaterial hinaus tiefergehend zu durchdringen, habe ich mir zu Hause ergänzend ein Tutorial-Video der „Tisfoulla Academy“ auf YouTube angesehen. Eine zentrale Erkenntnis daraus war, dass solche optionalen Parameter in FastAPI immer zwingend mit dem Typ-Hint Optional deklariert werden sollten. Dieses Wissen konnte ich direkt und elegant auf mein PATCH-Problem anwenden: Ich erstellte das separate Pydantic-Modell NoteUpdate, bei dem alle Felder explizit als Optional markiert sind und einen Default-Wert von None haben. Das signalisiert der API, dass nur die explizit mitgesendeten Daten überschrieben werden sollen.
Den Datumsfilter-Bug habe ich programmatisch sehr effizient gelöst: Ich habe den Code so angepasst, dass er die Länge des Eingabestrings prüft (if len(created_before) == 10:). Ist dies der Fall (also nur YYYY-MM-DD), kombiniert das System das Datum automatisch mit time.max (dem absoluten Ende des Tages um 23:59:59 Uhr), wodurch die Filterung nun logisch einwandfrei funktioniert. Den 404-Fehler im Browser konnte ich letztlich selbst interpretieren und beheben, indem ich die passende, aber bis dato schlichtweg vergessene Route (GET /categories/{category_name}/notes) im Code nachimplementierte.

---

## Week 2

### Day 4

#### 1. ✅ What did I accomplish?
Heute stand ein essenzielles Thema der professionellen Softwareentwicklung im Mittelpunkt: das automatisierte Testen von APIs. Mir wurde theoretisch wie praktisch grundlegend klar, warum eine hohe Testabdeckung bei eigenen Projekten so unverzichtbar ist. Es geht nicht nur darum, initiale Fehler präventiv zu finden, sondern vor allem um sogenanntes Regression Testing – also die Sicherheit, bei späteren Code-Änderungen sofort per Knopfdruck überprüfen zu können, ob bestehende Funktionen weiterhin reibungslos laufen.

Im ersten praktischen Schritt habe ich mich mit den Basis-Endpunkten des Tages (main-day4.py) beschäftigt und die dazugehörige Testdatei (test-day4.py) stark erweitert. Mithilfe der Bibliotheken pytest, requests und Faker (zur Generierung realistischer, zufälliger Testdaten wie Namen) habe ich umfassende Tests geschrieben. Dabei habe ich ganz bewusst die sogenannten Grenzfälle (Edge Cases) für die Altersprüfung abgedeckt. Ich habe explizite Tests für die Alterswerte 0, 17, 18, 120 und sogar den Extremwert 999 geschrieben, um zu prüfen, ab wann die Booleans is_adult, can_vote und can_drive exakt umschlagen. Ebenso habe ich Fehlerfälle intensiv getestet, etwa stark negative Zahlen oder falsche Datentypen (not-a-number), bei denen die API korrekterweise mit einem 400er- oder 422er-Statuscode antworten muss. Zudem habe ich geprüft, ob der Greeting-Endpunkt URL-encodierte Leerzeichen (%20) oder Namen mit Bindestrichen korrekt verarbeitet.

Als Hauptaufgabe habe ich anschließend eine komplett neue, sehr umfangreiche Testdatei (test-main.py) für unser echtes Hauptprojekt geschrieben. Diese Datei ist auf exakt 40 Tests angewachsen und sichert unsere gesamte Notes-API systematisch ab. Die Tests decken nun alles ab: von den alten Tag-1-Routen über die Fehlerbehandlung bei fehlenden Pflichtfeldern bis hin zu den komplexen Datenbank-Routen. Es wird nun vollautomatisch geprüft, ob Notizen korrekt angelegt, bearbeitet (PUT und PATCH), gelöscht und gefiltert (nach Kategorie, Datum oder Suchbegriff) werden. Zudem testen die Skripte die gesamte interne Logik bei den Tags, also ob leere Tags ignoriert, doppelte Tags entfernt und alle Eingaben vor dem Speichern systematisch kleingeschrieben werden.

---

#### 2. 🚧 What challenges did I face?
Beim Aufbau dieser massiven Testinfrastruktur bin ich auf mehrere praktische und konzeptionelle Hürden gestoßen. Die erste große Schwierigkeit bestand in der Architektur meiner Tests: Da ich die requests-Bibliothek nutzte, sendeten die Tests echte HTTP-Anfragen an die API. Das bedeutete, dass die Tests direkte Auswirkungen auf unsere echte notes.db SQLite-Datenbank hatten. Wenn dutzende Tests nacheinander in Millisekunden echte Notizen erstellen, verfälscht das nicht nur die Datenbank, sondern die Tests laufen Gefahr, sich gegenseitig zu stören – beispielsweise wenn ein Test eine Notiz löscht, die ein anderer, parallel laufender Test gerade abrufen oder aktualisieren will.

Zudem war es eine kreative wie konzeptionelle Herausforderung, exakt 40 sinnvolle und vor allem unterschiedliche Tests zu entwerfen, ohne Code einfach nur redundant zu kopieren oder triviale Dinge doppelt zu prüfen.

Auf technischer Ebene gab es zudem Startschwierigkeiten mit dem Test-Framework selbst: Als ich versuchte, die Tests auszuführen, wurde der Befehl pytest über das reguläre python3 im Terminal nicht erkannt oder war im globalen System nicht direkt verfügbar. Außerdem scheiterten meine Test-Anfragen anfangs komplett (Connection Refused), weil ich in der Eile vergessen hatte, dass die requests-Bibliothek einen laufenden Gegenpart benötigt und der FastAPI-Server nicht automatisch mit den Tests startet, sondern parallel auf 127.0.0.1:8000 laufen muss.

---

#### 3. 💡 How did I overcome them?
Um das kritische Problem mit der Datenbank und den kollidierenden Tests elegant zu lösen, habe ich die uuid-Bibliothek in mein Testskript integriert. Damit habe ich eine Hilfsfunktion (unique_text) geschrieben, die für jeden Testdurchlauf einzigartige, Hash-basierte Testdaten (wie Titel, Kategorien oder Tags, z. B. Test Note-8a2f...) generiert. So operiert jeder Test in seinem eigenen, isolierten Datenraum, die Tests kommen sich nicht in die Quere und die Filter-Routen finden immer genau die Daten, die sie auch suchen sollen.

Das technische Problem mit der Ausführung von pytest konnte ich durch die korrekte Nutzung unseres Paketmanagers uv umgehen. Mit dem Kommandozeilenbefehl uv run pytest --collect-only -q test-main.py konnte ich zunächst sauber verifizieren, ob alle 40 Tests vom System überhaupt korrekt erkannt werden, bevor ich sie durchlaufen ließ. Dass der lokale Server für die HTTP-Requests in einem zweiten Terminal-Fenster nebenbei laufen muss, habe ich nun als feste Regel in meinen Entwickler-Workflow aufgenommen.

Der für mich lehrreichste und wichtigste Schritt heute war jedoch mein intensiver Umgang mit KI als Lernwerkzeug: Da der Test-Code mit seinen Hilfsfunktionen und zahlreichen assert-Statements extrem lang und komplex wurde, habe ich mir fest vorgenommen, nichts blind in mein Projekt zu kopieren. Ich habe Gemini gezielt genutzt und mir absolut jede einzelne Code-Zeile, die ich durchgegangen bin, detailliert erklären lassen. Diese Vorgehensweise hat mir enorm geholfen, die Logik hinter den Assertions, dem Auslesen von JSON-Responses, den Statuscodes und der Faker-Bibliothek tiefgreifend zu verstehen. Ich habe den Code nicht einfach nur eingefügt, sondern das Konzept des automatisierten Testens nun so verinnerlicht, dass ich solche Test-Suiten künftig völlig eigenständig konzipieren und schreiben kann.

---

### Day 5

#### 1. ✅ What did I accomplish?
Zu Beginn des heutigen Tages habe ich direkt an die Test-Thematik von gestern angeknüpft: Ich habe ein Testskript einer Kommilitonin auf meinem Mac ausgeführt und erfolgreich verifiziert, dass unsere Systeme reibungslos miteinander kompatibel sind und ihre Tests bei mir auf Anhieb fehlerfrei durchliefen.

Anschließend lag der Schwerpunkt auf tiefgreifendem Code-Refactoring und der Implementierung einer strengen Datenvalidierung. Ich habe die main.py strukturell komplett aufgeräumt. Zuvor war der Code unübersichtlich gewachsen – so wurde die FastAPI()-Instanz anfangs doppelt erstellt und manche Routen wurden später unbeabsichtigt erneut registriert. Jetzt ist die Datei in klare, kommentierte und logische Bereiche gegliedert, was die Lesbarkeit enorm erhöht.

Fachlich habe ich die Notes-API durch Pydantic-Validierungen auf ein sehr robustes, professionelles Niveau gehoben. Ich habe Input-Validierungen implementiert, um sicherzustellen, dass nur korrekte und erwartete Daten vom System verarbeitet werden. Kategorien sind nun auf ein festes Set limitiert, Tags werden über Regex-Muster validiert und zusätzliche, nicht definierte Felder im Request werden durch extra="forbid" strikt blockiert. Um diese neuen Regeln abzusichern, habe ich eine neue Testdatei test_validation.py geschrieben, die gezielt Fehlerfälle provoziert.

---

#### 2. 🚧 What challenges did I face?
Die größte Herausforderung des Tages war eine direkte Konsequenz meiner eigenen Optimierungen: Durch die strengen Validierungsregeln fielen plötzlich viele meiner bestehenden Tests aus den vorherigen Tagen durch. Das lag daran, dass ich in den alten Tests zufällige Kategorienamen (z. B. mit UUIDs) generiert hatte, die nun vom System logischerweise mit einem 422-Fehler blockiert wurden.

Zudem war es anfangs gar nicht so einfach, alle relevanten Randfälle (Edge Cases) zu bedenken – zum Beispiel, wie das Framework intern reagiert, wenn Nutzer leere Strings oder ungültige Zeichen senden. Es war konzeptionell anspruchsvoll zu verstehen, wann Daten vor der eigentlichen Überprüfung bereinigt werden müssen (z. B. Whitespaces entfernen oder Strings in Kleinbuchstaben umwandeln) und wie man komplexe, feldübergreifende Abhängigkeiten prüft (wie etwa die neue Regel, dass eine Notiz der Kategorie "work" zwingend auch den Tag "work" enthalten muss), ohne dass die Applikation abstürzt.

---

#### 3. 💡 How did I overcome them?
Das Problem mit den fehlgeschlagenen Tests konnte ich beheben, indem ich die Logik der Testdaten-Generierung anpasste und nun valide Dummy-Werte (aus den ALLOWED_CATEGORIES) übergebe. Die Einzigartigkeit der Test-Notizen stelle ich jetzt nur noch über den Titel oder den Inhalt sicher.

Um die komplexe Syntax der Pydantic-Validatoren zu meistern und die Edge Cases besser zu greifen, habe ich auch heute gezielt KI-Unterstützung genutzt. Ich habe mir detailliert erklären lassen, wie der Datenfluss innerhalb von Pydantic funktioniert und wie genau sich die Dekoratoren @field_validator und @model_validator unterscheiden. Zudem habe ich die Endpunkte systematisch mit bewusst fehlerhaften Daten getestet. Meine wichtigste Erkenntnis heute war, dass eine strikte Validierung direkt am "Eingang" der API den eigentlichen Code viel sauberer macht, da man später innerhalb der Funktionen nicht mehr manuell prüfen muss, ob die Daten überhaupt stimmen.

---

### Day 6

#### 1. ✅ What did I accomplish?
Zu Beginn haben wir uns tiefgreifend mit dem Konzept der Decorators beschäftigt. Anhand des vom Dozenten bereitgestellten Codes habe ich gelernt, wie man klassenbasierte Decorators (wie Call_Counter und Cache) implementiert. Durch die Nutzung der magischen Methoden __init__ und __call__ wurde mir sehr anschaulich verdeutlicht, wie man bestehende Funktionen dynamisch "umwickeln" und um zusätzliche Verhaltensweisen erweitern kann, ohne den eigentlichen Quellcode der Funktion antasten zu müssen. Besonders das Cache-Beispiel, bei dem Argumente (args und frozenset(kwargs)) als Schlüssel in einem Dictionary gespeichert werden, um zeitaufwändige Berechnungen bei gleichen Eingaben zu überspringen, war ein enorm wertvolles Architektur-Konzept. Dieses Wissen war ein echter Aha-Moment, da mir nun viel klarer ist, was unter der Haube von FastAPI passiert, wenn wir Routen-Decorators wie @app.get(...) verwenden.

Im praktischen Hauptteil des Tages ging es dann darum, unsere API an eine massive, externe Test-Suite (test_main_martin.py) anzupassen. Diese Suite umfasste rund 70 hochkomplexe pytest-Funktionen. Meine Aufgabe bestand darin, meine main.py so zu refaktorieren, dass sie den exakten Spezifikationen und Erwartungen dieses fremden Codes entspricht. Hierfür musste ich tief in meine Pydantic-Modelle und Endpunkte eingreifen. Unter anderem habe ich die Datumsvalidierung für die Query-Parameter created_after und created_before drastisch verbessert: Ungültige Datumswerte (wie z. B. "not-a-date" oder logisch falsche Daten wie "2026-13-01") werden nun nicht mehr von der API ignoriert, sondern aktiv abgefangen und mit einem korrekten 422 Unprocessable Entity-Statuscode abgelehnt. Nach vielen systematischen Anpassungen konnte ich das Projekt am Ende des Tages in einen Zustand bringen, in dem alle 70 Tests von Martin absolut fehlerfrei und reibungslos durchliefen.

---

#### 2. 🚧 What challenges did I face?
Der Weg zu dieser fehlerfreien API war mit einer massiven und anfangs stark demotivierenden Herausforderung verbunden. Beim allerersten vollständigen Testlauf der test_main_martin.py auf meinem System kam es zu einem regelrecht erschlagenden Fehlerbild im Terminal. Das Ergebnis lautete: 17 failed, 14 passed, 39 errors.

Diese Zahlenfolge musste ich erst einmal intellektuell verarbeiten und systematisch interpretieren. Die 14 passed (bestandenen) Tests waren ein erster Lichtblick: Sie bewiesen, dass meine API nicht fundamental defekt war; grundlegende Routen funktionierten und der Server antwortete.
Das massivste Problem lag in den 39 errors. Wie sich herausstellte, entstanden diese nicht während der eigentlichen Testausführung, sondern brachen den Vorgang schon in der Vorbereitungsphase (den sogenannten Test-Fixtures wie _create_note) ab. Viele der vorgegebenen Tests versuchten, automatisch Test-Notizen in meiner Datenbank anzulegen. Diese automatisierten Notizen hatten oft die Zuweisung category="work", besaßen aber in Martins Setup keinen "work"-Tag. Genau hier kam es zu einem harten Konflikt mit meiner eigenen API-Logik: In der Hausaufgabe der vorherigen Tage hatte ich eine strenge, feldübergreifende Validierungsregel (Cross-Field-Validation via @model_validator) implementiert, die exakt dies verbot. Meine API blockte die Testdaten-Erstellung folglich konsequent mit einem 422-Fehler ab. Da diese fundamentalen Testdaten nicht erstellt werden konnten, schlugen alle 39 Tests, die von der Existenz dieser Daten abhängig waren, sofort als Error fehl, noch bevor sie überhaupt richtig starteten.

Die 17 failed wiederum waren "echte" Test-Fehlschläge. Das bedeutet, der Test konnte zwar ausgeführt werden, erhielt aber von meiner API ein völlig anderes Ergebnis als das Assert-Statement erwartete. Ein prägnantes Beispiel: Einige Tests erwarteten bei absichtlich fehlerhaften Datumsfiltern (z. B. "2026-99-99") einen 422-Fehlercode, während meine API das fehlerhafte Format vorher einfach stillschweigend geschluckt und ein 200 OK (oftmals mit einer leeren Liste) zurückgegeben hatte.

---

#### 3. 💡 How did I overcome them?
Um diese regelrechte Wand an roten Fehlermeldungen im Terminal systematisch abzuarbeiten, habe ich heute exzessiv auf KI-Unterstützung zurückgegriffen. Anstatt blind im Code zu raten oder Parameter wild zu verändern, habe ich mir die einzelnen Error-Traces und Failed-Logs aus dem Terminal kopiert und von der KI im Detail erklären lassen. Dadurch habe ich überhaupt erst den elementaren Unterschied im Pytest-Framework zwischen einem Test-Error (Fehler in der Setup-Phase/Fixture) und einem Test-Fail (falsches Assertion-Ergebnis bei der eigentlichen Überprüfung) verstanden.

Nach dieser sauberen Analyse konnte ich die Probleme in der main.py durch zwei wesentliche Architekturentscheidungen beheben:
Zum einen habe ich den logischen Konflikt bei der Notizen-Erstellung aufgelöst. Ich habe realisiert, dass man bei der Arbeit nach externen Spezifikationen manchmal eigene Regeln aufgeben muss. Daher habe ich die extrem strenge Hausaufgaben-Regel (die Pflicht, dass "work"-Notizen zwingend den "work"-Tag benötigen) aus meinem Pydantic-Modell restlos entfernt. Diese Anpassung erlaubte es der Test-Suite endlich, ihre Fixtures fehlerfrei aufzubauen, wodurch die 39 Errors auf einen Schlag verschwanden.
Zum anderen habe ich, wie im ersten Abschnitt beschrieben, die fehlende Strenge bei der Datumsvalidierung nachgerüstet. Indem ich sicherstellte, dass invalide Query-Parameter konsequent validiert und mit einem 422-Fehler beantwortet werden, konnte ich auch die restlichen 17 Failed-Tests beheben.

Diese hochgradig systematische Vorgehensweise – erst das kryptische Fehlerbild verstehen, dann mithilfe von KI die Ursachen isolieren und abschließend gezielte Code-Anpassungen vornehmen – war eine unglaublich lehrreiche Erfahrung. Sie hat mir eindrucksvoll gezeigt, wie wichtig es ist, fremden Code (in diesem Fall Martins Tests) lesen zu können und die eigene API flexibel, aber robust an ein vertraglich vorgegebenes API-Design anzupassen.

---

## Week 3

### Day 7

#### 1. ✅ What did I accomplish?
Der heutige Kurstag markierte einen spannenden Wechsel in unserem Projekt: Wir haben die reine Backend-Entwicklung vorerst verlassen und uns der Erstellung eines Frontends (einer grafischen Benutzeroberfläche) gewidmet.

Als kleine organisatorische Vorarbeit habe ich zunächst die klassenbasierte Decorator-Beispieldatei von letzter Vorlesung in einen Ordner namens exploration verschoben. Dies diente dazu, das Hauptverzeichnis des Projekts sauber und übersichtlich zu halten. Im Anschluss habe ich über das Terminal (uv run) verifiziert, dass die Datei trotz des neuen Pfades weiterhin syntaktisch korrekt ist und fehlerfrei ausgeführt werden kann.

Der inhaltliche Schwerpunkt lag danach vollständig auf dem Python-Framework Streamlit. Im gemeinsamen Teil der Vorlesung haben wir zunächst die Grundlagen erarbeitet. Wir haben eine simple Applikation geschrieben, die eine externe, öffentliche API (naas.isalman.dev/no) abfragt und die JSON-Antworten auf Knopfdruck im Browser darstellt. Hierbei haben wir zentrale Streamlit-Elemente wie st.button, st.text_input und st.write kennengelernt. Das wichtigste Konzept, das wir dabei implementiert haben, war die Zustandsverwaltung über st.session_state.

In der anschließenden Hausaufgabe habe ich dieses Wissen angewandt und völlig eigenständig eine echte Benutzeroberfläche für unsere lokale Notes-API programmiert. Ich habe die Datei frontend.py so erweitert, dass sie als Brücke zu unserer Datenbank fungiert.
Dazu habe ich zwei Hauptfunktionen implementiert: Erstens einen Lese-Bereich, in dem über die Funktion load_notes() alle vorhandenen Notizen per GET-Request vom Backend (127.0.0.1:8000) geladen und in einem interaktiven Dropdown-Menü (st.selectbox) übersichtlich präsentiert werden. Zweitens einen Schreib-Bereich in Form eines Eingabeformulars (st.form). Hier kann der Nutzer Titel, Inhalt, Kategorie (aus einem vorgegebenen Dropdown) und Tags eingeben. Über die von mir geschriebene Hilfsfunktion parse_tags() wird der eingegebene Tag-String sauber in eine Python-Liste umgewandelt und via POST-Request (Notes()) an das Backend gesendet. Bei erfolgreicher Erstellung erzwingt das Skript einen automatischen Page-Reload (st.rerun()) und zeigt über den Session-State eine Erfolgsmeldung (st.success) an, sodass die neue Notiz sofort in der UI sichtbar wird.

---

#### 2. 🚧 What challenges did I face?
Der Einstieg in die Frontend-Entwicklung brachte völlig neue architektonische und konzeptionelle Herausforderungen mit sich. Während der Vorlesung gab es bei mir anfangs deutliche Verständnisprobleme bezüglich der Ausführungslogik von Streamlit. Das Framework arbeitet mit einem reaktiven Paradigma: Bei jeder Benutzerinteraktion (z. B. einem Klick auf einen Button oder einer Texteingabe) wird das gesamte Python-Skript von oben nach unten neu ausgeführt. Es war für mich zunächst sehr unlogisch und verwirrend, warum normale Variablen dadurch bei jedem Klick ihre Werte verloren und warum wir zwingend Konstrukte wie if "text1" not in st.session_state: verwenden mussten, um Daten am Leben zu halten.

Die Hausaufgabe stellte mich dann vor noch größere praktische Hürden. Da ich bisher kaum Erfahrung in der Frontend-Gestaltung hatte, war es enorm schwierig, alles so hinzubekommen, wie es sein soll. Die korrekte Anordnung der UI-Elemente und das Verknüpfen der Buttons mit den Backend-Funktionen fühlten sich komplex an.
Eine sehr spezifische Hürde war die Verarbeitung der Benutzereingaben für die Tags. Da unsere FastAPI-Backend-Validierung aus den Vortagen extrem streng ist (Tags müssen eine Liste sein, kleingeschrieben, ohne Leerzeichen), musste ich sicherstellen, dass die rohe Texteingabe aus dem Frontend (z.B. "School , EXAM,") exakt in das erwartete Format umgewandelt wird, bevor der Request abgeschickt wird. Täte ich das nicht, würde das Backend den POST-Request sofort mit einem 422-Error ablehnen. Zudem musste ich sicherstellen, dass das Skript nicht abstürzt, wenn der Backend-Server versehentlich gar nicht läuft.

---

#### 3. 💡 How did I overcome them?
Die anfänglichen theoretischen Verständnisprobleme während der Vorlesung klärten sich erfreulicherweise im Laufe der gemeinsamen Programmierung. Durch die detaillierten Erklärungen des Professors und das direkte Beobachten, wie sich die Werte im st.expander("Session state") bei jedem Reload verhielten, hat es Klick gemacht. Ich habe die Notwendigkeit des Session-States für die Persistenz von Daten in Streamlit nun grundlegend durchdrungen.

Um die massiven Hürden bei der Hausaufgabe zu bewältigen, habe ich extrem intensiv auf KI-Unterstützung gesetzt. Da die Syntax von Streamlit und die Kombination mit der requests-Bibliothek für mich Neuland waren, habe ich nicht versucht, stundenlang blind herumzuprobieren. Stattdessen habe ich die KI als Mentor genutzt: Ich habe mir einzelne, komplexe Code-Zeilen (wie z. B. die Funktionsweise von response.raise_for_status(), die Lambda-Funktion innerhalb der st.selectbox oder das pop() beim Abrufen der Erfolgsmeldung aus dem Session-State) detailliert erstellen und erklären lassen.

Besonders bei der Datenaufbereitung hat mir diese Vorgehensweise geholfen: Ich habe eine saubere Logik für die Funktion parse_tags() entwickelt, die den String am Komma trennt (.split(",")), die Leerzeichen entfernt (.strip()) und alles in Kleinbuchstaben umwandelt (.lower()), sodass die Strenge unseres Backends befriedigt wird. Um Abstürze bei nicht laufendem Server zu verhindern, habe ich zudem gelernt, wie man einen sauberen try-except-Block (requests.exceptions.RequestException) um den API-Aufruf baut und dem Nutzer in Streamlit eine rote st.error-Box anzeigt, statt das Programm crashen zu lassen. Durch das zeilenweise Erklärenlassen habe ich den Code nicht einfach nur kopiert, sondern die Brücke zwischen Frontend (Nutzerinteraktion) und Backend (Datenverarbeitung) wirklich verstanden.

---

### Day 8

#### 1. ✅ What did I accomplish?
Am heutigen letzten Projekttag habe ich keine neuen Änderungen mehr am Code vorgenommen, sondern mich ausschließlich auf den finalen Checkup für die Abgabe konzentriert. Ich habe alle Projektdateien aufgeräumt und sauber strukturiert. Zum Abschluss habe ich die gesamte Test-Suite noch einmal vollständig durchlaufen lassen, um endgültig sicherzustellen, dass das System reibungslos funktioniert und das Projekt abgabebereit ist.

---

#### 2. 🚧 What challenges did I face?


/


---

#### 3. 💡 How did I overcome them?


/


# 🎉 Congratulations! You did it! 🎓✨













