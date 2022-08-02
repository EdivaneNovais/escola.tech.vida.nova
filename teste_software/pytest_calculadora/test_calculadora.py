# from Calculadora import Calculadora // primeiro coloco s classe que quero testar

# class TestCalculadora():
#     def setup_class(self):
#         self.calculadora = Calculadora(2, 3)

#     def test_soma(self):
#         assert self.calculadora.soma() == 5
#         assert self.calculadora.soma('5', '5') == 1

from Calculadora import Calculadora

class TestCalculadora:
    def setup_class(self):
        self.calculadora = Calculadora() 
        # chamo o nome da classe que quero testar 

    # metodo Tdd
    def test_soma(self):
       assert self.calculadora.soma(5 ,5) == 10
       assert self.calculadora.soma('10', '10') == 20
       assert self.calculadora.soma('A', 'B') == 'Parâmetros informados não são numéricos'