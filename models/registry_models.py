from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel, HttpUrl
from models.enums import FileType, SourceStatus

class RawSource(BaseModel):
    id: str
    name: str
    landing_url: HttpUrl
    notes: Optional[str] = None

class ResolvedSource(BaseModel):
    dataset_id: str
    file_url: HttpUrl
    file_type: FileType
    status: SourceStatus
    scanned_at: datetime
    columns_sample: Optional[list[str]] = None
    valid: bool = True
    extra_metadata: dict[str, Any] = {}
