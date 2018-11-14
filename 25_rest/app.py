from flask import Flask,render_template
import urllib, json
app = Flask(__name__)

@app.route('/')
def hello_world():
    s = '.mp4'
    while (s[-4:] != '.jpg'): #The API shows videos every so often, so if it happens reload page
        a = urllib.request.urlopen('https://random.dog/woof.json')
        d = json.loads(a.read())
        s = d['url']
    return render_template("basic_form.html", url = s)

app.debug = 1
app.run()
