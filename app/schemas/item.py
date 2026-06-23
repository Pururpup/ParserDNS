from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel
from uuid import UUID
from schemas.base import BaseResponseSchema


class ItemCreateInSchema(BaseModel):
    item_name: Annotated[str, MinLen(1), MaxLen(255)]
    category_id: UUID
    brand_id: UUID
    shop_id: UUID
    description: Annotated[str, MinLen(1), MaxLen(255)]


class ItemUpdateInSchema(BaseModel):
    item_name: Annotated[str, MinLen(1), MaxLen(255)] | None = None
    category_id: UUID | None = None
    brand_id: UUID | None = None
    shop_id: UUID | None = None
    description: Annotated[str, MinLen(1), MaxLen(255)] | None = None


class ItemResponseSchema(BaseResponseSchema):
    item_name: str
    category_id: UUID
    brand_id: UUID
    shop_id: UUID
    description: str