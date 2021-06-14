from flask import Flask, render_template, url_for, redirect, session, request, flash, jsonify, make_response

import data_handler
import util

app = Flask("amigo")
app.secret_key = b'_5#z2L"F7Q8q\n\xec]/'


# Authenticating user based on an SQL database query by comparing POST request form data.
# Form requires email address and password inputs. Upon successful authentication user role is set
# as student or amigo.
@app.route('/login', methods=['GET', 'POST'])
def login():
    amigos = data_handler.get_amigos()
    students = data_handler.get_students()

    if request.method == 'POST':
        # TODO: authentication function
        session['email'] = request.form['email']
        for user in amigos:
            if session['email'] == user['email']:
                session['amigo'] = True
                session['id'] = user['id']
                if util.verify_pw(request.form['password'], user['password']):
                    return redirect(url_for('home'))

        # Check if user is a student

        for user in students:
            if session['email'] == user['email']:
                session['amigo'] = False
                session['id'] = user['id']
                # Verify password
                if util.verify_pw(request.form['password'], user['password']):
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
        amigo = 0
    if request.method == 'POST':
        error = None
        email = request.form['email']
        name = request.form['name']
        pw = str(util.hash_it(request.form['password']))[2:-1]
        if not validate_email(email):
            error = "Ezzel az e-mail címmel már regisztráltak a rendszerünkbe. Kérjük, próbáld újra egy másik fiókkal."
            return render_template('register.html')
        else:
            if int(request.form['amigo']) == 1:
                data_handler.register_amigo(name, email, pw)
                session['amigo'] = True
            else:
                # student_id = data_handler.get_latest_id()['id'] + 1
                # data_handler.register_student(name, email, pw, birthday, languages, student_id)
                session['amigo'] = False
            session['email'] = email
            return redirect(url_for('home'))
    else:
        return render_template('register.html', amigo=amigo)


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


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if session['amigo']:
        amigo = data_handler.get_amigo(session['id'])
        if request.method == 'POST':
            data_handler.update_amigo(request.form['name'], request.form['birthday'], request.form['email'],
                                      session['id'])
        else:
            return render_template('amigo-profile.html', amigo=amigo)
    else:
        student = data_handler.get_student(session['id'])
        languages = data_handler.get_student_languages(session['id'])
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


@app.route('/my_exercises')
def my_exercises():
    return render_template('exercises.html')


@app.route('/solutions')
def solutions():
    return 'Implementation in process. '


@app.route('/students')
def students():
    return 'Implementation in process. '


# SORTING GAME

@app.route('/upload-words', methods=['POST'])
def upload_words():
    data = request.get_json()
    theme = data['theme']
    themes = data['themes']
    words = data['words']
    data_handler.save_sorting_exercise(theme, themes, words)
    return jsonify(data)


@app.route('/sorting-game-upload')
def sorting_game_upload():
    return render_template('sorting_game_upload.html')


@app.route('/sorting-game/<id>')
def sorting_game(id):
    theme = data_handler.get_sorting_exercise(id)['theme']
    themes = data_handler.get_sorting_exercise(id)['categories']
    words = data_handler.get_sorting_exercise(id)['words']
    return render_template('sorting_game.html', theme=theme, themes=themes, words=words)


@app.route('/sorting-games')
def sorting_games():
    exercise = "sorting-game"
    sorting_games = data_handler.get_sorting_games()
    return render_template('game-types.html', games=sorting_games, exercise=exercise)


# MATCHING GAME

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


@app.route('/matching-games')
def list_matching_games():
    exercise = "matching-game"
    matching_games = data_handler.get_matching_games()
    return render_template('game-types.html', games=matching_games, exercise=exercise)


@app.route('/matching-solution-saver/<game_id>', methods=['POST'])
def save_matching_solution(game_id):
    solution_time = request.get_json()
    data_handler.save_matching_game_solution(session['id'], game_id, solution_time)
    if not session['amigo']:
        data_handler.update_score(session['id'])
    return jsonify('Success', 200)


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


# Listening game

@app.route('/listening-games')
def list_listening_games():
    exercise = "listening-game"
    games = data_handler.get_listening_games()
    return render_template('game-types.html', games=games, exercise=exercise)


@app.route('/get-listening-game/<game_id>')
def get_listening_game(game_id):
    data = data_handler.get_listening_game(game_id)
    return jsonify(data)


@app.route('/listening-game/<game_id>')
def listening_game_with_id(game_id):
    return render_template('listening_game.html', game_id=game_id)


@app.route('/listening-game-upload', methods=['GET', 'POST'])
def listening_game_upload():
    if request.method == 'POST':
        data = request.get_json()
        game_id_data = data_handler.get_latest_listening_game_id()
        if game_id_data is None:
            game_id = 1
        else:
            game_id = game_id_data["game_id"] + 1
        for card in data["cards"]:
            data_handler.save_listening_game(game_id, data["theme"], data["language"], card)
        return jsonify('Success', 200)
    else:
        languages = data_handler.get_languages()
        return render_template('listening_game_upload.html', languages=languages)


@app.route('/listening-solution-saver/<game_id>', methods=['POST'])
def save_listening_solution(game_id):
    solution = request.get_json()
    data_handler.save_listening_game_solution(session['id'], game_id, solution)
    if not session['amigo']:
        data_handler.update_score(session['id'])
    return jsonify('Success', 200)


# COMPREHENSIVE READING

@app.route('/comprehensive-reading-upload', methods=['GET', 'POST'])
def comprehensive_reading_upload():
    if request.method == 'POST':
        theme_text_and_questions = request.get_json()
        theme = theme_text_and_questions['theme']
        long_text = theme_text_and_questions['long-text']
        questions = theme_text_and_questions['questions']
        data_handler.save_reading_exercise(theme, long_text, questions)
        return jsonify('Success', 200)
    else:
        return render_template('comprehensive_reading_upload.html')


@app.route('/comprehensive-readings')
def list_comprehensive_readings():
    exercise = "comprehensive-reading"
    games = data_handler.get_comprehensive_readings()
    return render_template('game-types.html', games=games, exercise=exercise)

@app.route('/get-comprehensive-reading/<game_id>')
def get_comprehensive_reading(game_id):
    data = data_handler.get_comprehensive_reading(game_id)
    return jsonify(data)


@app.route('/comprehensive-reading/<game_id>')
def comprehensive_reading_with_id(game_id):
    return render_template('comprehensive-reading.html', game_id=game_id)


@app.route('/comprehensive-reading-solution-saver/<game_id>', methods=['POST'])
def save_comprehensive_reading_solution(game_id):
    solution = request.get_json()
    data_handler.save_comprehensive_reading_solution(session['id'], game_id, solution)
    if not session['amigo']:
        data_handler.update_score(session['id'])
    return jsonify('Success', 200)


if __name__ == "__main__":
    app.run(
        debug=True,
        port=8000)
