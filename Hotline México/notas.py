notas = [
    [7.3,9.5,8.3,7.8],
    [4.5,6.7,8.9,9.9],
    [9.9,9.5,9.4,9.8],
    [6.8,3.1,5.6,8.9],
    [9.4,8.7,5.6,7.9]
]
al = 1
for linhas in notas:
    x=10
    for nota in linhas:
        if x>nota:
            x = nota
    print(f"A menor nota do aluno{al} é {x}")
    al+=1
print("\n")
for nota in range(len(notas[0])):
    x=10
    y=''
    for al in range(len(notas)):
        if notas[al][nota]<x:
            x=notas[al][nota]
            y=f"aluno{al+1}"
        elif notas[al][nota]==x:
            y+=f", aluno{al+1}"
    print(f"A menor nota da prova{nota+1} foi {x} do {y}.")