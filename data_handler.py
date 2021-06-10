import connection


def get_amigos():
    return connection.execute_select('SELECT id, email, password FROM amigo;')


def get_students():
    return connection.execute_select('SELECT id, email, password FROM student;')


def register_student(name, email, password, birthday, languages, student_id):
    add_student_languages(student_id, languages)
    query = """INSERT INTO student(name, email, password, birthday, points) 
               VALUES(%s, %s, %s, %s, 0)"""
    return connection.execute_dml_statement(query,
                                            {"name": name, "email": email, password: "password", "birthday": birthday,
                                             "languages": languages})


def register_amigo(name, email, password):
    query = """INSERT INTO amigo(name, email, password) 
                VALUES(%s, %s, %s)"""
    return connection.execute_dml_statement(query, {"name": name, "email": email, password: "password"})


def add_student_languages(student_id, languages):
    query = """INSERT INTO student_languages(student_id, language_id) VALUES(%s, %s)"""
    return connection.execute_dml_statement(query, {"student_id": student_id, "languages": languages})


def update_student_languages(student_id, languages):
    query = """UPDATE student_languages 
                SET language_id=(%s) 
                WHERE student_id=(%s)"""
    return connection.execute_dml_statement(query, {"languages": languages, "student_id": student_id})


def get_latest_id():
    return connection.execute_select('SELECT id FROM student ORDER BY id DESC LIMIT 1', fetchall=False)


def get_memory_cards(game_number):
    query = """
    SELECT * FROM memory_game
    WHERE id = 1
    """
    return connection.execute_select(query)


def get_amigo(amigo_id):
    query = """ SELECT * FROM amigo
                WHERE id = %(id)s;
    """
    return connection.execute_select(query, {"amigo_id": amigo_id}, fetchall=False)


def get_student(student_id):
    query = """ SELECT * FROM student
                WHERE id = %(student_id)s;"""
    return connection.execute_select(query, {"student_id": student_id}, fetchall=False)


def update_amigo(name, email, birthday, id):
    query = """ UPDATE amigo
            SET name = %(name)s, email = %(email)s
            WHERE id = %(id)s;
    """
    return connection.execute_dml_statement(query, {"name": name, "email": email, "birthday": birthday, "id": id})


def update_student(name, email, birthday, id):
    query = """ UPDATE student
            SET name = %(name)s, email = %(email)s, birthday = %(birthday)s
            WHERE id = %(id)s;
    """
    return connection.execute_dml_statement(query, {"name": name, "email": email, "birthday": birthday, "id": id})


def get_student_languages(student_id):
    query = """ SELECT string_agg(DISTINCT l.name, ', ') as languages FROM student
                INNER JOIN student_languages sl on student.id = sl.student_id
                INNER JOIN language l on sl.language_id=l.id;
    """
    return connection.execute_select(query, {"student_id": student_id}, fetchall=False)


def new_sorting_exercise(themes, words):
    query = 'INSERT INTO sorting_game(themes, words) VALUES (%(themes)s, %(words)s)'
    return connection.execute_dml_statement(query, {"themes": themes, "words": words})


def get_sorting_exercise(id):
    query = 'SELECT themes, words FROM sorting_game WHERE id=%(id)s;'
    return connection.execute_select(query, {"id": id}, fetchall=False)

