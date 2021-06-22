from schemas.Contact import UserContact
from fastapi import APIRouter
from config.db import conn
from models.ContactVO import contact

router= APIRouter()

@router.get("/")
async def readData():
    return conn.execute(contact.select()).fetchall()

@router.get("/{contactId}")
async def readDataById(contactId :int):
    return conn.execute(contact.select().where(contact.c.contactId == contactId)).fetchall()

@router.post("/")
async def newUser(user: UserContact):
    conn.execute(contact.insert().values(
        fullName=user.fullName,
        gender=user.gender
    ))
    return conn.execute(contact.select()).fetchall()


@router.put("/")
async def updateUser(contactId :int, user: UserContact):
    conn.execute(contact.update().values(
        fullName=user.fullName, 
        gender=user.gender
    )).where(contact.c.contactId==contactId)
    return conn.execute(contact.select()).fetchall()

@router.delete("/{contactId}")
async def deleteUser(contactId:int):
    conn.execute(contact.delete().where(contact.c.contactId==contactId))
    return conn.execute(contact.select()).fetchall()

