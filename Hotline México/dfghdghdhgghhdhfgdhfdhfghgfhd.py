import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Definir as configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Mudar Cor de uma Imagem')

# Definir cores
preto = (0, 0, 0)
branco = (255, 255, 255)

# Carregar a imagem
imagem_path = 'imagens/fundo.png'
imagem = pygame.image.load(imagem_path).convert()
imagem = pygame.transform.scale(imagem,(800,600))

# Definir a cor que você deseja substituir na imagem (nesse caso, branco)
cor_substituir = (255, 255, 255)

# Criar uma cópia da imagem
imagem_modificada = imagem.copy()
a=0
b=255
x=0
# Definir a cor que você deseja para a substituição


# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualizar lógica do jogo

    # Limpar a tela
    tela.fill(preto)
    if a<255 and x==0:
        a+=1
        b-=1
    elif b<255:
        a-=1
        b+=1
        x=1
    else:
        x=0
    print(a)
    cor_substituta = (int(b),255,int(a))  # Vermelho


    # Substituir a cor na imagem
    imagem_modificada = imagem.copy()
    imagem_modificada.set_colorkey(cor_substituir)
    imagem_modificada.fill(cor_substituta, special_flags=pygame.BLEND_RGBA_MULT)
    # Desenhar a imagem modificada
    tela.blit(imagem_modificada, (0, 0))
    

    # Atualizar a tela
    pygame.display.flip()
