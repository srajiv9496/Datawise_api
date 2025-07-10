from pydantic import BaseModel, Field
from typing import List, Optional

class DatasetCreateModel(BaseModel):
    name: str = Field(..., example="Sales Data 2024")
    owner: str = Field(..., example="rajiv")
    description: Optional[str] = Field("", example="Q1 dataset")
    tags: List[str] = Field(..., example=["finance", "q1"])

class DatasetUpdateModel(BaseModel):
    name: Optional[str]
    owner: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
