import pygame
from pygame.locals import *
from random import randrange
import time
import os

pygame.init()
tamox, tamoy = (1920,1080)
tamx, tamy=pygame.display.get_desktop_sizes()[0]
scy = tamy/tamoy
scx = tamx/tamox
scg = (scy+scx)/2
mus1 = ylin = pontos2 = pontos1 = yy = y = x = tempo = tem = m = 0
exe = debug = menu = False
tempo2 = time.time()
aberto = aberto2 = multiplayer2 = multiplayer = True
msgini = "Pressione espaco para iniciar"
som = pygame.mixer.Sound('arquivos/som.wav')
som2 = pygame.mixer.Sound('arquivos/ponto.wav')
musica = pygame.mixer.music.load("arquivos/musica/a.mp3")
pygame.mixer.music.play(-1)
cor_bola = [255,255,255]
speed_playersp = speed_players = speed_lim = round(35 * scg) #1
linlar=10*scg
linalt = tamy/27 
lim = 15*scg
acel2 = acel = 1.001#4
volume_som = volume_musica = 1
speed_bolay = speed_bolax = speed_bolap = speed_bola = round(10 * scg)
raio = 15*scg
largura = 25 * scg
altura = altura2 = round(150 * scg)
cor_fundo = [0,0,0]
menu = 0
loc_inic_cir = [tamx/2,tamy/2]
loc_temp_cir = loc_inic_cir[:]
tela = pygame.display.set_mode((tamx,tamy))
pygame.display.set_caption("Pong")
icon = pygame.image.load("arquivos/chaves-16.png")
pygame.display.set_icon(icon) 
fps = 100
clock = pygame.time.Clock()
y2 = y1 = tamy/2
rect2 = pygame.draw.rect(tela,(255,255,255),(0,0,largura,altura2))
rect1 = pygame.draw.rect(tela,(255,255,255),(0,0,largura,altura))
pygame.mixer_music.set_volume(volume_musica)
pygame.mixer.Sound.set_volume(som,volume_som)
pasta_musicas = os.listdir("arquivos/musica/")
mus = len(pasta_musicas)
def fonte(tam):
    return pygame.font.Font('arquivos/Minecrafter.Reg.ttf',tam)
def printa(fonte,x,espaco,espaco1,local,cor,tela,palavras):
    y=0
    espaco*=scg
    espaco1*=scg
    for a in palavras:
        msgm = fonte.render(a,False,cor,(0,0,0))
        if local == 'center':
            msgm_rect = msgm.get_rect(center = [x,espaco1+espaco*y])
        if local == 'topleft':
            msgm_rect = msgm.get_rect(topleft = [x,espaco1+espaco*y])
        if local == 'topright':
            msgm_rect = msgm.get_rect(topright = [x,espaco1+espaco*y])
        tela.blit(msgm,msgm_rect)
        y+=1
