##class Character :
##    def __init__(self, name, weapon) :
##        self.name = name
##        self.weapon = weapon
##
##    def intro(self) :
##        print("name :",self.name)
##        print("weapon: ",self.weapon)
##class action(Character) :
##    step = 0
##
##    def move_forward(self,n) :
##        self.step +=n
##        print("current location is %d. " % self.step)
##    def move_backward(self,n) :
##        self.step -=n
##        print("current location is %d. " % self.step)
##
##    def turn_right(self) :
##        print("turn", " right")
##
##    def turn_left(self) :
##        print("turn", " left")
##
##lugo = action("Lugo" , "gun")
##lugo.intro()
##lugo.move_forward(10)
##lugo.move_backward(3)
##lugo.turn_right()
##lugo.turn_left()

##max = 0
##for i in range(10) :
##    n = int(input("정수 n 입력: "))
##    if max < n :
##        max = n
##print(max)

##n = int(input("정수 n 입력: "))
##
##for i in range(n) :
##    for j in range(i+1) :
##        print('*',end = ''  ) 
##    print(' ')

##n = int(input("정수 n 입력 : "))
##
##for i in range(1,10) :
##    print("%d * %d = %d" % (n,i,n*i))
##   
x = int(input())
y = int(input())

if x >0 and y>0 :
    print("제1사분면")
elif x <0 and y>0 :
    print("제2사분면")
elif x< 0 and y<0 :
    print("제3사분면")
elif x > 0 and y < 0 :
    print("제4사분면")





    
    
