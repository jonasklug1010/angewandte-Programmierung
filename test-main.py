import uuid

import requests


BASE_URL = "http://127.0.0.1:8000"
TIMEOUT = 5


def unique_text(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4().hex[:8]}"


def create_test_note(
    title: str = None,
    content: str = None,
    category: str = None,
    tags: list[str] = None
) -> dict:
    note_data = {
        "title": title or unique_text("Test Note"),
        "content": content or unique_text("Test Content"),
        "category": category or unique_text("test-category"),
        "tags": tags or ["test"]
    }
    response = requests.post(f"{BASE_URL}/notes", json=note_data, timeout=TIMEOUT)
    assert response.status_code == 201
    return response.json()


##########
### 40 TESTS FUER MAIN.PY
##########

# Testet, ob die Root-Route die erwartete Hello-World-Nachricht liefert.
def test_main_root_message():
    response = requests.get(f"{BASE_URL}/", timeout=TIMEOUT)
    
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


# Testet, ob ein normaler Name korrekt begruesst wird.
def test_main_name_greeting_normal_name():
    response = requests.get(f"{BASE_URL}/name/Jonas", timeout=TIMEOUT)
    
    assert response.status_code == 200
    assert response.json()["message"] == "Hello, Jonas!"


# Testet, ob ein Name mit Leerzeichen korrekt verarbeitet wird.
def test_main_name_greeting_with_space():
    response = requests.get(f"{BASE_URL}/name/Max%20Mustermann", timeout=TIMEOUT)
    
    assert response.status_code == 200
    assert response.json()["message"] == "Hello, Max Mustermann!"


# Testet, ob die Summe von zwei positiven Zahlen korrekt berechnet wird.
def test_main_summe_positive_numbers():
    response = requests.get(f"{BASE_URL}/summe/4/6", timeout=TIMEOUT)
    
    assert response.status_code == 200
    assert response.json()["message"] == "Die Summe aus 4 + 6 = 10"


# Testet, ob die Summe mit einer negativen Zahl korrekt berechnet wird.
def test_main_summe_negative_number():
    response = requests.get(f"{BASE_URL}/summe/-5/3", timeout=TIMEOUT)
    
    assert response.status_code == 200
    assert response.json()["message"] == "Die Summe aus -5 + 3 = -2"


# Testet, ob ungueltige Zahlen bei der Summe mit 422 abgelehnt werden.
def test_main_summe_invalid_number_returns_422():
    response = requests.get(f"{BASE_URL}/summe/a/3", timeout=TIMEOUT)
    
    assert response.status_code == 422


# Testet, ob queryparameters ohne Parameter die komplette Namensliste liefert.
def test_main_queryparameters_without_params():
    response = requests.get(f"{BASE_URL}/queryparameters", timeout=TIMEOUT)
    
    assert response.status_code == 200
    assert "Jonas" in response.json()["namen"]


# Testet, ob queryparameters mit param1 die Namen filtert.
def test_main_queryparameters_filter_name():
    response = requests.get(f"{BASE_URL}/queryparameters?param1=Jo", timeout=TIMEOUT)
    
    assert response.status_code == 200
    assert response.json()["param1"] == "Jo"
    assert "Jonas" in response.json()["namen"]


# Testet, ob eine neue Notiz erfolgreich angelegt werden kann.
def test_main_create_note_success():
    note = create_test_note(tags=["create-test"])
    
    assert "id" in note
    assert note["title"].startswith("Test Note")
    assert note["tags"] == ["create-test"]


# Testet, ob Tags beim Erstellen kleingeschrieben werden.
def test_main_create_note_tags_are_lowercase():
    note = create_test_note(tags=["Urgent", "WORK"])
    
    assert note["tags"] == ["urgent", "work"]


# Testet, ob doppelte Tags beim Erstellen entfernt werden.
def test_main_create_note_duplicate_tags_removed():
    note = create_test_note(tags=["Work", "work", "WORK"])
    
    assert note["tags"] == ["work"]


