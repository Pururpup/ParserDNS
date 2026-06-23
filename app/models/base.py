from sqlalchemy.orm import DeclarativeBase
from uuid import UUID, uuid4
from sqlalchemy import UUID as PG_UUID, DateTime, func, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class Base(DeclarativeBase):
    pass


class BaseTable(Base):
    __abstract__ = True

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )