from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.base import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    title: Mapped[str] = mapped_column(
        String
    )

    price: Mapped[int] = mapped_column(
        Integer
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id")
    )

    category = relationship(
        "Category",
        back_populates="products"
    )