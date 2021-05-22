import connection


def get_teachers():
    return connection.execute_select('SELECT email, password FROM teacher;')


def get_students():
    return connection.execute_select('SELECT email, password FROM student;')
