import re
import json

def leitura():
    f = open("processos.txt")
    dados = []
    seenlines = []
    for line in f:
        if line not in seenlines:
            seenlines.append(line)
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
    return freq

def top5freq(freq):
    top5 = [(" ", 0), (" ", 0), (" ", 0), (" ", 0), (" ", 0)]
    for x in freq:
        value = int(freq.get(x))
        if value > top5[0][1]:
            i = 4
            while i > 0:
                top5[i] = top5[i-1]
                i -= 1
            top5[0] = (x, value)
            continue
        if value > top5[1][1]:
            i = 4
            while i > 1:
                top5[i] = top5[i-1]
                i -= 1
            top5[1] = (x, value)
            continue
        if value > top5[2][1]:
            i = 4
            while i > 2:
                top5[i] = top5[i-1]
                i -= 1
            top5[2] = (x, value)
            continue
        if value > top5[3][1]:
            i = 4
            while i > 3:
                top5[i] = top5[i-1]
                i -= 1
            top5[3] = (x, value)
            continue
        if value > top5[4][1]:
            top5[4] = (x, value)
            continue
    return top5      

def freqNome(dados):
    freqNprop = {}
    freqApelido = {}
    for pessoa in dados:
        nome = pessoa.get("nome")
        split = re.split(r' ', nome)
        nprop = split[0]
        apelido = split[-1]     
        if nprop in freqNprop:
            freqNprop[nprop] += 1
        else:
            freqNprop[nprop] = 1
        if apelido in freqApelido:
            freqApelido[apelido] += 1
        else:
            freqApelido[apelido] = 1
    top5Nprop = top5freq(freqNprop)
    top5Apelido = top5freq(freqApelido)
    print(top5Nprop)
    print(top5Apelido)                    
    
def freqRelacao(dados):
    freq = {}
    for pessoa in dados:
        obs = pessoa.get("Observações")
        if obs:
            lrelacoes = re.findall(r",((Tio|Irmao|Sobrinho|Tia|Avo)s*)[.| ]", obs)
            if lrelacoes:
                for relacao in lrelacoes:
                    if relacao[0] in freq:
                        freq[relacao[0]] += 1
                    else:
                        freq[relacao[0]] = 1
    return freq

def toJson(dados):
    f = open("processos.json", 'w')
    i = 0
    while i < 20:
        pessoa = dados[i]
        f.write(json.dumps(pessoa))
        if i < 19:
            f.write(",")
        i += 1
    f.close()    


dados = leitura()
freqAno(dados)
freqNome(dados)
print(freqRelacao(dados))
toJson(dados)        