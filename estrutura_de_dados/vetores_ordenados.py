class VetorOdernado:

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
        print('Capacidade atingida')
        return

      posicao = 0
      for i in range(self.ultima_posicao + 1):
        if self.valores[i] > valor:
          posicao = i
          break
        if i == self.ultima_posicao:
          posicao = i + 1

      x = self.ultima_posicao
      while x >= posicao:
        self.valores[x + 1] = self.valores[x]
        x -= 1

      self.valores[posicao] = valor
      self.ultima_posicao = self.ultima_posicao + 1

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


vetor = VetorOdernado(8)

vetor.insere(2)
vetor.insere(5)
vetor.insere(3)
vetor.imprime()

replicados, operacoes = vetor.Duplicatas(3)
print(f'operações {operacoes}')