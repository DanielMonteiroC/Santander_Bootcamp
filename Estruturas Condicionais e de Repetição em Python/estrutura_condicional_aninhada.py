conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com sucesso!')
        print('Você está usando o cheque especial.')
    else:
        print('Saldo insuficiente.')
elif conta_universitaria:
    if saque <= saldo:
        print('Saque realizado com sucesso!')
    else:
        print('Saldo insuficiente.')
else:
    print('Não foi possível realizar a operação, entre em contato com nossos canais.')