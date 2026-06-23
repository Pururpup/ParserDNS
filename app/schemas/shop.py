from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel
from schemas.base import BaseResponseSchema


class ShopCreateInSchema(BaseModel):
    address: Annotated[str, MinLen(1), MaxLen(255)]


class ShopUpdateInSchema(BaseModel):
    address: Annotated[str, MinLen(1), MaxLen(255)]


class ShopResponseSchema(BaseResponseSchema):
    address: str