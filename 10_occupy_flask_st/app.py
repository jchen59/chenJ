#Ji-N-Ja -- Jiayang Chen & Jabir Chowdhury
#SoftDev1 pd7
#K10: Jinja Tuning
#2018-09-23

from flask import Flask,render_template
from csvscript import make_dictionary,random_job

app = Flask(__name__)


@app.route("/occupations")
def occupation_table():
    occu_dict = make_dictionary("data/occupations.csv")
    return render_template("chart.html",
                           dict = occu_dict,
                           rand= random_job(occu_dict))

if __name__ == "__main__":
  app.debug = True
app.run()
