from flask import Flask,render_template,request,redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("basic_form.html")

@app.route('/auth')
def auth():
    if(request.args["username"] == ""):
        return redirect("/")
    return render_template("ya.html", name=request.args["username"],method = request.method)

app.debug = 1
app.run()
