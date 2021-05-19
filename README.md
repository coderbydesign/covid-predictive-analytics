# COVID Predictive Analytics
This project is an exploration into predictive analytics using Python, with a focus
on learning from historical demographic COVID datapoints to predict two things:

- likelihood of hospitalization after infection, given a set of demographic markers
- likelihood of death after infection, given a set of demographic markers

Data in this project is being sourced from [COVID-19 Case Surveillance Public Use Data](https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data/vbim-akqf)

## Desired Outcome
We hope to use a logistic regression data model to ultimately give us the probability
of hospitalization or death after a COVID infection, based on a number of demographic
datapoints.

We'll need to determine which fields to use from the dataset to train the model(s)
with in order to get a favorable outcome on analysis, but at a high-level we should
have a way to supply a dataset to the model like so:

```json
{"age": 38, "sex": "female", "ethnicity": "Hispanic/Latino", "underlying-conditions": false}
```

This should in turn provide us with the likelihood of hospitalization and/or death
after a COVID infection, and show what types of racial and ethnic disparities exist.

We may need to build some preset selections that will be available, to ensure
data we pass into the model will match on existing data values.

## Questions/Unknowns
### Which libraries/technologies should we use?
- jupyter: https://jupyter.org/
- pandas: https://pandas.pydata.org/getting_started.html
- NumPy: https://numpy.org/

### What is the difference between predictive analytics and machine learning?
- https://www.bmc.com/blogs/machine-learning-vs-predictive-analytics/

### Which model(s) should we use?
- logistic regression: https://en.wikipedia.org/wiki/Logistic_regression

### What are the steps to predictive analytics at a high-level
- Data exploration (what fields/types/etc, are in our data)
- Data cleaning (null/missing values/which columns should we use/remove)
- Choose a model and datapoints that will help the model learn
- Train the model
- Perform analysis/evaluation (how well does it perform)
- Tweak the model
- Predict

## Local Setup
### Get the data
Install git lfs: https://git-lfs.github.com/
```
$ git lfs install
$ git lfs checkout
```

To run one of the Jupyter notebooks, make sure you have Jupyter installed, and run
the command to open a specific notebook:
```
jupyter notebook covid-mortality.ipynb
```

To install dependencies and run the server:
```
$ pipenv install
$ flask run
```

## ToDo
- [] create notebooks to explore data for mortality _and_ hospitilizations
- [] save the trained models to `./models/`
- [] load the models into a module where we can have methods to pass in data to predict
  probabilities for either model
- [] create a simple API with Flask to accept data
- [] create a simple FE with select menus which will map the display values to the
  values in our mappings for sex, age group, race/ethnicity, and underlying conditions
- [] plot trends visually with `matplotlib` to show any data disparities

## Resources
- https://pandas.pydata.org/getting_started.html
- https://www.anaconda.com/products/individual
- https://jupyter.org/
- https://numpy.org/
- https://towardsdatascience.com/building-a-logistic-regression-in-python-step-by-step-becd4d56c9c8
- https://www.youtube.com/watch?v=Cx8Xie5042M
- https://learning.oreilly.com/playlists/8cdb9893-fb9b-4672-bcd4-49bac776b0fa
