from datetime import datetime, timezone
from enum import Enum
from uuid import uuid4
from pydantic import BaseModel, Field

class Status(str, Enum):
    DRAFT = "draft"
    READY = "ready"
    APPROVED = "approved"
    RENDERING = "rendering"
    COMPLETE = "complete"
    FAILED = "failed"

class Scene(BaseModel):
    number: int
    narration: str
    visual_prompt: str
    duration_seconds: int = Field(ge=3, le=30)

class Episode(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    title: str
    lesson: str
    age_range: str = "4-8"
    status: Status = Status.DRAFT
    description: str = ""
    tags: list[str] = []
    scenes: list[Scene] = []
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class GenerateRequest(BaseModel):
    topic: str = Field(min_length=3, max_length=120)
    lesson: str = Field(default="kindness", min_length=3, max_length=80)
    age_range: str = "4-8"
    scene_count: int = Field(default=6, ge=3, le=12)

class ApprovalRequest(BaseModel):
    approved: bool
