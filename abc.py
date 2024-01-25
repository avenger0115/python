##import random
##com = random.randint(1,2)
##user = int(input('odd : 1, even :2\n'))
##print('com(%d) : user(%d)'%(com,user))
##if com == user :
##    print('correct')
##else :
##    print('lncorrect')
##import random
##a = ['월','화','수','목','금','토','일',]
##b = random.randint(0,6)
##print(a[b])
##from random import *
##a= ['월','화','수','목','금']
##print(choice([True,False]))
##print(choices(a))
##from random import *
##a = choice('abcdefg')
##print(a)
##from random import *
##a = [1,2,3,4,5]
##print(choices(a,[1,1,10,1,1]))
##from random import *
##a=[1,2,3,4,5,]
##print(choices(a,[1,2,1,1,5],k=3))
##from random import *
##a=[0,1,2,3,4,5]
##b = choice(a)
##if b == 0:
##    print('loss!')
##else :
##    print('no,%d spot!')
##from random import *
##a = [1,2,3,4,5,6,7,8,9,10]
##b = choices(a,[2,2,2,2,2,2,1,2,2,2],k=3)
##if b[0]==7 and b[1]==7 and b[2]==7:
##    print('lucky!')
from random import *
import turtle
house = turtle.Turtle()
house.penup()
house.goto(300,-100)
house.pendown()
house.fillcolor("skyblue")
house.begin_fill()
house.forward(100)
house.left(90)
house.forward(100)
house.left(90)
house.forward(100)
house.left(90)
house.forward(100)
house.end_fill()
house.fillcolor("royalblue")
house.begin_fill()
house.backward(100)
house.left(180)
house.left(-30)
house.forward(100)
house.right(120)
house.forward(100)
house.right(120)
house.forward(100)
house.end_fill()
line = turtle.Turtle()
line.penup()
line.goto(-380,-100)
line.pendown()
line.write(0)
line.forward(340)
line.write(50)
line.forward(340)
line.write(100)
t = turtle.Turtle(shape = 'turtle')
t.penup()
t.goto(-400,-100)
t.pendown()
t.color("purple","pink")
t.penup()
g =turtle.Turtle()
g.write("씨큐브 코딩의 타자 게임!", True, font=("Arial",20,"bold"))
fruit = ["apple","banana", "strawberry","watermelon","mandarin"]
score = 0
n = randint(3,5)
for i in range(n):
   s = choice(fruit)
   word = turtle.textinput("fruit","%s(%d/%d)"%(s,i+1,n))
   if s ==word :
       score +=1
rate = score / n *100
g.penup()
g.goto(0,-50)
g.pendown()
g.write("%d/%d번 성공!" %(score,n), True,font = ("Arial",15,"bold"))
g.penup()
g.goto(0,-100)
g.pendown()
g.write("정확도 : %1f%%" % rate,True,font =("Arial", 15, "bold"))





        






       






























