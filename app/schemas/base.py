from datetime import datetime
from pydantic import BaseModel, ConfigDict
from uuid import UUID


class BaseResponseSchema(BaseModel):
    id: UUID
    created_at: datetime
    updated_at: datetime
    is_deleted: bool

    model_config = ConfigDict(from_attributes=True)