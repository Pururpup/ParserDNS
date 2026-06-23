from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel
from schemas.base import BaseResponseSchema


class BrandCreateInSchema(BaseModel):
    brand_name: Annotated[str, MinLen(1), MaxLen(255)]


class BrandUpdateInSchema(BaseModel):
    brand_name: Annotated[str, MinLen(1), MaxLen(255)]


class BrandResponseSchema(BaseResponseSchema):
    brand_name: str