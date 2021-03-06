from flask import Flask, render_template, request
import os
import sys
from CalcoloPunteggi.punteggi import Test
from Domande.quest import Domande
import time

app = Flask(__name__) # Creo l'app
script_dir = os.path.dirname(__file__)
valori_accettati= ['1', '2', '3', '4', '5'] # Valori accettati come risposta
domande = []

test = Test() # Creo oggetto della classe Test
d = Domande(script_dir=script_dir)

for dom in d.domande:
    domande.append(dom['quest'])

@app.route('/')
def test_page():
    return render_template('test.html', domande=domande)

@app.route('/results', methods=['GET', 'POST'])
def results():
    forms = request.form    # Legge tutti i forms (dizionario)
    count = 0
    for f in forms:
        if count < len(d.domande):
            if f and (forms[f] in valori_accettati): # Se ha messo la risposta
                print(d.domande[count]['func'])
                test.calcolaPunteggi(func=d.domande[count]['func'], value=forms[f])
        count += 1
    to_print = []
    for punt in test.punteggi:
        print(punt + ' ' + str(test.punteggi[punt]))
        to_print.append(punt + ': ' + str(test.punteggi[punt]))
    return render_template('results.html', to_print=to_print)

app.run()