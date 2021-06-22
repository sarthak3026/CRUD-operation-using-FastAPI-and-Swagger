from sqlalchemy.sql.schema import Column, Table
from sqlalchemy.sql.sqltypes import INTEGER, String
from config.db import meta

contact= Table(
    'contact' , meta, 
    Column('contactId', INTEGER, primary_key=True),
    Column('fullName', String(255)),
    Column('gender', String(255))
)
