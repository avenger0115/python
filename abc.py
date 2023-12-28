import random as rd
import turtle

t = turtle.Turtle()
t.shape('turtle')

x = rd.randint(-300,300)
y = rd.randint(-300,300)

t.goto(x,y)

x = rd.randint(-300,300)
y = rd.randint(-300,300)

t.goto(x,y)

x = rd.random() + rd.randint(-300,300)
x = rd.random() + rd.randint(-300,300)

t.goto(x,y)

x = rd.random() + rd.randint(-300,300)
x = rd.random() + rd.randint(-300,300)

t.goto(x,y)

turtle.done()





