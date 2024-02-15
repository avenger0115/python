##List = ['a','b','c']
##for s in List :
##    print(s)
##num_list =[1,2,3,4,5]
##sum = 0
##for num in num_list :
##    sum+= num
##print('avg : %d' %(sum//5))
##aList =[1,2,3]
##bList = [10,100,1000]
##for a in aList :
##    for b in bList :
##        print(a*b,end = ' ')
##    print()
##for i in range(10) :
##    print(i,end = ' ')
##for i in range(10,21) :
##    print(i,end = ' ')
##for i in range(1,10,2) :
##    print(i, end = ' ')
##List = ["Noah","Minsu","keily","Yuri"]
##
##for name in List :
##    print("%s, congratulation!" % name)
##for i in range(1,11) :
##    print(i,end = ' ')
##a = int(input(" 몇단? "))
##for i in range(1,10) :
##    print("%d * %d = %d" %(a , i, a*i))
##for i  in range(2,100,2) :
##    print(i, end = ' ')
##a = int(input("입력받은= "))
##for i in range(a,51) :
##    print(i,end = ' ')
##for i in range(3) :
##    for j in range(1,6) :
##        print(j, end = ' ')
##    print()
##for i in range(5) :
##    for j in range(5) :
##        print('*', end =  ")
##    print()
##for i in range(2,10) :
##    print("<%d단>"% i)
##    for j in range(1,10) :
##        print("%d*%d = %2d" %(i,j,i*j))
##    print()
import sys
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((400,300))

pygame.display.set_caption("Tick Tock Timer")

CLOCK = pygame.time.Clock()

sysfont = pygame.font.SysFont(None,36)

timer = 0

while True :

    for event in pygame.event.get() :

        if event.type == QUIT :
            pygam.quit()
            sys.exit()

    timer +=1

    screen.fill((255,255,255))

    cnt_txt = sysfont.render("Timer : %d" % timer, True,(0,0,0))

    screen.blit(cnt_txt, (140,140))

    pygame.display.update()

    CLOCK.tick(1)




                             
                            













            

































    
