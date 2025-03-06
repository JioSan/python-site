import flask
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)














































#https://prod.liveshare.vsengsaas.visualstudio.com/join?7E47BCA9C3A218D4414B7956B62977FA7503
