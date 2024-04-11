##f = open("alphabet.txt", "w")
##f.write("abcdefghijklmnopqrstuvwxyz")
##f.close()
##index = int(input("바꿀 포인터의 위치를 입력하세요.:"))
##f = open("alphabet.txt","r")
##f.seek(index)
##date = f.read()
##print(date)
##f.close()
##f = open("fruit.txt","r")
##word = f.readlines()
##for i in word:
##    i = i.strip()
##    if len(i)>=10:
##        print(i)
##f.close()
##f = open("anna.txt","r")
##data = f.readline()
##data = data.split()
##for i in data:
##    if 'b' in i:
##        print(i)
##f.close()
def read_file(file_name) :
    f = open(file_name,"r")
    lines = f.readlines()
    for line in lines :
        print(line.strip())
    f.close()    

def write_file(file_name, mode) :
    f = open(file_name,mode)
    while True:
        data = input()
        if data =="q":
            break
        f.write(data + "\n")
    f.close()
        

file_name = input("File name : ")
mode = input("File mode(r/w/a) : ")

if mode == "r" :
    read_file(file_name)
else :
    write_file(file_name,mode)

h = int(input("시간 입력 :"))
m = int(input("분 입력 :"))
m = 45

if m < 0:
    h = 1
    m += 60
if h < 0 :
    h+=24
print("%d %d" %(h,m))

        














