palavra_inicial = input('informe a palavra da forca: ').upper().strip()

max_erros= 7
erros = 0
letras_usadas = []
acertei_tudo = False

is_valid = palavra_inicial.isalpha()
if not is_valid:
    print('ERRO! Essa palavra não contém apenas letras')
    exit()

while erros < max_erros and not acertei_tudo:

    for letra in palavra_inicial:
        if letra in letras_usadas:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print()

    palpite = input('digite uma letra:').upper()

    palpite_valido = palpite.isalpha() and len(palpite) == 1

    while not palpite_valido:
        palpite = input('Seu palpite foi invalido, informe outro: ').upper()
        palpite_valido = palpite.isalpha() and len(palpite) == 1

    if palpite in letras_usadas:
        print('Esta palpite ja foi usado, tente novamente')

        pontos = 0 
        for letras in palavra_inicial:
            if letras in letras_usadas:
                pontos = pontos + 1
        if pontos == len(palavra_inicial):
            acertei_tudo = True

    else:
        letras_usadas.append(palpite)

        if palpite in palavra_inicial:
            print('Essa letra esta na palavra!')

            for letra in palavra_inicial:
                if letra not in letras_usadas:
                    acertei_tudo = False
                else:
                    acertei_tudo = True

        else:
            print('Você errou')
            erros = erros + 1
        print('Erros permitidos:', max_erros - erros)

    if(erros == 1):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if acertei_tudo:
    print(f'Parabén, você se livrou da forca! A palavra é {palavra_inicial}')
else:
    print(f'você foi ENFORCADO! A palavra era: {palavra_inicial}')