from marvel_viloes import Marvel_viloes

class Test_marvel_viloes:
    def setup_class(self):
        self.marvel_viloes_1 = Marvel_viloes("Coringa", ["luta"], 5)
        self.marvel_viloes_2 = Marvel_viloes('Avatar', ['fogo'], 4 )
        self.marvel_viloes_3 = Marvel_viloes('Super Homem', ['força'], 2)
   
    def test_primeiro_vilao(self):
        self.marvel_viloes_1.set_nome('coringa') 
        assert self.marvel_viloes_1.get_nome() == 'coringa'
        assert self.marvel_viloes_1.set_nome({}) == 'Somente entrada de letras'

    def test_segundo_vilao(self):
        self.marvel_viloes_2.set_nome('avatar')
        assert self.marvel_viloes_2.get_nome() == 'avatar'
        assert self.marvel_viloes_2.set_nome([]) == 'Somente entrada de letras'
    
    def test_terceiro_vilao(self):
        self.marvel_viloes_3.set_nome('super homem')
        assert self.marvel_viloes_3.get_nome() == 'super homem'
        assert self.marvel_viloes_3.set_nome(1234) == 'Somente entrada de letras'

    def test_poderes(self):
        self.marvel_viloes_1.set_poderes(['LUTA'])
        assert self.marvel_viloes_1.get_poderes() == (['LUTA'])
        assert self.marvel_viloes_1.set_poderes('luta') == 'Somente entrada de lista'

        self.marvel_viloes_2.set_poderes(['FOGO'])
        assert self.marvel_viloes_2.get_poderes() == (['FOGO'])
        assert self.marvel_viloes_2.set_poderes(123) == 'Somente entrada de lista'

        self.marvel_viloes_3.set_poderes(['FORÇA'])
        assert self.marvel_viloes_3.get_poderes() == (['FORÇA'])
        assert self.marvel_viloes_3.set_poderes({}) == 'Somente entrada de lista'

    def test_perigo(self):
        self.marvel_viloes_1.set_perigo(4)
        assert self.marvel_viloes_1.get_perigo() == (4)
        assert self.marvel_viloes_1.set_perigo(6) == 'Somente numero de 0 a 5'

        self.marvel_viloes_2.set_perigo(5)
        assert self.marvel_viloes_2.get_perigo() == (5)
        assert self.marvel_viloes_2.set_perigo(-1) == 'Somente numero de 0 a 5'

        self.marvel_viloes_3.set_perigo(1)
        assert self.marvel_viloes_3.get_perigo() == (1)
        assert self.marvel_viloes_3.set_perigo(7) == 'Somente numero de 0 a 5'
    
    def test_dominar_mundo(self):
        assert self.marvel_viloes_1.dominar_mundo() == 'vilão preso'
        assert self.marvel_viloes_2.dominar_mundo() == 'vilão dominou o mundo'
        assert self.marvel_viloes_3.dominar_mundo() == 'vilão morto'