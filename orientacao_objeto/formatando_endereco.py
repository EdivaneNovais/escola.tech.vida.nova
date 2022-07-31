informacoes = ['nome', 'logradouro', 'numero', 'complemento', 'bairro', 'cep', 'cidade', 'estado']
dados_usuario = {}

for dado in informacoes:
    pergunta = 'Por favor insira seu ' + dado + ':'
    dados_usuario[dado] = input(pergunta)
    
cep = dados_usuario['cep']
carta = """
{}
{}, {} {}
{}
{}-{} {}/{}
"""
print(carta.format(
    dados_usuario['nome'].upper(),
    dados_usuario['logradouro'],
    dados_usuario['numero'],
    dados_usuario['complemento'],
    dados_usuario['bairro'],
    cep[:5], cep[5:8],
    dados_usuario['cidade'],
    dados_usuario['estado'].upper()
))