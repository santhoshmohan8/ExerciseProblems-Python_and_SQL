from fastapi import FastAPI
import pickle
import sklearn


model = pickle.load(open('model.pkl','rb'))
feature_transform = pickle.load(open('vector.pkl','rb'))

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Routing Service is Healthy!! fourth check"}

@app.get("/predict")
async def predict():
    input = "You won $1000, click submit in your email inline to claim the reward "
    X = []
    X.append(input)

    data = feature_transform.transform(X)
    prediction = model.predict(data)
    output = ['Spam' if prediction == 1 else 'Ham']
    return(output)

# if __name__ == "__main__":
#     app.run(debug=True)