import connection


def get_teachers():
    return connection.execute_select('SELECT email, password FROM teacher;')


def get_students():
    return connection.execute_select('SELECT email, password FROM student;')


def register_student(name, email, password, bday):
    return connection.execute_select("""INSERT INTO student(name, email, password, birthday, points) VALUES(%s, %s, %s, %s, 0)""", [name, email, password, bday])  # TODO: figure out language_id -s


def register_teacher(name, email, password):
    return connection.execute_select("""INSERT INTO teacher(name, email, password) VALUES(%s, %s, %s)""", [name, email, password])


