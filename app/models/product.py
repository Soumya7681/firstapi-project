import uuid
from decimal import Decimal
from sqlalchemy import Numeric, Uuid, String, ForeignKey, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.mixins import TimestampMixin
from app.db.base import Base


class Product(TimestampMixin, Base):
    __tablename__ = "products"

    id:Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True
    )
    price: Mapped[Decimal] = mapped_column(
        Numeric(10,2),
        nullable=False
    )
    description: Mapped[str] = mapped_column(
        Text,
        nullable=True
    )
    stock : Mapped[int] = mapped_column(
        Integer,
        default=0,
        server_default="0"
    )
    image_path : Mapped[str] = mapped_column(
        String,
        nullable=True
    )
    owner_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    owner: Mapped["User"] = relationship(
        back_populates="products",
        lazy="raise"
    )

