escolha = int(input("""Digite qual função você deseja:\n
    1 - Para inserir dados do funcionário
    2 - Para informações do funcionário
    3 - Para inserir um salário do funcionário
    4 - Para informar o salário liquido do funcionário \n Opção:"""))

while escolha != 0:
    if escolha == 1 or escolha == 4:
    
        def dados ():
            nome1 = str(input("digite seu primeiro nome:")).upper()
            sobrenome1 = str(input("digite seu sobrenome:")).upper()
            cargo1 = str(input("digite o cargo:")).upper()
            vetordados = [nome1, sobrenome1, cargo1]

            return vetordados
            
        dadosfuncionario = dados()
    
    if escolha == 2 or escolha == 4:

        def informacoesFuncionario (infonome, infosobrenome, infocargo):
            print(f'\nNome Completo: {infonome} {infosobrenome}')
            print(f'cargo: {infocargo}')
            return

        informacoes = informacoesFuncionario (dadosfuncionario[0], dadosfuncionario[1], dadosfuncionario [2])

    if escolha == 3 or escolha == 4:

        def salario (valorsalario):
            print(f"\nSeu salario atual é de: {valorsalario}")
            

        pagamento = int(input("\ndigite o seu salario atual:"))
        valor = salario(pagamento)
    
    if escolha == 4 :
    

        def salarioLiquido (impostoRenda):

            if (impostoRenda <= 1903.98):
                print("Insento de descontos seu salário líquido é: R$", salario_bruto)
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

            return 
    
        salario_bruto = pagamento
        salario1 = salarioLiquido (salario_bruto)


    escolha = int(input("""\nDigite qual função você deseja:\n
    0 - para sair 
    1 - Para inserir dados do funcionário
    2 - Para informações do funcionário
    3 - Para inserir um salário do funcionário
    4 - Para informar o salário liquido do funcionário \n Opção:"""))

print("\nObrigado")