from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field
from typing import Literal,Annotated
import pickle
import pandas as pd

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

class userInput(BaseModel):

    age:Annotated[int, Field(..., gt=0,lt=120,description='age of the user')]
    weight:Annotated[float, Field(..., gt=0,description='weight of the user')]
    height:Annotated[float, Field(..., description='height of the user')]
    income_lpa:Annotated[int, Field(..., description='salary of the user in a year')]
    smoker:Annotated[bool, Field(..., description='user is a smoker or not')]
    city:Annotated[str, Field(...,description='age of the user')]
    occupation:Annotated[Literal['teacher','doctor','army','police'], Field(..., description='age of the user')]

@computed_field
@property
def bmi(self) -> float:
    self.weight/(self.height**2)

@computed_field
@property
def lifeStypeRisk(self) -> str:
    if self.bmi and self.smoker > 30:
        return 'high'
    elif self.bmi and self.smoker > 27:
        return 'medium'
    else:
        return 'low'

@computed_field
@property
def age_group(self) -> str:
    
    
