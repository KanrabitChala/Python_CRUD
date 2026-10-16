from sqlalchemy import create_engine,MetaData

engine = create_engine("mysql+pymys://root@localhost:3306/test")
meta = MetaData()
conn = engine.connect()