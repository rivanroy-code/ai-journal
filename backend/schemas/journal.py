from pydantic import BaseModel, Field
from datetime import date, datetime

class JournalUpsertRequest(BaseModel):
    date:date
    content:str=Field(min_length=1, max_length=50000)

class JournalEntryResponse(BaseModel):
    id:int
    user_id:int
    date:date
    content:str
    created_at:datetime
    updated_at:datetime | None

    class Config:
        from_attributes = True

class JournalListResponse(BaseModel):
    entries:list[JournalEntryResponse]