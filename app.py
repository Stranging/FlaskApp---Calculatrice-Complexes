# TODO Commenter
from flask import Flask, render_template, request
from complexe import Complexe

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calcul', methods=['GET', 'POST'])
def calcul():
    if (request.form['r1'] == ""):
        r1 = 0
    else:
        r1 = float(request.form['r1'])
    if (request.form['i1'] == ""):
        i1 = 0
    else:
        i1 = float(request.form['i1'])
    if (request.form['r2'] == ""):
        r2 = 0
    else:
        r2 = float(request.form['r2'])
    if (request.form['i2'] == ""):
        i2 = 0
    else:
        i2 = float(request.form['i2'])

    complexe1 = Complexe(r1, i1)
    complexe2 = Complexe(r2, i2)

    operator = request.form['radio']

    errorMessage = ""
    if operator == '+':
        resultat = complexe1 + complexe2
    elif operator == '-':
        resultat = complexe1 - complexe2
    elif operator == '*':
        resultat = complexe1 * complexe2
    else:
        try:
            resultat = complexe1 / complexe2
        except ZeroDivisionError as zde:
            errorMessage = zde.args[0]
            resultat = Complexe(0, 0)

    return render_template('calcul.html', complexe1=complexe1, complexe2=complexe2, operator=operator,
                           resultat=resultat, errorMessage=errorMessage)


if __name__ == "__main__":
    app.run(debug=True)
