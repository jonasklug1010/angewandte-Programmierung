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
from datetime import datetime, time
import json
from pathlib import Path
from typing import Optional

from sqlalchemy import func, or_
from sqlmodel import Session, select

from database import Note as DBNote
from database import NoteTagLink, SessionDep, Tag, create_db_and_tables, engine


app = FastAPI(
    title="Applied Programming Course HS-Coburg",
    description="Simple note managment API",
    version="1.0.0"
)

create_db_and_tables()
app.get("/")(root)
app.get("/name/{name}")(greet_name)
app.get("/summe/{zahl1}/{zahl2}")(add_age_numbers)


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

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[list[str]] = None


def note_to_response(note: DBNote) -> NoteResponse:
    return NoteResponse(
        id=note.id,
        title=note.title,
        content=note.content,
        category=note.category,
        tags=[tag.name for tag in note.tags],
        created_at=note.created_at.isoformat()
    )


def get_or_create_tags(tag_names: list[str], session: Session) -> list[Tag]:
    tag_objects = []
    seen_tags = set()
    
    for tag_name in tag_names:
        tag_name_lower = tag_name.lower().strip()
        if not tag_name_lower or tag_name_lower in seen_tags:
            continue
        
        seen_tags.add(tag_name_lower)
        
        statement = select(Tag).where(Tag.name == tag_name_lower)
        existing_tag = session.exec(statement).first()
        
        if existing_tag:
            tag_objects.append(existing_tag)
        else:
            new_tag = Tag(name=tag_name_lower)
            session.add(new_tag)
            tag_objects.append(new_tag)
    
    return tag_objects


def delete_unused_tags(session: Session) -> None:
    """Remove tags that are no longer connected to any note."""
    tags = session.exec(select(Tag)).all()
    
    for tag in tags:
        if not tag.notes:
            session.delete(tag)


def parse_created_at(created_at: str) -> datetime:
    try:
        return datetime.fromisoformat(created_at)
    except ValueError:
        return datetime.now()


NOTES_FILE = Path("data/notes.json")


def migrate_json_notes_to_database() -> None:
    """Migrate notes from data/notes.json into the SQLite database."""
    if not NOTES_FILE.exists():
        return
    
    with NOTES_FILE.open("r") as file:
        notes_data = json.load(file)
    
    with Session(engine) as session:
        for note_data in notes_data:
            note_id = note_data.get("id")
            db_note = session.get(DBNote, note_id) if note_id is not None else None
            
            if not db_note:
                db_note = DBNote(id=note_id)
            
            db_note.title = note_data["title"]
            db_note.content = note_data["content"]
            db_note.category = note_data["category"]
            db_note.created_at = parse_created_at(note_data["created_at"])
            db_note.tags = get_or_create_tags(note_data.get("tags", []), session)
            
            session.add(db_note)
        
        session.flush()
        delete_unused_tags(session)
        session.commit()


migrate_json_notes_to_database()
        
@app.post("/notes", status_code=201)
def create_note(note: NoteCreate, session: SessionDep) -> NoteResponse:
    """Create a new note in database"""
    
    db_note = DBNote(
        title=note.title,
        content=note.content,
        category=note.category
    )
    
    db_note.tags = get_or_create_tags(note.tags, session)
    
    session.add(db_note)
    session.commit()
    session.refresh(db_note)
    
    return note_to_response(db_note)

@app.get("/notes")
def list_notes(
    *,
    category: str = None,
    search: str = None,
    tag: str = None,
    created_after: str = None,
    created_before: str = None,
    session: SessionDep
) -> list[NoteResponse]:
    ######### Änderung Tag 3 Hausaufgabe 
    statement = select(DBNote)
    
    if category:
        statement = statement.where(DBNote.category == category)
    
    if search:
        search_like = f"%{search.lower()}%"
        statement = statement.where(
            or_(
                func.lower(DBNote.title).like(search_like),
                func.lower(DBNote.content).like(search_like)
            )
        )
    
    if tag:
        tag_lower = tag.lower().strip()
        statement = (
            statement
            .join(NoteTagLink, DBNote.id == NoteTagLink.note_id)
            .join(Tag, Tag.id == NoteTagLink.tag_id)
            .where(Tag.name == tag_lower)
        )
    
    if created_after:
        statement = statement.where(DBNote.created_at >= parse_created_at(created_after))
    
    if created_before:
        created_before_value = parse_created_at(created_before)
        if len(created_before) == 10:
            created_before_value = datetime.combine(created_before_value.date(), time.max)
        
        statement = statement.where(DBNote.created_at <= created_before_value)
    
    notes_db = session.exec(statement).all()
    return [note_to_response(note) for note in notes_db]
    
@app.get("/notes/stats")
def get_notes_stats(session: SessionDep):
    """
    Get statistics about notes
    
    Returns:
    - Total notes
    - Notes per category
    - Most used tags (top 5)
    - Total number of unique tags
    """
    total_notes = session.exec(select(func.count(DBNote.id))).one()
    
    category_rows = session.exec(
        select(DBNote.category, func.count(DBNote.id))
        .group_by(DBNote.category)
    ).all()
    categories = {category: count for category, count in category_rows}
    
    tag_rows = session.exec(
        select(Tag.name, func.count(NoteTagLink.note_id))
        .join(NoteTagLink, Tag.id == NoteTagLink.tag_id)
        .group_by(Tag.name)
        .order_by(func.count(NoteTagLink.note_id).desc(), Tag.name)
        .limit(5)
    ).all()
    
    top_tags = []
    for tag, count in tag_rows:
        top_tags.append({
            "tag": tag,
            "count": count
        })
    
    unique_tags_count = session.exec(select(func.count(Tag.id))).one()
    
    return {
        "total_notes": total_notes,
        "by_category": categories,
        "top_tags": top_tags,
        "unique_tags_count": unique_tags_count
    }


@app.get("/notes/category/{category}")
def get_notes_by_category(category: str, session: SessionDep) -> list[NoteResponse]:
    """Get all notes in a specific category"""
    statement = select(DBNote).where(DBNote.category == category)
    notes_db = session.exec(statement).all()
    return [note_to_response(note) for note in notes_db]


@app.get("/notes/{note_id}")
def get_note(note_id: int, session: SessionDep) -> NoteResponse:
    """Get a specific note by ID"""
    note = session.get(DBNote, note_id)
    if note:
        return note_to_response(note)
    
    raise HTTPException(
        status_code=404,
        detail=f"Note with ID {note_id} not found"
    )


@app.put("/notes/{note_id}")
def update_note(note_id: int, note_update: NoteCreate, session: SessionDep) -> NoteResponse:
    """Update an existing note"""
    note = session.get(DBNote, note_id)
    if not note:
        raise HTTPException(
            status_code=404,
            detail=f"Note with ID {note_id} not found"
        )
    
    note.title = note_update.title
    note.content = note_update.content
    note.category = note_update.category
    note.tags = get_or_create_tags(note_update.tags, session)
    
    session.add(note)
    session.flush()
    delete_unused_tags(session)
    session.commit()
    session.refresh(note)
    return note_to_response(note)


@app.patch("/notes/{note_id}")
def partial_update_note(note_id: int, note_update: NoteUpdate, session: SessionDep) -> NoteResponse:
    """
    Partially update a note (only provided fields)
    
    Unlike PUT, PATCH only updates fields you provide
    """
    note = session.get(DBNote, note_id)
    if not note:
        raise HTTPException(
            status_code=404,
            detail=f"Note with ID {note_id} not found"
        )
    
    if note_update.title is not None:
        note.title = note_update.title
    
    if note_update.content is not None:
        note.content = note_update.content
    
    if note_update.category is not None:
        note.category = note_update.category
    
    if note_update.tags is not None:
        note.tags = get_or_create_tags(note_update.tags, session)
    
    session.add(note)
    session.flush()
    delete_unused_tags(session)
    session.commit()
    session.refresh(note)
    return note_to_response(note)


@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int, session: SessionDep):
    """Delete a note"""
    note = session.get(DBNote, note_id)
    if not note:
        raise HTTPException(
            status_code=404,
            detail=f"Note with ID {note_id} not found"
        )
    
    session.delete(note)
    session.flush()
    delete_unused_tags(session)
    session.commit()
    return


@app.get("/categories")
def list_categories(session: SessionDep) -> list[str]:
    """Get all unique categories from all notes"""
    statement = select(DBNote.category).distinct().order_by(DBNote.category)
    categories = session.exec(statement).all()
    return list(categories)


@app.get("/categories/{category_name}/notes")
def get_notes_by_category_name(category_name: str, session: SessionDep) -> list[NoteResponse]:
    """Get all notes in a specific category"""
    statement = select(DBNote).where(DBNote.category == category_name)
    notes_db = session.exec(statement).all()
    return [note_to_response(note) for note in notes_db]


@app.get("/tags")
def list_tags(session: SessionDep) -> list[str]:
    """Get all unique tags from the Tag table"""
    statement = select(Tag)
    tags = session.exec(statement).all()
    
    return sorted([tag.name for tag in tags])


@app.get("/tags/{tag_name}/notes")
def get_notes_by_tag(tag_name: str, session: SessionDep) -> list[NoteResponse]:
    """Get all notes with specific tag"""
    
    # Find the tag (case-insensitive)
    tag_lower = tag_name.lower()
    statement = select(Tag).where(Tag.name == tag_lower)
    tag = session.exec(statement).first()
    
    if not tag:
        return []  # No notes if tag doesn't exist
    
    # Return all notes associated with this tag
    return [
        note_to_response(note)
        for note in tag.notes
    ]


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
