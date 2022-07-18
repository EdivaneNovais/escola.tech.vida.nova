def total_palavras():
    with open ('palavras.txt', 'r', encoding='utf-8') as arquivo:
        total_palavras = 0
        for linha in arquivo:
            total_palavras = total_palavras + 1
        print('Total de palavras:', (total_palavras))
    print()


def total_letras_alfabeto():
    with open ('palavras.txt', 'r', encoding='utf-8') as arquivo:
        contador = []
        alfabeto ="aãáàâbcdeéêfghiíjklmnoóôõpqrstuúvwxyz"
        for elemento in range(37):
            contador.append(0)
        for linha in arquivo:
            for elem in linha.lower():
                if elem in alfabeto:
                    index = alfabeto.index(elem)#mostra onde esta a letra na string
                    contador[index] += 1
        for elemento in range(37):
            print(f'Quantidade da letra {alfabeto[elemento]} é: {contador[elemento]}')
        print()
    

def palavras_iniciais_nome():
    arquivo = open ('palavras.txt', 'r', encoding='utf-8')
    arquivo_letra = open ('palavra_edi.txt', 'w', encoding='utf-8')
    texto = arquivo.read()
    lista_texto = texto.lower().split('\n')
    for palavra in lista_texto:
        if palavra[:3] == 'edi':
            arquivo_letra.write(palavra)
            arquivo_letra.write('\n')
    arquivo.close()

            
def palavras_palindromo():
    arquivo = open ('palavras.txt', 'r', encoding='utf-8')
    arquivo_letra = open ('palavra_palíndromo.txt', 'w', encoding='utf-8')
    texto = arquivo.read()
    lista_texto = texto.lower().split('\n')
    for palavra in lista_texto:
        palavra_invertida = palavra[::-1]
        if palavra_invertida == palavra:  
            arquivo_letra.write(palavra)
            arquivo_letra.write('\n')
    arquivo.close()
    arquivo_letra.close()

    
def total_letras_iniciais():
    arquivo = open ('palavras.txt', 'r', encoding='utf-8')
    texto = arquivo.read()
    lista_texto = texto.lower().split('\n')
    
    alfabetos = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0,
    'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}

    for palavra in lista_texto:
        primeira_letra = str(palavra[0])
        if primeira_letra == 'a':
            alfabetos[primeira_letra] += 1
        elif primeira_letra == 'b':
            alfabetos[primeira_letra] += 1
        elif primeira_letra == 'c':
            alfabetos[primeira_letra] += 1
        elif primeira_letra == 'd':
            alfabetos[primeira_letra] += 1
        elif primeira_letra == 'e':
            alfabetos[primeira_letra] += 1
        elif primeira_letra == 'f':
            alfabetos[primeira_letra] += 1
        elif primeira_letra == 'g':
            alfabetos[primeira_letra] += 1
        elif primeira_letra == 'h':
            alfabetos[primeira_letra] += 1 
        elif primeira_letra == 'i':
            alfabetos[primeira_letra] += 1
        elif primeira_letra == 'j':
            alfabetos[primeira_letra] += 1
        elif primeira_letra == 'k':
            alfabetos[primeira_letra] += 1
        elif primeira_letra == 'l':
            alfabetos[primeira_letra] += 1
        elif primeira_letra == 'm':
            alfabetos[primeira_letra] += 1
        elif primeira_letra == 'n':
            alfabetos[primeira_letra] += 1
        elif primeira_letra == 'o':
            alfabetos[primeira_letra] += 1
        elif primeira_letra == 'p':
            alfabetos[primeira_letra] += 1
        elif primeira_letra == 'q':
            alfabetos[primeira_letra] += 1
        elif primeira_letra == 'r':
            alfabetos[primeira_letra] += 1
        elif primeira_letra == 's':
            alfabetos[primeira_letra] += 1
        elif primeira_letra == 't':
            alfabetos[primeira_letra] += 1
        elif primeira_letra == 'u':
            alfabetos[primeira_letra] += 1
        elif primeira_letra == 'v':
            alfabetos[primeira_letra] += 1
        elif primeira_letra == 'w':
            alfabetos[primeira_letra] += 1
        elif primeira_letra == 'x':
            alfabetos[primeira_letra] += 1
        elif primeira_letra == 'y':
            alfabetos[primeira_letra] += 1
        elif primeira_letra == 'z':
            alfabetos[primeira_letra] += 1

    for elemento in alfabetos:
        print(f'Quantidade de palavras que inicia com a letra {elemento} é: {alfabetos[elemento]}')

total_palavras()
total_letras_alfabeto()
palavras_iniciais_nome()
palavras_palindromo()
total_letras_iniciais()
