

from tkinter import *
import time

win = Tk()
win.geometry('750x300')
win.resizable(False,False)

win.config(bg='black')

sec = StringVar()
Entry(win, textvariable=sec, width = 2).grid(row=0,column=2)
sec.set('')
mins= StringVar()
Entry(win, textvariable = mins, width =2).grid(row=0,column=1)
mins.set('')
hrs= StringVar()
Entry(win, textvariable = hrs, width =2).grid(row=0,column=0)
hrs.set('')

def timer():
   times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
   while times > -1:
      minute,second = (times // 60 , times % 60)
      hour =0
      if minute > 60:
         hour , minute = (minute // 60 , minute % 60)
      sec.set(second)
      mins.set(minute)
      hrs.set(hour)
      win.update()
      time.sleep(1)
      if(times == 0):
         sec.set('00')
         mins.set('00')
         hrs.set('00')
      times -= 1

Button(win, text='Начать', command = timer).grid(row=2,column=1)
win.mainloop()
