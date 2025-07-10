from pydantic import BaseModel, Field
from typing import Optional

class QualityLogCreateModel(BaseModel):
    status: str = Field(..., regex="^(PASS|FAIL)$")
    details: Optional[str] = ""
