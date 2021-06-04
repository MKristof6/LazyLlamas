import connection
from psycopg2._psycopg import AsIs

def get_teachers():
    return connection.execute_select('SELECT id, email, password FROM teacher;')


def get_students():
    return connection.execute_select('SELECT id, email, password FROM student;')


def register_student(name, email, password, bday, languages, student_id):
    add_student_languages(student_id, languages)
    query = """INSERT INTO student(name, email, password, birthday, points, language_id) 
               VALUES(%s, %s, %s, %s, 0, %s)"""
    return connection.execute_dml_statement(query, [name, email, password, bday, languages])


def register_teacher(name, email, password):
    query = """INSERT INTO teacher(name, email, password) 
                VALUES(%s, %s, %s)"""
    return connection.execute_dml_statement(query, [name, email, password])

#TODO: student language managing
def add_student_languages(student_id, languages):
    query = """INSERT INTO student_languages(student_id, language_id) VALUES(%s, %s)"""
    return connection.execute_dml_statement(query, [student_id, languages])


def update_student_languages(student_id, languages):
    query = """UPDATE student_languages 
                SET language_id=(%s) 
                WHERE student_id=(%s)"""
    return connection.execute_dml_statement(query, [languages, student_id])


def get_latest_id():
    return connection.execute_select('SELECT id FROM student ORDER BY id DESC LIMIT 1', fetchall=False)


def get_teacher(id):
    query = """ SELECT * FROM teacher
                WHERE id = %(id)s;
    """
    return connection.execute_select(query, id, fetchall=False)


def get_student(student_id):
    query = """ SELECT * FROM student
                WHERE id = %(student_id)s
    """
    return connection.execute_select(query, student_id)

def update_teacher(name, email, password, id):
    query =""" UPDATE teacher
            SET name = %(name)s, email = %(email)s, password = %(password)s
            WHERE id = %(id)s
    """
    return connection.execute_dml_statement(query, [name, email, password, id])

def update_student(name, email, password, id):
    query =""" UPDATE student
            SET name = %(name)s, email = %(email)s, password = %(password)s
            WHERE id = %(id)s
    """
    return connection.execute_dml_statement(query, [name, email, password, id])