# Testet, ob leere Tags beim Erstellen ignoriert werden.
def test_main_create_note_empty_tags_ignored():
    note = create_test_note(tags=["", "   ", "valid"])
    
    assert note["tags"] == ["valid"]


# Testet, ob eine Notiz auch ohne Tags erstellt werden kann.
def test_main_create_note_without_tags():
    note_data = {
        "title": unique_text("No Tags"),
        "content": "Created without tags",
        "category": unique_text("no-tags-category")
    }
    response = requests.post(f"{BASE_URL}/notes", json=note_data, timeout=TIMEOUT)
    
    assert response.status_code == 201
    assert response.json()["tags"] == []


# Testet, ob eine Notiz ohne Pflichtfeld title mit 422 abgelehnt wird.
def test_main_create_note_missing_title_returns_422():
    note_data = {
        "content": "Missing title",
        "category": "validation",
        "tags": ["validation"]
    }
    response = requests.post(f"{BASE_URL}/notes", json=note_data, timeout=TIMEOUT)
    
    assert response.status_code == 422


# Testet, ob eine erstellte Notiz ueber ihre ID wieder geladen werden kann.
def test_main_get_note_by_id():
    note = create_test_note(tags=["get-by-id"])
    response = requests.get(f"{BASE_URL}/notes/{note['id']}", timeout=TIMEOUT)
    
    assert response.status_code == 200
    assert response.json()["id"] == note["id"]


# Testet, ob eine unbekannte Notiz-ID 404 liefert.
def test_main_get_unknown_note_returns_404():
    response = requests.get(f"{BASE_URL}/notes/999999999", timeout=TIMEOUT)
    
    assert response.status_code == 404


# Testet, ob die Notizenliste eine neu erstellte Notiz enthaelt.
def test_main_list_notes_contains_created_note():
    note = create_test_note(tags=["list-test"])
    response = requests.get(f"{BASE_URL}/notes", timeout=TIMEOUT)
    ids = [item["id"] for item in response.json()]
    
    assert response.status_code == 200
    assert note["id"] in ids


# Testet, ob Notizen nach Kategorie gefiltert werden koennen.
def test_main_list_notes_filter_by_category():
    category = unique_text("filter-category")
    note = create_test_note(category=category, tags=["category-filter"])
    response = requests.get(f"{BASE_URL}/notes?category={category}", timeout=TIMEOUT)
    ids = [item["id"] for item in response.json()]
    
    assert response.status_code == 200
    assert note["id"] in ids


# Testet, ob Notizen nach Suchbegriff im Titel gefunden werden.
def test_main_list_notes_filter_by_search_title():
    search_word = unique_text("specialtitle")
    note = create_test_note(title=search_word, tags=["search-title"])
    response = requests.get(f"{BASE_URL}/notes?search={search_word}", timeout=TIMEOUT)
    ids = [item["id"] for item in response.json()]
    
    assert response.status_code == 200
    assert note["id"] in ids


# Testet, ob Notizen nach Suchbegriff im Content gefunden werden.
def test_main_list_notes_filter_by_search_content():
    search_word = unique_text("specialcontent")
    note = create_test_note(content=f"Content mit {search_word}", tags=["search-content"])
    response = requests.get(f"{BASE_URL}/notes?search={search_word}", timeout=TIMEOUT)
    ids = [item["id"] for item in response.json()]
    
    assert response.status_code == 200
    assert note["id"] in ids


# Testet, ob Notizen nach Tag gefiltert werden koennen.
def test_main_list_notes_filter_by_tag():
    tag = unique_text("tagfilter")
    note = create_test_note(tags=[tag])
    response = requests.get(f"{BASE_URL}/notes?tag={tag}", timeout=TIMEOUT)
    ids = [item["id"] for item in response.json()]
    
    assert response.status_code == 200
    assert note["id"] in ids


