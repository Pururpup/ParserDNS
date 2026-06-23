from uuid import UUID
from sqlalchemy import UUID as PG_UUID, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from models.base import BaseTable


class Shop(BaseTable):
    __tablename__ = "shops"

    address: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )