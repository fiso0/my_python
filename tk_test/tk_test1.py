from tkinter import *

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()
	
	def say_hi(self):
		print('Hi there!')
	
	def createWidgets(self):
		self.QUIT = Button(self)
		self.QUIT['text'] = 'QUIT'
		self.QUIT['fg'] = 'red'
		self.QUIT['command'] = self.quit
		
		self.QUIT.pack({'side':'left'})
		
		self.hi = Button(self)
		self.hi['text'] = 'Hello'
		self.hi['command'] = self.say_hi
		
		self.hi.pack({'side':'left'})

tk=Tk()
app=Application(master=tk)
app.mainloop()
tk.destory()