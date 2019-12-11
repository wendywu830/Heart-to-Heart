import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
# Use sci-kit learn to utilize KNN approach to classify new cases 
from pathlib import Path

# Used to find best k value by testing a range of them 1-50
def find_k_value():
  errors = []
  for i in range(1, 30):
    test_knn = KNeighborsClassifier(n_neighbors = i)  # n_neighbors means k
    test_knn.fit(x_train, y_train)
    pred = test_knn.predict(x_test)
    errors.append(np.mean(pred != y_test))

  plt.figure(figsize=(12, 6))
  plt.plot(range(1, 30), errors, color='blue')
  plt.title('Error Rate of Different K Values')
  plt.xlabel('K Value')
  plt.ylabel('Mean Error')
  plt.show(block=True)

base_path = Path(__file__).parent
filepath = (base_path / "./heart.csv").resolve()
df = pd.read_csv(filepath)

# in data set, "target" = 1 if yes disease, 0 if no disease
characteristics = df.drop('target', 1).values
target_results = df.target.values
x_train, x_test, y_train, y_test = train_test_split(characteristics, target_results, test_size=0.2, random_state=3)

k = 11 #derived as explained on web app
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(x_train, y_train)

def classify(data_arr): #pass in all features of person in arr form
  data_arr = np.array(data_arr)
  print(str(data_arr))
  prediction = knn.predict([data_arr])
  return prediction

#find_k_value()