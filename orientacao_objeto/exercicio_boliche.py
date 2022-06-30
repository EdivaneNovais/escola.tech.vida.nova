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
    # Gostei que você usou o random para sortear pinos. 
    # Mas você reparou que ele sorteia apenas um por vez? Se a ideia fosse sortear mais de um por vez, como você faria?
    jogada = [random.randint(1, 10)]
    for pino in jogada:
        posicao = numero_dos_pinos[str(pino)]
        if pista[posicao] == "_":
            print("Você não derrubou nada")
        else:
            pista[posicao] = "_"          
            # Veja que, se mudarmos esse "x = x + 1" para cá, ele só será somado caso o pino seja de fato derrubado. 
            # Assim você não precisa subtrair 1 no caso anterior (por isso removi aquela expressão)
            x = x + 1

    mostra_pista(pista) 