from fastapi import FastAPI, Request, templating, Form, UploadFile, File
from fastapi.responses import HTMLResponse
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
# @app.post("/{user_name}") # index.html - DONE
# async def root(req : Request, user_name : str):
#     return template.TemplateResponse(name='index.html', context={'request':req, 'username':user_name})


# index page
@app.get("/") # index.html - DONE
async def root(req : Request):
    return template.TemplateResponse(name='index.html', context={'request':req})

# output page
@app.post("/predict_webpage") # DONE
async def predict_webpage(req : Request, Email: str = Form(...)):
    input = []
    input.append(Email)
    data = feature_transform.transform(input)
    prediction = model.predict(data)[0]
    # return f'Prediction : {prediction} message'
    return template.TemplateResponse(name='output.html', context={'request':req, 'Prediction':prediction})

# @app.get ("/predict_text") # DONE
# async def predict_text():
#     input = "You won $1000, click submit in your email inline to claim the reward "
#     X = []
#     X.append(input)
#     data = feature_transform.transform(X)
#     prediction = model.predict(data)
#     output = ['Spam Message' if prediction == 1 else 'Ham Message']
#     return(output)

# @app.get ("/predict_json") # DONE
# async def pred_json(input_parameters : values):
#     input = input_parameters.json()
#     input = json.loads(input)
#     X=[]
#     X.append(input['Message'])
#     data = feature_transform.transform(X)
#     prediction = model.predict(data)
#     output = ['Spam Message' if prediction == 1 else 'Ham Message']
#     return(output)

@app.post ("/predict_file") # DONE
async def pred_json(file : UploadFile = File(...)):
    file_content = file.file.read().decode('utf-8')
    msg = file_content.splitlines()

    data = feature_transform.transform(msg)
    prediction = model.predict(data)
    output = ['Spam Message' if item == 1 else 'Ham Message' for item in prediction]
    df = pd.DataFrame(msg,output).reset_index(drop=False).rename(columns={'index':'Prediction',0:'Message'})
    return HTMLResponse(df.to_html())


# if __name__ == "__main__":
#     app.run(debug=True)

# python3 -m uvicorn app:app --reload