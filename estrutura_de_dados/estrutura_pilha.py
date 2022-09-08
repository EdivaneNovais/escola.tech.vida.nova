class Pilha:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.valores = self.capacidade * [0]

    def imprime(self):
        if self.topo == -1:
            print('A pilha esta vazio')
        else:
            for i in range(self.topo, -1, -1):
                print(i, ' - ', self.valores[i])

    def empilhar(self, valor):
        if self.topo == self.capacidade - 1:
            print('Pilha esta cheia')
        else:
            self.topo += 1
            self.valores[self.topo] = valor


    def desempilhar(self):
        if self.topo == -1:
            print('Pilha esta vazia')
        else:
            valor_tmp = self.valores[self.topo]
            self.topo -= 1
            return valor_tmp



vetor = Pilha(8)
vetor.empilhar(4)
vetor.empilhar(7)
vetor.empilhar(1)
vetor.empilhar(2)
vetor.empilhar(5)
vetor.empilhar(4)
vetor.empilhar(12)
vetor.imprime()

print(f'Tirei o valor: {vetor.desempilhar()}')
print(f'Tirei o valor: {vetor.desempilhar()}')
vetor.imprime