# Testet, ob Kategorie und Tag gemeinsam als Filter funktionieren.
def test_main_list_notes_filter_by_category_and_tag():
    category = unique_text("combo-category")
    tag = unique_text("combo-tag")
    note = create_test_note(category=category, tags=[tag])
    response = requests.get(f"{BASE_URL}/notes?category={category}&tag={tag}", timeout=TIMEOUT)
    ids = [item["id"] for item in response.json()]
    
    assert response.status_code == 200
    assert note["id"] in ids


# Testet, ob created_after alte Notizen nicht ausschliesst, wenn das Datum sehr weit in der Vergangenheit liegt.
def test_main_list_notes_filter_created_after_past():
    note = create_test_note(tags=["created-after"])
    response = requests.get(f"{BASE_URL}/notes?created_after=1900-01-01", timeout=TIMEOUT)
    ids = [item["id"] for item in response.json()]
    
    assert response.status_code == 200
    assert note["id"] in ids


# Testet, ob created_before neue Notizen nicht ausschliesst, wenn das Datum sehr weit in der Zukunft liegt.
def test_main_list_notes_filter_created_before_future():
    note = create_test_note(tags=["created-before"])
    response = requests.get(f"{BASE_URL}/notes?created_before=2999-01-01", timeout=TIMEOUT)
    ids = [item["id"] for item in response.json()]
    
    assert response.status_code == 200
    assert note["id"] in ids


# Testet, ob die alte Kategorie-Route /notes/category/{category} funktioniert.
def test_main_get_notes_by_category_old_route():
    category = unique_text("old-category-route")
    note = create_test_note(category=category, tags=["old-category"])
    response = requests.get(f"{BASE_URL}/notes/category/{category}", timeout=TIMEOUT)
    ids = [item["id"] for item in response.json()]
    
    assert response.status_code == 200
    assert note["id"] in ids


# Testet, ob die Kategorienliste eine neu erstellte Kategorie enthaelt.
def test_main_list_categories_contains_created_category():
    category = unique_text("category-list")
    create_test_note(category=category, tags=["category-list"])
    response = requests.get(f"{BASE_URL}/categories", timeout=TIMEOUT)
    
    assert response.status_code == 200
    assert category in response.json()


# Testet, ob die neue Kategorien-Route /categories/{category}/notes funktioniert.
def test_main_get_notes_by_category_new_route():
    category = unique_text("new-category-route")
    note = create_test_note(category=category, tags=["new-category"])
    response = requests.get(f"{BASE_URL}/categories/{category}/notes", timeout=TIMEOUT)
    ids = [item["id"] for item in response.json()]
    
    assert response.status_code == 200
    assert note["id"] in ids


# Testet, ob die Tag-Liste einen neu erstellten Tag enthaelt.
def test_main_list_tags_contains_created_tag():
    tag = unique_text("tag-list")
    create_test_note(tags=[tag])
    response = requests.get(f"{BASE_URL}/tags", timeout=TIMEOUT)
    
    assert response.status_code == 200
    assert tag in response.json()


# Testet, ob Notizen ueber /tags/{tag}/notes gefunden werden.
def test_main_get_notes_by_tag_route():
    tag = unique_text("tag-route")
    note = create_test_note(tags=[tag])
    response = requests.get(f"{BASE_URL}/tags/{tag}/notes", timeout=TIMEOUT)
    ids = [item["id"] for item in response.json()]
    
    assert response.status_code == 200
    assert note["id"] in ids


# Testet, ob ein unbekannter Tag eine leere Liste liefert.
def test_main_get_notes_by_unknown_tag_returns_empty_list():
    tag = unique_text("unknown-tag")
    response = requests.get(f"{BASE_URL}/tags/{tag}/notes", timeout=TIMEOUT)
    
    assert response.status_code == 200
    assert response.json() == []


