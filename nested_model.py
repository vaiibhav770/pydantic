from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pincode:int

address_dict={'city':'faridabad','state':'delhi','pincode':'1234'}

address1=Address(**address_dict)

class Patient(BaseModel):

    name:str
    age:int
    gender:str
    address:Address

patient_dict={'name':'str','age':'23','gender':'male','address':address1}

patient1=Patient(**patient_dict)

temp=patient1.model_dump(include=['name','gender'])

print(temp)
print(type(temp))

print(patient1)
print(patient1.address.city)
print(patient1.address.state)
print(patient1.address.pincode)
