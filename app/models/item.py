from uuid import UUID
from sqlalchemy import UUID as PG_UUID, String, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column
from models.base import BaseTable


class Item(BaseTable):
    __tablename__ = "items"

    item_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    external_id: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
    )

    category_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("categories.id"),
        nullable=False,
    )

    brand_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("brands.id"),
        nullable=False,
    )

    shop_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("shops.id"),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )