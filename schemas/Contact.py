from pydantic import BaseModel

class UserContact(BaseModel):
    fullName: str
    gender: str
    country: int
    countryCode: int 
    state: str
    stateCode: str
    city: str
    cityCode: str
    address1: str
    address2: str
    adress3: str
    zip: str
    lanCode: str
    lang: str
    primaryContact: str
    secondaryContact: str