while aberto:
    clock.tick(fps)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
                aberto = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                if not(exe):
                    exe=True
                    k=randrange(2)
                    if k == 1:
                        speed_bolax*=-1
                    q=randrange(2)
                    if q == 1:
                        speed_bolay*=-1
            if event.key == K_m and not(exe):
                if multiplayer:
                    multiplayer=False
                else:
                    multiplayer=True
            if event.key == K_p:
                if multiplayer2 and not(exe):
                    multiplayer2=False
                else:
                    multiplayer2=True
            if event.key == K_ESCAPE:
                aberto = False
            if event.key == K_F1:
                if debug:
                    debug = False
                else:
                    debug = True
            if event.key == K_F2:
                mus1+=1
                musica = pygame.mixer.music.load(f"arquivos/musica/{pasta_musicas[mus1]}")
                if mus1 == mus-1:
                    mus1=-1
                pygame.mixer.music.play(-1)
            if event.key == K_r and not(exe):
                pontos1=0
                pontos2=0
            if event.key == K_c:
                if menu:
                    menu = False
                else:
                    menu = True
    if menu:
        clock.tick(10)
        tela.fill(cor_fundo)
        if pygame.key.get_pressed()[K_e] and volume_musica<1:
            volume_musica+=0.01
            pygame.mixer_music.set_volume(volume_musica)
        if pygame.key.get_pressed()[K_q] and volume_musica>0:
            volume_musica-=0.01
            pygame.mixer_music.set_volume(volume_musica)
        if pygame.key.get_pressed()[K_d] and volume_som<1:
            volume_som+=0.01
            pygame.mixer.Sound.set_volume(som,volume_som)
            pygame.mixer.Sound.set_volume(som2,volume_som)
        if pygame.key.get_pressed()[K_a] and volume_som>0:
            volume_som-=0.01
            pygame.mixer.Sound.set_volume(som,volume_som)
            pygame.mixer.Sound.set_volume(som2,volume_som)
        printa(fonte(int(50*scg)),tamx/2,50,50,'center',(150,255,150),tela,['p para player1 virar bot','m para player2 virar bot','r para resetar pontos','f2 para trocar a musica','f1 para debug','esc para sair',f'musica  q {int(volume_musica*100)} e',f'efeitos sonoros  a {int(volume_som*100)} d','','debug layout','','Limite velocida bola 1 2','aceleracao bola 3 4','velocida bola padrao 5 6','velocida player 7 8','tamanho player1 9 0','tamanho player2 menos igual','fps f g','','c para sair do menu'])
        tempo2 = time.time() - tempo
    else:
        clock.tick(fps)
        tela.fill(cor_fundo)
        while ylin<tamy:
            pygame.draw.rect(tela,(255,255,255),(tamx/2-linlar/2,ylin,linlar,linalt))
            ylin+=2*linalt
        ylin=0
        msg1 = str(pontos1)
        msg2 = str(pontos2)
        printa(fonte(int(100*scg)),tamx/2-25,0,lim+25,'topright',(255,255,255),tela,[msg1])
        printa(fonte(int(100*scg)),tamx/2+25,0,lim+25,'topleft',(255,255,255),tela,[msg2])
        lim3=pygame.draw.rect(tela,(255,255,255),(0,0,tamx,lim))
        lim4=pygame.draw.rect(tela,(255,255,255),(0,tamy-lim,tamx,lim))
        if exe:
            if multiplayer2:
                if pygame.key.get_pressed()[K_w] and not(rect1.colliderect(lim3)):
                    y1-=speed_players-round(10*scg)
                elif rect1.colliderect(lim3) and not(pygame.key.get_pressed()[K_s]):
                    y1=lim+altura/2-2
                if pygame.key.get_pressed()[K_s] and not(rect1.colliderect(lim4)):
                    y1+=speed_players-round(10*scg)
                elif rect1.colliderect(lim4) and not(pygame.key.get_pressed()[K_w]):
                    y1=tamy-lim-altura/2+1
                if tempo > tem and m == 0:
                    tem = tempo
            else:
                if y1 < bola.center[1] and not(rect1.colliderect(lim4)):
                    if multiplayer:
                        y1+=speed_players-round(2*scg)
                    else:
                        y1+=speed_players
                elif rect1.colliderect(lim4) and not(y1 > bola.center[1]):
                    y1=tamy-lim-altura/2+1
                if y1 > bola.center[1] and not(rect1.colliderect(lim3)):
                    if multiplayer:
                        y1-=speed_players-round(2*scg)
                    else:
                        y1-=speed_players
                elif rect1.colliderect(lim3) and not(y1 < bola.center[1]):
                    y1=lim+altura/2-1
                m=1
            if multiplayer:
                if pygame.key.get_pressed()[K_UP] and not(rect2.colliderect(lim3)):
                    y2-=speed_players-round(10*scg)
                elif rect2.colliderect(lim3) and not(pygame.key.get_pressed()[K_DOWN]):
                    y2=lim+altura2/2-1
                if pygame.key.get_pressed()[K_DOWN] and not(rect2.colliderect(lim4)):
                    y2+=speed_players-round(10*scg)
                elif rect2.colliderect(lim4) and not(pygame.key.get_pressed()[K_UP]):
                    y2=tamy-lim-altura2/2+1
            else:
                if y2 < bola.center[1] and not(rect2.colliderect(lim4)):
                    y2+=speed_players
                elif rect2.colliderect(lim4) and not(y2 > bola.center[1]):
                    y2=tamy-lim-altura2/2+1
                if y2 > bola.center[1] and not(rect2.colliderect(lim3)):
                    y2-=speed_players
                elif rect2.colliderect(lim3) and not(y2 < bola.center[1]):
                    y2=lim+altura2/2-1
                tempo = time.time() - tempo2
                tempo = round(tempo,2)
                tempo1 = fonte(int(50*scg)).render(str(tempo)+' s',0,(255,255,255))
                tela.blit(tempo1, (25, 25+lim))
            printa(fonte(int(50*scg)),tamx-int(25*scg),0,25+lim,'topright',(255,255,255),tela,[f'{tem} s'])
            rect1.center=(largura,y1)
            rect2.center=(tamx-largura,y2)
            bola = pygame.draw.circle(tela,cor_bola,loc_temp_cir,raio)

            if x == 0:
                if bola.colliderect(rect1) or bola.colliderect(rect2):
                    som.play()
                    speed_bolax*=-1 
                    cor_bola = [randrange(0,256),randrange(0,256),randrange(0,256)]
                    x = 5
            else:
                x -= 1
            if yy == 0:
                if bola.colliderect(lim4) or bola.colliderect(lim3):
                    speed_bolay*=-1
                    som.play()
                    cor_bola = [randrange(0,256),randrange(0,256),randrange(0,256)]
                    yy=5
            else:
                yy -= 1
            if not(speed_bola>speed_lim):
                speed_bola *= acel
                speed_bolax = speed_bola*speed_bolax/abs(speed_bolax)
                speed_bolay = speed_bola*speed_bolay/abs(speed_bolay) 
            elif y == 0:
                speed_bolax = speed_lim
                speed_bolay = speed_lim
                y=1
            loc_temp_cir[0]+=speed_bolax
            loc_temp_cir[1]+=speed_bolay
            if raio>loc_temp_cir[0]+100 or raio>tamx-loc_temp_cir[0]+100:
                if raio>loc_temp_cir[0]:
                    pontos2+=1
                    som2.play()
                else:
                    pontos1+=1
                    som2.play()
                loc_temp_cir = loc_inic_cir[:]
                speed_bola = speed_bolap
                y1 = tamy/2
                y2 = tamy/2
                exe=False
            acel = acel2
            speed_players*=1
        else:
            tempo2=time.time()
            pygame.draw.rect(tela,(255,255,255),rect1)
            pygame.draw.rect(tela,(255,255,255),rect2)
            speed_players = speed_playersp
            speed_bola = speed_bolap
            bola = pygame.draw.circle(tela,(255,255,255),loc_temp_cir,raio)
            rect1.center=(largura,tamy/2)
            rect2.center=(tamx-largura,tamy/2)
            printa(fonte(int(50*scg)),tamx-int(25*scg),0,25+lim,'topright',(255,255,255),tela,[f'{tem} s'])
            printa(fonte(int(50*scg)),tamx/2,100,200,'center',(150,255,150),tela,[msgini,'Aperte c para comandos'])
        rect1[3]=altura
        rect2[3]=altura2
        rect1[2]=largura
        rect2[2]=largura
        if multiplayer:
            pygame.draw.rect(tela,(255,255,255),rect2)
        else:
            pygame.draw.rect(tela,(255,0,0),rect2)
        if multiplayer2:
            pygame.draw.rect(tela,(255,255,255),rect1)
        else:
            pygame.draw.rect(tela,(0,255,0),rect1)
        if debug:
            if pygame.key.get_pressed()[K_1]:
                speed_lim += 1
            if pygame.key.get_pressed()[K_2]:
                speed_lim -= 1
            if pygame.key.get_pressed()[K_3]:
                acel2 += 0.0001
            if pygame.key.get_pressed()[K_4]:
                acel2 -= 0.0001
            if pygame.key.get_pressed()[K_5]:
                speed_bolap += 1
            if pygame.key.get_pressed()[K_6]:
                speed_bolap -= 1
            if pygame.key.get_pressed()[K_7]:
                speed_playersp += 1
            if pygame.key.get_pressed()[K_8]:
                speed_playersp -= 1
            if pygame.key.get_pressed()[K_9]:
                altura += 1
            if pygame.key.get_pressed()[K_0]:
                altura -= 1
            if pygame.key.get_pressed()[K_MINUS]:
                altura2 += 1
            if pygame.key.get_pressed()[K_EQUALS]:
                altura2 -= 1
            if pygame.key.get_pressed()[K_LEFT]:
                largura += 1
                lim+=1
            if pygame.key.get_pressed()[K_RIGHT]:
                largura -= 1
                lim-=1
            if pygame.key.get_pressed()[K_f]:
                fps += 1
            if pygame.key.get_pressed()[K_g]:
                fps -= 1
            printa(fonte(int(50*scg)),25,50,25,'topleft',(150,255,150),tela,[str(speed_lim),str(acel2),str(speed_bolap),str(speed_players),str(altura),str(altura2),str(fps)])
    pygame.display.flip()
pygame.quit()