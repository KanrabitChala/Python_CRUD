from fastapi import APIRouter,HTTPException
from config.db import conn,engine
from models.index import users
from schemas.index import User
user = APIRouter()

# @user.get("/")
# async def read_data():
#     return conn.execute(users.select()).fetchall()
@user.get("/")
def read_data():
    with engine.connect() as conn:
        result = conn.execute(users.select())
        return [dict(row._mapping) for row in result.fetchall()]
    
@user.get("/{id}")
async def read_data(id: int):
    return conn.execute(users.select().where(users.c.id==id)).fetchall()

# @user.post("/")
# async def write_data(user: User):
#     conn.execute(users.insert().values(
#         name=user.name,
#         email=user.email,
#         password=user.password
#     ))
#     return conn.execute(users.select()).fetchall()

@user.post("/")
def write_data(user: User):
    with engine.begin() as conn:
        result = conn.execute(
            users.insert().values(
                name=user.name,
                email=user.email,
                password=user.password
            )
        )

        new_id = result.inserted_primary_key[0]

        saved_user = conn.execute(
            users.select().where(users.c.id == new_id)
        ).fetchone()

        return dict(saved_user._mapping)
    

@user.put("/{id}")
async def update_data(id: int, user: User):
    conn.execute(
        users.update().where(users.c.id == id).values(
            name=user.name,
            email=user.email,
            password=user.password
        )
    )
    conn.commit()
    # return conn.execute(users.select()).fetchall()
    return [dict(row._mapping) for row in conn.execute(users.select()).fetchall()]

@user.delete("/{id}")
async def read_data():
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select()).fetchall()