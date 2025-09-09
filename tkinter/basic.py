import tkinter

win = tkinter.Tk()
win.title("GUI")
win.minsize(width=500,height = 300)
#Label
lab = tkinter.Label(text = "First GUI Program" , font=("Arial",26) )
lab.pack()
win.mainloop() 