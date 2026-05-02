from datetime import datetime
from typing import Annotated, Optional

from fastapi import Depends
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine


class NoteTagLink(SQLModel, table=True):
    __tablename__ = "note_tag_link"

    note_id: Optional[int] = Field(default=None, foreign_key="notes.id", primary_key=True)
    tag_id: Optional[int] = Field(default=None, foreign_key="tags.id", primary_key=True)


class Note(SQLModel, table=True):
    __tablename__ = "notes"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    category: str
    created_at: datetime = Field(default_factory=datetime.now)

    tags: list["Tag"] = Relationship(back_populates="notes", link_model=NoteTagLink)


class Tag(SQLModel, table=True):
    __tablename__ = "tags"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)

    notes: list[Note] = Relationship(back_populates="tags", link_model=NoteTagLink)


engine = create_engine("sqlite:///notes.db", connect_args={"check_same_thread": False})


def create_db_and_tables() -> None:
    """Create database tables for notes, tags, and their link table."""
    SQLModel.metadata.create_all(engine)


def get_session():
    """Create a new database session for each request."""
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


if __name__ == "__main__":
    create_db_and_tables()
