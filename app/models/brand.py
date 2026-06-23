from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import BaseTable


class Brand(BaseTable):
    __tablename__ = "brands"

    brand_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )