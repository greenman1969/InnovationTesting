#!/usr/bin/python3
from flask import Flask, request

app = Flask(__name__)

homePage = '''<!DOCTYPE html>
            <html>
                <head>
                    <style>
                        html {
				margin: auto; 
				width: 50%; 
				background-color: ##a9e8a9;
                                border-style:solid;
				border-color:grey;
				border-width: 1.5px;
				}
				
                        h1 {
				color:#033c8c;
                      		font-size: 20px;
				text-align: center;}
                    </style>
                </head>
                <body>
                    <h1> Innovation Challenge Team 5 </h1>
                    <p>Enter Gross Dometic Product (GDP) in US Dollars and population below:</p>
                    <form method="POST" action="/">
                        <input name="gdp" value="GDP">
			<input name="pop" value="Population">
                        <input type="submit">
                    </form>
                </body>
            </html>'''

@app.route('/', methods=['GET','POST'])
def function():
    if request.method=='GET':
        return homePage
    elif request.method=='POST':
        return "Return the estimated value"

#@app.route('/<name>')
#def hello_name(name):
#    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
