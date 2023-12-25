from fastapi import FastAPI, Request, templating
import pickle
import json

# app instance
app = FastAPI()

# load pickle files
model = pickle.load(open('model.pkl','rb'))
feature_transform = pickle.load(open('vector.pkl','rb'))

# templates

template = templating.Jinja2Templates(directory='templates')

# index page
@app.get("/") # index.html - DONE
async def root(req : Request):
    return template.TemplateResponse(name='index.html', context={'request':req})

# output page
@app.post("/predict_webpage") # method not allowed error
async def predict_webpage(req : Request):
    text = Request.form
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
async def predict_json(input_parameters : str):
    input = input_parameters.json()
    input = json.loads(input)
    X=list(input['Message'])

    data = feature_transform.transform(X)
    prediction = model.predict(data)
    output = ['Spam Message' if prediction == 1 else 'Ham Message']
    return(output)

# @app.post("/predict_json_2")
# async def predict_json_2():
#     return




# if __name__ == "__main__":
#     app.run(debug=True)

# python3 -m uvicorn app:app --reload