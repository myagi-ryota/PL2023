import json
import re
import csv

def leitura():
    jsonArray = []
    
    with open("alunos.csv", encoding='utf-8') as csvf:
        first = True
        specialheadindex = 0
        specialheads = []
        shFunc = []
        for line in csvf:
            if first:
                cabecas = re.split(r'(?<!{\d),\s*(?!\d})', line)[:-1]
                for head in cabecas:
                    specialhead = re.fullmatch(r'(\w+){(\d+,*\d*)}((::)(?P<func>sum|media))*', head)
                    if specialhead:
                        name = specialhead.group(1)
                        specialheads.append(name)
                        if specialhead.group('func'):
                            shFunc.append(specialhead.group('func'))
                        else:
                            shFunc.append(None)
                        cabecas[cabecas.index(head)] = name
                first = False
                continue
            else:    
                dados = re.split(r',', line)
                dados[-1] = re.sub(r'\n', '', dados[-1])
                xindex = 0
                pessoa = {}
                for x in dados:
                    if x != '':
                        if cabecas[xindex] == '':
                            pessoa[specialheads[specialheadindex]].append(int(x))
                        elif cabecas[xindex] in specialheads:
                            sh = cabecas[xindex] #special head
                            specialheadindex = specialheads.index(sh)
                            pessoa[sh] = [int(x)]
                        else:
                            pessoa[cabecas[xindex]] = x               
                    xindex += 1
            funcindex = 0
            for func in shFunc:
                if func == 'sum':
                    label = specialheads[funcindex]
                    label += "_sum"
                    pessoa[label] = sum(pessoa[specialheads[funcindex]])
                    del pessoa[specialheads[funcindex]]
                elif func == 'media':
                    label = specialheads[funcindex]
                    label += "_media"
                    pessoa[label] = sum(pessoa[specialheads[funcindex]]) / len(pessoa[specialheads[funcindex]])
                    del pessoa[specialheads[funcindex]]     
                funcindex += 1    
                                 
            jsonArray.append(pessoa)
                
        return jsonArray      
                
        
print(leitura())        