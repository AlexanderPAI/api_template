from datetime import datetime

from typing import Dict, Any, Optional

from pydantic import BaseModel, Field


class Data(BaseModel):
    data_id: int = Field(..., examples=[1, 2, 333], alias="id", title="Айдишник", description="Очень важная херня")
    data: str
    comment: Optional[str] = None


class DataResponse(BaseModel):
    new_data: str = Field(..., examples=["this is new data", "this is new data", "this is new data"], title="то, что возвращается")