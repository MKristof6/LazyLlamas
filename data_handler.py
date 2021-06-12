import connection


def get_teachers():
    return connection.execute_select('SELECT email, password FROM teacher;')


def get_students():
    return connection.execute_select('SELECT email, password FROM student;')


def register_student(name, email, password, bday, languages, student_id):
    update_student_languages(student_id, languages)
    return connection.execute_dml_statement(
        """INSERT INTO student(name, email, password, birthday, points, language_id) VALUES(%s, %s, %s, %s, 0, %s)""",
        [name, email, password, bday, languages])


def register_teacher(name, email, password):
    return connection.execute_dml_statement("""INSERT INTO teacher(name, email, password) VALUES(%s, %s, %s)""",
                                            [name, email, password])


def update_student_languages(student_id, languages):
    return connection.execute_dml_statement("""INSERT INTO student_languages(student_id, language_id) VALUES(%s, %s)""",
                                            [student_id, languages])


def get_latest_id():
    return connection.execute_select('SELECT id FROM student ORDER BY id DESC LIMIT 1', fetchall=False)



def get_languages():
    query="""
    SELECT name, voice_code FROM language
    """
    return connection.execute_select(query)


def get_latest_listening_game_id():
    return connection.execute_select('SELECT game_id FROM listening_game ORDER BY game_id DESC LIMIT 1', fetchall=False)


def save_listening_game(game_id, theme, language,  answers):
    query ="""
    INSERT INTO listening_game(game_id, theme, language, answers, correct_answer) VALUES (%(game_id)s, %(language)s, %(theme)s, 
    %(answers)s, %(correct)s);
    """
    return connection.execute_dml_statement(query, {"game_id": game_id, "language": language, "theme": theme, "answers": answers,
                                                    "correct": answers[0]})
