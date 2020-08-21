#!/usr/bin/python3
from flask import Flask, request

app = Flask(__name__)

homePage = '''<!DOCTYPE html>
            <html>
                <head>
                    <style>
                        body {background-color: #32a852; opacity: .3; border-style:solid; border-color:grey;}
                        h1 {color:#033c8c; font-size: 20px;}
                        
                    </style> 
                </head>
                <body>
                    <h1> Innovation Challenge Team 5 </h1> 
                    <p>Enter Gross Dometic Product (GDP) in US Dollars bellow:</p>
                    <form method="POST" action="/">
                        <input name="gdp">
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
