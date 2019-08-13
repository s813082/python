import tkinter as tk
import select_mssql as select_mssql

windows = tk.Tk()
windows.title("Update Ext.")
windows.geometry("200x200")



on_hit = False
title = tk.Label(windows, text='想查詢的分機號碼')

type_Phone = tk.Entry(windows,show = None)

show_phone = tk.Text(windows,height=2)

def getValue():
    show_phone_var = show_phone.get()
    type_Phone_var = type_Phone.get()
    # rows = select_mssql.SeleteData(show_phone_var)
    if show_phone_var =='':
        show_phone.insert('insert',show_phone_var)
        # print(type(show_phone_var)) str
    else:
        show_phone.delete(0,'end')
        show_phone.insert('insert',type_Phone_var)

b= tk.Button(windows,
    text='Summit',
    width = 10,
    height = 1,
    command = getValue
)

title.pack()
type_Phone.pack()
b.pack()
show_phone.pack()




# 窗口內容結束
windows.mainloop()