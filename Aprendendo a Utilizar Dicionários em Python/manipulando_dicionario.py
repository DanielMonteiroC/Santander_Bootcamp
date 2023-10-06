contatos = {
    "danmon@gmail.com": {"nome": "Dan Mon", "telefone": "1010-1010"},
    "mondan@gmail.com": {"nome": "Mon Dan", "telefone": "0101-0101", "outrodic": {"d": 1}},
}

"""telefone = contatos["danmon@gmail.com"] #[telefone]
print(telefone)"""

"""outrodic = contatos["mondan@gmail.com"]["outrodic"]["d"]
print(outrodic)"""

"""for chave in contatos:
    print(chave, contatos[chave])"""

for chave, valor in contatos.items():
    print(chave, valor)