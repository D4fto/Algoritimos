import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Configurações da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Imagem em Preto e Branco')

# Carregar a imagem
imagem = pygame.image.load('chavinho3.png').convert_alpha()
imagem = pygame.transform.scale(imagem,(imagem.get_size()[0]*4,imagem.get_size()[1]*4))

# Criar uma superfície preta para sobrepor na imagem
cor_substituta = (250, 0, 0)  # Preto no ,ormato RGBA

imagem = pygame.transform.grayscale(imagem)

# Loop principal
while True:
    tela.fill((255,255,0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Desenhar a imagem preto e branco na tela
    tela.blit(imagem, (100, 100))


    # Atualizar a tela
    pygame.display.flip()