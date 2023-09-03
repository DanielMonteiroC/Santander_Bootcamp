MAIOR_IDADE =18
IDADE_ESPECIAL = 65

idade = int(input("Digite sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você pode portar CNH.")

if idade < MAIOR_IDADE:
    print("Você ainda não pode portar CNH.")


if idade >= MAIOR_IDADE:
    print("Você pode portar CNH.")
else:
    print("Você ainda não pode portar CNH.")



if idade >= MAIOR_IDADE and idade < IDADE_ESPECIAL:
    print("Você pode portar CNH.")
elif idade >= IDADE_ESPECIAL:
    print("Você pode portar CNH, porém, deve ter cuidados especiais.")
else:
    print("Você ainda não pode portar CNH.")
