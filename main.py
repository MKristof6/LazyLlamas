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
        if not validate_email(email):
            error = "Ezzel az e-mail címmel már regisztráltak a rendszerünkbe. Kérjük, próbáld újra egy másik fiókkal."
            return render_template('register.html')
        else:
            if int(request.form['amigo']) == 0:
                data_handler.register_teacher(name, email, pw)
                session['amigo'] = True
            else:
                bday, languages = student_register()
                student_id = data_handler.get_latest_id()['id'] + 1
                data_handler.register_student(name, email, pw, bday, languages, student_id)
                session['amigo'] = False
            session['email'] = email
            return redirect(url_for('home'))
    else:
        return render_template('register.html', amigo=amigo)


def student_register():
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
    return bday, languages


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


@app.route('/solutions')
def solutions():
    return 'Implementation in process. Don\'t be an impatient dick!'


@app.route('/students')
def students():
    return 'Implementation in process. Don\'t be an impatient dick!'


@app.route('/exercises')
def exercises():
    return 'Implementation in process. Don\'t be an impatient dick!'


@app.route('/matching-game', methods=['GET', 'POST'])
def matching_game():
    if request.method == 'POST':
        words = []
        images = []
        for i in range(1, 7):
            words.append(request.form['text' + str(i)])
            images.append(util.get_image(request.files['img' + str(i)]))
        word1 = words[0]
        word2 = words[1]
        word3 = words[2]
        word4 = words[3]
        word5 = words[4]
        word6 = words[5]
        image1 = images[0]
        image2 = images[1]
        image3 = images[2]
        image4 = images[3]
        image5 = images[4]
        image6 = images[5]
        data_handler.new_matching_exercise(word1, word2, word3, word4, word5, word6, image1, image2, image3, image4, image5, image6)
        return 'shit'
    else:
        return render_template('matching.html')


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
