import pygame
import sys


# Inicializar o Pygame
pygame.init()

# Definir as configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Usando LayeredUpdates')

# Definir cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
azul = (0, 0, 255)

# Definir a classe da sprite
class MinhaSprite(pygame.sprite.Sprite):
    def __init__(self, cor, largura, altura, x, y, camada):
        super().__init__()
        self.image = pygame.Surface((largura, altura))
        self.image.fill(cor)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.camada = camada

# Criar um sprite group com camadas
grupo_sprites = pygame.sprite.LayeredUpdates()

# Criar sprites em diferentes camadas
sprite1 = MinhaSprite(branco, 50, 50, 100, 100, 1)
sprite2 = MinhaSprite(vermelho, 50, 50, 125, 125, 2)
sprite3 = MinhaSprite(azul, 50, 50, 150, 150, 3)

# Adicionar sprites ao grupo
grupo_sprites.add(sprite3)
grupo_sprites.add(sprite1)
grupo_sprites.add(sprite2)


grupo_sprites.change_layer(sprite1,-90)
grupo_sprites.change_layer(sprite1,1)
print(grupo_sprites.get_layer_of_sprite(sprite1))

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualizar lógica do jogo

    # Limpar a tela
    tela.fill(preto)

    # Desenhar as sprites (a ordem é gerenciada automaticamente)
    grupo_sprites.draw(tela)

    # Atualizar a tela
    pygame.display.flip()