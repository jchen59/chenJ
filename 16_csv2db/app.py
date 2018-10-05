#BluePenguinz -- Jason Lin, Jiayang Chen
#SoftDev1 pd07
#K16 -- No Trouble
#2018-10-04

from flask import Flask, render_template, request
import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

app = Flask(__name__) # instantiates an instance of Flask


DB_FILE="foo.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

with open('./data/courses.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    command = "CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)"
    c.execute(command)    
    for row in reader:
        command = "INSERT INTO courses VALUES(\" " + row['code']+"\"," +  row['mark'] + "," + row['id'] + ")"
        c.execute(command)

with open('./data/peeps.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    command = "CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER)"
    c.execute(command)   
    for row in reader:
        command = "INSERT INTO peeps VALUES(\" " + row['name']+"\"," +  row['age'] + "," + row['id'] + ")"
        c.execute(command)
#==========================================================

db.commit() #save changes
db.close() #close database


@app.route("/") #Linking a function to a route
def home():
    return "Hello, World!"

if __name__ != "__main__":
    app.debug = True
    app.run()
