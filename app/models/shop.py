from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from models.base import BaseTable


class Shop(BaseTable):
    __tablename__ = "shops"

    address: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )