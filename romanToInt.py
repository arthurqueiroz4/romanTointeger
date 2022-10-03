def transforma(x):
    if x == 'I':
        return 1
    elif x == 'V':
        return 5
    elif x == 'X':
        return 10
    elif x == 'L':
        return 50
    elif x == 'C':
        return 100
    elif x == 'D':
        return 500
    elif x == 'M':
        return 1000
        
entrada = input()
romanos = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
fatiamento = []
resultado = []
saida = 0

for x in range(0, len(entrada)):
    fatiamento.append(entrada[x])


i = 0
while i < len(entrada):
    if i == len(entrada) - 1:
        resultado.append(transforma(fatiamento[i]))
    elif i == len(entrada):
        break
    else:
        if romanos.index(fatiamento[i]) < romanos.index(fatiamento[i+1]):
            var1 = transforma(fatiamento[i])
            var2 = transforma(fatiamento[i+1])
            resultado.append(var2 - var1)
            i += 1
        else:
            resultado.append(transforma(fatiamento[i]))
    i += 1  
saida = 0

for i in resultado:
    saida += i

print(saida)


