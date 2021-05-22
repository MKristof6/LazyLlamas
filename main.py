from flask import Flask, render_template

app = Flask("amigo")


@app.route('/')
def speech():
    return render_template('speech.html')


if __name__ == "__main__":
    app.run(
        debug=True,
        port=8000)
