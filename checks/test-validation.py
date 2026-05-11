import uuid

import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def client():
    return TestClient(app)


def unique_title(prefix: str = "Validation Note") -> str:
    return f"{prefix} {uuid.uuid4().hex[:8]}"


def valid_note_payload(
    title: str = None,
    content: str = "This is valid content.",
    category: str = "general",
    tags: list[str] = None
) -> dict:
    return {
        "title": title or unique_title(),
        "content": content,
        "category": category,
        "tags": tags if tags is not None else []
    }


##########
### VALIDATION TESTS FUER DIE HAUSAUFGABE
##########

# Testet, ob ein zu kurzer Titel beim Erstellen mit 422 abgelehnt wird.
def test_create_note_rejects_short_title(client):
    response = client.post("/notes", json=valid_note_payload(title="Hi"))
    
    assert response.status_code == 422


# Testet, ob eine unbekannte Kategorie beim Erstellen mit 422 abgelehnt wird.
def test_create_note_rejects_unknown_category(client):
    response = client.post("/notes", json=valid_note_payload(category="travel"))
    
    assert response.status_code == 422


# Testet, ob Tags beim Erstellen bereinigt, kleingeschrieben und dedupliziert werden.
def test_create_note_normalizes_tags(client):
    response = client.post(
        "/notes",
        json=valid_note_payload(category="work", tags=[" Work ", "URGENT", "urgent"])
    )
    
    assert response.status_code == 201
    assert response.json()["category"] == "work"
    assert set(response.json()["tags"]) == {"work", "urgent"}


# Testet, ob zusaetzliche Felder durch extra="forbid" mit 422 abgelehnt werden.
def test_create_note_forbids_extra_fields(client):
    payload = valid_note_payload()
    payload["tagz"] = ["wrong-field"]
    response = client.post("/notes", json=payload)
    
    assert response.status_code == 422


# Testet, ob eine work-Notiz zwingend den Tag work enthalten muss.
def test_work_note_requires_work_tag(client):
    response = client.post(
        "/notes",
        json=valid_note_payload(category="work", tags=["urgent"])
    )
    
    assert response.status_code == 422


# Testet, ob PATCH mit leerem Body erlaubt ist und keine Daten aendert.
def test_patch_with_empty_body_succeeds(client):
    create_response = client.post("/notes", json=valid_note_payload(tags=["patch-empty"]))
    note = create_response.json()
    
    response = client.patch(f"/notes/{note['id']}", json={})
    
    assert create_response.status_code == 201
    assert response.status_code == 200
    assert response.json()["title"] == note["title"]


# Testet, ob PATCH mit leerem Titel durch die NoteUpdate-Validierung fehlschlaegt.
def test_patch_with_invalid_title_fails(client):
    create_response = client.post("/notes", json=valid_note_payload(tags=["patch-title"]))
    note = create_response.json()
    
    response = client.patch(f"/notes/{note['id']}", json={"title": "   "})
    
    assert create_response.status_code == 201
    assert response.status_code == 422


# Testet, ob ein ungueltiger Tag-Name mit Leerzeichen/Sonderformat abgelehnt wird.
def test_tag_name_rejects_uppercase(client):
    response = client.post(
        "/notes",
        json=valid_note_payload(tags=["BAD TAG"])
    )
    
    assert response.status_code == 422


# Testet, ob eine Grossbuchstaben-Kategorie normalisiert und gespeichert wird.
def test_create_note_normalizes_uppercase_category(client):
    response = client.post(
        "/notes",
        json=valid_note_payload(category="WORK", tags=["work"])
    )
    
    assert response.status_code == 201
    assert response.json()["category"] == "work"


# Testet, ob mehr als zehn Tags mit 422 abgelehnt werden.
def test_create_note_rejects_too_many_tags(client):
    tags = [f"tag-{index}" for index in range(11)]
    response = client.post("/notes", json=valid_note_payload(tags=tags))
    
    assert response.status_code == 422


# Testet, ob ein zu kurzer Tag mit 422 abgelehnt wird.
def test_create_note_rejects_short_tag(client):
    response = client.post("/notes", json=valid_note_payload(tags=["a"]))
    
    assert response.status_code == 422


# Testet, ob PATCH eine Kategorie ebenfalls normalisiert.
def test_patch_normalizes_category(client):
    create_response = client.post("/notes", json=valid_note_payload(tags=["patch-category"]))
    note = create_response.json()
    
    response = client.patch(f"/notes/{note['id']}", json={"category": "SCHOOL"})
    
    assert create_response.status_code == 201
    assert response.status_code == 200
    assert response.json()["category"] == "school"
