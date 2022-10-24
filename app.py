
from flask import Flask, request
from datetime import datetime
import json
import requests
app = Flask(__name__)
app.debug = True

@app.route('/')
def studentNumber():
    dictionary=  {"Student Number" : "200525033"}
    return json.dumps(dictionary)



@app.route('/webhook', methods=['POST'])
def index():
    body = request.json
    city = body['queryResult']['parameters']['geo-city']
    
    api_url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=21cdfe226882b9302e6a9a05cc53fff3'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(api_url, headers=headers)
    r=response.json()

    temp = str(int(r['main']['temp']))
    sunset = str(r["sys"]["sunset"])
    td = int(sunset)
    utchour = int(datetime.utcfromtimestamp(td).strftime('%H'))
    dawnhour = utchour-4
    str_dawnhour = str(dawnhour)
    reply = '{"fulfillmentMessages": [ {"text": {"text": ["The temperature in ' + city +',  is  '+ temp + ' and the sunrise time is ' + str_dawnhour + ' AM."] } } ] }'
    return reply

if __name__ == '__main__':
    app.run()
