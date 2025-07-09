from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class DatasetSchema(BaseModel):
    name: str
    owner: str
    description: Optional[str] = ""
    tags: List[str]

class QualityLogSchema(BaseModel):
    status: str  # 'PASS' or 'FAIL'
    details: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
