import tkinter as tk

windows = tk.Tk()
windows.title("my window")
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


Entry = tk.Entry(windows,show=None)

Button1 = tk.Button(windows,text='insert point',width=15,height=2,command = insert_point)
Button2 = tk.Button(windows,text='insert end',command = insert_end)
Text = tk.Text(windows,height=2)


Entry.pack()
Button1.pack()
Button2.pack()
Text.pack()
# 窗口內容結束
windows.mainloop()