from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import BaseTable


class Category(BaseTable):
    __tablename__ = "categories"

    category_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )