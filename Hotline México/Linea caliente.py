import pygame
import math
from pygame.locals import *


pygame.init()
#region tela
offset = pygame.math.Vector2()
cor_fundo = [0,255,255]
bora = cor_fundo
tamx, tamy=pygame.display.get_desktop_sizes()[0]
tamy -= 50
tela = pygame.display.set_mode((tamx,tamy))
pygame.display.set_caption("Linea Caliente México")
icon = pygame.image.load("chaves-16.png")
pygame.display.set_icon(icon) 
#endregion

class personagem(pygame.sprite.Sprite):
    def __init__(self,spr,x,y,escala) :
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(spr)
        
        self.imagem = pygame.transform.scale(img,(int(img.get_width() * escala), int(img.get_height() * escala)))
        self.rect = self.imagem.get_rect()
        self.rect.center = (x,y)

#region mouse
mouse_pos = pygame.mouse.get_pos()
#endregion
velo_x = velo_y = velox = veloy = 0
speed = 8
acel = 1.02
freio = 1

x = tamx/2
y = tamy/2
ver = True
verd = True
azul = True

player = personagem("chavinho3.png",x,y,4)

fps = 60

clock = pygame.time.Clock()
#region rotacao
img_rot = player.imagem

angulo = 0
#endregion
aberto = True
while aberto:
    
    pygame.time.Clock().tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                aberto = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            bora = cor_fundo
            cor_fundo = [255,255,255]
        else:
            cor_fundo= bora
        if event.type == pygame.KEYDOWN:
            if event.key == K_a:
                velo_x = speed
            if event.key == K_d:
                velox = speed
            if event.key == K_w:
                velo_y = speed
            if event.key == K_s:
                veloy = speed
            if event.key == K_ESCAPE:
                if event.type == pygame.QUIT:
                    aberto = False


    mouse_pos = pygame.mouse.get_pos()
    xmou = mouse_pos[0] - player.rect.center[0]
    ymou = mouse_pos[1] - player.rect.center[1]
    angulo = math.degrees(math.atan2(xmou, ymou))
    img_rot = pygame.transform.rotozoom(player.imagem, angulo+180, 1)
    player.rect = img_rot.get_rect()
    player.rect.center = (x,y)
    tela.fill(cor_fundo)
    pygame.draw.rect(tela,(150,150,0),(400-offset.x,200-offset.y,800,500))
    pygame.draw.rect(tela,(50,50,50),(400-offset.x,200-offset.y,800,500),25)
    pygame.draw.rect(tela,(150,150,0),(400-offset.x,300-offset.y,25,200))
    pygame.draw.rect(tela,(150,100,50),(400-offset.x,300-offset.y,15,200))
    
    tela.blit(img_rot,player.rect)
    pygame.draw.circle(tela,(100,50,0),(1000-offset.x,350-offset.y),90)
    pygame.draw.circle(tela,(75,25,0),(1000-offset.x,350-offset.y),75)
    
    if cor_fundo[0]!=255 and cor_fundo[2]!=0:
        cor_fundo[0]+=1
        cor_fundo[2]-=1
    elif cor_fundo[0]!=0:
        cor_fundo[0]-=1
    if cor_fundo[2]<255:
        cor_fundo[2]+=1
    print(cor_fundo)
    if not(pygame.key.get_pressed()[K_d] and pygame.key.get_pressed()[K_a]):
        if pygame.key.get_pressed()[K_d]:
            velox*=acel
        elif velox>velo_x:
            velox-=freio
        else:
            velox = 0
        if pygame.key.get_pressed()[K_a]:
            velo_x*=acel
        elif velo_x>0:
            velo_x-=freio
        else:
            velo_x = 0
    else:
        if velox>velo_x:
            velox-=freio
        else:
            velox = 0
        if velo_x>0:
            velo_x-=freio
        else:
            velo_x = 0
        
    if not(pygame.key.get_pressed()[K_w] and pygame.key.get_pressed()[K_s]):
        if pygame.key.get_pressed()[K_w]:
            velo_y*=acel
        elif velo_y>0:
            velo_y-=freio
        else:
            velo_y = 0
        if pygame.key.get_pressed()[K_s]:
            veloy*=acel
        elif veloy>0:
            veloy-=freio
        else:
            veloy = 0
    else:
        if veloy>velo_y:
            veloy-=freio
        else:
            veloy = 0
        if velo_y>0:
            velo_x-=freio
        else:
            velo_x = 0
    
    
    
    print(offset)
    
    
    offset.x+=velox-velo_x 
    offset.y+=veloy-velo_y
    pygame.display.update()
pygame.quit()