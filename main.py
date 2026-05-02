###############################
### Hochschule (Day1)
###############################

#Tag 1
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, World!"}


@app.get("/name/{name}")
def greet_name(name:str):
    return {"message": f"Hello, {name}!"}





###################################
### Hausaufgabe (Day1)
###################################


@app.get("/summe/{zahl1}/{zahl2}")
def add_age_numbers(zahl1:int, zahl2:int):
    ergebnis = zahl1 + zahl2
    return {"message": f"Die Summe aus {zahl1} + {zahl2} = {ergebnis}"}


###################################
### Hochschule (Day2)
###################################


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Optional

from sqlmodel import select

from database import Note as DBNote
from database import SessionDep, Tag, create_db_and_tables


app = FastAPI(
    title="Applied Programming Course HS-Coburg",
    description="Simple note managment API",
    version="1.0.0"
)

create_db_and_tables()


# API Input model
class NoteCreate(BaseModel):
    title: str
    content: str
    category: str
    tags: list[str] = []


# API Output model
class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    category: str
    tags: list[str]
    created_at: str
    
    class Config:
        from_attributes = True

class Note(BaseModel):
    id: int
    title: str
    content: str
    category: str
    tags: list[str] = []
    created_at: str

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[list[str]] = None
    
NOTES_FILE = Path("data/notes.json")

def load_notes():
    """Load notes from JSON file and return notes list and next ID"""
    notes_db = []
    note_id_counter = 1

    if NOTES_FILE.exists():
        with open(NOTES_FILE, 'r') as f:
            data = json.load(f)
            notes_db = [Note(**note) for note in data]

            # Set counter to max ID + 1
            if notes_db:
                note_id_counter = max(note.id for note in notes_db) + 1

    return notes_db, note_id_counter


def save_notes(notes_db):
    """Save notes to JSON file after each change"""
    
    # Ensure data directory exists
    NOTES_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(NOTES_FILE, 'w') as f:
        
        # Convert Note objects to dicts
        notes_data = [note.dict() for note in notes_db]
        json.dump(notes_data, f, indent=2)
        
@app.post("/notes", status_code=201)
def create_note(note: NoteCreate, session: SessionDep) -> NoteResponse:
    """Create a new note in database"""
    
    # Create note
    db_note = DBNote(
        title=note.title,
        content=note.content,
        category=note.category
    )
    
    # Get or create tags (case-insensitive, deduplicated)
    tag_objects = []
    seen_tags = set()
    
    for tag_name in note.tags:
        tag_name_lower = tag_name.lower().strip()
        if not tag_name_lower or tag_name_lower in seen_tags:
            continue
        
        seen_tags.add(tag_name_lower)
        
        # Find existing tag or create new one
        statement = select(Tag).where(Tag.name == tag_name_lower)
        existing_tag = session.exec(statement).first()
        
        if existing_tag:
            tag_objects.append(existing_tag)
        else:
            new_tag = Tag(name=tag_name_lower)
            session.add(new_tag)
            tag_objects.append(new_tag)
    
    db_note.tags = tag_objects
    
    session.add(db_note)
    session.commit()
    session.refresh(db_note)
    
    return NoteResponse(
        id=db_note.id,
        title=db_note.title,
        content=db_note.content,
        category=db_note.category,
        tags=[tag.name for tag in db_note.tags],
        created_at=db_note.created_at.isoformat()
    )

@app.get("/notes")
def list_notes(
    category: str = None,
    search: str = None,
    tag: str = None,
    created_after: str = None,
    created_before: str = None
) -> list[Note]:
    ######### Änderung Tag 3 Hausaufgabe 
    notes_db, _ = load_notes()
    
    
    filtered = []
    for note in notes_db:
        
        if category and note.category != category:
            continue
        
        
        if search:
            search_lower = search.lower()
            title_match = search_lower in note.title.lower()
            content_match = search_lower in note.content.lower()
            if not (title_match or content_match):
                continue
        
        
        if tag and tag not in note.tags:
            continue

        if created_after and note.created_at < created_after:
            continue  

        if created_before and note.created_at > created_before:
            continue  
        
        filtered.append(note)
    
    return filtered
    
###################################
### Hausaufgabe (Day2)
###################################

notes_db, note_id_counter = load_notes()
save_notes_day2 = save_notes

def save_notes(notes_db_to_save=None):
    global notes_db, note_id_counter

    if notes_db_to_save is None:
        notes_db_to_save = notes_db
    else:
        notes_db = notes_db_to_save
        if notes_db:
            note_id_counter = max(note.id for note in notes_db) + 1
        else:
            note_id_counter = 1

    save_notes_day2(notes_db_to_save)



def create_note(note: NoteCreate):
    global note_id_counter
    
    new_note = Note(
        id=note_id_counter,
        title=note.title,
        content=note.content,
        category=note.category,  
        tags=note.tags,
        created_at=datetime.now().isoformat()
    )
    
    notes_db.append(new_note)
    note_id_counter += 1
    
    save_notes()  
    return new_note


