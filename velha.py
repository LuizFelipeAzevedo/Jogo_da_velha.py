def criaTabuleiro():
    mat = []
    mat.append([''] * 3)
    mat.append([''] * 3)
    mat.append([''] * 3)
    return mat

def trocaJogador(jogador):
    #se jogador é X retorna O caso 
    #contrario retorna X
    if jogador == 'X':
        return 'O'
    else:
        return 'X'

def temEspaco(matriz):
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == '':
                return True

def haGanhador(m):
    #verificando as linhas
    for i in range(3):
        if m[i][0] == m[i][1] and m[i][1] == m[i][2] and m[i][0] != '':
            return True
    
    #verificando as colunas
    for j in range(3):
        if m[0][j] == m[1][j] and m[1][j] == m[2][j] and m[0][j] != '':
            return True

    #verificando as diagonais
    if m[0][0] == m[1][1] and m[1][1] == m[2][2] and m[0][0] != '':
        return True    
    if m[0][2] == m[1][1] and m[1][1] == m[2][0] and m[0][2] != '':
        return True

    return False


def joga(matriz, lin, col, jogador):
    if lin < 0 or lin > 2 or col < 0 or col > 2:
        return False

    if matriz[lin][col] == '':
        matriz[lin][col] = jogador
        return True
    else:
        return False


def imprime(matriz):
    for lin in matriz:
        print(lin)