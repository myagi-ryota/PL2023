onOff = 1
soma = 0

while True:
    data = input("Escrever mensagem:\n")
    if 'Sair' == data:
        break
    
    words = data.split()
    lista = []
    for s in words:
        s = s.upper()
        if s == 'ON':
            onOff = 1
        if s == 'OFF':
            onOff = 0
        if s.isdigit() and onOff == 1:
            lista.append(int(s))
    for n in lista:
        soma += n

print(f'Soma = {soma}')
print("Saída com sucesso")
