import json
import requests

url = "http://127.0.0.1:8000/predict_json"

input = {'Message':'You won $1000, click submit in your email inline to claim the reward'}
input_json= json.dumps(input)
request = requests.post(url, data=input_json)