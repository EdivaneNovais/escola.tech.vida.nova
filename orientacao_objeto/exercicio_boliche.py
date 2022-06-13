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

jogada = [random.randint(1,10)]
x=0
while x < (len(pista)): 
    jogada = [random.randint(1, 10)]
    for pino in jogada:
        posicao = numero_dos_pinos[str(pino)]
        pista[posicao] = "_"
        for posicao in pista:
            if posicao == "I" or posicao == "\n":
                continue
    if pista == "_":
        break
    x = x + 1
  
    mostra_pista(pista) 