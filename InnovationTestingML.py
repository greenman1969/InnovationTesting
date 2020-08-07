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

# Load Dataset
url = "https://github.com/greenman1969/InnovationTesting/raw/master/Dataset/GDP.csv"
names = ['gdp']
gdp = read_csv(url, names=names)

url = "https://github.com/greenman1969/InnovationTesting/raw/master/Dataset/Deaths.csv"
names = ['covid-deaths']
deaths = read_csv(url,names=names)

XData = deaths.values   # Death Data
YData = gdp.values   # GDP Data
print(XData)
print(YData)