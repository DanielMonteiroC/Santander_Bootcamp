contatos = {
    "danmon@gmail.com": {"nome": "Dan Mon", "telefone": "1010-1010"},
    "mondan@gmail.com": {"nome": "Mon Dan", "telefone": "0101-0101", "outrodic": {"d": 1}},
}

copia = contatos.copy()

print(copia)

print(copia.clear())

print(copia.fromkeys(["nome", "telefone"], "Algo pode ser colocado aqui"))


print(contatos.get("danmon@gmail.com", "Não encontrado"))

print(contatos.get("casa",".get quando não existe o valor"))

print(contatos.items())

print(contatos.keys())

print(contatos.pop("abcd@gmail.com", ".pop quando não existe o valor"))

print(contatos.popitem())

contatos.setdefault("idade", 35)
print(contatos)

contatos.update({"mondan@gmail.com": {"nome": "Mon Dan", "telefone": "0101-0101", "outrodic": {"d": 1}}})
print(contatos)

print(contatos.values())

resultado = "danmon@gmail.com" in contatos
print(resultado)

resultado2 = "nome" in contatos ["mondan@gmail.com"]
print(resultado2)

del contatos["mondan@gmail.com"]["outrodic"]
print(contatos)

del contatos
print(contatos)