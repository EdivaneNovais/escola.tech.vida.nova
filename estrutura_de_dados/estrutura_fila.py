class Fila:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.num_elementos = 0
        self.valores = self.capacidade * [0]

    def imprime(self):
        if self.final == -1:
            print('A fila esta vazio')
        else:
            if self.inicio >= self.final:
                for i in range(self.inicio, self.capacidade):
                    print(i, ' - ', self.valores[i])
                for i in range(0, self.final + 1):
                    print(i, ' - ', self.valores[i])
            else:
                for i in range(self.inicio, self.final + 1):
                    print(i, ' - ', self.valores[i])

    def enfileirar(self,valor):
        if (((self.final == self.inicio - 1) or                                     
                (self.final == self.capacidade - 1 and self.inicio == 0)) and  
                    (self.num_elementos == self.capacidade)):                       
            print("A Fila esta cheia")
            return
        else:
            if self.final == self.capacidade - 1:
                self.final = 0
            else:
                self.final += 1
            self.valores[self.final] = valor
            self.num_elementos += 1

    def desenfileirar(self):
        if (((self.final == self.inicio - 1) or                                     
                (self.final == self.capacidade - 1 and self.inicio == 0)) and       
                    (self.num_elementos == 0)):                                     
            print("A Fila esta vazia")
            return
        else:

            temp = self.valores[self.inicio]    # guardando o valor do elemento
            self.inicio += 1
            if self.inicio == self.capacidade:
                self.inicio = 0
            self.num_elementos = self.num_elementos - 1

            return temp




vetor = Fila(5)

for i in range(5):
    vetor.enfileirar(2*i)
vetor.imprime()
print()
vetor.desenfileirar()
vetor.imprime()

