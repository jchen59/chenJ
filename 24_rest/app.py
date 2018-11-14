from flask import Flask,render_template
import urllib, json
app = Flask(__name__)

@app.route('/')
def hello_world():
    a = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=UX8lyV4tHkJcX5cMG6JYm8vtuAgtCchI9MpkNt0z')
    d = json.loads(a.read())
    return render_template("basic_form.html", name = d['title'], vid = d['url'])

app.debug = 1
app.run()
