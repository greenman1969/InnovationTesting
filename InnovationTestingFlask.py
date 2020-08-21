#!/usr/bin/python3
from flask import Flask, request, g
import csv
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import sqlite3

DATABASE = 'database.db'
conn = sqlite3.connect('database.db')
print("Opened Database")
conn.close()

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
                    body {text-align: center; background-color: DarkSeaGreen; padding: 10px;}
                    html {background-color: DarkSeaGreen;}
                </style>
                </head>
                <body>
                    <h1> Innovation Challenge Team 5 </h1>
                    <p>Enter Gross Dometic Product (GDP) in US Dollars and population below:</p>
                    <form method="POST" action="/">
                        <input type="number" name="gdp" placeholder="GDP" min="0" required>
			            <input type="number" name="pop" placeholder="Population" min="0" required>
                        <input type="number" name="expect" placeholder="Expected Deaths" min="0">
                        <input type="submit" class="btn btn-light">
                    </form>
                </body>
            </html>'''

def returnValue(value, accuracy=-1, offBy=-1):
    homePage = '''<!DOCTYPE html>
            <html>
                <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
                <style> 
                    body {text-align: center; background-color: DarkSeaGreen; padding: 10px;}
                    html {background-color: DarkSeaGreen;}
                </style>
                </head>
                <body>
                    <h1> Innovation Challenge Team 5 </h1>
                    <p>Your expected deaths are: '''+str(int(value[0]))+''' deaths</p>'''
    if not accuracy == -1:
        homePage += '''<p>Model was '''+str(float(accuracy))+'''&#37; accurate<p>'''
    if not offBy == -1:
        homePage += '''<p>Model was off by: '''+str(int(offBy))+''' deaths</p>'''
                    
    homePage += '''</body>
            </html>'''
    return homePage
@app.route('/', methods=['GET','POST'])
def function():
    if request.method=='GET':
        return homePage
    elif request.method=='POST':
        conn = sqlite3.connect('database.db')
        gdp = request.form['gdp']
        pop = request.form['pop']
        expect = float(request.form['expect'])
        
        features = np.array([[float(gdp), float(pop)]])
        prediction = reg.predict(features)

        if not expect == '':
            #compare prediction to actual value
            residual = 100-100*abs((expect - prediction)/expect)
            offby = abs(expect-prediction)
            conn.execute(generateSQLString(gdp,pop,expect,prediction))
            conn.commit()
            conn.close()
            return returnValue(prediction, residual, offby)
        conn.execute(generateSQLString(gdp,pop,0,prediction))
        conn.commit()
        conn.close()
        return returnValue(prediction)

def generateSQLString(gdp, population, expect, result):
    return "insert into outputs (gdp, population, expect, result) values ("+str(int(gdp))+", "+str(int(population))+", "+str(int(expect))+", "+str(int(result))+");"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
