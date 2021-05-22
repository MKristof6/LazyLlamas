import bcrypt


def hash_it(psw):
    encrypted_pw = bcrypt.hashpw(psw.encode('utf-8'), bcrypt.gensalt())
    return encrypted_pw


def verify_pw(stored_pw, pw):
    return bcrypt.checkpw(pw.encode('utf-8'), stored_pw.encode('utf-8'))
