from pydantic import BaseModel,EmailStr
from typing import List, Dict, Optional

class patient(BaseModel):

    name:str
    age:int
    Email:EmailStr
    weight:float
    married:Optional[bool]=False
    allergies:Optional[List[str]]=None
    contacts_details:Dict[str,str]

def insert_patient_info(patient: patient):
    print(patient.name)
    print(patient.Email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contacts_details)
    print('updated')


patient_info = {'name':'dk','Email':'abc@gmail.com','age':'22','weight':'67.0','married':'true','contacts_details':{'phone_no':'0987654321'}}

patient1 = patient(**patient_info)

insert_patient_info(patient1)