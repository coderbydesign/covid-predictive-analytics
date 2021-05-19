from flask import Flask, render_template, request, abort

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    prediction_data = None
    sex = request.form.get("sex")
    age_range = request.form.get("age")
    race_ethnicity = request.form.get("race-ethnicity")
    has_underlying_conditions = request.form.get("underlying-conditions")

    if request.method == "POST":
        if any(ele == "" for ele in [sex, age_range, race_ethnicity, has_underlying_conditions]):
            return render_template("index.html", error="Not all form values were supplied.")

        # mocked out for now, but will call our module to run data through our model
        prediction_data = {"hospitilization_probability": 0.1, "death_probability": 0.01}

    return render_template("index.html", prediction_data=prediction_data)
