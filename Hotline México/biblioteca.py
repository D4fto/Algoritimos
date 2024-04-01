def inserirlivro():
    cantidad = eval(input("Insira o número de livros: "))
    biblioteca = []
    for _ in range(cantidad):
        lista2 = []
        libro = input("Insira o titúlo: ")
        lista = [libro]
        libro = input("Insira o autor: ")
        lista.append(libro)
        libro = eval(input("Insira o ano: "))
        lista.append(libro)
        print("'parar' para terminar os generos")
        while True:
            genero = input("Insira o genero do livro: ")
            if genero == 'parar':
                break
            lista2.append(genero)
        lista.append(lista2)
        biblioteca.append(lista)
    return biblioteca
def procura_autor(biblioteca,autor):
    libros = []
    for libro in biblioteca:
        if libro[1] == autor:
            libros.append(libro)
    if libros == []:
        print("Não temos livros desse autor em nossa biblioteca!")
    else:
        print("O autor escreveu esses livros:\n")
        for a in libros:
            print(a)
def procura_genero(biblioteca,genero):
    libros = []
    for libro in biblioteca:
        if genero in libro[3]:
            libros.append(libro)
    if libros == []:
        print("Não temos livros desse genero em nossa biblioteca!")
    else:
        print("Os livros desse gênero são:\n")
        for a in libros:
            print(a)
print("para parar escreva 'parar'")
biblioteca = [
    ['Acredite se puder', 'Felipe Neto', 2019, ['curiosidades', 'informação', 'diversão', 'youtuber', 'youtube', 'crianças', 'jovens']],
    ['você sabia?', 'lucas molo', 2017, ['curiosidades', 'almanaque', 'você sabia?', 'guia', 'jovens','youtuber']],
    ['Dois mundos um herói', 'rezendeevil', 2015, ['minecraft', 'jogo', 'games', 'youtuber']],
    ['Não faz sentido', 'Felipe Neto', 2013, ['Documentário', 'literatura', 'nacional','youtuber','jovens','games','informação']]
]
while True:
    escolha = input("\n'livro' para adicionar um ou mais livros.\n'autor' para pesquisar livros por autor.\n'genero' para pesquisar livros por genero.\n'mostrar' para mostrar a biblioteca\n\nFaça sua escolha: ").lower()
    if escolha=='parar':
        break
    if escolha == 'mostrar':
        print(biblioteca)
    if escolha=='livro':
        minibiblioteca = inserirlivro()
        for a in minibiblioteca:
            biblioteca.append(a)
    if escolha=='autor':
        autor = input("Insira o autor: ")
        procura_autor(biblioteca,autor)
    if escolha=='genero':
        genero = input("Insira o genero: ")
        procura_genero(biblioteca,genero)