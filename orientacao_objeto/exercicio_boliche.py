import random

def mostra_pista(pinos):
    for e in pinos:
        print(e, end="")
    print()

pista = [
    "I", " ", "I", " ", "I", " ", "I", "\n", " ", "I", " ", "I", " ", "I", "\n", " "," ", "I", " ", "I", "\n", " ", " ", " ", "I", " "
]


numero_dos_pinos = {
    "1": 24,
    "2": 17,
    "3": 19,
    "4": 9,
    "5": 11,
    "6": 13,
    "7": 0,
    "8": 2,
    "9": 4,
    "10": 6
}

x=0
while x < 10: 
    jogada = [random.randint(1, 10)]
    for pino in jogada:
        posicao = numero_dos_pinos[str(pino)]
        if pista[posicao] == "_":
            x = x - 1
            print("Você não derrubou nada")
        else:
            pista[posicao] = "_"          
    x = x + 1

    mostra_pista(pista) 