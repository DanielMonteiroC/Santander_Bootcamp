nome = "Daniel"
idade = 35
profissao = "Programador"
linguagem = "Python"
saldo = 45.235

dados = {"nome": "Daniel", "idade": 35, "profissao": "Programador", "linguagem": "Python"}

print("Old School")
print("Nome: %s, Idade: %d, Profissão: %s, Linguagem: %s" % (nome, idade, profissao, linguagem))

print(".format()")
print("Nome: {}, Idade: {}, Profissão: {}, Linguagem: {}".format(nome, idade, profissao, linguagem))
print("Nome: {0}, Idade: {1}, Profissão: {2}, Linguagem: {3}".format(nome, idade, profissao, linguagem))
print("Nome: {nome}, Idade: {idade}, Profissão: {profissao}, Linguagem: {linguagem}".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))  
print("Nome: {nome}, Idade: {idade}, Profissão: {profissao}, Linguagem: {linguagem}".format(**dados))

print("f-strings")
print(f"Nome: {nome}, Idade: {idade}, Profissão: {profissao}, Linguagem: {linguagem}, Saldo: {saldo:.2f}")
print(f"Nome: {nome}, Idade: {idade}, Profissão: {profissao}, Linguagem: {linguagem}, Saldo: {saldo: 10.2f}")

