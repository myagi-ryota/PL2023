import re

def moedatoSaldo(moeda):
    a = re.fullmatch(r'((?P<num>\d{1,2})(?P<ec>e|c))', moeda)
    if a.group('ec') == 'e':
        return float(a.group('num'))
    else:
        return 0.01 * float(a.group('num'))
    
def SaldotoString(saldo):
    e = int(saldo)
    saldo -= e
    saldo *= 100
    s = f'{e}e{int(saldo)}c'
    return s

exit = False
estado = 0 #Estado fica a 0 até que se use o 'LEVANTAR'
saldo = 0
valCoins = ['5c', '10c', '20c', '50c', '1e', '2e']
erlineMoedas = re.compile(r'MOEDA ')
erlineT = re.compile(r'T=[00]?\d{9}')
while not exit:
    line = input("")
    if line == "LEVANTAR" and estado == 0:
        estado = 1
        print("Introduza moedas.")
        continue
    if estado:
        if line == "POUSAR":
            estado = 0
            print(f"troco={SaldotoString(saldo)}; Volte sempre!")
            exit = True
        if line == "ABORTAR":
            estado = 0
            print(f"troco={SaldotoString(saldo)}; Volte sempre!")
            exit = True
        if erlineMoedas.match(line):
            erMoedas = re.compile(r' (\d{1,2}[e|c])[,|.]')
            moedas = erMoedas.findall(line)
            for moeda in moedas:
                if moeda in valCoins:
                    saldo += moedatoSaldo(moeda)
                else:
                    print(f'{moeda} - moeda inválida; ')
            print(f'saldo = {SaldotoString(saldo)}.')
        if erlineT.fullmatch(line):
            er1 = re.compile(r'T=[601|641]')
            er2 = re.compile(r'T=00')
            er3 = re.compile(r'T=2')
            er4 = re.compile(r'T=800')
            er5 = re.compile(r'T=808')
            if er1.match(line):
                print("Esse número não é permitido neste telefone. Queira discar novo número!")
            elif er2.match(line):
                if saldo >= 1.5:
                    saldo -= 1.5
                    print(f'saldo = {SaldotoString(saldo)}')
                else:
                    print(f"Saldo insuficiente para realizar a chamada! Introduza mais moedas ou disque novo número.")
            elif er3.match(line):
                if saldo >= 0.25:
                    saldo -= 0.25
                    print(f'saldo = {SaldotoString(saldo)}')
                else:
                    print(f"Saldo insuficiente para realizar a chamada! Introduza mais moedas ou disque novo número.")
            elif er4.match(line):
                print(f'saldo = {SaldotoString(saldo)}')
            elif er5.match(line):
                if saldo >= 0.1:
                    saldo -= 0.1
                    print(f'saldo = {SaldotoString(saldo)}')
                else:
                    print(f"Saldo insuficiente para realizar a chamada! Introduza mais moedas ou disque novo número.")
                            
                                
            
            
            
            
                
    