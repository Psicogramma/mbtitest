funzioni = ('Si', 'Se', 'Ni', 'Ne', 'Ti', 'Te', 'Fi', 'Fe')

def aggiornaPunteggi(risposta, func):
    for f in funzioni:
        if f == func:
            print(f, func, risposta)

    