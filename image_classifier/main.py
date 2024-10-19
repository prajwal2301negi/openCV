import os

from skimage.io import imread
from skimage.transform import resize
import numpy as np


# 1.PREPROCESSING DATA
input_dir = r"C:\Users\prajwal\Downloads\clf-data\clf-data"
categories = ['empty', 'not_empty']


data = []
labels = []

for category_idx, category in enumerate(categories):
    for file in os.listdir(os.path.join(input_dir, category)):
        img_path = os.path.join(input_dir, category, file)
        img = imread(img_path)
        img = resize(img, (15, 15))
        data.append(img.flatten())  # we have to pass like this only
        labels.append(category_idx)

data = np.asarray(data)
labels = np.asarray(labels)


# train/test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size = 0.2, shuffle = True, stratify = labels)
# stratify ---> maintaining proportion of data.


# 2.TRAIN MODEL(CLASSIFIER)
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

classifier = SVC()

# Key-value pairs
parameters = [{'gamma':[0.01, 0.001, 0.0001], 'C':[1, 10, 100, 1000]}]

grid_search = GridSearchCV(classifier, parameters)
# We will train image classifier for each combination we have ---> 12

grid_search.fit(X_train, y_train)



# 3.TESTING MODEL
best_estimator = grid_search.best_estimator_
# choosing best classifier

y_pred = best_estimator.predict(X_test)
from sklearn.metrics import accuracy_score

score = accuracy_score(y_pred, y_test)

print(score)
# will be between 0-1


# 4.SAVE MODEL
import pickle
pickle.dump(best_estimator, open('./model.p', 'wb'))