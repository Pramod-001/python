from tkinter import *
import math
red = "#e7305b"
blue = "#0a0741"
yellow = "#f7f5dd"
Font = "Courier"
work = 25
sb = 5
lb = 20
clock = None

#Count Down
def count(a):
    global clock
    minute = math.floor(a/60)
    sec = a % 60
    canvas.itemconfig(time,text= f"{minute}:{sec}")
    if a >0 :
        clock = win.after(1000,count,a-1)
    
#Timer 
def timer():
    count(5*60)    

#Reset

def stop():    
    win.after_cancel(clock)
def reset():
    canvas.itemconfig(time,text="00:00")
#UI setup

win = Tk()
win.title("Timer")
win.config(padx=100,pady=50,bg=yellow)
title = Label(text="Timer",fg=blue,bg=yellow,font=(Font,45,"bold"))
title.grid(column=1,row=0)

canvas = Canvas(width=250,height=300)
alarm = PhotoImage(file="alarm.png")
canvas.create_image(125,150,image = alarm)
time = canvas.create_text(125,160, text = "00:00",font=(Font,30,"bold"))

canvas.grid(column=1,row=1)

start = Button(text="Start",highlightthickness=0,command=timer)
start.grid(column=0,row=2)
end = Button(text="Stop",highlightthickness=0,command=stop)
end.grid(column=1,row=2)

end = Button(text="Reset",highlightthickness=0,command=reset)
end.grid(column=2,row=2)
win.mainloop()