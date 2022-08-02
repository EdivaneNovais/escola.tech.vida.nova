# class Calculadora:

#     def __init__(self, numero1, numero2):
#         self.numero1 = numero1
#         self.numero2 = numero2

#     def soma(self, numero1, numero2):
#         self.numero1 = numero1
#         self.numero2 = numero2
#         return self.numero1 + self.numero2

class Calculadora:
    def soma(self, num1, num2):
        try:
            return int(num1 )+ int(num2)
        except ValueError:
            return('Parâmetros informados não são numéricos')
