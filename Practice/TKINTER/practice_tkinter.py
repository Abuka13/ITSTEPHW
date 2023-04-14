
import tkinter as tk

win = tk.Tk()
#TODO поменять иконку приложения
photo = tk.PhotoImage(file="milan.png")
win.iconphoto(False,photo)
#TODO backround color
#win.config(bg='red')
#win.geometry("500x600") #длина и ширина
win.geometry("500x600") #где окно появится (+10+10)







#TODO НАДПИСЬ
# label_1 = tk.Label(win, text='Hello',
#                    bg = 'red', #TODO Цвет надписи
#                    fg = 'white', #TODO Цвет букв
#                    font=('Arial',20,'bold'),
#                    padx = 10, #TODO дальность от ширины надписи
#                    pady = 10,  #TODO дальность от длины надписи
#                    height = 10, #TODO высота
#                    width= 10 #TODO ширина
#                    )
# label_1.pack()








#TODO Кнопка
# def say_hello():
#     print('hello')
# def add_label():
#     label = tk.Label(win,text='fg')
#     label.pack()
# def counter():
#     global count
#     count+=1
#     btn4['text'] = f'Счетчик: {count}'
# count = 0
# btn1 = tk.Button(win, text='Hello',
#                  command=say_hello)
# btn2 = tk.Button(win, text='Add',
#                  command=add_label)
# btn4 = tk.Button(win, text=f'Счетчик: {count}',
#                  command=counter,
#                  activebackground='blue', #TODO Если нажать то на время превращается в синий
#                  bg='red'
#                  )
# btn2.pack()
# btn1.pack()
# btn4.pack()







#TODO ПОЗИЦИОНИРОВАНИЕ
## btn1 = tk.Button(win,text='Hello 1')
# btn2 = tk.Button(win,text='Hello 2')
# btn1.grid(row=0,column=0)
# btn2.grid(row=1,column=1)
##TODO еще куча инфомации которую можно загуглить))







#TODO Ввод и Удаление
def get_entry():
    value = name_enter.get()
    if value:
        print(value)
    else:
        print('Empty Entry')
def delete_entry():
    name_enter.delete(0)
def delete_entry():
    name_enter.delete(0,tk.END)
tk.Label(win,text='Имя').grid(row = 0, column=0)

name_enter = tk.Entry(win)
name_enter.grid(row=0,column=1)
password 

tk.Button(win,text='get',command=get_entry).grid(row=1,column=0,stick='we')
tk.Button(win,text='delete',command=delete_entry).grid(row=1,column=1,stick='we')


win.mainloop()

