import tkinter as tk

windows = tk.Tk()
windows.title("my window")
windows.geometry("600x400")
# 窗口內容開始
# l = tk.Label(windows,text='Hello world',bg='green',font=('Arial',12),width=15,height=2)
# l.pack()
var1 = tk.StringVar()

def insert_select():
    var = ListBox.get(ListBox.curselection())
    var1.set(var)

Label = tk.Label(windows,bg='yellow',width=20,height=2,textvariable=var1)
Button1 = tk.Button(windows,text='print selection',command=insert_select)

var2 = tk.StringVar()
var2.set((11,22,33,44))
ListBox = tk.Listbox(windows,listvariable=var2)

List_items = [1,2,3,4]
List_items.insert(1,'Barry')
for number in List_items:
    ListBox.insert('end',number)
ListBox.insert(3,'Uni')


Label.pack()
Button1.pack()
ListBox.pack()

# 窗口內容結束
windows.mainloop()