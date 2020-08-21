#!/usr/bin/python3
from flask import Flask, request
import csv
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

#import data from csv into dataframe 'df'
df = pd.read_csv('Dataset/WholeData.csv')

#ensure data has no infinites, NA's, or execessively large values
df.replace([np.inf, -np.inf], np.nan)
df.dropna()
df.round(8)
df = df[~df.isin([np.nan, np.inf, -np.inf]).any(1)]

#Establish the Features and the Target in X and y variables repsectively
X = df[['GDP','Population']]
y = df.Deaths

#convert x and y from dataframe to numpy array
X = X.to_numpy()
y = y.to_numpy()

#just checking up on the data to make sure it looks right
print(X)
print("X -",X.shape)
print("Y -",y.shape)

#train the model
reg = LinearRegression().fit(X,y)

#print info
print("Score: ",reg.score(X,y))
print("coef: ",reg.coef_)
print("intercept",reg.intercept_)

app = Flask(__name__)

homePage = '''<!DOCTYPE html>
            <html>
                <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
                <style> 
                    body {text-align: center;}
                </style>
                </head>
                <body>
                    <h1> Innovation Challenge Team 5 </h1>
                    <p>Enter Gross Dometic Product (GDP) in US Dollars and population below:</p>
                    <form method="POST" action="/">
                        <input type="number" name="gdp" placeholder="GDP" min="0">
			            <input type="number" name="pop" placeholder="Population" min="0">
                        <input type="number" name="expect" placeholder="Expected Value" min="0">
                        <input type="submit">
                    </form>
                </body>
            </html>'''

def returnValue(value, accuracy=-1):
    homePage = '''<!DOCTYPE html>
            <html>
                <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
                <style> 
                    body {text-align: center;}
                </style>
                </head>
                <body>
                    <h1> Innovation Challenge Team 5 </h1>
                    <p>Your expected deaths are: '''+str(int(value[0]))+'''</p>'''
    if not accuracy == -1:
        homePage += '''<p>Model was off by: '''+str(int(value[0]))+'''<p>'''
                    
    homePage += '''</body>
            </html>'''
    return homePage

@app.route('/', methods=['GET','POST'])
def function():
    if request.method=='GET':
        return homePage
    elif request.method=='POST':
        gdp = request.form['gdp']
        pop = request.form['pop']
        expect = float(request.form['expect'])
        
        features = np.array([[float(gdp), float(pop)]])
        prediction = reg.predict(features)

        if not expect == '':
            #compare prediction to actual value
            residual = abs((expect - prediction)/expected)
            return returnValue(prediction, residual)
        return returnValue(prediction)



if __name__ == '__main__':
    app.run(host='0.0.0.0')
