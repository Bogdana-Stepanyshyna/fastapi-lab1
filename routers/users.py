from fastapi import APIRouter
from schemas.user import User

router = APIRouter()

users_db = {}


@router.post("/users")
def create_user(user: User):
    users_db[user.id] = user
    return user


@router.get("/users")
def get_users():
    return users_db


@router.get("/users/{user_id}")
def get_user(user_id: int):
    return users_db.get(user_id)


@router.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    users_db[user_id] = user
    return user


from fastapi import HTTPException

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return users_db.pop(user_id)