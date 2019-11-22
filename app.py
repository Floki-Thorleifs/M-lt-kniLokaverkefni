from flask import Flask, render_template, request
from translate import translateSent, translateEn
app = Flask(__name__)

# Þetta skjal er bara til þess að setja upp síðu

# Fall til að þýða íslensku yfir í ensku
@app.route("/submit", methods=["GET", "POST"])
def indexen():
    message1 = ''
    if request.method == 'POST':
        message1 = request.form['Msg']
    if message1:
        msg = translateSent(message1)
    return render_template("index.html", original=message1, translation=msg)

# Skilar síðunni til að þýða ensku yfir í íslensku
@app.route('/english')
def english():
    return render_template("enindex.html")

# Fall til að þýða ensku yfir í íslensku
@app.route("/ensubmit", methods=["GET", "POST"])
def index():
    message1 = ''
    if request.method == 'POST':
        message1 = request.form['Msg']
    if message1:
        msg = translateEn(message1)
    return render_template("enindex.html", original=message1, translation=msg)

# Skilar síðunni til að þýða íslensku yfir í ensku
@app.route("/")
def main():
    return render_template("index.html")


# Flask stuff
if __name__ == "__main__":
    app.run()
