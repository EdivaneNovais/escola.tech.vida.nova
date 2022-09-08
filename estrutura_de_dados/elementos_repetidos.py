# Ex 02: Contar quais são os elementos repetidos em uma lista.
lista = [13, 6, 2, 7, 12, 5, 11, 1, 3, 10, 9, 15, 5, 2, 10, 10, 12]


# Projeto varrendo todos os ítens após o atual
def rep_1(lista):
  repetidos = []
  operacoes = 0
  for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
      operacoes += 1
      if lista[i] == lista[j]:
        repetidos.append(lista[i])
  return repetidos, operacoes

# Projeto varrendo a lista uma única vez e colocando as ocorrências
def rep_2(lista, limite):
  recor = limite*[0]
  repetidos = []
  operacoes = 0

  for i in lista:
    operacoes += 1
    recor[i - 1] += 1

  for i in range(len(recor)):
    operacoes += 1
    if recor[i] > 1:
      repetidos.append(i + 1)

  return repetidos, operacoes


lista_1, operacoes_1 = rep_1(lista)
print(lista_1, end=' | ')
print(f'operacoes {operacoes_1}')

lista_2, operacoes_2 = rep_2(lista, 15)
print(lista_2, end=' | ')
print(f'operacoes {operacoes_2}')
