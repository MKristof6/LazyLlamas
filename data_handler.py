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


def get_listening_game_data(game_id):
    query = """
    SELECT  answer, language, array_agg(possibility) AS possibilities FROM listening_game_answer
    FUll JOIN listening_cards ON listening_cards.id = listening_game_answer.id
    FULL JOIN listening_game_possibilities lgp on listening_cards.task_id = lgp.task_id AND lgp.card_id = listening_cards.id
    WHERE listening_cards.task_id = %(game_id)s
    GROUP BY answer,language
    """
    return connection.execute_select(query, {'game_id': game_id})


def get_languages():
    query="""
    SELECT name, voice_code FROM language
    """
    return connection.execute_select(query)






# a p
# a p2
# a p3
#
# a p p2 p3

# , listening_game_answer.id, lgp.card_id, listening_cards.id, lgp.task_id
#, listening_game_answer.id, answer, lgp.card_id, listening_cards.id, lgp.task_id
