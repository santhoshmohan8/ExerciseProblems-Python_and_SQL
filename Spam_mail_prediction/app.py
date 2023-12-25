from fastapi import FastAPI
import pickle
import json

model = pickle.load(open('model.pkl','rb'))
feature_transform = pickle.load(open('vector.pkl','rb'))

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Routing Service is Healthy!! fourth check"}


@app.get ("/predict_text")
async def predict_text():
    input = "You won $1000, click submit in your email inline to claim the reward "
    X = []
    X.append(input)
    data = feature_transform.transform(X)
    prediction = model.predict(data)
    output = ['Spam Message' if prediction == 1 else 'Ham Message']
    return(output)

@app.post ("/predict_json")
async def predict_json(input_parameters):
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

# @app.post("/predict_webpage")
# async def predict_webpage():
#     return


# if __name__ == "__main__":
#     app.run(debug=True)

# python3 -m uvicorn app:app --reload