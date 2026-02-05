from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from datetime import date
from typing import List, Optional
from .models import JournalEntry
from schemas.journal import JournalUpsertRequest, JournalEntryResponse

def get_entry_by_user_and_date(db: Session, user_id: int, entry_date: date):
    return (db.query(JournalEntry).filter(
        JournalEntry.user_id == user_id,
        JournalEntry.date == entry_date
    )
    .first()
    )

def upsert_entry(db: Session, user_id: int, date, content: str):
    entry = get_entry_by_user_and_date(db, user_id, date)

    if entry:
        entry.content = content
    else:
        entry = JournalEntry(user_id=user_id, date=date, content=content)
        db.add(entry)

    db.commit()
    db.refresh(entry)
    return entry

def get_entries_in_range(db: Session, user_id: int, start_date: date, end_date: date):
    return (db.query(JournalEntry)
            .filter(
                JournalEntry.user_id == user_id,
                JournalEntry.date >= start_date,
                JournalEntry.date <= end_date
            )
            .order_by(JournalEntry.date).all()
    )