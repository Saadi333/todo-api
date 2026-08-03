from pydantic import BaseModel, Field
from datetime import datetime

# Schema for creating todo
class TodoCreate(BaseModel):
    title: str = Field(min_length=2, max_length=100, description="Todo title")
    description: str = Field(min_length=3, max_length=500, description="Todo details")
    completed: bool = False

# Schema for updating todo
class TodoUpdate(BaseModel):
    title: str | None = Field(None, min_length=2, max_length=100)
    description: str | None = Field(None, min_length=3, max_length=500)
    completed: bool | None = None