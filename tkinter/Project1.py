from tkinter import *

windows = Tk()

windows.title("My First Project")
windows.geometry("600x400")
# 窗口內容開始
# l = tk.Label(windows,text='Hello world',bg='green',font=('Arial',12),width=15,height=2)
# l.pack()

def insert_point():
    var = Entry.get()
    Text.insert('insert',var)

def insert_end():
    var = Entry.get()
    Text.insert('end',var)


Entry = Entry(windows,show=None)

Button1 = Button(windows,text='Add',width=15,height=2,command = insert_point)
Button2 = Button(windows,text='Delete',command = insert_end)
Text = Text(windows,height=2)


Entry.pack
Button1.pack(side=LEFT)
Button2.pack(side=LEFT)
Text.pack
# 窗口內容結束
windows.mainloop()