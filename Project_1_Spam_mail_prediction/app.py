from fastapi import FastAPI, Request, templating, Body
import pandas as pd
import numpy as np
import pickle
import json
from pydantic import BaseModel

# app instance
app = FastAPI()

# load pickle files
model = pickle.load(open('model.pkl','rb'))
feature_transform = pickle.load(open('vector.pkl','rb'))

# templates

template = templating.Jinja2Templates(directory='templates')

# basemodel
class values(BaseModel):
    Message : str

# index page
@app.post("/") # index.html - DONE
async def root(req : Request):
    return template.TemplateResponse(name='index.html', context={'request':req})

# output page
@app.post("/predict_webpage") # method not allowed error
async def predict_webpage(req : Request):
    text = req.form
    input = list(text)
    data = feature_transform.transform(input)
    prediction = model.predict(data)
    return template.TemplateResponse(name='output.html', prediction=prediction)

@app.get ("/predict_text") # DONE
async def predict_text():
    input = "You won $1000, click submit in your email inline to claim the reward "
    X = []
    X.append(input)
    data = feature_transform.transform(X)
    prediction = model.predict(data)
    output = ['Spam Message' if prediction == 1 else 'Ham Message']
    return(output)

@app.post ("/predict_json") # method not allowed error
async def predict_json(input_parameters : values):
    input = input_parameters.json()
    print(input)
    input = json.loads(input)
    X=list(input['Message'])

    data = feature_transform.transform(X)
    prediction = model.predict(data)
    output = ['Spam Message' if prediction == 1 else 'Ham Message']
    return(output)



# if __name__ == "__main__":
#     app.run(debug=True)

# python3 -m uvicorn app:app --reload