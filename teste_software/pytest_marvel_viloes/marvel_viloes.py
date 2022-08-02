class Marvel_viloes:

    def __init__ (self, nome = str, poderes = list, perigo = int):
        self.nome = nome
        self.poderes = poderes
        self.perigo = perigo

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        if type(nome) != str:
            return ('Somente entrada de letras')
        self.nome = nome
    
    def get_poderes(self):
        return self.poderes

    def set_poderes(self, poderes):
        if type(poderes) != list:
            return 'Somente entrada de lista'
        self.poderes = poderes
    
    def get_perigo(self):
        return int(self.perigo)
    
    def set_perigo(self, perigo):
        if perigo >= 0 and perigo <=5:
            self.perigo = perigo           
        else:
            return 'Somente numero de 0 a 5'
    
    def dominar_mundo(self):
        if self.perigo <=2:
            return 'vilão morto'
        elif self.perigo > 2 and self.perigo < 5:
            return 'vilão preso' 
        elif self.perigo == 5:
            return 'vilão dominou o mundo'
        
