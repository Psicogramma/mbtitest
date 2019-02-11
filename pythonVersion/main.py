from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def test():
    return render_template('test.html')

@app.route('/results', methods=['GET', 'POST'])
def results():

    # Leggo le richieste POST
    var1 = request.form['d1']
    var2 = request.form['d2']
    var3 = request.form['d3']

    print(var1, var2, var3)
    return render_template('results.html')

app.run()