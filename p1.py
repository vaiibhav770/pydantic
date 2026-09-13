from pydantic import BaseModel

class patient(BaseModel):

    name:str
    age:int

def insert_patient_info(patient: patient):
    print(patient.name)
    print(patient.age)

patient_info = {'name':'dk','age':'22'}

patient1 = patient(**patient_info)

insert_patient_info(patient1)