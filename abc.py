##def square(a,b) :
##    return a **b
##
##a = int(input("a를 입력 : "))
##b = int(input("b 를 입력 : "))
##
##n = square(a,b) 
##print(n)
##
##def warning() :
##    for _ in range(3) :
##        print("Fier!")
##warning()
##
##def two_times() :
##    for i in range(1,10) :
##        print("2 * %d = %d" % (i, 2* i), end = ' ')
##two_times()
##
##def say(name) :
##    print("Welcome,", name)
##    return
##say("minsu")
##
##def day(m,d) :
##    print("Today is %s/%s." %(m,d))
##day(12,7)
##
##a = 0
##def f() :
##    global a
##    global b
##    print(a)
##    a = 10
##    b = 20
##f()
##print(a)
##print(b)
##
##def A() :
##    print(1)
##    r = B()
##    print(r)
##def B() :
##    print(2)
##    return 3
##A()
##print(4)
##
##def f(n) :
##     print(n)
##     if n > 1 :
##         f(n-1)
##f(3)
##
##def factorial(n) :
##    if n == 1 :
##        return 1
##    else :
##        return n * factorial(n-1)
##
##fac = factorial(4)
##print("4! =", fac)
## 
##def judge(n) :
##    if n > 0 :
##        print("plus")
##    elif n < 0 :
##        print("minus")
##    else :
##        print("zero")
##
##n = int(input())
##judge(n)
##
##def season(n) :
##    if n > 2 and n <6 :
##        print("spring")
##    elif n > 5 and n < 9 :
##        print("summer")
##    elif n > 8 and n < 12 :
##        print("fall")
##    else :
##        print("winter")
##
##n = int(input("월 입력"))
##season(n)

from random import *

def lotto() :
    lot = []

    for i in range(6) :
        lot.append(randint(1,45))
    lot.sort()
    print(lot)

lotto()

from random import *

def lotto() :
    lot = set()

    while len(lot) < 6 :
        lot.add(randint(1,45))#set()에 요소를 추가하는 함수
        
    lot = list(lot)
    lot.sort()
    print(lot)

lotto()







        
















     









