##from tkinter import *
##win = Tk()
##
##img = PhotoImage(file = "pizza.png")
##hihi = Label(win,image = img)
##abc = Label(win,text = "pizza",bg = "yellow",fg = "red")
##hihi.pack()
##abc.pack()
##
##
##win.mainloop()

##from tkinter import *
##win = Tk()
##
##apple = Button(win,text = "Button")
##apple.pack()
##win.mainloop()

##from tkinter import *
##win = Tk()
##
##def click():
##    if btn['text'] == "red":
##        btn['text'] = "blue"
##        btn['bg'] = "blue"
##    else:
##        btn['text'] = "red"
##        btn['bg'] = "red"
##
##btn = Button(win,text = "red",fg="white",bg ="red",command=click)
##btn.pack()
##
##win.mainloop()

##from tkinter import *
##win = Tk()
##
##def click():
##    if hihi['text'] == "hello":
##        hihi['text'] = "python"
##        hihi['bg'] = "green"
##    else:
##        hihi['text'] = "hello"
##        hihi['bg'] = "orange"
##        
##hihi = Label(win,text = "hello",bg="orange",fg ="white")
##btn = Button(win,text = "Button", command=click)
##hihi.pack()
##btn.pack()
##
##win.mainloop()

from tkinter import *
win = Tk()

def message(event):
    lbl['text'] = entry.get()

entry = Entry(win)
entry.bind("<Return>",message)
entry.pack()
lbl = Label(win,text = " ")
lbl.pack()
win.mainloop()








