import uuid
from sqlalchemy import String, Uuid, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.mixins import TimestampMixin
from app.db.base import Base


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id:Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email:Mapped[str]= mapped_column(
        String(255),
        nullable=False,
        unique=True
    )

    hashed_password: Mapped[str] = mapped_column(
        String(256),
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True
    )
    avatar: Mapped[str] = mapped_column(
        String,
        nullable=True
    )

    products : Mapped[list["Products"]] = relationship(
        back_populates="owner",
        lazy="raise",
        cascade="all, delete-orphan"
    )
