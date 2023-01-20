
from winsound import PlaySound
import pygame
import time
import random
pygame.init()
sizex=1900
sizey=1000

screen=pygame.display.set_mode((sizex,sizey))
pygame.display.set_caption("temple")
icon=pygame.image.load("temple.png")
pygame.display.set_icon(icon)
playerC=pygame.image.load("temple.png")
spike=pygame.image.load("spike.png")
b=100
px=300
py=900
sx=round(random.randint(0,sizex-100),100)
sy=0
playerC=pygame.transform.scale(playerC,(b,b))
spike=pygame.transform.scale(spike,(100,100))
def player(Px,Py):
    screen.blit(playerC,(Px,Py))
def spik(x,y):
    screen.blit(spike,(x,y))
def spik1(x,y):
    screen.blit(spike,(x,y))
score=0
k=7
speed=100
r=str(random.randint(0,sizex))
opened=True
while opened:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            opened=False
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_a):
                if(px>0):
                    px-=speed

            if(event.key == pygame.K_d):    
                if(px<sizex-100):
                    px+=speed

            if(event.key == pygame.K_w):
                if(py>0):
                    py-=speed

            if(event.key == pygame.K_s):
                if(py<sizey-100):
                    py+=speed
    sy+=k
             
    screen.fill((255,255,255))
    spik(sx,sy)
    if(sy>100):
        if(len(r)==4):
            p=int(r[0])*1000+int(r[1])*100
        else:
            p=int(r[0])*100
        spik1(p,0)
    if(sy>1000):
        if(len(r)==4):
            sx=int(r[0])*1000+int(r[1])*100
        else:
            sx=int(r[0])*100
        sy=0
        k+=.1
        score+=1
        r=str(random.randint(0,sizex))
        #hi ayush bhaiya at the time I made this project the play sound library was working but now its
        try:
            audio_file1 ='hit.wav'
            PlaySound(audio_file1)
        except:
            pass
    if(sy>900):
        if(sx==px):
            print("great")
            break
    player(px,py)
    pygame.display.update()
# we print scored
print("you scored : ",score)
try:
    audio_file ='h.mp3'
    PlaySound(audio_file)
except:
    pass