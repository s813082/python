import tkinter as tk

windows = tk.Tk()
windows.title("Update Ext.")
windows.geometry("600x400")
# 窗口內容開始
# l = tk.Label(windows,text='Hello world',bg='green',font=('Arial',12),width=15,height=2)
# l.pack()
on_hit = False
tk.Label(windows, text='想查詢的分機號碼').place(x=50, y= 10)

type_Phone = tk.Entry(windows,show = None)
type_Phone.pack()

var = tk.StringVar()
l = tk.Label(
    windows,
    textvariable=var,
    font=('Arial',12),
    width = 15,
    height = 2
)

def hit_me():
    global on_hit
    if on_hit ==False:
        on_hit = True
        var.set("you hit me")
    else:
        on_hit = False
        var.set("")
        
b= tk.Button(windows,
    text='Summit',
    width = 10,
    height = 1,
    command=hit_me
)
l.pack()
b.pack()



# 窗口內容結束
windows.mainloop()