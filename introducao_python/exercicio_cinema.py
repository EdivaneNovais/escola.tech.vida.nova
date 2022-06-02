nLugares = int(input("Digite o total de lugares disponíveis:"))
lugares = ["_ "] * nLugares
coluna =   {"a": 1,
            "b": 2,
            "c": 3,
            "d": 4,
            "e": 5,
            "f": 6,
            "g": 7,
            "h": 8,
            "i": 9,
            "j": 10}

print ("Bem vindo ao cinema Vida Nova, escolha seu lugar")

y = 0
while (y < len(lugares)):
    print("a b c d e f g h i j")
    numerofileira = 1
    for x in range (1, nLugares+1):
        print(lugares [x-1], end="")
        if x % 10 == 0 or x == nLugares:
            print(f"Fileira {numerofileira} \n")
            numerofileira +=1 
    
    reservaColuna = input("\nDigite a Letra da COLUNA, que deseja:").lower()
    reservaFila = int(input("Digite o numero da FILEIRA que deseja:"))
    lugar = (reservaFila-1) * 10 + coluna[reservaColuna]

    if lugares [lugar-1] == "x ":
        print("\n\n**ASSENTO OCUPADO, escolha outro lugar**")
        y = y -1
   
    y = y  + 1
    lugares[lugar-1] = "x "
    
print("\n\nSALA DO CINEMA CHEIA, A SESSÃO VAI COMEÇAR\n")