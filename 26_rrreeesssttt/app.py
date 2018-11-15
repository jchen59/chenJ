from flask import Flask,render_template

import json,urllib
app = Flask(__name__)

@app.route('/')
def hello_world():
    a = urllib.request.urlopen('https://www.boredapi.com/api/activity')
    d = json.loads(a.read())
    s = d['activity']
    darksky = urllib.request.urlopen('https://api.darksky.net/forecast/605bc9bbfcbfd2140fc5b6e638f39f6f/37.8267,-122.4233')
    d1 = json.loads(darksky.read())
    weather = d1['currently']['summary']
    temp = d1['currently']['temperature']
    return render_template("basic_form.html", activity = s, summary = weather + ' ' + str(temp) + 'F')

app.debug = 1
app.run()
