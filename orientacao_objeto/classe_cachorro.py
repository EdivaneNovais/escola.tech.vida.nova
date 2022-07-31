class Cachorro:
    def __init__(self, nome, peso, cidade):
        self.nome = nome
        self.peso = peso
        self.cidade = cidade
        self.classifica_peso ()

    def latir(self):
        print('au, au')

    def classifica_peso(self):
        peso = self.peso
        if peso < 6:
            self.categoria_peso = 'pequeno'
        elif peso >= 6 and peso < 10:
            self.categoria_peso = 'medio'
        else:
            self.categoria_peso = 'grande'

    def emagrecer(self, kilos):
        self.peso = self.peso - kilos
        self.classifica_peso()

meu_cachorro = Cachorro('Bidu', 12, 'Londres')
print(meu_cachorro.nome, meu_cachorro.peso, meu_cachorro.cidade, meu_cachorro.categoria_peso)

meu_cachorro.emagrecer(4)
print(meu_cachorro.nome, meu_cachorro.peso, meu_cachorro.cidade, meu_cachorro.categoria_peso)
