import connection


def get_amigos():
    return connection.execute_select('SELECT id, email, password FROM amigo;')


def get_students():
    return connection.execute_select('SELECT id, email, password FROM student;')


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


def get_languages():
    query = """
    SELECT name, voice_code FROM language
    """
    return connection.execute_select(query)


def get_amigo(amigo_id):
    query = """ SELECT * FROM amigo
                WHERE id = %(amigo_id)s;
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

def update_score(student_id):
    query = """UPDATE student
                    SET points = points + 10
                    WHERE id=(%s)"""
    return connection.execute_dml_statement(query, {"student_id": student_id})


def get_student_exercises(student_id, game_type):
    query ="""
    SELECT game_id FROM student_exercises
    WHERE student_id = %(student_id)s AND game_type = %(game_type)s;
    """
    return connection.execute_select(query, {"student_id": student_id, "game_type": game_type})

def add_student_exercises(student_id, game_id, game_type):
    query ="""
        INSERT INTO student_exercises (student_id, game_id, game_type) VALUES (%(student_id)s, %(game_id)s, %(game_type)s);
    """
    return connection.execute_dml_statement(query, {"student_id": student_id, "game_id": game_id, "game_type": game_type})

#LISTENING GAME

def get_listening_games():
    query = """
        SELECT DISTINCT game_id as id, theme FROM listening_game;"""
    return connection.execute_select(query)

def get_latest_listening_game_id():
    return connection.execute_select('SELECT game_id FROM listening_game ORDER BY game_id DESC LIMIT 1', fetchall=False)


def save_listening_game(game_id,  language, theme, answers):
    query = """
    INSERT INTO listening_game(game_id, language, theme, answers, correct_answer) VALUES (%(game_id)s,  %(language)s,  
    %(theme)s,
    %(answers)s, %(correct)s);
    """
    return connection.execute_dml_statement(query, {"game_id": game_id, "language": language, "theme": theme,
                                                    "answers": answers,
                                                    "correct": answers[0]})


def get_listening_game(game_id):
    query = """
    SELECT * FROM listening_game
    WHERE game_id = %(game_id)s
     """
    return connection.execute_select(query, {"game_id": game_id})

def save_listening_game_solution(student_id, game_id, solution):
    query = """
       INSERT INTO listening_game_solution(student_id, game_id, solution) VALUES (%(student_id)s, %(game_id)s,   %(solution)s);
       """
    return connection.execute_dml_statement(query, {"game_id": game_id, "solution": solution, "student_id": student_id})


#MEMORY GAME

def get_memory_games():
    query = """
        SELECT id, theme FROM memory_game;
    """
    return connection.execute_select(query)

def get_memory_cards(game_id):
    query = """
    SELECT * FROM memory_game
    WHERE id = %(game_id)s
    """
    return connection.execute_select(query, {"game_id": game_id}, fetchall=False)

def save_memory_game_solution(student_id, game_id, solution_time):
    query = """
    INSERT INTO memory_game_solution(student_id, game_id, solution_time) 
               VALUES(%(student_id)s, %(game_id)s, %(solution_time)s)
    """
    return connection.execute_dml_statement(query, {"student_id": student_id, "game_id": game_id,
                                                    "solution_time": solution_time})


def save_memory_game(language, theme, images):
    query = """
    INSERT INTO memory_game(language, theme, image1, text1, image2, text2, image3, text3, image4, text4, image5, text5, image6, text6)
               VALUES(%(language)s, %(theme)s, %(image1)s, %(text1)s, %(image2)s, %(text2)s, %(image3)s, %(text3)s, %(image4)s, %(text4)s, %(image5)s, %(text5)s, %(image6)s, %(text6)s)
    """
    return connection.execute_dml_statement(query, {"language": language, "theme": theme, "image1": images[0]["image"],
                                                    "text1": images[0]["text"], "image2": images[1]["image"],
                                                    "text2": images[1]["text"],
                                                    "image3": images[2]["image"], "text3": images[2]["text"],
                                                    "image4": images[3]["image"],
                                                    "text4": images[3]["text"], "image5": images[4]["image"],
                                                    "text5": images[4]["text"],
                                                    "image6": images[5]["image"], "text6": images[5]["text"]})

# SORTING GAME

def save_sorting_exercise(language, theme, categories, words):
    query = 'INSERT INTO sorting_game(language, theme, categories, words) VALUES (%(language)s, %(theme)s, %(categories)s, %(words)s)'
    return connection.execute_dml_statement(query, {"language": language, "theme": theme, "words": words, "categories": categories})


def get_sorting_exercise(id):
    query = 'SELECT theme, categories, words FROM sorting_game WHERE id=%(id)s;'
    return connection.execute_select(query, {"id": id}, fetchall=False)

def get_sorting_games():
    query = """
            SELECT id, theme FROM sorting_game;
        """
    return connection.execute_select(query)


#MATCHING GAME

def save_matching_game(language, theme, images):
    query = """
        INSERT INTO matching_game(language, theme, image1, text1, image2, text2, image3, text3, image4, text4, image5, text5, image6, text6)
                   VALUES(%(language)s, %(theme)s, %(image1)s, %(text1)s, %(image2)s, %(text2)s, %(image3)s, %(text3)s, %(image4)s, %(text4)s, %(image5)s, %(text5)s, %(image6)s, %(text6)s)
        """
    return connection.execute_dml_statement(query, {"language": language, "theme": theme, "image1": images[0]["image"],
                                                    "text1": images[0]["text"], "image2": images[1]["image"],
                                                    "text2": images[1]["text"],
                                                    "image3": images[2]["image"], "text3": images[2]["text"],
                                                    "image4": images[3]["image"],
                                                    "text4": images[3]["text"], "image5": images[4]["image"],
                                                    "text5": images[4]["text"],
                                                    "image6": images[5]["image"], "text6": images[5]["text"]})


def get_matching_games():
    query = """
        SELECT id, theme FROM matching_game;
    """
    return connection.execute_select(query)


def get_matching_game(game_id):
    query = """
    SELECT * FROM matching_game
    WHERE id = %(game_id)s"""
    return connection.execute_select(query, {"game_id": game_id}, fetchall=False)


def save_matching_game_solution(student_id, game_id, solution_time):
    query = """
     INSERT INTO matching_game_solution(student_id, game_id, solution_time) 
                VALUES(%(student_id)s, %(game_id)s, %(solution_time)s)
     """
    return connection.execute_dml_statement(query, {"student_id": student_id, "game_id": game_id,
                                                    "solution_time": solution_time})


#COMPREHENSIVE READING

def save_reading_exercise(language, theme, long_text, questions):
    query = """INSERT INTO comprehensive_reading(language, theme, long_text, questions) VALUES (%(language)s, %(theme)s, %(long_text)s, %(questions)s);"""
    return connection.execute_dml_statement(query, {"language": language, "theme": theme, "long_text": long_text, "questions": questions})


def get_comprehensive_readings():
    query = """
             SELECT id, theme FROM comprehensive_reading;
         """
    return connection.execute_select(query)


def get_comprehensive_reading(game_id):
    query = """
    SELECT * FROM comprehensive_reading
    WHERE id = %(game_id)s
     """
    return connection.execute_select(query, {"game_id": game_id}, fetchall=False)


def save_comprehensive_reading_solution(student_id, game_id, solution):
    query = """
       INSERT INTO comprehensive_reading_solution(student_id, game_id, solution) VALUES (%(student_id)s, %(game_id)s,   %(solution)s);
       """
    return connection.execute_dml_statement(query, {"game_id": game_id, "solution": solution, "student_id": student_id})



def student_search_by_language(language):
    query = """
    SELECT student.name AS name , email , DATE_PART('year', birthday) AS birthday,  array_agg(l.name)  AS language , points  FROM student
    FULL JOIN student_languages sl on student.id = sl.student_id
    FULL JOIN language l on sl.language_id = l.id
    WHERE l.name ILIKE %(language)s AND student.name IS NOT NULL
    GROUP BY student.name, email, DATE_PART('year', birthday), points
    """
    return connection.execute_select(query, {'language': '%' + language + '%'})


def student_search_by_email(student_email):
    query = """
    SELECT student.name  , email , DATE_PART('year', birthday) AS birthday,  array_agg(l.name)   AS language, points  FROM student
    join student_languages sl on student.id = sl.student_id
    join language l on sl.language_id = l.id
    WHERE email ILIKE %(student_email)s
    GROUP BY student.name, email, DATE_PART('year', birthday), points
    """
    return connection.execute_select(query, {'student_email': '%' + student_email + '%'})


def student_search_by_birthday(bday):
    query = """
    SELECT student.name , email , DATE_PART('year', birthday) AS birthday, array_agg(l.name)  AS language, points  FROM student
    join student_languages sl on student.id = sl.student_id
    join language l on sl.language_id = l.id
    WHERE DATE_PART('year', birthday) > %(bday)s
    GROUP BY student.name, email, DATE_PART('year', birthday), points
    """
    return connection.execute_select(query, {'bday': bday})
