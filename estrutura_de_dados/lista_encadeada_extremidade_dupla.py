class Noh:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostra_noh(self):
        print(self.valor)

    def mostra_proximo(self):
        print(self.proximo)


class ListaEncadeada:

    def __init__(self, aceita_duplicatas = True):
        self.head = None
        self.tail = None
        self.aceita_duplicatas = aceita_duplicatas

    def insere_inicio(self, valor):

        # Busca pelo elemento
        if not self.aceita_duplicatas:
            atual = self.head
            while atual != None:
                if atual.valor == valor:
                    print("Item ja adicionado")
                    return
                else:
                    atual = atual.proximo

        # Insere o elemento
        novo = Noh(valor)
        novo.proximo = self.head
        self.head = novo

        # Aponta o primeiro elemento
        if self.tail == None:
            self.tail = novo

    def insere_final(self, valor):
        novo = Noh(valor)
        if self.head == None:
            self.insere_inicio(valor)
        else:
            self.tail.proximo = novo
            self.tail = novo


    def exclui_inicio(self):
        if self.head != None:
            if self.head.proximo == None:
                self.tail = None
            temp = self.head.valor
            self.head = (self.head).proximo # (self.head) == primeiro_noh
        else:
            temp = None
            print("Lista vazia")
        return temp

    def excluir_posicao(self, valor):
        atual = self.head
        anterior = None
        while atual != None:
            if atual.valor == valor:
                # Se sim, exclui
                anterior.proximo = atual.proximo
                atual = atual.proximo
                if not self.aceita_duplicatas:
                    return
            else:
                # Se não, vai pro proximo
                anterior = atual
                atual = atual.proximo


    def mostrar(self):
        atual = self.head
        while atual != None:
            atual.mostra_noh()
            atual = atual.proximo

lista = ListaEncadeada()

lista.insere_inicio(1)
lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_final(7)
lista.insere_final(9)
lista.mostrar()
print()
lista.exclui_inicio()
lista.mostrar()
print()
lista.excluir_posicao(8)
lista.mostrar()

