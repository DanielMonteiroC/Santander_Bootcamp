numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []
quadrado = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print("Sem compreensão de listas:", pares)


pares_compreensao = [numero for numero in numeros if numero % 2 == 0]
print("Com compreensão de listas:", pares_compreensao)



for numero in numeros:
    quadrado.append(numero ** 2)
print("Sem compreensão de listas:", quadrado)


quadrado_compreensao = [numero ** 2 for numero in numeros]
print("Com compreensão de listas:", quadrado_compreensao)