
import pygame
import math
from pygame.locals import *
from sys import exit
import os
import time
import random



pygame.init()
dir_main = os.path.dirname(__file__)
dir_img = os.path.join(dir_main,'imagens')
dir_psng = os.path.join(dir_img,'personagens')
dir_player = os.path.join(dir_psng,'Player')
dir_misc = dir_psng = os.path.join(dir_img,'misc')
tamx, tamy=pygame.display.get_desktop_sizes()[0]
anda = False
speed=40
tela = pygame.display.set_mode((tamx,tamy))
lista_c = []
spr_c1 = pygame.sprite.Group()
spr_c2 = pygame.sprite.Group()
spr_c3 = pygame.sprite.Group()
lista_c.extend([spr_c1,spr_c2,spr_c3])
rodando = False
morte = False
menu = True
def fonte(fonte,tam):
    return pygame.font.Font(fonte,tam)
def iniciar():
    global spr, player1, fundo, tempo_o,timer
    spr = pygame.sprite.LayeredUpdates()
    player1 = Player(os.path.join(dir_player,"chaves.png"),[tamx/2,tamy/2],25,3,spr,3)
    adiciona(spr,fundo,0)
    tempo_o = time.time()
    timer = random.randrange(1,5)
def reinicia():
    global spr, player1, fundo, tempo_o,timer, lista_c
    for i in range(len(lista_c)):
        lista_c[i]=pygame.sprite.Group()
    spr = pygame.sprite.LayeredUpdates()
    tempo_o = 0
    timer = 0
def detec_colis(obj,layer,x):
    if pygame.sprite.spritecollide(obj,lista_c[layer],x):
        pygame.sprite.spritecollide(obj,lista_c[layer],x)[0].colidido=True
        obj.colidido = True
def adiciona(grupo,spr,layer):
    grupo.add(spr)
    grupo.change_layer(spr,layer)
def spawn():
    if random.randrange(2)==1:
        x=random.randrange(-tamx,0)
    else:
        x=random.randrange(tamx,tamx*2)
    if random.randrange(2)==1:
        y=random.randrange(-tamx,0)
    else:
        y=random.randrange(tamy,tamy*2)
    en = Enemy(os.path.join(dir_player,"chaves.png"),[x,y],25,3,spr,2,player1)
    
class Personagem(pygame.sprite.Sprite,object):
    def __init__(self,spr,loc,tam,escala,group,layer):
        pygame.sprite.Sprite.__init__(self)
        self.anda = False
        self.spr=spr
        self.loc=loc
        self.escala = escala
        self.sprite_sheet = pygame.image.load(spr).convert_alpha()
        self.tam = tam
        self.imgs = []
        for i in range(int(self.sprite_sheet.get_width()/tam)):
            img = self.sprite_sheet.subsurface((i*tam, 0),(tam,tam))
            img = pygame.transform.scale(img,(tam*escala,self.sprite_sheet.get_height()*escala))
            self.imgs.append(img)
        self.index_imgs = 0
        self.imagem_origem = self.image = self.imgs[self.index_imgs]
        self.angulo = 0
        self.rect = self.image.get_rect()
        self.rect.center = loc
        self.image_colide = pygame.surface.Surface(self.image.get_size())
        adiciona(group,self,layer)
    def update(self):
        if self.anda == True:
            if self.index_imgs > int(self.sprite_sheet.get_width()/self.tam)-1:
                self.index_imgs = 0 
            self.index_imgs +=0.5
            self.imagem_origem = self.image = self.imgs[int(self.index_imgs)]
        self.origem_pos = self.rect.center
        self.image = pygame.transform.rotate(self.imagem_origem,self.angulo+180)
        self.rect = self.image.get_rect()
        self.rect.center = self.origem_pos
        
