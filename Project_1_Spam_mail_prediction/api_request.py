import json
import requests

input = {
    'Message':'You won $1000, click submit in your email inline to claim the reward'
    #'Message':'Please find attached PayPal offer letter, Review and acknowledge'
    }
r = requests.get("http://127.0.0.1:8000/predict_json/", data=json.dumps(input))
print(r.text)