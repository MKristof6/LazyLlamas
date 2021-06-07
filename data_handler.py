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


def get_listening_game_answer(id):
    query = """
    SELECT * FROM listening_game
    WHERE id =%(question_id)s
    """
    return connection.execute_select(query, {'question_id':id})

def get_listening_game_possibilities(question_id, c_id):
    query="""
    SELECT * FROM listening_game_possibilities
    WHERE id = %(question_id)s AND card_id = %(c_id)s
    """
    return connection.execute_select(query, {'question_id':question_id, 'c_id':c_id})

