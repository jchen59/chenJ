#BluePenguinz -- Jason Lin, Jiayang Chen
#SoftDev1 pd07
#K16 -- No Trouble
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="foo.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
def read_files():
	# Create and populate the courses table
	with open('../data/courses.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		command = "CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)"
		c.execute(command)
		for row in reader:
		    command = 'INSERT INTO courses VALUES("{0}",{1},{2})'.format(row['code'],row['mark'],row['id'])
		    c.execute(command)

	# Create and populate the courses table
	with open('../data/peeps.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		command = "CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER)"
		c.execute(command)
		for row in reader:
		    command = 'INSERT INTO peeps VALUES("' + row['name']+'",' +  row['age'] + "," + row['id'] + ")"
		    c.execute(command)
	#==========================================================



	db.commit() #save changes

	
def grades(student_id):
	command = "SELECT mark FROM courses WHERE courses.id = {}".format(student_id))
	c.execute(command)
	grades = c.fetchall()
	command = "SELECT name FROM peeps WHERE id = {}".format(student_id)
	
	print(grades)
	return grades

read_files()
grades(1)
	
	
	
	
	
db.close() #close database
	
	
	
	
	
	
	
	
	
	
	
	
