from pydantic import BaseModel
from typing import Optional

class Habit(BaseModel):
    id: Optional[str]
    name: str
    description: Optional[str] = None
    is_complete: bool = False
