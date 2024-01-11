##s1 = set([1,2,3,])
##s2 = set('apple')
##print(s1)
##print(s2)
##a = 1
##print(a)
##a += 1
##print(a)
##a *= 2
##print(a)
##t1 = (1,)
##t2 = (4,5,6,)
##print(t1+t2)
##print(t2*2)
##print(t2[0])
##print(t2[1:3])
##del t2[0]
##s1 =set([1,2,3,4,5,6,])
##s2 = set([4,5,6,7,8,9,])
##print(s1-s2)
##print(s1 & s2)
##print(s2 | s2)
##a = {'a' : 1, 'b' : 2, 'c' :3, 'd' :4}
##print(a.keys())
##print(a.values())
##print(a.items())
##a.clear()
##print(a)
##a = {'name' : 'minsu', 'address' : 'seoul', 'phone' : '010-1234-1234'}
##print(a.keys())
##a =set([1,2,3,])
##a.add(4)
##print(a)
##a.update('abc')
##print(a)
##a.remove('c')
##print(a)
##import turtle
##t = turtle.Turtle()
##t.fillcolor('red')
##t.begin_fill()
##t.right(60)
##t.circle(25,180)
##t.right(120)
##t.circle(25,180)
##t.right(120)
##t.circle(25,180)
##t.right(120)
##t.circle(25,180)
##t.right(120)
##t.circle(25,180)
##t.right(120)
##t.circle(25,180)
##t.end_fill()
##
##t.fillcolor('yellow')
##t.begin_fill()
##t.right(60)
##t.circle(50)
##t.end_fill()
##
##turtle.done()
##
##import turtle
##t = turtle. Turtle()
##
## 사용자에게 문자열 입력받기
##s = turtle.textinput('즐거운 씨큐브 코딩', '이름을 알려주세요')
##t.write("%s님 반갑습니다^^" % s)
##turtle.done()
##import turtle
##t = turtle.Turtle(shape = "turtle")
##s = "즐거운 씨큐브 코딩"
## 사용자에게 숫자 입력받기
##n = turtle.numinput(s, "압으로 얼마나 이동할까요?")
##t.forward(n)
##ang = turtle.numinput(s, "오른쪽으로 얼마나 호전할까요? :", default = 0, minval = 0, maxval = 360)
##t.right(ang)
##turtle.done()
##a = (1,)
##b = (2,3,4,)
##print(a+b)
##s1 = set([1,2,3,4])
##print(s1)
##a = set(['a','b','c','c','d','e','a'])
##print(a)
##a = {'a' : 90, 'b' :85, 'c' : 95}
##a['e'] = 70
##a['a'] = 100
##print(a)
d = {'plus' : ['더하기','장점'],
     'minus' :['빼기','적자'],
     'multiply' : ['곱하기','다양하게'],
     'division' :['나누기','분열']}
word = input('영어단어를 입력하세요.:')
print(d[word])

























