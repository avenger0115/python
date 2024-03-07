##def add(x,y) :
##    s = x+y
##    return s
##
##result = add(10,20) + add(20,30)
##print(result)
##def get_max(x,y) :
##    if x > y :
##        return x
##    else :
##        return y
##
##x =int(input())
##y = int(input())
##
##n = get_max(x,y)
##print(n)

##def plus(x) :
##    if x > 0 :
##       return True
##    else :
##       return False
##
##x = int(input("정수를 입력하세요.:"))
##print(plus(x))
        
##def get_sum(n) :
##    s = 0
##    for i in range(1,n+1) :
##        s+= i
##    return s
##
##n = int(input())
##print("1부터 %d까지의 합은 %d입니다." %(n,get_sum(n)))

##def get_sum(a,b) :
##    s = 0
##    for i in range(a,b+1) :
##        s+= i
##    return s
##    
##a = int(input())
##b = int(input())
##print("%d부터 %d까지의 합은 %d입니다." %(a,b,get_sum(a,b)))

##def area(x,y) :
##    s = x*y
##    return s
##    
##w = int(input("가로입력 :"))
##h = int(input("세로입력 :"))     
##
##n = area(w,h)
##print(n)

##def area(w) :
##    s = 3.14*w*w
##    return s
##
##w = int(input("반지름 입력 : "))
##
##n = area(w)
##print(n)

##def number(w) :
##    if w % 2 == 0 :
##        return "even"
##    else :
##        return "odd"
##
##w = int(input("정수를 입력하세요:"))
##
##n = number(w)
##print(n)

def square(a,b) :   
    return a **b
        
a = int(input("a 를 입력 : "))
b = int(input("b 를 입력 : "))

n = square(a,b)
print(n)



