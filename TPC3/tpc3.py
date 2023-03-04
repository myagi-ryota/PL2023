import re

def leitura():
    f = open("processos.txt")
    dados = []
    for line in f:
        pessoa = {}
        split = re.split(r'::+', line)
        split = split[:-1]
        for x in split:
            dano = len(re.findall(r'Doc.Danificado', line))
        if dano==0:
            if len(split) > 0:
                pessoa['pasta'] = split[0]    
            if len(split) > 1:    
                pessoa['data'] = split[1]
            if len(split) > 2:    
                pessoa['nome'] = split[2]
            if len(split) > 3:    
                pessoa['Pai'] = split[3]
            if len(split) > 4:
                pessoa['Mãe'] = split[4]
            if len(split) > 5:
                pessoa['Observações'] = split[5]    
            if pessoa:
                dados.append(pessoa)    
    #print(dados)        
    return dados

def freqAno(dados):
    freq = {}
    for pessoa in dados:
        data = pessoa.get("data")
        ano = re.split(r'-', data)[0]
        if ano in freq:
            freq[ano] += 1
        else:
            freq[ano] = 1
    print(freq)            
             

        
dados = leitura()
freqAno(dados)        