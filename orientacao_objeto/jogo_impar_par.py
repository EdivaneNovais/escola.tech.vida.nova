from random import randint

def imprime_resultado (soma_numeros, jogador):

    if soma_numeros % 2 == 0 and jogador == 'par':
        print('par, você ganhou, computador perdeu')
        return 0
    
    elif soma_numeros % 2 == 1 and jogador == 'impar':
        print(f'impar, voĉe ganhou computador perdeu')
        return 0

    elif soma_numeros % 2 == 0 and jogador == 'impar':
        print('par, computador ganhou, você perdeu')
        return 1

    elif soma_numeros % 2 == 1 and jogador == 'par':
        print('impar, computador ganhou, você perdeu')
        return 1
    

print('JOGO ÍMPAR OU PAR')
print('*' * 18)

jogada = input('você quer par ou ímpar?:').lower().strip()
while jogada not in ('par', 'impar'):
    erro = input('ERRO, DIGITE CORRETAMENTE SUA ESCOLHA, (PAR OU IMPAR): ').lower().strip()
    jogada = erro
    
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

retorno = imprime_resultado (total_numeros,jogada )
print (f'Retorna (0) caso o jogador ganhe e retorna (1) caso o computador ganhe: {retorno}')


