from flask import Flask, render_template, request
from translate import translateSent
app = Flask(__name__)


@app.route("/output")
def output():
    a = translateSent('Ég er svangur')
    return render_template("index.html", name=a)


@app.route("/submit", methods=["GET", "POST"])
def index():
    message1 = ''
    if request.method == 'POST':
        message1 = request.form['Msg']
    if message1:
        print(message1)
        msg = translateSent(message1)
        print(msg)
    return render_template("index.html", original=message1, translation=msg)


@app.route("/")
def main():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
