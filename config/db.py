from sqlalchemy import create_engine, MetaData

engine=create_engine("mysql+pymysql://username:password@localhost:3306/database")

meta=MetaData()
conn = engine.connect()