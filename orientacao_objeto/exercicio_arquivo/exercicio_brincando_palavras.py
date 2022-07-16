# Neste aqui a sua lógica está certa. Só posso te dar uma dica:
#     Vejo que você está armazenando todas as palavras em uma lista e depois 
#     você obtém a conta usando a função len. Isso funciona, mas pense o seguinte:
#     Como você só quer contar as palavras, você não precisa armazená-las em algum lugar,
#     já que isso consome memória (e dependendo da qtd de palavras pode até deixar seu código mais lento).
#     Você literalmente só precisa contá-las. Veja abaixo
def total_palavras():
    with open ('palavras.txt', 'r', encoding='utf-8') as arquivo:
        # palavras = []
        total_palavras = 0  # Trocamos a lista por uma variável de contagem
        for linha in arquivo:
            linha = linha.strip()  # Como só estamos contando, você não precisa se preocupar em usar o strip. Isso é só para quando queremos processar e usar a string de fato
            # palavras.append(linha)
            total_palavras = total_palavras + 1  # Para cada linha do arquivo adicionamos 1 na contgem
        # print('Total de palavras:', (len(palavras)))
        print('Total de palavras:', (total_palavras))


# Aqui você também usou a lógica certinho.
# Você estabeleceu quais seriam as letras que você queria contar (alfabeto)
# E depois criou uma lista com um contador para cada letra, todos começando em zero
# Aqui a dica é menor, mas no geral é isso mesmo!
def total_letras_alfabeto():
    with open ('palavras.txt', 'r', encoding='utf-8') as arquivo:
        contador = []
        alfabeto ="abcdefghijklmnopqrstuvwxyz"
        for elemento in range(26):
            contador.append(0)
        for linha in arquivo:
            for elem in linha.lower():
                # if 'a' <= elem <= 'z':  
                # A única dica é aqui. Ao invés de verificar se a letra está entre a e z dá pra fazer assim: 
                if elem in alfabeto:
                    # Isso garante que você possa contar outras letras também caso queira, como "á" e "õ", desde que você inclua elas na variável alfabeto
                    index = alfabeto.index(elem)#mostra onde esta a letra na string
                    contador[index] += 1
        for elemento in range(26):
            print(f'Quantidade da letra {alfabeto[elemento]} é: {contador[elemento]}')


# Perfeito! 
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
