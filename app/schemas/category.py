from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel
from schemas.base import BaseResponseSchema


class CategoryCreateInSchema(BaseModel):
    category_name: Annotated[str, MinLen(1), MaxLen(255)]


class CategoryUpdateInSchema(BaseModel):
    category_name: Annotated[str, MinLen(1), MaxLen(255)]


class CategoryResponseSchema(BaseResponseSchema):
    category_name: str