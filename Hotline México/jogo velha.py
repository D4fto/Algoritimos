import pygame
aberto = True
tela = pygame.display.set_mode((1200,900))
tamanho = 150
maxx = int((tela.get_size()[0]/2)+1.5*tamanho)
minx = int((tela.get_size()[0]/2)-1.5*tamanho)
maxy = int((tela.get_size()[1]/2)+1.5*tamanho)
miny = int((tela.get_size()[1]/2)-1.5*tamanho)
xx=0
for i in range(1,10):
    globals()['x'+str(i)] = False
matriz = [[0,0,0],[0,0,0],[0,0,0]]
lista = [(minx,miny,minx+tamanho,miny+tamanho),(minx,miny,minx+2*tamanho,miny+tamanho),(minx,miny,minx+3*tamanho,miny+tamanho)]
b = a = m = n = 1

def x(pos,pos2,cor,tela,tam):
    pygame.draw.line(tela,cor,pos,pos2,tam)
    pygame.draw.line(tela,cor,(pos[0],pos2[1]),(pos2[0],pos[1]),tam)
def o(pos,pos2,cor,tela,tam):
    pygame.draw.circle(tela,cor,((pos[0]+pos2[0])/2,(pos[1]+pos2[1])/2),(pos[1]-pos2[1])*-1/2,tam)
def verifica(matriz,k):
    p = d = d1 = dia = x = y = 0
    for linhas in range(3):
        for colunas in range(3):
            if matriz[linhas][colunas] == k:
                x+=1
            if p == 0:
                for linhas2 in range(3):
                    if matriz[linhas2][colunas] == k:
                        y+=1
                if y == 3:
                    dia = True
                y=0
        p=1
        if matriz[(linhas*-1)-1][linhas] == k:
            d += 1
        if matriz[linhas][linhas] == k:
            d1 += 1
        if x == 3:
            dia = True
        x=0
    if d == 3:
        dia = True
    return dia
def coloca(pos,tam,dist,xx):
    if xx == 0:
        x((pos[0]+dist,pos[1]+dist),(tam[0]-dist,tam[1]-dist),(255,0,0),tela,10)
    elif xx == 1:
        o((pos[0]+dist,pos[1]+dist),(tam[0]-dist,tam[1]-dist),(0,0,255),tela,10)
def area_click(postam,tam):
    
    mouse = pygame.mouse.get_pos()
    
    if postam[0] < mouse[0] < tam[0] and postam[1] < mouse[1] < tam[1]:
        return True
    else:
        return False
while aberto:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            aberto = False
        if ev.type == pygame.MOUSEBUTTONDOWN:
            for k in range(1,10):
                if area_click((minx+tamanho*(a-1),miny+tamanho*(b-1)),(minx+a*tamanho,miny+b*tamanho)):
                    if globals()['x'+str(k)] == False:
                        globals()['x'+str(k)+str(k)] = xx
                        if xx == 0:
                            matriz[b-1][a-1] = 1
                            xx=1
                            
                        elif xx == 1:
                            matriz[b-1][a-1] = 2
                            xx=0
                            
                    globals()['x'+str(k)] = True
                if a%3 == 0:
                    a=0
                    b+=1
                a+=1

            a=1
            b=1
    tela.fill((255,255,255))
    pygame.draw.line(tela,(0,0,0),(minx+tamanho,miny),(minx+tamanho,maxy),5)
    pygame.draw.line(tela,(0,0,0),(maxx-tamanho,miny),(maxx-tamanho,maxy),5)
    pygame.draw.line(tela,(0,0,0),(minx,miny+tamanho),(maxx,miny+tamanho),5)
    pygame.draw.line(tela,(0,0,0),(minx,maxy-tamanho),(maxx,maxy-tamanho),5)
    for l in range(1,10):   
        if globals()['x'+str(l)]:
            coloca((minx+tamanho*(m-1),miny+tamanho*(n-1)),(minx+m*tamanho,miny+n*tamanho),15,globals()['x'+str(l)+str(l)])
            
        if m%3 == 0:
            m=0
            n+=1
        m+=1
    m=1
    n=1
    verifica(matriz,1)
    verifica(matriz,1)
    pygame.display.update()