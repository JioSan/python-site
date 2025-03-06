import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return 'Это меню'

@app.route('/user/<username>')
def show_user_profile(username):
  return f'User {username}'

if __name__ == '__main__': #для запуска
    app.run(debug=True)









































#https://prod.liveshare.vsengsaas.visualstudio.com/join?7E47BCA9C3A218D4414B7956B62977FA7503
