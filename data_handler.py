import connection


def get_teachers():
    return connection.execute_select('SELECT email, password FROM teacher;')


def get_students():
    return connection.execute_select('SELECT email, password FROM student;')


def register_student(name, email, password, bday, languages):
    return connection.execute_select("""INSERT INTO student(name, email, password, birthday, points) VALUES(%s, %s, %s, %s, %s)""", [name, email, password, bday, languages])  # TODO: figure out language_id -s


def register_teacher(name, email, password):
    return connection.execute_select("""INSERT INTO teacher(name, email, password) VALUES(%s, %s, %s)""", [name, email, password])


