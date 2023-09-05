numeros = set([1, 2, 3, 1, 3, 4])

numeros = list(numeros)
print(numeros[0])


letras = set('Python')

letras = list(letras)
print(letras[0:2])


linguagens = set(('Python', 'Java', 'C', 'C++', 'Python', 'Java'))
linguagens = list(linguagens)

print(linguagens[3])


linguagens_2 = {'Python', 'Java', 'C', 'C++', 'Python', 'Java'}

for linguagem in linguagens_2:
    print(linguagem)

for indice, linguagem in enumerate(linguagens_2):
    print(f"{indice}: {linguagem}")
