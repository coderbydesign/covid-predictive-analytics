from flask import Flask, render_template, request, abort
from predictor import run_predictions

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction_data = None
    sex = request.form.get("sex")
    age_range = request.form.get("age")
    race_ethnicity = request.form.get("race-ethnicity")
    has_underlying_conditions = request.form.get("underlying-conditions")

    if request.method == "POST":
        if any(ele == "" for ele in [sex, age_range, race_ethnicity, has_underlying_conditions]):
            return render_template("index.html", error="Not all form values were supplied.")

        prediction_data = run_predictions(
            sex=sex,
            age_range=age_range,
            race_ethnicity=race_ethnicity,
            has_underlying_conditions=has_underlying_conditions
        )

    return render_template("index.html", prediction_data=prediction_data)
