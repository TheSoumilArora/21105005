from tkinter import *
window = Tk()
window.iconbitmap('/Users/soumilarora/Downloads/AnyConv.com__PECFEST logo.icns')
window.minsize(width=1080,height=1080)
window.maxsize(width=1080,height=1080)
lbl1 = Label(window, text='Enter name',bg='black',fg='green',font=('Marvel',60),width=30)
lbl1.pack()

window.mainloop()