from pack import aggiornaPunteggi
import os
import sys

_domande = [] # Lista provvisoria per memorizzare le domande
domande = {'Si': [], 'Se': [], 'Ni': [], 'Ne': [], 'Ti': [], 'Te': [], 'Fi': [], 'Fe': []} # Dizionario per le domande (ad ogni funzione associo una lista di domande)
punteggi = {'Si': 1, 'Se': 2, 'Ni': 3, 'Ne': 4, 'Ti': 5, 'Te': 6, 'Fi': 7, 'Fe': 8} 
funzioni = ('Si', 'Se', 'Ni', 'Ne', 'Ti', 'Te', 'Fi', 'Fe')

n_domande = 4

# Per simulazione
domanda = {'func': 'Si', 'numero': 1}

try:
    file = open('domande.txt', 'r')
    _domande = file.read().splitlines()
    file.close() 
except FileNotFoundError as notFound:
    print(notFound)
except:
    print('Errore non previsto')

print('Conto le domande... ')

# Controllo di avere il numero giusto di domande
if len(_domande) == n_domande:
    print('Registrate ' + str(len(_domande)) + ' domande')
else:
    print('Errore lettura domande (lette ' + str(len(_domande)) + ' su ' + str(n_domande) + ')')
    sys.exit()

# Suddivido le domande per funzioni
for d in _domande:
    w = d.split() # divide in parole la frase
    # print(w[0]) stampa la parola numero 0
    domande[w[0]].append(d[3:]) # w[0] nel file di testo è la funzione. Aggiungo, alla lista di posto w[0] nel dizionario, la domanda d (escludo i caratteri 1,2,3 perchè sono 'funzione ')
del _domande # Cancello la lista provvisoria di domande

input('Pronto! Premi invio per iniziare \n')

i = 1
for f in funzioni:
    for d in domande[f]:
        print('\n\n\n')
        risposta = input(str(i) + " di " + str(n_domande) + ": \n" + d + '\n')
        aggiornaPunteggi(risposta, domanda['func'])   # Aggiorna punteggi funzioni
        i+=1

print(punteggi)