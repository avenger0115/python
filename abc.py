##1.
##a = int (input("inch : "))
##print("%fcm"%(a*2.54))
##2.
##a = int (input("inch : "))
##b = a*2.54
##print(b)
##x = 10
##y = 50
##print('x : %d, y : %d' %(x,y))
##print('x와 y는같다?', x==y)
##print('x와 y는 다르다?',x !=y)
##print('x는 y보다 크다?',x > y)
##print('x는 y보다 작다?', x <y)
##print('x는 y보다 크거나 같다?', x >=y)
##print('x는 y보다 작거나 같다?', x<=y)
##a = int(input())
##b = int(input())
##c = int(input())
##print(a>=140 and b>=140 and c>=140)
##score = int(input('score : '))
##if score >= 60 : 
##    print('Pass')
##else :
##a = int(input())
##if a%2==0 :
##    print('EVEN')
##else :
##    print('ODD')
##score=input("성별을 입력하세요. : ")
##if score == 'M' :
##    print('Man')
##elif score == 'W' :  
##    print('Woman')
##else :
##    print('what')
##score = input('월을 입력하세요. : ')
##score = int(score)
##if score>=1 and score<=6 :
##    print('first haif')
##elif score>=7 and score<=12 :
##    print('second haif')
score = input('다음과 같은 메뉴가 있습니다. : ')
score = int(score)
if score == 1 :
    print('burgers are not available')
elif score>=2 and score<=3 :
    print('what would you like to drink?')
elif score == 4 :
    print('l like coke, too.',)
else :
    print('would you like hot or cold?')

