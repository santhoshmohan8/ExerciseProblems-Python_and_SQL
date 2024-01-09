import json
import requests

input = {
    'Message':'You won $1000, click submit in your email inline to claim the reward'
    }
print(input)
r = requests.post("http://127.0.0.1:8000/predict_json/", data=json.dumps(input))
print(r.text)


# curl -X POST -H "content_type:application/json" -d "{'Message':'You won $1000, click submit in your email inline to claim the reward'}" http://127.0.0.1:8000/predict_json/