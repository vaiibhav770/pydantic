from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List, Dict, Optional,Annotated

class patient(BaseModel):

    name:Annotated[str,Field(max_length=50, title='Name of the patient',description='Give the name of the patient in less than 50 words',examples=['nitish','amit'])]
    age:int=Field(gt=0,lt=120)
    Email:EmailStr
    weight:float=Field(gt=0)
    linkdin_url:AnyUrl
    married:Annotated[bool,Field(default=None,description='is the patient married or not?')]
    allergies:Optional[List[str]]=Field(default=None,max_length=5)
    contacts_details:Dict[str,str]

def insert_patient_info(patient: patient):
    print(patient.name)
    print(patient.Email)
    print(patient.age)
    print(patient.weight)
    print(patient.linkdin_url)
    print(patient.married)
    print(patient.allergies)
    print(patient.contacts_details)
    print('updated')


patient_info = {'name':'dk','Email':'abc@gmail.com','age':'22','weight':'67.0','linkdin_url':'https://linkdin.com/123','married':'true','contacts_details':{'phone_no':'0987654321'}}

patient1 = patient(**patient_info)

insert_patient_info(patient1)