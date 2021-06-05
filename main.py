from flask import Flask, render_template, url_for, redirect, session, request, flash

import data_handler
import util

app = Flask("amigo")
app.secret_key = b'_5#z2L"F7Q8q\n\xec]/'


@app.route('/speech')
def speech():
    return render_template('speech.html')


# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    # get all amigos from database
    amigos = data_handler.get_amigos()
    # get all students from database
    students = data_handler.get_students()

    if request.method == 'POST':
        # Get login data from request form
        session['pw'] = request.form['password']
        session['email'] = request.form['email']
        for user in amigos:
            # Check if user is an amigo
            if session['email'] == user['email']:
                session['amigo'] = True
                session['id'] = user['id']
                # Verify password
                if util.verify_pw(session['pw'], user['password']):
                    return redirect(url_for('home'))
        #Check if user is a student
        for user in students:
            if session['email'] == user['email']:
                session['amigo'] = False
                session['id'] = user['id']
                # Verify password
                if util.verify_pw(session['pw'], user['password']):
                    return redirect(url_for('home'))
        else:
            return 'A felhasználó nem található, próbáld újra. Ha nincs még profilod, regisztrálj!'
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.args:
        #Check if user is trying to register as amigo
        amigo = int(request.args.get('amigo'))
    else:
        #Ha nem amigo, akkor lesz 1 az amigo változó?
        amigo = 1
    if request.method == 'POST':
        error = None
        email = request.form['email']
        name = request.form['name']
        pw = str(util.hash_it(request.form['password']))[2:-1]
        if not validate_email(email):
            error = "Ezzel az e-mail címmel már regisztráltak a rendszerünkbe. Kérjük, próbáld újra egy másik fiókkal."
            return render_template('register.html')
        else:
            if int(request.form['amigo']) == 0:
                data_handler.register_amigo(name, email, pw)
                session['amigo'] = True
            else:
                birthday, languages = student_register()
                # TODO: sort out latest id
                student_id = data_handler.get_latest_id()['id'] + 1
                data_handler.register_student(name, email, pw, birthday, languages, student_id)
                session['amigo'] = False
            session['email'] = email
            return redirect(url_for('home'))
    else:
        return render_template('register.html', amigo=amigo)


def student_register():
    birthday = request.form['birthday']
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
    return birthday, languages


def validate_email(email):
    users = [data_handler.get_students(), data_handler.get_amigos()]
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
        id = session['id']
        return render_template('index.html', id=id)


@app.route('/my_exercises')
def my_exercises():
    return 'Implementation in process. Don\'t be an impatient dick!'


# Route for accessing user profile
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    # Check if user is an amigo
    if session['amigo']:
        # Get the user data by email address
        amigo = data_handler.get_amigo(session['id'])
        # Update data if modifying post request was sent
        if request.method == 'POST':
            data_handler.update_amigo(request.form['name'], request.form['birthday'], request.form['email'], session['id'])
        else:
            return render_template('amigo-profile.html', amigo=amigo)
    else:
         # Get the user data by email address
        student = data_handler.get_student(session['id'])
        # Update data if modifying post request was sent
        if request.method == 'POST':
            data_handler.update_student(request.form['name'], request.form['email'], request.form['birthday'], session['id'])
            student = data_handler.get_student(session['id'])
            return render_template('student-profile.html', student=student)
        else:
            return render_template('student-profile.html', student=student)


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


@app.route('/matching-game')
def matching_game():
    return 'Implementation in process. Don\'t be an impatient dick!'


@app.route('/memory-game')
def memory_game():
    return 'Implementation in process. Don\'t be an impatient dick!'


@app.route('/sorting-game')
def sorting_game():
    return 'Implementation in process. Don\'t be an impatient dick!'


@app.route('/listening-game')
def listening_game():
    return 'Implementation in process. Don\'t be an impatient dick!'


@app.route('/comprehensive-reading')
def comprehensive_reading():
    return 'Implementation in process. Don\'t be an impatient dick!'


@app.route('/filling-game')
def filling_game():
    return 'Implementation in process. Don\'t be an impatient dick!'


if __name__ == "__main__":
    app.run(
        debug=True,
        port=8000)
