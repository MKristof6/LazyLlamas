from flask import Flask, render_template, url_for, redirect, session, request, flash, jsonify

import data_handler
import util

app = Flask("amigo")
app.secret_key = b'_5#z2L"F7Q8q\n\xec]/'


@app.route('/login', methods=['GET', 'POST'])
def login():
    amigos = data_handler.get_amigos()
    students = data_handler.get_students()
    if request.method == 'POST':
        session['pw'] = request.form['password']
        session['email'] = request.form['email']
        for user in amigos:
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
                data_handler.register_amigo(name, email, pw)
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


@app.route('/matching_-ame')
def matching_game():
    return 'Implementation in process. Don\'t be an impatient dick!'


@app.route('/memory-game')
def memory_game():
    return 'Implementation in process. Don\'t be an impatient dick!'


@app.route('/sorting-game')
def sorting_game():
    return 'Implementation in process. Don\'t be an impatient dick!'


@app.route('/listening-game')
def list_listening_games():
    games = data_handler.get_listening_games()
    return render_template('listening_game.html')


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
        return render_template('listening_game_upload.html',  languages=languages)


@app.route('/listening-solution-saver/<game_id>', methods=['POST'])
def save_matching_solution(game_id):
    solution = request.get_json()
    data_handler.save_listening_game_solution(session['id'], game_id, solution)
    if not session['amigo']:
        data_handler.update_score(session['id'])
    return jsonify('Success', 200)


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
