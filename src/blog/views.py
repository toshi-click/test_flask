# flask_blog/views.py
from flask import request, redirect, url_for, render_template, flash, session
from . import app


@app.route('/')
def show_entries():
    return render_template('entries/index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            print(' ユーザ 名 が 異なり ます')
        elif request.form['password'] != app.config['PASSWORD']:
            print(' パスワード が 異なり ます')
        else:
            return redirect('/')
    return render_template('login.html')


@app.route('/logout')
def logout():
    return redirect('/')
