anterior = 0
proximo = 1
c = 3
n = (int(input("Digite até que número você quer a sequência:")))
print(f"({anterior}")
print(f"{proximo}")

while c <= n:
    aux = anterior + proximo
    print(f"{aux}")
    anterior = proximo
    proximo = aux
    c =  c + 1
print("FIM")
