#Cool Cids Club - Jabir Chowdhury, Jiayang Chen, Peter Cwalina
#SoftDev1 pd07
#K17 - Average
#2018-10-06

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="data.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
cur = db.cursor()               #facilitate db ops

def read_files():
	# Create and populate the courses table
	with open('./data/courses.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		c = "CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)"
		cur.execute(c)
		for row in reader:
			c = 'INSERT INTO courses VALUES(?,?,?)'
			cur.execute(c,(row['code'],row['mark'],row['id']))

	# Create and populate the peeps table
	with open('./data/peeps.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		c = "CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER)"
		cur.execute(c)
		for row in reader:
			c = 'INSERT INTO peeps VALUES(?,?,?)'
			cur.execute(c, (row['name'],row['age'],row['id']))
	db.commit() #save changes

def get_grades(id):
	c = "SELECT mark FROM 'courses' WHERE courses.id = ?"
	cur.execute(c,(id,))
	grades = []
	for grade in cur.fetchall():
		grades += [grade[0]]
	return grades

def get_averages():
	c = 'SELECT id FROM "peeps"'
	cur.execute(c)
	averages = {}
	for name in cur.fetchall():
		grades = get_grades(name[0])
		averages[name[0]] = sum(grades)/len(grades)

	return averages

def make_table():
	c = "CREATE TABLE peeps_avg(id INTEGER, average INTEGER)"
	cur.execute(c)
	averages = get_averages()
	for grade in averages:
		c = 'INSERT INTO peeps_avg VALUES(?,?)'
		cur.execute(c, (grade,averages[grade]))
read_files()


make_table()
cur.execute("SELECT * FROM peeps_avg")
print(cur.fetchall())
db.close() #close database
