from flask import Flask, render_template
import PJs


app = Flask(__name__)

@app.route("/occupations")
def occupants():
    return render_template("chart.html", coll = PJs.make_dictionary("occupations.csv"))










if __name__ == "__main__":
    app.debug = True
app.run()
