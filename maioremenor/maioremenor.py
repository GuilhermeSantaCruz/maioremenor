numeros = []
for c in range(1, 6):
    n = int(input(f"Digite o {c}º valor: "))
    numeros.append(n)
    if c == 1:
        menor = maior = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
print("**" * 20)            
print(f"A lista completa: {numeros} ")
print(f"O MENOR número da lista: {menor} ")
print(f"O MAIOR número da lista: {maior} ")
print("**" * 20)


