salario_bruto = float(input("Por favor, digite seu salário: R$ "))

if (salario_bruto <= 1903.98):
    print("Insento de descontos seu salário líquido é: R$", salario_bruto)
elif (salario_bruto >= 1903.99 and salario_bruto <= 2826.65):
    salario_liquido = salario_bruto - (salario_bruto * 7.5 / 100)
    print("Você teve um desconto de 7.5%, e seu salário líquido será: R$", salario_liquido)
elif (salario_bruto >= 2826.66 and salario_bruto <= 3751.05): 
    salario_liquido = salario_bruto - (salario_bruto * 15 / 100)
    print("Você teve um desconto de 15%, e seu salário líquido será: R$", salario_liquido)  
elif (salario_bruto >= 3751.06 and salario_bruto <=4664.68):
    salario_liquido = salario_bruto - (salario_bruto * 22.5 / 100)
    print("Você teve um desconto de 22.5%, e seu salário líquido será: R$", salario_liquido)
else:
    salario_liquido = salario_bruto - (salario_bruto * 27.5 / 100)  
    print("Você teve um desconto de 27.5%, e seu salário líquido será: R$", salario_liquido)
