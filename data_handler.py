import connection
from psycopg2._psycopg import AsIs

def get_amigos():
    return connection.execute_select('SELECT id, email, password FROM amigo;')


def get_students():
    return connection.execute_select('SELECT id, email, password FROM student;')


def register_student(name, email, password, birthday, languages, student_id):
    add_student_languages(student_id, languages)
    query = """INSERT INTO student(name, email, password, birthday, points, language_id) 
               VALUES(%s, %s, %s, %s, 0, %s)"""
    return connection.execute_dml_statement(query, {"name": name, "email": email, password:"password", "birthday": birthday, "languages": languages})


def register_amigo(name, email, password):
    query = """INSERT INTO amigo(name, email, password) 
                VALUES(%s, %s, %s)"""
    return connection.execute_dml_statement(query, {"name": name, "email": email, password:"password"})

#TODO: student language managing
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
    query =""" UPDATE amigo
            SET name = %(name)s, email = %(email)s
            WHERE id = %(id)s
    """
    return connection.execute_dml_statement(query, {"name": name, "email": email, "birthday": birthday, "id": id})

def update_student(name, email, birthday, id):
    query =""" UPDATE student
            SET name = %(name)s, email = %(email)s, birthday = %(birthday)s
            WHERE id = %(id)s
    """
    return connection.execute_dml_statement(query, {"name": name, "email": email, "birthday": birthday, "id": id})
