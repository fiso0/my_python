from tkinter import *

def say_hi():
	print('Hi')
	
def helloInWindow():
	from tkinter import messagebox
	messagebox.showinfo( "Hello Python", "Hello World")

tk=Tk()

frame = Frame(tk,relief=RIDGE,borderwidth=2)
frame.pack(fill=BOTH,expand=1)

label = Label(frame,text='Hi~')
label.pack(fill=X,expand=1)

button = Button(frame,text='Exit',command=tk.destroy)
button.pack(side=BOTTOM)

btn_hi = Button(frame,text='Hi',command=say_hi)
btn_hi.pack(side=BOTTOM)

btn_hello = Button(frame,text='Hello in Window',command=helloInWindow)
btn_hello.pack(side=RIGHT)

tk.mainloop()