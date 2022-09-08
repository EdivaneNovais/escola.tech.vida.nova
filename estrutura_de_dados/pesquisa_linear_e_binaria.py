import random

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = self.capacidade*[0] # diferente de []


    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])


    def insere(self, valor):

        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return

        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        x = self.ultima_posicao
        #while x > posicao:
        while x >= posicao:    # <=== Erro era um maior que deveria ser um maior ou igual.
            self.valores[x + 1] = self.valores[x]
            x = x - 1
        
        self.valores[posicao] = valor
        self.ultima_posicao = self.ultima_posicao + 1


    def pesquisa_linear(self, valor):
        operacoes = 0
        for i in range(self.ultima_posicao + 1):
            operacoes += 1
            if self.valores[i] == valor:
                return i, operacoes
        return -1, operacoes


    def pesquisa_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao

        operacoes = 0
        while True:
            operacoes += 1
            posicao_atual = int((limite_inferior + limite_superior) / 2)
            # Se achou na primeira tentativa
            if self.valores[posicao_atual] == valor:
                return posicao_atual, operacoes
            # Se não achou
            elif limite_inferior > limite_superior:
                return -1, operacoes
            # Divide os limites
            else:
                # Limite inferior
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1
                # Limite superior
                else:
                    limite_superior = posicao_atual - 1


    def excluir(self, valor):
        posicao, operacoes = self.pesquisa_linear(valor)
        if posicao == -1:
            return operacoes
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao = self.ultima_posicao - 1
        return operacoes



# =====================================
# ADICIONEM TESTES A PARTIR DAQUI
# =====================================
# Chamando a Classe
amostragem = [1, 10, 100, 1000, 10000]

print("n \t lin \t bin")
for num_elementos in amostragem:
    #num_elementos = 1000
    vetor = VetorOrdenado(num_elementos)
    valores = random.sample(range(0, 2*num_elementos), num_elementos)
    #print(valores)

    for valor in valores:
        vetor.insere(valor)
    #vetor.imprime()

    interacoes = 5
    operacoes_binaria_media = 0
    operacoes_linear_media = 0
    for i in range(interacoes):
        endereco, operacoes_linear = vetor.pesquisa_linear(random.randrange(0,2*num_elementos))
        operacoes_linear_media += operacoes_linear
        
        endereco, operacoes_binaria = vetor.pesquisa_binaria(random.randrange(0,2*num_elementos))
        operacoes_binaria_media += operacoes_binaria

    operacoes_linear_media = int(operacoes_linear_media/interacoes)
    operacoes_binaria_media = int(operacoes_binaria_media/interacoes)

    print("{} \t {} \t {}".format(num_elementos, operacoes_linear_media, operacoes_binaria_media))
