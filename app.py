from flask import Flask, render_template, request
from translate import translateSent, translateEn
app = Flask(__name__)


@app.route("/submit", methods=["GET", "POST"])
def indexen():
    message1 = ''
    if request.method == 'POST':
        message1 = request.form['Msg']
    if message1:
        msg = translateSent(message1)
    return render_template("index.html", original=message1, translation=msg)


@app.route('/english')
def english():
    return render_template("enindex.html")


@app.route("/ensubmit", methods=["GET", "POST"])
def index():
    message1 = ''
    if request.method == 'POST':
        message1 = request.form['Msg']
    if message1:
        msg = translateEn(message1)
    return render_template("enindex.html", original=message1, translation=msg)


@app.route("/")
def main():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
