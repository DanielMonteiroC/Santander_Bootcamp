linguagens = ["python", "js", "c", "java", "csharp"]


linguagens_2 = linguagens.copy()
print("Metodo copy: ", linguagens_2)

linguagens_2.clear()
print("Metodo clear: ", linguagens_2)

linguagens_2.append("python")
print("Metodo append: ", linguagens_2)

print("Metodo count: ", linguagens_2.count("python"))

linguagens_2.extend(["python", "js", "c", "java", "csharp", "python"])
print("Metodo extend: ", linguagens_2)

print("Metodo index: ", linguagens_2.index("python"))

linguagens_2.pop()
print("Metodo pop: ", linguagens_2)

linguagens_2.remove("python")
print("Metodo remove: ", linguagens_2)

linguagens_2.reverse()
print("Metodo reverse: ", linguagens_2)

linguagens_2.sort()
print("Metodo sort: ", linguagens_2)

linguagens_2.sort(reverse=True)
print("Metodo sort reverse: ", linguagens_2)

linguagens_2.sort(key=lambda x: len(x))
print("Metodo sort tamanho das strings: ", linguagens_2)

linguagens_2.sort(key=lambda x: len(x), reverse=True)
print("Metodo sort tamanho das strings reverse: ", linguagens_2)

print("Metodo len: ", len(linguagens_2))

print("Metodo sorted: ", sorted(linguagens_2))

print("Metodo sorted tamanho das strings: ", sorted(linguagens_2, key=lambda x: len(x)))

print("Metodo sorted tamanho das strings reverse: ", sorted(linguagens_2, key=lambda x: len(x), reverse=True))

print(f"""\n 
      ======================= Listas =======================\n
      Linguagens: {linguagens} 
      Linguagens ID: {id(linguagens)}\n
      Linguagens_2: {linguagens_2}
      Linguagens_2 ID: {id(linguagens_2)}\n
      ======================================================
""")
