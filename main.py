from flask import Flask, render_template, url_for, redirect, session, request, flash

import data_handler
import util

app = Flask("amigo")
app.secret_key = b'_5#z2L"F7Q8q\n\xec]/'


@app.route('/speech')
def speech():
    return render_template('speech.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    teachers = data_handler.get_teachers()
    students = data_handler.get_students()
    if request.method == 'POST':
        session['pw'] = request.form['password']
        session['email'] = request.form['email']
        for user in teachers:
            if session['email'] == user['email']:
                session['amigo'] = True
                if util.verify_pw(session['pw'], user['password']):
                    return redirect(url_for('home'))
        for user in students:
            if session['email'] == user['email']:
                session['amigo'] = False
                if util.verify_pw(session['pw'], user['password']):
                    return redirect(url_for('home'))
        else:
            return 'Fuck off, register first!'
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.args:
        amigo = int(request.args.get('amigo'))
    else:
        amigo = 1
    if request.method == 'POST':
        error = None
        email = request.form['email']
        name = request.form['name']
        pw = str(util.hash_it(request.form['password']))[2:-1]
        bday = request.form['bday']
        languages = []
        try:
            if request.form['eng']:
                languages.append(int(request.form['eng']))
        except KeyError:
            pass
        try:
            if request.form['fra']:
                languages.append(int(request.form['fra']))
        except KeyError:
            pass
        try:
            if request.form['ita']:
                languages.append(int(request.form['ita']))
        except KeyError:
            pass
        try:
            if request.form['esp']:
                languages.append(int(request.form['esp']))
        except KeyError:
            pass
        if not validate_email(email):
            error = "Ezzel az e-mail címmel már regisztráltak a rendszerünkbe. Kérjük, próbáld újra egy másik fiókkal."
            return render_template('register.html')
        else:
            student_id = data_handler.get_latest_id()['id'] + 1
            data_handler.register_student(name, email, pw, bday, languages, student_id)
            session['email'] = email
            session['amigo'] = False
            return redirect(url_for('home'))
    else:

        return render_template('register.html', amigo=amigo)


def validate_email(email):
    users = [data_handler.get_students(), data_handler.get_teachers()]
    for userz in users:
        for user in userz:
            if email == user['email']:
                return False
    return True


@app.route('/')
def home():
    if not session:
        return redirect(url_for('login'))
    else:
        return render_template('index.html')


@app.route('/my_exercises')
def my_exercises():
    return 'Implementation in process. Don\'t be an impatient dick!'


@app.route('/profile')
def profile():
    return 'Implementation in process. Don\'t be an impatient dick!'


@app.route('/new_exercise')
def new_exercise():
    return 'Implementation in process. Don\'t be an impatient dick!'


@app.route('/solutions')
def solutions():
    return 'Implementation in process. Don\'t be an impatient dick!'


@app.route('/students')
def students():
    return 'Implementation in process. Don\'t be an impatient dick!'


@app.route('/exercises')
def exercises():
    return 'Implementation in process. Don\'t be an impatient dick!'


if __name__ == "__main__":
    app.run(
        debug=True,
        port=8000)
