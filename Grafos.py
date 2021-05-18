def ex(array):
    soma = 0
    impares = 0
    for i in range (len(array)):
        for j in range (len(array)):
            soma += array[i][j]
        if (soma%2 != 0):
            impares += 1
        soma = 0
    return impares

array = ([[0, 2, 1, 0, 0],
          [2, 0, 1, 0, 0],
          [1, 1, 0, 1, 1],
          [0, 0, 1, 0, 2],
          [0, 0, 1, 2, 0]])
for i in range(len(array)):
    for j in range(len(array[i])):
        array[i][j] = int(input(f'Insira a matriz: [{i+1}][{j+1}]: '))

imp = ex(array)

if (imp == 2 or imp == 0):
    print("GRAFO POSSUI CAMINHO EULERIANO!")
else:
    print("GRAFO NAO POSSUI CAMINHO EULERIANO!")