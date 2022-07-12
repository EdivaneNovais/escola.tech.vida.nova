def total_palavras():
    with open ('palavras.txt', 'r', encoding='utf-8') as arquivo:
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
        print('Total de palavras:', (len(palavras)))


def total_letras_alfabeto():
    with open ('palavras.txt', 'r', encoding='utf-8') as arquivo:
        contador = []
        alfabeto ="abcdefghijklmnopqrstuvwxyz"
        for elemento in range(26):
            contador.append(0)
        for linha in arquivo:
            for elem in linha.lower():
                if 'a' <= elem <= 'z':
                    index = alfabeto.index(elem)#mostra onde esta a letra na string
                    contador[index] += 1
        for elemento in range(26):
            print(f'Quantidade da letra {alfabeto[elemento]} é: {contador[elemento]}')


def palavras_iniciais_nome():
    arquivo = open ('palavras.txt', 'r', encoding='utf-8')
    arquivo_letra = open ('palavra_edi.txt', 'w')
    texto = arquivo.read()
    lista_texto = texto.lower().split('\n')
    for palavra in lista_texto:
        if palavra[:3] == 'edi':
            arquivo_letra.write(palavra)
            arquivo_letra.write('\n')
    arquivo.close()

            
def palavras_palindromo():
    arquivo = open ('palavras.txt', 'r', encoding='utf-8')
    arquivo_letra = open ('palavra_palíndromo.txt', 'w')
    texto = arquivo.read()
    lista_texto = texto.lower().split('\n')
    for palavra in lista_texto:
        palavra_invertida = palavra[::-1]
        if palavra_invertida == palavra:  
            arquivo_letra.write(palavra)
            arquivo_letra.write('\n')
    arquivo.close()

def total_letras_iniciais():
    arquivo = open ('palavras.txt', 'r', encoding='utf-8')
    texto = arquivo.read()
    lista_texto = texto.lower().split('\n')

    a= 0
    b= 0
    c= 0
    d= 0

    for palavra in lista_texto:
        if 'a' in palavra[0]:
            a+=1
        elif 'b' in palavra[0]:
            b+=1
        elif 'c' in palavra[0]:
            c+=1
        elif 'd' in palavra[0]:
            d+=1

    print(f'total palavras iniciais com A: {a}')
    print(f'total palavras iniciais com B: {b}')
    print(f'total palavras iniciais com C: {c}')
    print(f'total palavras iniciais com D: {d}')

total_palavras()
total_letras_alfabeto()
palavras_iniciais_nome()
palavras_palindromo()
total_letras_iniciais()
