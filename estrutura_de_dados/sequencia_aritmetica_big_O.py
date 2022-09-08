# Ex 01: Calcular o valor dos n primeiros números naturais!
# lista = 1, 2, 3, 4, ...

# Número de elementos a somar
n = 10

# Projeto do programador 1 - Ordem O(n²) - Quadrático
# Aqui realizamos a conta como se fosse "contando nos dedos"
def sum_1(n):
  operacoes = 0
  soma = 0
  for i in range (1, n + 1):
    for j in range(1, i + 1):
      soma = soma + 1
      operacoes +=1
  return soma, operacoes

# Projeto do Programador 2 - Ordem O(n) - Linear
# Aqui realizamos a soma de cada item em uma soma acumulada
def sum_2(n):
  soma = 0
  operacoes = 0
  for i in range(1, n +1):
    soma = soma + i
    operacoes += 1

# Projeto do Programador 3 - Ordem O(1) - Constante
# Aqui utilizamos a formula da Progressao Aritimetica (P.A.)
def sum_3(n):
  return n*(n + 1) // 2, 3

# Prints da quantidade de operações
print("soma_1: %d  |  operacoes: %d" % sum_1(n))
print("soma_2: %d  |  operacoes: %d" % sum_2(n))
print("soma_3: %d  |  operacoes: %d" % sum_3(n))
