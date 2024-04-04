from tkinter import *
from random import *

win =Tk()
win.title("Rock Scissors Paper game")

def change_img(user) :
    List = ["scissors.png", "rock.png","paper.png"]

    com = randint(0,2)

    comcom_ing = PhotoImage(file = List[com])
    useruser_ing = PhotoImage(file = List[user])

    com_img['image'] = comcom_ing
    com_img.image = comcom_ing

    user_img['image'] = useruser_ing
    user_img.image = useruser_ing
    
    game(com,user)

def game(com,user) :
     if user == 0:
         if com == 0:
             lbl_res['text'] = "Draw"
         elif com ==1:
             lbl_res['text'] = "Computer win"
         else :
             lbl_res['text'] = "User wins"
     elif user == 1:
        if com == 0:
            lbl_res['text'] = "User wins"
        elif com == 1:
            lbl_res['text'] = "Draw"
        else :
            lbl_res['text'] = "Computer win"
     else :
        if com == 2:
            lbl_res['text'] = "Draw"
        elif com == 1:
            lbl_res['text'] = "User wins"
        else :
            lbl_res['text'] = "Computer win"
        
        


        

    
    
basic_img = PhotoImage(file = "ready.png")

com_img = Label(win,image = basic_img,relief = "solid")
user_img = Label(win,image = basic_img,relief = "solid")
lbl_com = Label(win, text = "Computer")
lbl_user = Label(win, text = "User")
lbl_res = Label(win, text = " ",width = 15,fg = "brown" ,bg = "lightyellow")

btn_scissors = Button(win,text = "scissors",bg = "skyblue",width = 15,command = lambda : change_img(0))
btn_rock = Button(win,text = "rock",bg = "pink",width = 15,command = lambda : change_img(1))
btn_paper = Button(win,text = "paper",bg = "light green",width = 15,command = lambda : change_img(2))

com_img.grid(row = 0,column = 0)
lbl_res.grid(row = 0,column = 1)
user_img.grid(row = 0,column = 2)
lbl_com.grid(row = 1,column = 0)
lbl_user.grid(row = 1,column = 2)

btn_scissors.grid(row = 2, column = 0)
btn_rock.grid(row = 2,column = 1)
btn_paper.grid(row =2,column = 2)
win.mainloop()
