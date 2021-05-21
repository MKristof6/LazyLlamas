from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def speech():
    return render_template('speech.html')



if __name__ == "__main__":
    app.run(
        debug=True
    )
