from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Literal,Annotated
import pickle
import pandas as pd

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()

tire1city=['Bangalore','Chennai','Hyderabad','Pune','Mumbai']
tire2city=['Kolkata','Delhi','Jaipur','Lucknow','Ahmedabad']

class userInput(BaseModel):

    age:Annotated[int, Field(..., gt=0,lt=120,description='age of the user')]
    weight:Annotated[float, Field(..., gt=0,description='weight of the user')]
    height:Annotated[float, Field(..., gt=0,description='height of the user')]
    income_lpa:Annotated[int, Field(..., description='salary of the user in a year')]
    smoker:Annotated[bool, Field(..., description='user is a smoker or not')]
    city:Annotated[str, Field(...,description='city of the user')]
    occupation:Annotated[Literal['teacher','doctor','army','police'], Field(..., description='choose from teacher,doctor,army,police')]

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight/(self.height**2)

    @computed_field
    @property
    def lifeStypeRisk(self) -> str:
        if self.smoker and self.bmi > 30:
            return 'high'
        elif self.smoker and self.bmi > 27:
            return 'medium'
        else:
            return 'low'

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 30:
            return 'young'
        elif self.age < 50:
            return 'middle-aged'
        else:
            return 'old'

    @computed_field
    @property
    def city_tire(self) -> str:
        if self.city in tire1city:
            return 'tire1'
        elif self.city in tire2city:
            return 'tire2'
        else:
            return 'other'
@app.get("/")
def home():
    return {"message": "Insurance premium API is running. Go to /docs to test."}

@app.post("/predict")
def predict_premium(data: userInput):

    input_df = pd.DataFrame([{
        'bmi': data.bmi,
        'age_group': data.age_group,
        'city_tire': data.city_tire,
        'occupation': data.occupation,
        'lifeStypeRisk': data.lifeStypeRisk,
        'income_lpa': data.income_lpa
    }])
    
    prediction = model.predict(input_df)[0]

    return JSONResponse(status_code=200, content={'prediction': prediction})
