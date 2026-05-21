from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models.user import User
from models.profile import Profile
from models.category import Category
from models.product import Product
from models.order import Order

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)

with Session(engine) as session:

    user1 = User(
        name="Dmytro",
        email="dmytro@gmail.com"
    )

    user2 = User(
        name="Bogdana",
        email="bogdana@gmail.com"
    )

    session.add_all([user1, user2])
    session.commit()

    profile1 = Profile(
        bio="Student",
        user_id=1
    )

    profile2 = Profile(
        bio="Developer",
        user_id=2
    )

    category1 = Category(
        name="Electronics"
    )

    category2 = Category(
        name="Clothes"
    )

    session.add_all([
        profile1,
        profile2,
        category1,
        category2
    ])

    session.commit()

    product1 = Product(
        title="Laptop",
        price=25000,
        category_id=1
    )

    product2 = Product(
        title="Phone",
        price=15000,
        category_id=1
    )

    order1 = Order(
        status="created",
        user_id=1
    )

    order2 = Order(
        status="completed",
        user_id=2
    )

    session.add_all([
        product1,
        product2,
        order1,
        order2
    ])

    session.commit()

print("Done")