from flask import Flask, render_template, url_for, redirect, session, request, flash, jsonify, make_response

import data_handler
import util

app = Flask("amigo")
app.secret_key = b'_5#z2L"F7Q8q\n\xec]/'


@app.route('/speech')
def speech():
    return render_template('speech.html')


# Authenticating user based on an SQL database query by comparing POST request form data.
# Form requires email address and password inputs. Upon successful authentication user role is set
# as student or amigo.
@app.route('/login', methods=['GET', 'POST'])
def login():
    amigos = data_handler.get_amigos()
    students = data_handler.get_students()

    if request.method == 'POST':
        # TODO: authentication function
        session['pw'] = request.form['password']
        session['email'] = request.form['email']
        for user in amigos:
            if session['email'] == user['email']:
                session['amigo'] = True
                session['id'] = user['id']
                if util.verify_pw(session['pw'], user['password']):
                    return redirect(url_for('home'))

        # Check if user is a student

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
        # Check if user is trying to register as amigo
        amigo = int(request.args.get('amigo'))
    else:
        # Ha nem amigo, akkor lesz 1 az amigo változó?
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
    return render_template('exercises.html')


# Route for accessing user profile
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    # Check if user is an amigo
    if session['amigo']:
        # Get the user data by amigo id
        amigo = data_handler.get_amigo(session['id'])
        # Update data if modifying post request was sent
        if request.method == 'POST':
            data_handler.update_amigo(request.form['name'], request.form['birthday'], request.form['email'],
                                      session['id'])
        else:
            return render_template('amigo-profile.html', amigo=amigo)
    else:
        # Get the user data by student id
        student = data_handler.get_student(session['id'])
        # Get studied languages by student id
        languages = data_handler.get_student_languages(session['id'])
        # Update data if modifying post request was sent
        if request.method == 'POST':
            data_handler.update_student(request.form['name'], request.form['email'], request.form['birthday'],
                                        session['id'])
            student = data_handler.get_student(session['id'])
            return render_template('student-profile.html', student=student, languages=languages)
        else:
            return render_template('student-profile.html', student=student, languages=languages)


@app.route('/new_exercise')
def new_exercise():
    return render_template("new_exercises.html")


@app.route('/solutions')
def solutions():
    return 'Implementation in process. '


@app.route('/students')
def students():
    return 'Implementation in process. '


@app.route('/exercises')
def exercises():
    return 'Implementation in process. '


@app.route('/matching-game')
def matching_game():
    return 'Implementation in process. '


@app.route('/upload-words', methods=['POST'])
def upload_words():
    data = request.get_json()
    themes = data['themes']
    words = data['words']
    data_handler.new_sorting_exercise(themes, words)
    return jsonify(data)


@app.route('/sorting-game-upload')
def sorting_game_upload():
    return render_template('sorting_game_upload.html')


@app.route('/sorting-game/<id>')
def sorting_game(id):
    themes = data_handler.get_sorting_exercise(id)['themes']
    words = data_handler.get_sorting_exercise(id)['words']
    return render_template('sorting_game.html', themes=themes, words=words)


@app.route('/sorting-games')
def sorting_games():
    return 'Implementation in process.'


@app.route('/listening-game')
def listening_game():
    return 'Implementation in process.'


@app.route('/comprehensive-reading')
def comprehensive_reading():
    return 'Implementation in process. '


@app.route('/filling-game')
def filling_game():
    return 'Implementation in process.'


# MEMORY GAME

@app.route('/memory-game-upload', methods=['GET', 'POST'])
def memory_game_upload():
    if request.method == 'POST':
        data = request.get_json()
        data_handler.save_memory_game(data["language"], data["theme"], data["images"])
        return jsonify('Success', 200)
    else:
        return render_template('memory-game-saver.html')


@app.route('/memory-games')
def list_memory_games():
    exercise = "memory-game"
    memory_games = data_handler.get_memory_games()
    return render_template('game-types.html', games=memory_games, exercise=exercise)


@app.route('/matching-games')
def list_matching_games():
    exercise = "matching-game"
    matching_games = data_handler.get_matching_games()
    return render_template('game-types.html', games=matching_games, exercise=exercise)

@app.route('/memory-game/<game_id>')
def memory_game_with_id(game_id):
    return render_template('memory-game.html', game_id=game_id)


@app.route('/get-memory-game/<game_id>')
def get_memory_game(game_id):
    data = data_handler.get_memory_cards(game_id)
    return jsonify(data)


@app.route('/memory-solution-saver/<game_id>', methods=['POST'])
def save_memory_solution(game_id):
    solution_time = request.get_json()
    data_handler.save_memory_game_solution(session['id'], game_id, solution_time)
    if not session['amigo']:
        data_handler.update_score(session['id'])
    return jsonify('Success', 200)


@app.route('/matching-game-upload', methods=['GET', 'POST'])
def matching_game_upload():
    if request.method == 'POST':
        data = request.get_json()
        data_handler.save_matching_game(data["language"], data["theme"], data["images"])
        return jsonify('Success', 200)
    else:
        return render_template('matching_upload.html')

@app.route('/get-matching-game/<game_id>')
def get_matching_game(game_id):
    data = data_handler.get_matching_game(game_id)
    return jsonify(data)

@app.route('/matching-game/<game_id>')
def matching_game_with_id(game_id):
    return render_template('matching-game.html', game_id=game_id)


    #
    # # Getting the data through row id
    # theme_and_images_and_words = data_handler.get_matching_exercise(id)
    # data = []
    # theme = theme_and_images_and_words[0]['theme']
    # for t in theme_and_images_and_words:
    #     for i in range(1, 7):
    #         data.append((t['image' + str(i)], t['word' + str(i)]))
    # return render_template('matching-game.html', data=data, theme=theme)


if __name__ == "__main__":
    app.run(
        debug=True,
        port=8000)
