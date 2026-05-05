from datetime import datetime
import re
from typing import Annotated, Optional

from fastapi import Depends
from pydantic import field_validator
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine


TAG_NAME_PATTERN = re.compile(r"^[a-z0-9-]+$")


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
    name: str = Field(unique=True, index=True, min_length=2, max_length=30)

    notes: list[Note] = Relationship(back_populates="tags", link_model=NoteTagLink)
    
    @field_validator("name", mode="before")
    @classmethod
    def normalize_name(cls, value):
        if isinstance(value, str):
            return value.strip().lower()
        return value
    
    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        if not TAG_NAME_PATTERN.fullmatch(value):
            raise ValueError("Tag name may only contain lowercase letters, digits, and dashes")
        return value


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
