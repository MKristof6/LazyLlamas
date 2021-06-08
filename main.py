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


@app.route('/matching-game-upload', methods=['GET', 'POST'])
def matching_game_upload():
    if request.method == 'POST':    # What if multiple amigos give the same theme? Folder path will be compromised, needs fix!
        theme = request.form['theme']
        word1 = request.form['word1']
        word2 = request.form['word2']
        word3 = request.form['word3']
        word4 = request.form['word4']
        word5 = request.form['word5']
        word6 = request.form['word6']
        # Saving image file to static/images/theme folder, and returning with the path + filename
        image1 = util.get_image(request.files['img1'])
        image2 = util.get_image(request.files['img2'])
        image3 = util.get_image(request.files['img3'])
        image4 = util.get_image(request.files['img4'])
        image5 = util.get_image(request.files['img5'])
        image6 = util.get_image(request.files['img6'])
        # Inserting form data to database
        data_handler.new_matching_exercise(theme, word1, word2, word3, word4, word5, word6, image1, image2, image3, image4,
                                           image5, image6)
        # Redirecting using the newly inserted row's id
        id = data_handler.get_latest_matching_exercise_id()['id']
        return redirect('/matching-game/' + str(id))
    else:
        return render_template('matching_upload.html')


@app.route('/matching-game/<id>')
def matching_game(id):
    # Getting the data through row id
    theme_and_images_and_words = data_handler.get_matching_exercise(id)
    print(theme_and_images_and_words)
    data = []
    theme = theme_and_images_and_words[0]['theme']
    for t in theme_and_images_and_words:
        for i in range(1, 7):
            data.append((t['image' + str(i)], t['word' + str(i)]))
    print(data)
    return render_template('matching_game.html', data=data, theme=theme)



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
