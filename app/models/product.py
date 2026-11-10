import uuid
from decimal import Decimal
from sqlalchemy import Numeric, Uuid, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.mixins import TimestampMixin
from app.db.base import Base


class Product(Base, TimestampMixin):
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
    owner_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    owner: Mapped["User"] = relationship(
        back_populates="products"
    )

