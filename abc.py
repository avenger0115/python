##from tkinter import *
##
##win = Tk()
##
##def click() :
##
##     if btn['text'] == "hello" :
##         btn['text'] = "python"
##         btn['bg'] = "green"
##     else :
##         btn['text'] = "hello"
##         btn['bg'] = "orange"
##         
##         
##btn = Label(win,text = "hello", fg = "white", bg = "orange")
##btn2 = Button(win,text = "Button",command = click)
##btn.pack()
##btn2.pack()
##win.mainloop()
##
##from tkinter import *
##win = Tk()
##win.title("red")
##abc1 = Label(win, width = 10,height = 5,bg = "red")
##abc2 = Label(win, width = 10,height = 5,bg = "orange")
##abc3 = Label(win, width = 10,height = 5,bg = "yellow")
##abc4 = Label(win, width = 10,height = 5,bg = "green")
##abc5 = Label(win, width = 10,height = 5,bg = "blue")
##abc6 = Label(win, width = 10,height = 5,bg = "purple")
##
##abc1.grid(row = 0,column = 0)
##abc2.grid(row = 0,column = 1)
##abc3.grid(row = 0,column = 2)
##abc4.grid(row = 1,column = 0)
##abc5.grid(row = 1,column = 1)
##abc6.grid(row = 1,column = 2)
##
##win.mainloop()

##add = lambda x,y : x+y
##print(add(10,100))
##
##def  remains(a,b) :
##     return a%b
##remains = lambda a,b : a%b
##print(remains(10,3))
##
##say = lambda name :print("hello "+name)
##say("noonoo")
##
##from tkinter import *
##
##def Click(shape) :
##    if shape == "circle" :
##        img = pPhotoLmage(file = "circle.png")
##    elif shape == "triangle" :
##        img = PhotoLmage(file = "triangle.png")
##    else :
##        img = Photolmage(file = "star.png")
##
##    lbl['image'] =img
##    lbl.image = img
##
##win = Tk()
##
##img = PhotoImage(file = "circle.png")
##lbl = Label(win,image = img)
##
##btn1 = Button(win,text = "circle",command = lambda : Click("circle"))
##btn2 = Button(win,text = "triangle",command = lambda : Click("triangle"))
##btn3 = Button(win,text = "star",command = lambda : Click("star"))
##
##lbl.grid(row = 0,column = 0, columnspan = 3)
##btn1.grid(row = 1,column = 0)
##btn2.grid(row = 1,column = 1)
##btn3.grid(row = 1,column = 2)
##
##win.mainloop()

from tkinter import *
win =Tk()
win.title("Rock Scissors Paper game")

basic_img = PhotoImage(file = "ready.png")

com_img = Label(win,image = basic_img,relief = "solid")
user_img = Label(win,image = basic_img,relief = "solid")
lbl_com = Label(win, text = "Computer")
lbl_user = Label(win, text = "User")
lbl_res = Label(win, text = " ",width = 15,fg = "brown" ,bg = "lightyellow")

btn_scissors = Button(win,text = "scissors",bg = "skyblue",width = 15,command = lambda : change_img(0))
btn_rock = Button(win,text = "scissors",bg = "pink",width = 15,command = lambda : change_img(0))
btn_paper = Button(win,text = "scissors",bg = "light green",width = 15,command = lambda : change_img(0))

com_img.grid(row = 0,column = 0)
lbl_res.grid(row = 0,column = 1)
user_img.grid(row = 0,column = 2)
lbl_com.grid(row = 1,column = 0)
lbl_user.grid(row = 1,column = 2)

btn_scissors.grid(row = 2, column = 0)
btn_rock.grid(row = 2,column = 1)
btn_paper.grid(row =2,column = 2)
win.mainloop()
    




















