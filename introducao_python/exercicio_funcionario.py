def dados ():
    nome1 = str(input("digite seu primeiro nome:")).upper()
    sobrenome1 = str(input("digite seu sobrenome:")).upper()
    cargo1 = str(input("digite o cargo:")).upper()

    vetordados = [nome1, sobrenome1, cargo1]

    return vetordados


def informacoesFuncionario (infonome, infosobrenome, infocargo):
    print(f'\nNOME COMPLETO: {infonome} {infosobrenome}')
    print(f'CARGO: {infocargo}')
    

def salario ():
    try:
        pagamento = float(input("\ndigite o seu salario atual:"))
        print(f"\nSeu salario atual é de: {pagamento}")
        return pagamento
    except:
        print("******ERRO! DIGITE UM VALOR CORRETO******")
        

def salarioLiquido (impostoRenda):

    if (impostoRenda <= 1903.98):
        print("Insento de descontos seu salário líquido é: R$", impostoRenda)
    elif (impostoRenda >= 1903.99 and impostoRenda <= 2826.65):
        salario_liquido = impostoRenda - (impostoRenda * 7.5 / 100)
        print("Seu salário líquido será: R$", salario_liquido)
    elif (impostoRenda >= 2826.66 and impostoRenda <= 3751.05): 
        salario_liquido = impostoRenda - (impostoRenda * 15 / 100)
        print("Seu salário líquido será: R$", salario_liquido)  
    elif (impostoRenda >= 3751.06 and impostoRenda <=4664.68):
        salario_liquido = impostoRenda - (impostoRenda * 22.5 / 100)
        print("Seu salário líquido será: R$", salario_liquido)
    else:
        salario_liquido = impostoRenda - (impostoRenda * 27.5 / 100)  
        print("Seu salário líquido será: R$", salario_liquido)
        

dadosfuncionario = []
valor = 0
escolha = 0
while escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4:
    try:
        escolha = int(input("""Digite qual função você deseja:\n
                1 - Para inserir dados do funcionário
                2 - Para informações do funcionário
                3 - Para inserir um salário do funcionário
                4 - Para informar o salário liquido do funcionário \n Opção:"""))
    except(ValueError, TypeError):
        print("******ERRO! ESCOLHA OPÇÃO CORRETA******")
    continue

while escolha != 0:
    if escolha == 1:
        dadosfuncionario = dados()
    
    if escolha == 2:
        if dadosfuncionario == []:
            dadosfuncionario = dados()
            informacoes = informacoesFuncionario (dadosfuncionario[0], dadosfuncionario[1], dadosfuncionario [2])
        else: 
            informacoes = informacoesFuncionario (dadosfuncionario[0], dadosfuncionario[1], dadosfuncionario [2])

    if escolha == 3:
        valor = salario()
        
    if escolha == 4:
        if dadosfuncionario == []:
            dadosfuncionario = dados()
            salariofuncionario = salario()
            salarioLiquido(salariofuncionario)
            informacoes = informacoesFuncionario (dadosfuncionario[0], dadosfuncionario[1], dadosfuncionario [2])

        else:
            valor = salario ()
            salarioLiquido(valor)

    try:
        escolha = int(input("""\nDigite qual função você deseja:\n
        0 - para sair 
        1 - Para inserir dados do funcionário
        2 - Para informações do funcionário
        3 - Para inserir um salário do funcionário
        4 - Para informar o salário liquido do funcionário \n Opção:"""))
    except(ValueError, TypeError):
        print("******ERRO! ESCOLHA OPÇÃO CORRETA******")
 
print("\nObrigado")
