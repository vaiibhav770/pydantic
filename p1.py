from pydantic import BaseModel
from typing import List, Dict, Optional

class patient(BaseModel):

    name:str
    age:int
    weight:float
    married:Optional[bool]=None
    allergies:Optional[List[str]]=None
    contacts_details:Dict[str,str]

def insert_patient_info(patient: patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contacts_details)
    print('updated')


patient_info = {'name':'dk','age':'22','weight':'67.0','married':'true','contacts_details':{'email':'abc@gmail.com','phone_no':'0987654321'}}

patient1 = patient(**patient_info)

insert_patient_info(patient1)