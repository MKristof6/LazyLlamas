from flask import Flask, render_template, url_for, redirect, session, request

import data_handler
import util

app = Flask("amigo")
app.secret_key = b'_5#z2L"F7Q8q\n\xec]/'


@app.route('/')
def speech():
    return render_template('speech.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    users = [data_handler.get_teachers(), data_handler.get_students()]
    if request.method == 'POST':
        session['email'] = request.form['email']
        for userz in users:
            for user in userz:
                if session['email'] == user['email']:
                    session['pw'] = request.form['password']
                    if util.verify_pw(user['password'], session['pw']):
                        return redirect(url_for('speech'))
                else:
                    return 'Wrong password!<br><br><a href="/login">Go back</a>'
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('speech'))


if __name__ == "__main__":
    app.run(
        debug=True,
        port=8000)
