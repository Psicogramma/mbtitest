from web import app
from flask import render_template

user = {'username': 'Matteo'}
types = ('INTP', 'INTJ', 'ISTP', 'ISTJ', 'INFP', 'INFJ', 'ISFP', 'ISFJ', 'ENTP', 'ENTJ', 'ESTP', 'ESTJ', 'ENFP', 'ENFJ', 'ESFP', 'ESFJ')
functions = ('Si', 'Se', 'Ni', 'Ne', 'Ti', 'Te', 'Fi', 'Fe')

# simulo i post
posts = [
        {
            'author': {'username': 'Matteo'},
            'body': 'Prova namber uan'
        },
        {
            'author': {'username': 'Johnny'},
            'body': 'Prova namber ciù'
        }
    ]

# Homepage del sito
@app.route('/')
def main():
	return render_template('homepage.html', title='Home', user=user, posts=posts) # Stampa sulla pagina il file homepage.html con i parametri forniti

# Pagina effettiva del test
@app.route('/test')
def test():
	return render_template('test.html', title='Test', user=user)
	

# Pagina dei risultati
@app.route('/results')
def results():
	return render_template('results.html', title='Risultati', user=user)

#################### Descrizione dei tipi ##########################

# Descrizione tipi: INTP
@app.route('/types/intp')
def intp():
	return "INTP"

# Descrizione tipi: INTJ
@app.route('/types/intj')
def intj():
	return "INTJ"

# Descrizione tipi: ISTP
@app.route('/types/istp')
def istp():
	return "ISTP"

# Descrizione tipi: ISTJ
@app.route('/types/istj')
def istj():
	return "ISTJ"

# Descrizione tipi: INFP
@app.route('/types/infp')
def infp():
	return "INFP"

# Descrizione tipi: INFJ
@app.route('/types/infj')
def infj():
	return "INFJ"

# Descrizione tipi: ISFP
@app.route('/types/isfp')
def isfp():
	return "ISFP"

# Descrizione tipi: ISFJ
@app.route('/types/isfj')
def isfj():
	return "ISFJ"

# Descrizione tipi: ENTP
@app.route('/types/entp')
def entp():
	return "ENTP"

# Descrizione tipi: ENTJ
@app.route('/types/entj')
def entj():
	return "ENTJ"

# Descrizione tipi: ESTP
@app.route('/types/estp')
def estp():
	return "ESTP"

# Descrizione tipi: ESTJ
@app.route('/types/estj')
def estj():
	return "ESTJ"

# Descrizione tipi: ENFP
@app.route('/types/enfp')
def enfp():
	return "ENFP"

# Descrizione tipi: ENFJ
@app.route('/types/enfj')
def enfj():
	return "ENFJ"

# Descrizione tipi: ESFP
@app.route('/types/esfp')
def esfp():
	return "ESFP"

# Descrizione tipi: ESFJ
@app.route('/types/esfj')
def esfj():
	return "ESFJ"

####################################################################






#################### Descrizione delle funzioni ####################

# Descrizione funzioni: Si
@app.route('/functions/si')
def si():
	return "Si"

# Descrizione funzioni: Se
@app.route('/functions/se')
def se():
	return "Se"

# Descrizione funzioni: Ni
@app.route('/functions/ni')
def ni():
	return "Ni"

# Descrizione funzioni: Ne
@app.route('/functions/ne')
def ne():
	return "Ne"

# Descrizione funzioni: Ti
@app.route('/functions/ti')
def ti():
	return "Ti"

# Descrizione funzioni: Te
@app.route('/functions/te')
def te():
	return "Te"

# Descrizione funzioni: Fi
@app.route('/functions/fi')
def fi():
	return "Fi"

# Descrizione funzioni: Fe
@app.route('/functions/fe')
def fe():
	return "Fe"

####################################################################