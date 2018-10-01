from flask import Flask,render_template,request,redirect,url_for,session
import os

app = Flask(__name__)

# Generates random key
app.secret_key = os.urandom(32)
user = 'duck'
passwd = 'goose'


@app.route('/')
def login_page():
    # If user is already logged in, redirect them
    if 'logged_in' in session and session['logged_in'] == True:
        return redirect(url_for('logged_in'))
    else:
        return render_template("home.html")

@app.route('/auth')
def auth():
    #Sees if username/password are correct
    username_passed = request.args['username'] == user
    password_passed = request.args['password'] == passwd
    failed_cases = []
    if(not username_passed):
        failed_cases += ['Username']
    if(not password_passed):
        failed_cases += ['Password']
    #If either are not correct, redirects to home page with info
    if(not username_passed or not password_passed):
        session['fail'] = ' and '.join(failed_cases) + " incorrect" #Lists the failed parameters
        return render_template("home.html", msg = session['fail'])

    #If everything passed, add to session
    session['logged_in'] = True
    session['username'] = user
    if 'fail' in session:
        session.pop('fail') #Gets rid of old failed login messages
    return redirect(url_for('logged_in'))

# Everything works and the user is logged in
@app.route('/secretKlub')
def logged_in():
    return render_template("logged_in.html", name=session['username'])

# Logout
@app.route('/logout')
def logout():
    # Gets rid of session information
    if ('logged_in' in session):
        session.pop('logged_in')
    if ('username' in session):
        session.pop('username')
    # Sends them back to homepage
    return redirect(url_for('login_page'))




app.debug = 1
app.run()
