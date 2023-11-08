from pydantic import BaseModel
import numpy as np
from joblib import load
import pathlib
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI

origins = ['*']

app = FastAPI(title = 'Heart Disease Prediction')

app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=['*'],
   allow_headers=['*']
)

model = load(pathlib.Path('model/weatherHistory-v1.joblib'))

class InputData(BaseModel):
    Humidity:float=0.89
    WindSpeed:float=14.1197
    WindBearing:float=251.0
    Visibility:float=15.826300000000002
    Pressure:float=1015.1

class OutputData(BaseModel):
    Temperature:float=9.472222222222221

@app.post('/prediction', response_model = OutputData)
def score(data:InputData):
    model_input = np.array([v for k,v in data.dict().items()]).reshape(1,-1)
    result = model.predict(model_input)

    return {'Temperature':result}
