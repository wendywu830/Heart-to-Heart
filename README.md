# CIS 192 Final Project

### How to Run
1. After cloning/downloading, `cd Final`
2. `pip install -r requirements.txt`
3. `python manage.py makemigrations core`
4. `python manage.py migrate`
5. It should be ready now! Run `python manage.py runserver` and go to localhost:8000

### Code structure
This has the normal structure of a django web app. There is the main app called "core" that holds the models in models.py and the main web rendering functionality with the templates folder and views.py. There is also a file called data.py that runs the machine learning component in which it reads in data and trains a KNN model to predict whether or not someone has heart disease based on their health profile.

### Parts
1. One class definition (with at least two magic methods) = HealthProfile class w/ methods (__str__, __eq__)
2. Two non-trivial first-party packages = pathlib, random
3. Two non-trivial third-party packages = Django, scikit-learn, pandas, numpy, etc.
