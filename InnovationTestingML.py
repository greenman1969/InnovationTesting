#!/usr/bin/python3

# Load libraries
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import numpy as np

# Load Dataset
url = "https://github.com/greenman1969/InnovationTesting/raw/master/Dataset/GDP.csv"
names = ['gdp']
gdp = read_csv(url, names=names)

url = "https://github.com/greenman1969/InnovationTesting/raw/master/Dataset/Deaths.csv"
names = ['covid-deaths']
deaths = read_csv(url,names=names)

Xe = deaths.values   # Death Data
Ye = gdp.values   # GDP Data

XData = np.array([])
YData = np.array([])

for i in Xe:
    XData = np.append(XData, int(i[0]))
for i in Ye:
    YData = np.append(YData, int(i[0]))


print(len(XData))
print(len(YData))

X_train, X_Validation, Y_train, Y_validation = train_test_split(XData,YData, test_size=0.2, random_state=1)



models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
# Evaluate each Model
results = []
names = []
for name, model in models:
    print("Beep")
    kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
    print("Beep")
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
    print("Beep")
    results.append(cv_results)
    names.append(name)
    print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))