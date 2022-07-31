def criptografa(p):
    cripto_palavra = ''
    for letra in p:
        if letra == 'A':
            cripto_palavra = cripto_palavra + '4'
        elif letra == 'E':
            cripto_palavra = cripto_palavra + '3'
        elif letra == 'S':
            cripto_palavra = cripto_palavra + '5'

        else:
            cripto_palavra = cripto_palavra + letra

    return cripto_palavra

palavra = input('digite uma palavra:').upper()


letras_mapping = {
    'E': '3',
    'A': '4',
    'S': '5'
}

palavra_codificada = criptografa(palavra)
print(palavra_codificada)