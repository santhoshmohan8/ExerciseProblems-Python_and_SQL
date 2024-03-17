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
scaler = pickle.load(open('standardscaler.pkl','rb'))

# templates

template = templating.Jinja2Templates(directory='templates')

# basemodel
# class values(BaseModel):
#     Message : str

# index page
@app.get("/")
async def root(req : Request):
    return template.TemplateResponse(name='index.html', context={'request':req})

@app.post ("/predict_file")
async def pred_json(file : UploadFile = File(...)):
    file_content = file.file.read().decode('utf-8')
    x_str = file_content.splitlines()
    # x_float = [float(x) for x in x_str]
    # print(x_float)
    # x_int = int.from_bytes(file_content, byteorder='little')
    print(x_str)



    # data = scaler.transform(x_live)
    # prediction = model.predict(data)
    # return(prediction)

    # df = pd.DataFrame(msg,output).reset_index(drop=False).rename(columns={'index':'Prediction',0:'Message'})
    # return HTMLResponse(df.to_html())


# if __name__ == "__main__":
#     app.run(debug=True)

# python3 -m uvicorn app:app --reload