@app.get("/notes/stats")
def get_notes_stats():
    """
    Get statistics about notes
    
    Returns:
    - Total notes
    - Notes per category
    - Most used tags (top 5)
    - Total number of unique tags
    """
    notes_db, _ = load_notes()
    
    # Count by category
    categories = {}
    for note in notes_db:
        if note.category in categories:
            categories[note.category] += 1
        else:
            categories[note.category] = 1
    
    # Count tags
    tags = {}
    for note in notes_db:
        for tag in note.tags:
            if tag in tags:
                tags[tag] += 1
            else:
                tags[tag] = 1
    
    top_tags = []
    sorted_tags = sorted(tags.items(), key=lambda item: item[1], reverse=True)
    for tag, count in sorted_tags[:5]:
        top_tags.append({
            "tag": tag,
            "count": count
        })
    
    return {
        "total_notes": len(notes_db),
        "by_category": categories,
        "top_tags": top_tags,
        "unique_tags_count": len(tags)
    }


@app.get("/notes/category/{category}")
def get_notes_by_category(category: str):
    """Get all notes in a specific category"""
    filtered_notes = []
    
    for note in notes_db:
        if note.category == category:
            filtered_notes.append(note)
    
    return filtered_notes


@app.get("/notes/{note_id}")
def get_note(note_id: int):
    """Get a specific note by ID"""
    for note in notes_db:
        if note.id == note_id:
            return note
    
    # Not found - raise 404 error
    raise HTTPException(
        status_code=404,
        detail=f"Note with ID {note_id} not found"
    )


@app.put("/notes/{note_id}")
def update_note(note_id: int, note_update: NoteCreate) -> Note:
    """Update an existing note"""
    
    notes_db, _ = load_notes()
    
    
    for i, note in enumerate(notes_db):
        if note.id == note_id:
            
            updated_note = Note(
                id=note.id,
                title=note_update.title,
                content=note_update.content,
                category=note_update.category,
                tags=note_update.tags,
                created_at=note.created_at
            )
            
            notes_db[i] = updated_note
            save_notes(notes_db)
            return updated_note
    
    
    raise HTTPException(
        status_code=404,
        detail=f"Note with ID {note_id} not found"
    )


@app.patch("/notes/{note_id}")
def partial_update_note(note_id: int, note_update: NoteUpdate) -> Note:
    """
    Partially update a note (only provided fields)
    
    Unlike PUT, PATCH only updates fields you provide
    """
    notes_db, _ = load_notes()
    
    for i, note in enumerate(notes_db):
        if note.id == note_id:
            if note_update.title is not None:
                note.title = note_update.title
            
            if note_update.content is not None:
                note.content = note_update.content
            
            if note_update.category is not None:
                note.category = note_update.category
            
            if note_update.tags is not None:
                note.tags = note_update.tags
            
            notes_db[i] = note
            save_notes(notes_db)
            return note
    
    raise HTTPException(
        status_code=404,
        detail=f"Note with ID {note_id} not found"
    )


@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int):
    """Delete a note"""
    
    notes_db, _ = load_notes()
    
    #
    for i, note in enumerate(notes_db):
        if note.id == note_id:
            notes_db.pop(i)
            save_notes(notes_db)
            return  
    
    
    raise HTTPException(
        status_code=404,
        detail=f"Note with ID {note_id} not found"
    )


@app.get("/categories")
def list_categories() -> list[str]:
    """Get all unique categories from all notes"""
    notes_db, _ = load_notes()
    
    categories = set()
    for note in notes_db:
        categories.add(note.category)
    
    return sorted(list(categories))


@app.get("/categories/{category_name}/notes")
def get_notes_by_category_name(category_name: str) -> list[Note]:
    """Get all notes in a specific category"""
    
    notes_db, _ = load_notes()
    
    filtered = []
    for note in notes_db:
        if note.category == category_name:
            filtered.append(note)
    
    return filtered


@app.get("/tags")
def list_tags() -> list[str]:
    """Get all unique tags from all notes"""
    
    notes_db, _ = load_notes()
    
    
    all_tags = set()
    for note in notes_db:
        for tag in note.tags:
            all_tags.add(tag)
    
    
    return sorted(list(all_tags))


@app.get("/tags/{tag_name}/notes")
def get_notes_by_tag(tag_name: str) -> list[Note]:
    """Get all notes with a specific tag"""
    
    notes_db, _ = load_notes()
    
    filtered = []
    for note in notes_db:
        if tag_name in note.tags:
            filtered.append(note)
    
    return filtered


###################################
### Hochschule (Day3)
###################################


@app.get("/queryparameters")
def query_parameters(param1: str = None, param2: int = None) -> dict:
    
    namen = ["Jonas", "Anna", "Johannes", "Maria", "Jörg"]
    
    if not param1:
        return {"namen": namen}
    
    namen_gefiltert = []
    for name in namen:
        if param1 and param1 in name:
            namen_gefiltert.append(name)
    
    return {
        "param1": param1, 
        "param2": param2,
        "namen": namen_gefiltert
    }
