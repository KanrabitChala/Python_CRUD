from models.user import users
from config.db import engine, meta

meta.create_all(engine)