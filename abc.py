####f = open("example.txt","w")
####f.close()
####f = open("example.txt","a")
####alphabet = ['a','b','c','d','e']
####for c in alphabet :
####    f.write(c)
####f.close()
####f = open("example.txt","r")
####data = f.read()
####print(data)
####f.close()
####f = open("example.txt","r")
####while True :
####    line = f.readline()
####    if not line : break
####    print(line,end = '')
####f.close()
####f = open("example.txt","r")
####data = f.readlines()
####for line in data :
####    print(line,end = '')
####f.close()
##f = open("example.txt","r")
##while True :
##    print(f.tell(), end = ' ')
##    line = f.readline()
##    print(line.strip())
##    if not line : break
##f.seek(26)
##print("after setting apointer : %d(%s)" % (f.tell(), f.read()[0]))
##f.close()
f = open("profile.txt","w")
name = input("Name : ")
age = input("Age : ")
f.write("Name : %s\n" % name)
f.write("Age : %s\n" % age)       
f.close()




