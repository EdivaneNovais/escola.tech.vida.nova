from random import randint

class Adversario:

    def __init__ (self, nome, chances):
        self.nome = nome
        self.chances = chances
        self.vitoria_jogador = 0
        self.vitoria_computador = 0 

    def jogo_impar_par (self):

        jogador = input('você quer par ou ímpar?:').lower().strip()
        while jogador != 'par' and jogador != 'impar':
            erro = input('ERRO, DIGITE CORRETAMENTE SUA ESCOLHA, (PAR OU IMPAR): ').lower().strip()
            jogador = erro
            
        while  True:
            numero = (input('Digite um número inteiro:')).strip()
        
            if numero.isnumeric():  
                numero_correto = int(numero)
                break
                
            else:
                print('ERRO!!')

        computador = randint(0, 5)
        total_numeros =  computador + numero_correto 
        print(f'Total: {total_numeros}')
        print(f'Computador jogou: {computador}')

        if total_numeros % 2 == 0 and jogador == 'par':
            print(f'par, {self.nome} ganhou, computador perdeu')
            self.vitoria_jogador = self.vitoria_jogador + 1 
    
        elif total_numeros % 2 == 1 and jogador == 'impar':
            print(f'impar,{self.nome} ganhou, computador perdeu')
            self.vitoria_jogador = self.vitoria_jogador + 1 

        elif total_numeros % 2 == 0 and jogador == 'impar':
            print('par, computador ganhou, você perdeu')
            self.vitoria_computador = self.vitoria_computador + 1

        elif total_numeros % 2 == 1 and jogador == 'par':
            print('impar, computador ganhou, você perdeu')
            self.vitoria_computador = self.vitoria_computador + 1

                
    def campeonato (self):
        x = 0
        while x < self.chances:
            self.jogo_impar_par()
            x = x + 1
        if self.vitoria_jogador > self.vitoria_computador:
            print(f'{self.nome} ganhou de {self.vitoria_jogador} x {self.vitoria_computador}')
        elif self.vitoria_computador > self.vitoria_jogador:
            print(f'Computador ganhou de {self.vitoria_computador} x {self.vitoria_jogador}')
        else:
            print(f'Empate - Computador {self.vitoria_computador} x {self.nome} {self.vitoria_jogador}')
        


nome = input('Digite o seu nome: ')
chances = int(input('Digite quantas vezes deseja jogar com o computador:'))

jogador_obj = Adversario(nome, chances)
jogador_obj.campeonato()