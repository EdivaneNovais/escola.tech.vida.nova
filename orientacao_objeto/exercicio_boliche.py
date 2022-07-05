from random import choices, randint


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
    "10": 6 }

x=0
while x < 10:
    sorteio = randint(1, 4) #defini a quantidade de numeros que serão sorteados
    jogada = choices([1,2,3,4,5,6,7,8,9,10], k = sorteio)
        
    for pino in jogada:
        pinos_derrubados = 0
        posicao = numero_dos_pinos[str(pino)]
        if pista[posicao] == "_":
            print("Você não derrubou")
        else:
            pista[posicao] = "_"  
            print('Você acertou o pino, parabéns') 
             
            x = x + 1

    mostra_pista(pista) 

print("Você derrubou todos os pinos")
  