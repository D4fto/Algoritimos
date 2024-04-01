matriz = []
for linha in range(5):
    matriz.append([])
    for _ in range(5):
        matriz[linha].append(0)
matriz[2][2]=1
matriz[3][2]=1

'''
matriz[27][25]=1
matriz[28][26]=1
matriz[28][27]=1
matriz[27][27]=1
matriz[26][27]=1
'''



matriz[4][2]=1
matriz_copia = []
for elemento in range(len(matriz)):
    matriz_copia.append([])
    matriz_copia[elemento] = matriz[elemento][:]

matriz_copia[4][4]=1
matriz_copia[4][3]=1
matriz_copia[4][2]=1
matriz_copia[4][1]=1
for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        vivos = 0
        for a in range(-1,2):
            for i in range(-1,2):
                if coluna+i>4:
                    continue
                if linha+a>4:
                    continue
                if matriz[linha+a][coluna+i]:
                    vivos+=1
        if matriz[linha][coluna]:
            vivos-=1
            
        print(vivos)