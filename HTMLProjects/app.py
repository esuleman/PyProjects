from flask import Flask, render_template, redirect, request

app = Flask(__name__)

FAVORITE_GAMES = []

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/test')
def test():
    return render_template('IntroToWebProgramming.html')

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/add')
def add_game():
    name = request.form['name']
    game = request.form['game']
    FAVORITE_GAMES.append({'name': name, 'game': game})
    return redirect('/')
