def leia_matriz(): 
    matriz = []
    m = eval(input("Número de linhas: "))
    n = eval(input("Número de colunas: "))

    for i in range(m):
        matriz.append([])
        for a in range(n):
            elem = input(f'Digite o número ({i},{a}) da matriz: ')
            matriz[i].append(elem)
    return matriz
def main(matriz):
    p = 0
    lin = 0
    col = 0
    x = 0
    y = 0
    m = len(matriz)
    n = len(matriz[0])
    for linhas in range(m):
        for colunas in range(n):
            if matriz[linhas][colunas] == '0':
                x+=1
            if p == 0:
                for linhas2 in range(m):
                    if matriz[linhas2][colunas] == '0':
                        
                        y+=1
            
                if y == m:
                    col+=1
                y=0
        p=1
        if x == n:
            lin+=1
        x=0
    print(f"\nLinhas nulas = {lin}")
    print(f"Colunas = {col}")
    
matriz = leia_matriz()
print(f"\n{matriz}")
main(matriz)
