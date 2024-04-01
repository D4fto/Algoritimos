import pygame 
import math
pygame.init()

tamx=pygame.display.get_desktop_sizes()[0][0]
tamy=pygame.display.get_desktop_sizes()[0][1]
tela = pygame.display.set_mode([tamx,tamy])
cor_fundo = [0,0,0]
velo_x=0
velo_y=0
velo__x=0
velo__y=0
velocidade = 2
aberto = True
x=tamx/2

y=tamy/2
escala = 2
mouse = pygame.mouse.get_pos()
clock = pygame.time.Clock()
player = pygame.image.load('imagens/personagens/player/chavinho2.png')
player = pygame.transform.scale(player,(int(player.get_width() * escala), int(player.get_height() * escala)))



while aberto:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            aberto = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                velo_x=velocidade
            if event.key == pygame.K_a:
                velo__x=-velocidade
            if event.key == pygame.K_s:
                velo_y=velocidade
                player = pygame.transform.rotate(player,180)
            if event.key == pygame.K_w:
                velo__y=-velocidade
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                velo_x=0
            if event.key == pygame.K_a:
                velo__x=-0
            if event.key == pygame.K_s:
                velo_y=0
            if event.key == pygame.K_w:
                velo__y=-0
    tela.fill(cor_fundo)
    player = pygame.transform.rotate(player,1)
    
    
    #player = pygame.draw.rect(tela,[0,255,200],[x,y,20,20])

    
    
    tela.blit(player,(x,y))
    
    pygame.display.flip()
    clock.tick(30)
pygame.quit()