from flask import Flask
app = Flask(__name__)


@app.route('/')
def function():
    return "Enter Gross Domestic Profit (GDP) in US Dollars to see an estimate of COVID-19 Deaths."


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()
