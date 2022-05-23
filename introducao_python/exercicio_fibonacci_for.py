anterior = 0
proximo = 1
c = 3
n = int(input("Digite até que número você quer a sequência Fibonacci:"))
print (anterior)
print (proximo)
for c in range (c, n+1):
    aux = anterior + proximo
    print (aux)

    anterior = proximo 
    proximo = aux
    c += 1
print("FIM")