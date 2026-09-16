from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator,computed_field
from typing import List, Dict, Optional,Annotated

class patient(BaseModel):

    name:Annotated[str,Field(max_length=50, title='Name of the patient',description='Give the name of the patient in less than 50 words',examples=['nitish','amit'])]
    age:int=Field(gt=0,lt=120)
    Email:EmailStr
    weight:Annotated[float,Field(gt=0,strict=True)]
    height:int
    linkdin_url:AnyUrl
    married:Annotated[bool,Field(default=None,description='is the patient married or not?')]
    allergies:Optional[List[str]]=Field(default=None,max_length=5)
    contacts_details:Dict[str,str]

    @computed_field
    @property
    def calculate_bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
  

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age > 60 and 'emergency' not in model.contacts_details:
            raise ValueError('patient above 60 must have emergency no')

    @field_validator('Email')
    @classmethod
    def email_validator(cls,value):

        valid_domains=['hdfc.com','icici.com']
        domain_name=value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('not a valid domain')

        return value

    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()

    @field_validator('age',mode='after')
    @classmethod
    def valid_age(cls,value):
        if 0<value<100:
            return value
        else:
            raise ValueError('Age should be 0-100')


def insert_patient_info(patient: patient):
    print(patient.name)
    print(patient.Email)
    print(patient.age)
    print(patient.weight)
    print(patient.linkdin_url)
    print(patient.married)
    print(patient.allergies)
    print('BMI',patient.calculate_bmi)
    print(patient.contacts_details)
    print('updated')


patient_info = {'name':'aman','height':'140','Email':'abc@hdfc.com','age':'70','weight':67.0,'linkdin_url':'https://linkdin.com/123','married':'true','contacts_details':{'phone_no':'0987654321','emergency':'89765'}}

patient1 = patient(**patient_info)

insert_patient_info(patient1)