class Player(Personagem):
    def __init__(self, spr, loc, tam, escala,group,layer):
        super().__init__(spr, loc, tam, escala,group,layer)
        self.veloy = self.velox = self.velo_y = self.velo_x = 0
        self.colide_ = Colide(self.image_colide,self)
        lista_c[2].add(self.colide_)
        self.arma=0
        
    def input(self, input):
        if input.type == KEYDOWN:
            if input.key == K_d:
                self.velox=speed
            if input.key == K_a:
                self.velo_x=-speed
            if input.key == K_s:
                self.veloy=speed
            if input.key == K_w:
                self.velo_y=-speed
        if input.type == KEYUP:
            if input.key == K_d:
                self.velox=0
            if input.key == K_a:
                self.velo_x=0
            if input.key == K_s:
                self.veloy=0
            if input.key == K_w:
                self.velo_y=0
        if input.type == MOUSEBUTTONDOWN and input.button == 1:
                if self.arma == 0:
                    for _ in range(50):
                        angulo = random.randrange(-25,25)
                        bala1 = bala(self)
                        bala1.angulo_rad -=math.radians(angulo)
                        bala1.roda(self.angulo-90-(angulo))
                        adiciona(spr,bala1,1)
    def andar(self):
        self.rect.move_ip(self.velox+self.velo_x,self.veloy+self.velo_y)
    def update(self):
        global rodando, morte
        
        if pygame.mouse.get_pressed()[1]:
            if self.arma == 0:
                for _ in range(10):
                    angulo = random.randrange(-5,5)
                    bala1 = bala(self)
                    bala1.angulo_rad -=math.radians(angulo)
                    bala1.roda(self.angulo-90-(angulo))
                    adiciona(spr,bala1,1)
        self.andar()
        if self.velox+self.velo_x !=0 or self.veloy+self.velo_y !=0:
            self.anda = True
        else: 
            self.anda = False
        super().update()
        mouse_pos = pygame.mouse.get_pos()
        xmou = mouse_pos[0] - self.rect.center[0]
        ymou = mouse_pos[1] - self.rect.center[1]
        angulo = math.degrees(math.atan2(xmou, ymou))
        self.angulo = angulo
        
        if len(pygame.sprite.spritecollide(self.colide_,lista_c[1],True))!=0:
                spr.draw(tela)
                spr.update()
                rodando=False
                morte = True
                self.kill()
                reinicia()
        
class Enemy(Personagem):
    def __init__(self, spr, loc, tam, escala,group,layer,player):
        super().__init__(spr, loc, tam, escala,group,layer)
        for i in range(len(self.imgs)):
            self.imgs[i] = pygame.transform.grayscale(self.imgs[i])
        self.player = player
        self.anda=True
        self.unidade=0
        self.colide_ = Colide(self.image_colide,self)
        lista_c[1].add(self.colide_)
        
        
    def update(self):
        
        super().update()
        if self.unidade==0 and rodando==False:
            self.kill()
            self.unidade=1
        xmou = self.rect.centerx - self.player.rect.centerx
        ymou = self.rect.centery - self.player.rect.centery
        self.angulo = math.degrees(math.atan2(xmou, ymou))+180
        self.angulo_rad = math.radians(self.angulo-180)
        self.rect.move_ip(math.sin(self.angulo_rad)*-10,math.cos(self.angulo_rad)*-10)
        
        detec_colis(self.colide_,0,False)
class Fundo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(dir_misc,"fundo3.png"))
        self.image = self.image_origem = pygame.transform.scale(self.image,pygame.display.get_desktop_sizes()[0])
        self.rect = self.image.get_rect()
        self.cor_1=0
        self.cor_2=255
        self.mudanca=-15
        self.x=0
        self.y=0
        cor_substituta = (int(self.cor_2),255,int(self.cor_1))
        self.image.set_colorkey((255,255,255))
        self.image = self.image_origem.copy()
        self.image.fill(cor_substituta, special_flags=pygame.BLEND_RGBA_MULT)
    def update(self):
        if self.y == 15:
            if self.cor_1==255 or self.cor_1 == 0:
                self.mudanca*=-1
            self.cor_1+=self.mudanca
            self.cor_2-=self.mudanca
            self.image = self.image_origem.copy()
            self.image.fill((int(self.cor_2),255,int(self.cor_1)), special_flags=pygame.BLEND_RGBA_MULT)
            self.y = 0
            global rodando
            if rodando:
                if spr.get_layer_of_sprite(fundo)!=spr.get_bottom_layer():
                    spr.move_to_back(fundo)
        self.y+=1
