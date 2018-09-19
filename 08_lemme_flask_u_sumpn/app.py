from flask import Flask
from random import randint

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Yup'

@app.route('/hello')
def random_num():
    return str(randint(0,100))

@app.route('/wow')
def finders_keepers():
    return "Losers weepers!"

if __name__ == "__main__":
    app.debug = True
    app.run()
