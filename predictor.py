import pickle
import numpy as np

def run_predictions(**kwargs):
    sex = kwargs.get("sex")
    age_range = kwargs.get("age_range")
    race_ethnicity = kwargs.get("race_ethnicity")
    has_underlying_conditions = kwargs.get("has_underlying_conditions")

    with open('./models/mortality.pickle', 'rb') as f:
        clf = pickle.load(f)
        death_prediction = clf.predict_proba((np.array([sex, age_range, race_ethnicity, has_underlying_conditions]).reshape(1, -1)))[0]
        _, mortality_prob = death_prediction

    with open('./models/hospitality.pickle', 'rb') as f:
        clf = pickle.load(f)
        hosp_prediction = clf.predict_proba((np.array([sex, age_range, race_ethnicity, has_underlying_conditions]).reshape(1, -1)))[0]
        _, hospitality_prob = hosp_prediction

    return {
        "hospitalization_probability": f"{round((hospitality_prob * 100), 2)}%",
        "death_probability": f"{round((mortality_prob * 100), 2)}%"
    }
