from pydantic import BaseModel


class ParserItemSchema(BaseModel):
    title: str
    entity_id: str
    code: str
    description: str
    category_name: str
    address: str
    brand_name: str