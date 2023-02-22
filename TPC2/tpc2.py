onOff = 1
soma = 0

while True:
    data = input("Escrever mensagem:\n")
    if 'Sair' == data:
        break
    if onOff == 1:
        lista = [int(s) for s in data.split() if s.isdigit()]
        for n in lista:
            soma += n

print(f'Soma = {soma}')
print("Saída com sucesso")