class Projetil(pygame.sprite.Sprite):
    def __init__(self,spr,escala):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(spr)
        self.imagem_origem = self.image = pygame.transform.scale(img,(int(img.get_width() * escala), int(img.get_height() * escala)))
        self.rect = self.image.get_rect()
        self.rect.center = (0,0)
        self.unidade=0
        self.velox = self.veloy = 0
        self.image_colide = pygame.surface.Surface(self.image.get_size())
        self.colide_ = Colide(self.image_colide,self)
        lista_c[0].add(self.colide_)
    def roda(self,angulo):
        loc = self.rect.center
        self.image = pygame.transform.rotate(self.imagem_origem,angulo)
        self.rect = self.image.get_rect()
        self.rect.center = loc
    def update(self):
        if self.unidade==0 and rodando==False:
            self.kill()
            self.unidade=1
        self.rect.move_ip(self.velox,self.veloy)
        
            
class bala(Projetil):
    def __init__(self,obj, spr='bala.png', escala=1):
        super().__init__(spr, escala)
        self.e = self.f =50
        self.tempo_o = time.time()
        self.angulo_rad = math.radians(obj.angulo)
        super().roda(obj.angulo-90)
        self.rect.center = (obj.rect.centerx,obj.rect.centery)
    def update(self):
        
        self.tempo = time.time() - self.tempo_o
        
        self.velox, self.veloy = math.sin(self.angulo_rad)*self.e,math.cos(self.angulo_rad)*self.f
        super().update()
        
        if self.rect.centerx < 0 or self.rect.centerx>tamx or self.rect.centery<0 or self.rect.centery>tamy:
            self.kill()
        
class Colide(pygame.sprite.Sprite):
    def __init__(self,imagem,obj):
        pygame.sprite.Sprite.__init__(self)
        self.obj = obj
        self.image = imagem
        self.unidade=0
        self.rect = self.image.get_rect()
        self.rect.center = self.obj.rect.center
        self.colidido = False
        
    def update(self):
        if self.unidade==0 and rodando==False:
            self.kill()
            self.unidade=1
        if self.colidido:
            self.obj.kill()
            self.kill()
        if len(pygame.sprite.Sprite.groups(self.obj)) == 0:
            self.kill()
        
        self.rect.center = self.obj.rect.center
        
class Texto(pygame.sprite.Sprite):
    def __init__(self,fonte,loc):
        pygame.sprite.Sprite.__init__(self)
        
clock = pygame.time.Clock()
a = 1

fundo = Fundo()

while True:
    fundo.update()
    tela.blit(fundo.image,(fundo.x,fundo.y))
    
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                exit()    
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()
            if not(rodando):
                if event.key == K_SPACE:
                    rodando=True
                    reinicia()
                    player1 = Player(os.path.join(dir_player,"chaves.png"),[tamx/2,tamy/2],25,3,spr,3)
                    adiciona(spr,fundo,0)
                    
        if rodando:
            player1.input(event)
    if rodando:
        spr.draw(tela)
        spr.update()
        if time.time() - tempo_o > timer:
            spawn()
            spawn()
            spawn()
            spawn()
            spawn()
            spawn()
            spawn()
            tempo_o = time.time()
            timer = random.randrange(2)
        for grupos in lista_c:
            grupos.update()
        
         
    
    pygame.display.flip()