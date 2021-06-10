import connection


def get_teachers():
    return connection.execute_select('SELECT email, password FROM teacher;')


def get_students():
    return connection.execute_select('SELECT email, password FROM student;')


def register_student(name, email, password, bday, languages, student_id):
    update_student_languages(student_id, languages)
    return connection.execute_dml_statement("""INSERT INTO student(name, email, password, birthday, points, language_id) VALUES(%s, %s, %s, %s, 0, %s)""", [name, email, password, bday, languages])


def register_teacher(name, email, password):
    return connection.execute_dml_statement("""INSERT INTO teacher(name, email, password) VALUES(%s, %s, %s)""", [name, email, password])


def update_student_languages(student_id, languages):
    return connection.execute_dml_statement("""INSERT INTO student_languages(student_id, language_id) VALUES(%s, %s)""", [student_id, languages])


def get_latest_id():
    return connection.execute_select('SELECT id FROM student ORDER BY id DESC LIMIT 1', fetchall=False)


def get_listening_game_data(game_id):
    query = """
    SELECT answer, possibility FROM listening_game_answer
    LEFT JOIN listening_cards ON listening_cards.id = listening_game_answer.id
    LEFT JOIN listening_game_possibilities lgp on listening_cards.id = lgp.card_id
    WHERE listening_cards.task_id = %(game_id)s
    """
    return connection.execute_select(query, {'game_id': game_id})

