from flask.helpers import url_for
from app import app, sender
from flask import request, render_template, redirect


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='Home')


@app.route('/action', methods=['GET', 'POST'])
def action():
    if request.form['actionbtn'] == 'LEFT':
        sender.send('LEFT')
    elif request.form['actionbtn'] == 'RIGHT':
        sender.send('RIGHT')
    elif request.form['actionbtn'] == 'ROTATE':
        sender.send('ROTATE')
    return redirect(url_for('index'))
