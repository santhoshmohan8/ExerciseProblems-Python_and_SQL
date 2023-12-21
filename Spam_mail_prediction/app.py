from fastapi import FastAPI
import pickle

model = pickle.load(open('model.pkl','rb'))
feature_transform = pickle.load(open('feature_transform.pkl','rb'))

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Routing Service is Healthy!! Second check"}
