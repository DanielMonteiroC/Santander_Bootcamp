saldo = 2000
saque = 500

status = "Saque realizado com sucesso." if saldo >= saque else "Saldo insuficiente."


print(f"{status}")