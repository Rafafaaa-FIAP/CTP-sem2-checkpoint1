# Rafael Cristofali - RM553521

# 1 - Faça uma função que recebe uma matriz como parâmetro e printa linha a linha, forma convencional de uma matriz.(2 pontos)
def printarMatriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return True



# 2 - Faça uma função que recebe o número de linhas e colunas como parâmetros e cria uma matriz de dimensões linhas x colunas contendo somente zeros (2 pontos)
def gerarMatriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz



# 3 - Crie uma matriz 8x8 contendo o padrão de um tabuleiro de xadrez (2 pontos).
xadrez = gerarMatriz(8,8)
for i in range(len(xadrez)):
    for j in range(len(xadrez)):
        if ((i+j) % 2 == 0):
            xadrez[i][j] = 1
printarMatriz(xadrez)


# 4 - Faça uma função que recebe uma matriz quadrada e retorne sua transposta.
def transposta(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            aux = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = aux
    return matriz
