##from random import *
##import turtle
##house = turtle.Turtle()
##house.penup()
##house.goto(300,-100)
##house.pendown()
##house.fillcolor("skyblue")
##house.begin_fill()
##house.forward(100)
##house.left(90)
##house.forward(100)
##house.left(90)
##house.forward(100)
##house.left(90)
##house.forward(100)
##house.end_fill()
##house.fillcolor("royalblue")
##house.begin_fill()
##house.backward(100)
##house.left(180)
##house.left(-30)
##house.forward(100)
##house.right(120)
##house.forward(100)
##house.right(120)
##house.forward(100)
##house.end_fill()
##line = turtle.Turtle()
##line.penup()
##line.goto(-380,-100)
##line.pendown()
##line.write(0)
##line.forward(340)
##line.write(50)
##line.forward(340)
##line.write(100)
##t = turtle.Turtle(shape = 'turtle')
##t.penup()
##t.goto(-400,-100)
##t.pendown()
##t.color("purple","pink")
##t.penup()
##g =turtle.Turtle()
##g.write("씨큐브 코딩의 타자 게임!", True, font=("Arial",20,"bold"))
##fruit = ["apple","banana", "strawberry","watermelon","mandarin"]
##score = 0
##n = randint(3,5)
##for i in range(n):
##   s = choice(fruit)
##   word = turtle.textinput("fruit","%s(%d/%d)"%(s,i+1,n))
##   if s ==word :
##       score +=1
##rate = score / n *100
##g.penup()
##g.goto(0,-50)
##g.pendown()
##g.write("%d/%d번 성공!" %(score,n), True,font = ("Arial",15,"bold"))
##g.penup()
##g.goto(0,-100)
##g.pendown()
##g.write("정확도 : %1f%%" % rate,True,font =("Arial", 15, "bold"))
##
##distance = t.distance(line)/100*rate
##t.speed(1)
##t.forward(distance)
##if rate == 100:
##    t.write("집에 데려다줘서 고마워!! ", False,"center",font = ("Arial",15,"bold"))
##    t.left(60)
##    t.right(60)
##    t.left(60)
##    t.right(60)
##elif rate > 80:
##    t.write("집이 코압인데!!한 번만 더 시도해줘!! ", False,"center",font = ("Arial",15,"normal"))
##elif rate > 50 :
##    t.write("집에 가고 싶어 ㅠ0ㅠ!! ", False,"center",font = ("Arial",15,"normal"))
##else  :
##    t.color('black')
##    t.right(360)
##    t.write("거북이가 쓰러졌어요 ㅠ_ㅠ!! ", False,"center",font = ("Arial",15,"normal"))
##turtle.done()
##
##i = 1
##while i <=10 :
##    print(i,end = ' ')
##    i += 1
##sum = 0
##i =1
##while i <= 100 :
##   sum += i
##   i+=1
##print(sum)
##i = 0
##while i <10:
##    i += 1
##    if i % 2 == 0 :
##        continue
##    print(i,end = ' ')
##a = input()
##a = int(a)
##
##print(a%2)
##    
##while True :
##    ans = input("Shall we close? (y/n) ")
##    if ans == 'y' :
##         print("The end")
##         break
##ans = ' '
##while ans != "Yes" :
##    ans = input("Are you ready? ")
##print("going out")

##i = 1
##while i <=100 : 
##     print(i, end = ' ')
##     i +=1
##a =input("정수를 입력하세요. : ")
##a =int(a)
##sun = 0
##i = 1
##while i <= a :
##    sun += i
##    i += 1
##print(sun)
##i =0
##while i < 5:
##    i +=1
##    a = int(input('input : '))
##    if a % 5 !=0:    
##        print(a)
##    else:
##        continue
while True:
    n = int(input('입력하세요,:'))
    if n==0 :
        break







