numeros = []
for c in range(0, 5):
    n = int(input(f"Digite o {c+1}º valor: "))
    numeros.append(n)
    if c == 0:
        menor = maior = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
print(f"A lista completa: {numeros} ")
print(f"O MENOR número da lista: {menor} ")
print(f"O MAIOR número da lista: {maior} ")


