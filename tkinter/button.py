import tkinter as tk

windows = tk.Tk()
windows.title("my window")
windows.geometry("200x100")
# 窗口內容開始
# l = tk.Label(windows,text='Hello world',bg='green',font=('Arial',12),width=15,height=2)
# l.pack()

var = tk.StringVar()
l = tk.Label(
    windows,
    textvariable=var,
    bg='green',font=('Arial',12),
    width = 15,
    height = 2
)
l.pack()

on_hit = False

def hit_me():
    global on_hit
    if on_hit ==False:
        on_hit = True
        var.set("you fuck me")
    else:
        on_hit = False
        var.set("")
        
b= tk.Button(windows,
    text='FUCK ME!!!',
    width = 15,
    height = 3,
    command=hit_me
)
b.pack()


# 窗口內容結束
windows.mainloop()