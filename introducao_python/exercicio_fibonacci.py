n = (int(input("Digite até que número você quer a sequência Fibonacci:")))
sair = 1
while sair != 0:
    anterior = 0
    proximo = 1
    c = 3
    if n == 1:
        print(f"{anterior}")
    elif n > 1:
        print(f"{anterior}")
        print(f"{proximo}")
    while c <= n: 
        aux = anterior + proximo
        print(f"{aux}")

        anterior = proximo
        proximo = aux 
        c = c + 1
    print("FIM\n")
    
    sair = (int(input("digite novamente a sequência que deseja de numeros Fibonacci, ou digite 0(zero) para encerrar:")))

    if sair == 0:
        break
    n = sair 
    
print("\nOBRIGADO")