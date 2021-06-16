import json

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


@app.route('/my-exercises/<id>')
def my_exercises_student(id):
    return render_template('student-exercises.html', student_id=id)


@app.route('/send/<game_type>/<game_id>', methods=['GET', 'POST'])
def send_game_to_student(game_type, game_id):
    if request.method == 'POST':
        student_list = request.get_json()
        for student in student_list:
            data_handler.add_student_exercises(student, game_id, game_type)
        return jsonify('Success', 200)
    else:
        return render_template('send-task.html', game_type=game_type, game_id=game_id)


@app.route('/save/pictures/<game_type>', methods=['GET', 'POST'])
def save_picture_game(game_type):
    if request.method == 'POST':
        data = request.get_json()
        data_handler.save_picture_game(game_type.replace('-', '_'), data["language"], data["theme"], data["images"])
        return jsonify('Success', 200)
    else:
        return render_template('picture-upload.html', game_type=game_type)



@app.route('/solutions')
def solutions():
    return render_template('solutions.html')


@app.route('/feedback/<student_id>', methods=['GET', 'POST'])
def feedbacks(student_id):
    if request.method == 'POST':
        amigo_id = session['id']
        title = request.form['title']
        feedback = request.form['feedback']
        data_handler.give_feedback(amigo_id, student_id, title, feedback)
        return redirect(url_for('students'))
    else:
        return render_template('feedback.html', student_id=student_id)


@app.route('/students')
def students():
    return render_template("list_students.html")


@app.route('/search/<search_column>/<search_param>')
def search_students(search_param, search_column):
    data = data_handler.search_students(search_param.capitalize(), search_column)
    return jsonify(data)


@app.route('/game-list/<game_type>')
def list_games(game_type):
    games = data_handler.get_games(game_type.replace('-', '_'))
    if session['amigo']:
        return render_template('amigo-game-types.html', games=games, exercise=game_type)
    else:
        return render_template('game-types.html', all=True, games=games, exercise=game_type)


@app.route('/game-list/<game_type>/<student_id>')
def list_student_games(game_type, student_id):
    exercise = game_type.replace('-', '_')
    game_ids = data_handler.get_student_exercises(student_id, game_type)
    if len(game_ids) != 0:
        games = []
        for g_id in game_ids:
            games.append(data_handler.get_game_by_id(exercise, g_id['game_id']))
        return render_template('game-types.html', games=games, exercise=game_type)
    else:
        return render_template('game-types.html', exercise=game_type)


@app.route('/get-game/<game_type>/<game_id>')
def get_game(game_type, game_id):
    data = data_handler.get_game_by_id(game_type.replace('-', '_'), game_id)
    return jsonify(data)


@app.route('/play-game/<game_type>/<game_id>')
def get_game_with_id(game_type, game_id):
    return render_template(f"{game_type}.html", game_id=game_id)

# SORTING GAME

@app.route('/sorting-game-upload', methods=['GET', 'POST'])
def sorting_game_upload():
    if request.method == 'POST':
        data = request.get_json()
        language = data['language']
        theme = data['theme']
        categories = data['categories']
        words = data['words']
        data_handler.save_sorting_exercise(language, theme, categories, words)
        return jsonify('Success', 200)
    else:
        return render_template('sorting_game_upload.html')


@app.route('/sorting-solution-saver/<game_id>', methods=['POST'])
def save_sorting_solution(game_id):
    data = request.get_json()
    data = json.dumps(data)     # Converts JSON object to string, which can be inserted into DB
    data_handler.save_sorting_game_solution(session['id'], game_id, data)
    if not session['amigo']:
        data_handler.update_score(session['id'])
    return jsonify('Success', 200)

# MATCHING GAME

@app.route('/matching-solution-saver/<game_id>', methods=['POST'])
def save_matching_solution(game_id):
    solution_time = request.get_json()
    data_handler.save_matching_game_solution(session['id'], game_id, solution_time)
    if not session['amigo']:
        data_handler.update_score(session['id'])
    return jsonify('Success', 200)


# MEMORY GAME

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
    if session['amigo']:
        return render_template('amigo-game-types.html', games=games, exercise=exercise)
    else:
        return render_template('game-types.html', all=True, games=games, exercise=exercise)


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
            data_handler.save_listening_game(game_id, data["language"], data["theme"], card)
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


@app.route('/listening-games/<id>')
def list_student_listening_games(id):
    exercise = "listening-game"
    game_ids = data_handler.get_student_exercises(id, exercise)
    if len(game_ids) != 0:
        listening_games = []
        for g_id in game_ids:
            listening_games.append(data_handler.get_listening_game(g_id['game_id']))
            print(listening_games[0])
        return render_template('game-types.html', games=listening_games, exercise=exercise)
    else:
        return render_template('game-types.html', exercise=exercise)


# COMPREHENSIVE READING

@app.route('/comprehensive-reading-upload', methods=['GET', 'POST'])
def comprehensive_reading_upload():
    if request.method == 'POST':
        theme_text_and_questions = request.get_json()
        language = theme_text_and_questions['language']
        theme = theme_text_and_questions['theme']
        long_text = theme_text_and_questions['long-text']
        questions = theme_text_and_questions['questions']
        data_handler.save_reading_exercise(language, theme, long_text, questions)
        return jsonify('Success', 200)
    else:
        return render_template('comprehensive_reading_upload.html')


@app.route('/comprehensive-reading-solution-saver/<game_id>', methods=['POST'])
def save_comprehensive_reading_solution(game_id):
    solution = request.get_json()
    data_handler.save_comprehensive_reading_solution(session['id'], game_id, solution)
    if not session['amigo']:
        data_handler.update_score(session['id'])
    return jsonify('Success', 200)


# FILLING GAPS

@app.route('/filling-gaps-upload', methods=['GET', 'POST'])
def filling_gaps_upload():
    if request.method == 'POST':
        data = request.get_json()
        theme = data['theme']
        long_text = data['long']
        gaps = data['gaps']
        data_handler.save_filling_exercise(theme, long_text, gaps)
        return jsonify('Success', 200)
    else:
        return render_template('filling_upload.html')


@app.route('/filling-gap-solution-saver/<game_id>', methods=['POST'])
def save_filling_game_solution(game_id):
    solution = request.get_json()
    data_handler.save_filling_game_solution(session['id'], game_id, solution)
    if not session['amigo']:
        data_handler.update_score(session['id'])
    return jsonify('Success', 200)


if __name__ == "__main__":
    app.run(
        debug=True,
        port=8000)
