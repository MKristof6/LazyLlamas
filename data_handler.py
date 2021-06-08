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


def new_matching_exercise(theme, word1, word2, word3, word4, word5, word6, image1, image2, image3, image4, image5, image6):
    connection.execute_dml_statement(
        """INSERT INTO matching_exercise(theme, word1, word2, word3, word4, word5, word6, image1, image2, image3, image4, image5, image6) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
        [theme, word1, word2, word3, word4, word5, word6, image1, image2, image3, image4, image5, image6])


def get_matching_exercise(id):
    return connection.execute_select("""SELECT theme, word1, image1, word2, image2, word3, image3, word4, image4, word5, image5, word6, image6 FROM matching_exercise WHERE id = %s""", [id])


def get_latest_matching_exercise_id():
    return connection.execute_select('SELECT id FROM matching_exercise ORDER BY id DESC LIMIT 1', fetchall=False)
