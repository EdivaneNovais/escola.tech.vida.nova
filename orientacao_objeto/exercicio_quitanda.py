def calculo_troco (divida, valor_pago):
        troco = valor_pago - divida
        if divida == valor_pago :
            print("o dinheiro a pagar é igual ao dinheiro recebido")
        if valor_pago < divida:
            print("ERRO!!!\nO valor recebido é inferior ao valor a pagar")
        else:
            troco = valor_pago - divida
            print(f"o valor do troco é de R$ {(troco)}0")

            for cedula in [20, 5, 1]:
                quantidade = troco // cedula
                troco = troco % cedula
                if quantidade > 0:
                    print(f"{int(quantidade)} nota(s) de R$ {cedula},00")
                    
precos = {
    'morango': 7,
    'melancia' : 20,
    'laranja': 5
}

mensagem = """
temos seguintes frutas:
morango
melancia
laranja
"""

total = 0
resposta = 's'
n = False
while resposta != "n":
    print(mensagem)
    fruta = input('que fruta voĉe gostaria?(Escreva o nome da fruta):').lower()
    if fruta in precos:
        preco = precos[fruta]
        print(f'o preco unitario dessa fruta é: R${preco},00')
    else:
        print("fruta errada")

    qtd = int(input('quantas unidades você gostaria:?'))

    total = total + qtd * preco
    print(f'O valor total da compra é de: R$ {total},00')
    resposta = input("Deseja compra mais? digite (s)sim (n)não:").lower()
    
    if resposta == 'n':
        dinheirorecebido = float(input("dinheiro recebido:"))
    
        calculo = calculo_troco(total,dinheirorecebido)

print("\nObrigado, Volte sempre!")