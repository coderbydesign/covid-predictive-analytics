import pickle
import numpy as np

def run_predictions(**kwargs):
    sex = kwargs.get("sex")
    age_range = kwargs.get("age_range")
    race_ethnicity = kwargs.get("race_ethnicity")
    has_underlying_conditions = kwargs.get("has_underlying_conditions")

    with open('./models/mortality.pickle', 'rb') as f:
        clf = pickle.load(f)
        deat_prediction = clf.predict_proba((np.array([sex, age_range, race_ethnicity, has_underlying_conditions]).reshape(1, -1)))[0]
        survival_prob, mortality_prob = deat_prediction

    return {
        "hospitilization_probability": "N/A",
        "death_probability": f"{(mortality_prob * 100)}%"
    }
