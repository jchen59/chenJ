#Ji-N-Ja -- Jiayang Chen & Jabir Chowdhury
#SoftDev1 pd7
#K10: Jinja Tuning
#2018-09-23

from flask import Flask,render_template
from util import csvscript

app = Flask(__name__)


@app.route("/occupations")
def occupation_table():
    occu_dict = csvscript.make_dictionary("data/occupations.csv")#makes a dictionary using occupations.csv
    table_headings = ["Job Class", "Percentage", "Start your career"]
    return render_template("chart.html",
                           dict = occu_dict,   #passes the dictionary to a variable used in jinja
                           rand= csvscript.random_job(occu_dict),#passes a random weighted occupation from dictionary
                           tab = table_headings)

if __name__ == "__main__":
  app.debug = True
  app.run()
