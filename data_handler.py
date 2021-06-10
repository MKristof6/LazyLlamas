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


def new_matching_exercise(theme, word1, word2, word3, word4, word5, word6, image1, image2, image3, image4, image5,
                          image6):
    connection.execute_dml_statement(
        """INSERT INTO matching_exercise(theme, word1, word2, word3, word4, word5, word6, image1, image2, image3, image4, image5, image6) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
        [theme, word1, word2, word3, word4, word5, word6, image1, image2, image3, image4, image5, image6])


def get_matching_exercise(id):
    query = """SELECT theme, word1, image1, word2, image2, word3, image3, word4, image4, word5, image5, word6, image6 FROM matching_exercise WHERE id = %(id)s"""
    return connection.execute_select(query, {"id": id}, fetchall=False)


def get_latest_matching_exercise_id():
    return connection.execute_select('SELECT id FROM matching_exercise ORDER BY id DESC LIMIT 1', fetchall=False)


def get_memory_cards(game_id):
    query = """
    SELECT * FROM memory_game
    WHERE id = %(game_id)s
    """
    return connection.execute_select(query, {"game_id": game_id})


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


def save_memory_game_solution(student_id, game_id, solution_time):
    query = """
    INSERT INTO memory_game_solution(student_id, game_id, solution_time) 
               VALUES(%(student_id)s, %(game_id)s, %(solution_time)s)
    """
    return connection.execute_dml_statement(query, {"student_id": student_id, "game_id": game_id,
                                                    "solution_time": solution_time})


def save_memory_game(theme, images):
    query = """
    INSERT INTO memory_game(theme, image1, text1, image2, text2, image3, text3, image4, text4, image5, text5, image6, text6)
               VALUES(%(theme)s, %(image1)s, %(text1)s, %(image2)s, %(text2)s, %(image3)s, %(text3)s, %(image4)s, %(text4)s, %(image5)s, %(text5)s, %(image6)s, %(text6)s)
    """
    return connection.execute_dml_statement(query, {"theme": theme, "image1": images[0]["image"],
                                                    "text1": images[0]["text"], "image2": images[1]["image"],
                                                    "text2": images[1]["text"],
                                                    "image3": images[2]["image"], "text3": images[2]["text"],
                                                    "image4": images[3]["image"],
                                                    "text4": images[3]["text"], "image5": images[4]["image"],
                                                    "text5": images[4]["text"],
                                                    "image6": images[5]["image"], "text6": images[5]["text"]})


def get_memory_games():
    query = """
        SELECT id, theme FROM memory_game;
    """
    return connection.execute_select(query)
