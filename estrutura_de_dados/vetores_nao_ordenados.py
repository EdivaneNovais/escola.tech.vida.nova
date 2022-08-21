class VetorNaoOrdenado:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    self.valores = self.capacidade*[0]

  def imprime(self):
    if self.ultima_posicao == -1:
      print('o vetor esta vazio')
    else:
      for i in range(self.ultima_posicao + 1):
        print(i, ' - ', self.valores[i])

  def insere(self, valor):
    if self.ultima_posicao == self.capacidade -1:
      print('Capacidade maxima atingida')
    else:
      self.ultima_posicao = self.ultima_posicao + 1
      self.valores[self.ultima_posicao] = valor

  def pesquisa(self, valor):
    for i in range(self.ultima_posicao + 1):
      if self.valores[i] == valor:
        return i
    return -1

  def excluir(self, valor):
    posicao = self.pesquisa(valor)
    operacoes = 0
    if posicao == -1:
      return -1
    else:
      for i in range(posicao, self.ultima_posicao):
        operacoes += 1
        self.valores[i] = self.valores[i + 1]
      self.ultima_posicao = self.ultima_posicao - 1
      return operacoes

  def Duplicatas(self, valor):
    duplicados = []
    operacoes = 0
    for i in range(self.ultima_posicao + 1):
      operacoes += 1
      posicao = self.valores.index(self.valores[i])
      if self.valores[posicao] == valor:
        duplicados.append(valor)
        print(f'O número ({valor}) já existe')
        break
    return duplicados, operacoes



vetor = VetorNaoOrdenado(8)

vetor.imprime()
print()
vetor.insere(4)
vetor.insere(2)
vetor.insere(1)
vetor.insere(7)
vetor.insere(3)
vetor.insere(4)
vetor.insere(5)
vetor.insere(6)
vetor.imprime()

print()
vetor.insere(20)

print()
print(vetor.pesquisa(9))
print(vetor.pesquisa(33))

print()
operacoes_1 = vetor.excluir(3)
print(f'operaçoes {operacoes_1}')
vetor.imprime()

print()
replicados, operacoes = vetor.Duplicatas(5)
print(f'operações {operacoes}')