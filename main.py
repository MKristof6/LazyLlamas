import time

import flask
from flask import Flask, render_template, url_for, redirect, session, request, flash

import data_handler
import util

app = Flask("amigo")
app.secret_key = b'_5#z2L"F7Q8q\n\xec]/'


@app.route('/speech')
def speech():
    return render_template('speech.html')


@app.route('/', methods=['GET', 'POST'])
def login():
    users = [data_handler.get_teachers(), data_handler.get_students()]
    if request.method == 'POST':
        session['email'] = request.form['email']
        for userz in users:
            for user in userz:
                if session['email'] == user['email']:
                    session['pw'] = request.form['password']
                    if util.verify_pw(session['pw'], user['password']):
                        return redirect(url_for('speech'))
                else:
                    return 'Wrong password!<br><br><a href="/login">Go back</a>'
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('speech'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        error = None
        email = request.form['email']
        name = request.form['name']
        pw = util.hash_it(request.form['password'])
        bday = request.form['bday']
        # TODO: figure out language_id-s
        if not validate_email(email):
            error = "Ezzel az e-mail címmel már regisztráltak a rendszerünkbe. Kérjük, próbáld újra egy másik fiókkal."
            return render_template('register.html', error=error)
        else:
            data_handler.register_student(name, email, pw, bday)
            return redirect(url_for('speech'))
    else:
        return render_template('register.html')


def validate_email(email):
    users = [data_handler.get_students(), data_handler.get_teachers()]
    for userz in users:
        for user in userz:
            if email == user['email']:
                return False
    return True


if __name__ == "__main__":
    app.run(
        debug=True,
        port=8000)