# Testet, ob eine Notiz komplett mit PUT aktualisiert werden kann.
def test_main_update_note_with_put():
    note = create_test_note(tags=["before-put"])
    update_data = {
        "title": "Updated PUT Title",
        "content": "Updated PUT Content",
        "category": "updated-put-category",
        "tags": ["after-put"]
    }
    response = requests.put(f"{BASE_URL}/notes/{note['id']}", json=update_data, timeout=TIMEOUT)
    
    assert response.status_code == 200
    assert response.json()["title"] == "Updated PUT Title"
    assert response.json()["tags"] == ["after-put"]


# Testet, ob PUT bei einer unbekannten Notiz-ID 404 liefert.
def test_main_update_unknown_note_returns_404():
    update_data = {
        "title": "Unknown",
        "content": "Unknown",
        "category": "unknown",
        "tags": ["unknown"]
    }
    response = requests.put(f"{BASE_URL}/notes/999999999", json=update_data, timeout=TIMEOUT)
    
    assert response.status_code == 404


# Testet, ob PATCH nur den Titel einer Notiz aktualisiert.
def test_main_patch_note_title_only():
    note = create_test_note(title="Before Patch", content="Content stays", tags=["patch-title"])
    response = requests.patch(
        f"{BASE_URL}/notes/{note['id']}",
        json={"title": "After Patch"},
        timeout=TIMEOUT
    )
    
    assert response.status_code == 200
    assert response.json()["title"] == "After Patch"
    assert response.json()["content"] == "Content stays"


# Testet, ob PATCH nur die Tags einer Notiz aktualisiert.
def test_main_patch_note_tags_only():
    note = create_test_note(tags=["old-patch-tag"])
    response = requests.patch(
        f"{BASE_URL}/notes/{note['id']}",
        json={"tags": ["New-Patch-Tag"]},
        timeout=TIMEOUT
    )
    
    assert response.status_code == 200
    assert response.json()["tags"] == ["new-patch-tag"]


# Testet, ob PATCH bei einer unbekannten Notiz-ID 404 liefert.
def test_main_patch_unknown_note_returns_404():
    response = requests.patch(
        f"{BASE_URL}/notes/999999999",
        json={"title": "Does not exist"},
        timeout=TIMEOUT
    )
    
    assert response.status_code == 404


# Testet, ob eine Notiz geloescht werden kann.
def test_main_delete_note_success():
    note = create_test_note(tags=["delete-test"])
    response = requests.delete(f"{BASE_URL}/notes/{note['id']}", timeout=TIMEOUT)
    
    assert response.status_code == 204


# Testet, ob eine geloeschte Notiz danach nicht mehr gefunden wird.
def test_main_deleted_note_returns_404_after_delete():
    note = create_test_note(tags=["delete-get-test"])
    delete_response = requests.delete(f"{BASE_URL}/notes/{note['id']}", timeout=TIMEOUT)
    get_response = requests.get(f"{BASE_URL}/notes/{note['id']}", timeout=TIMEOUT)
    
    assert delete_response.status_code == 204
    assert get_response.status_code == 404


# Testet, ob DELETE bei einer unbekannten Notiz-ID 404 liefert.
def test_main_delete_unknown_note_returns_404():
    response = requests.delete(f"{BASE_URL}/notes/999999999", timeout=TIMEOUT)
    
    assert response.status_code == 404


# Testet, ob der Statistik-Endpunkt die erwarteten Hauptfelder enthaelt.
def test_main_stats_contains_expected_keys():
    response = requests.get(f"{BASE_URL}/notes/stats", timeout=TIMEOUT)
    data = response.json()
    
    assert response.status_code == 200
    assert "total_notes" in data
    assert "by_category" in data
    assert "top_tags" in data
    assert "unique_tags_count" in data


# Testet, ob die Statistik eine neu erstellte Kategorie mitzaehlt.
def test_main_stats_counts_created_category():
    category = unique_text("stats-category")
    create_test_note(category=category, tags=["stats-category"])
    response = requests.get(f"{BASE_URL}/notes/stats", timeout=TIMEOUT)
    
    assert response.status_code == 200
    assert response.json()["by_category"][category] >= 1
