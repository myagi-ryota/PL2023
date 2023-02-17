import re

def leitura(amostra):    
    f = open("c:/Users/Tiago/Desktop/PL2023/TPC1/myheart.csv")
    for linha in f:
        pessoa = []
        pessoa = re.split(',|\n', linha)
        pessoa = pessoa[:-1]
        amostra.append(pessoa)
    amostra.pop(0)    

def dsexo(amostra):
    counter = [0,0,0,0] # n homens com doença | n homens | n mulheres com doença | n mulheres
    for pessoa in amostra:
        if pessoa[1] == 'M':
            counter[1] = counter[1] + 1
            if pessoa[5] == '1':
                counter[0] = counter[0] + 1
        if pessoa[1] == 'F':
            counter[3] = counter[3] + 1
            if pessoa[5] == '1':
                counter[2] = counter[2] + 1       
    
    return {'M': [counter[0],counter[1]], 'F': [counter[2],counter[3]]}   # Doentes/população
            
def didade(amostra):
    counter = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for pessoa in amostra:
        idade = int(pessoa[0])
        doente = int(pessoa[5])
        if idade < 35:
            counter[1] += 1
            if doente:
                counter[0] += 1
            continue    
        if idade < 40:
            counter[3] += 1
            if doente:
                counter[2] += 1
            continue    
        if idade < 45:
            counter[5] += 1
            if doente:
                counter[4] += 1
            continue    
        if idade < 50:
            counter[7] += 1
            if doente:
                counter[6] += 1
            continue    
        if idade < 55:
            counter[9] += 1
            if doente:
                counter[8] += 1
            continue    
        if idade < 60:
            counter[11] += 1
            if doente:
                counter[10] += 1
            continue    
        if idade < 65:
            counter[13] += 1
            if doente:
                counter[12] += 1
            continue    
        if idade < 70:
            counter[15] += 1
            if doente:
                counter[14] += 1 
        
    counter = [counter[x:x+2] for x in range(0, len(counter), 2)]
    distribuicao = {"[30-34]": counter[0], "[35-39]": counter[1], "[40-44]": counter[2], "[45-49]": counter[3], "[50-54]": counter[4],"[55-59]": counter[5],"[60-64]": counter[6],"[65-69]": counter[7]}                               
    return distribuicao    
            
def linferior(amostra):
    min = 100000
    for pessoa in amostra:
        colestrol = int(pessoa[3])
        if colestrol != 0:
            if colestrol < min:
                min = colestrol
    return min                        
                
            
a = []            
leitura(a)
print(linferior(a))
#print(didade(a))