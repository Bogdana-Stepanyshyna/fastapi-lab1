from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String
    )

    email: Mapped[str] = mapped_column(
        String,
        unique=True
    )

    profile = relationship(
        "Profile",
        back_populates="user",
        uselist=False
    )

    orders = relationship(
        "Order",
        back_populates="user"
    )