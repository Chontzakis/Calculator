from tkinter import *

window = Tk()
window.geometry('300x500+300+300')
window.configure(background = 'black')
numbers=[]
numbers.append(Button(window,text='1',width='11').grid(row=4,column=2))
numbers.append(Button(window,text='2',width='11').grid(row=4,column=1))
numbers.append(Button(window,text='3',width='11').grid(row=4,column=0))
numbers.append(Button(window,text='4',width='11').grid(row=3,column=2))
numbers.append(Button(window,text='5',width='11').grid(row=3,column=1))
numbers.append(Button(window,text='6',width='11').grid(row=3,column=0))
numbers.append(Button(window,text='7',width='11').grid(row=2,column=2))
numbers.append(Button(window,text='8',width='11').grid(row=2,column=1))
numbers.append(Button(window,text='9',width='11').grid(row=2,column=0))
signs = []
signs.append(Button(window,text='+',width='11').grid(row=5,column=0)) #0
signs.append(Button(window,text='*',width='11').grid(row=5,column=1)) #1
signs.append(Button(window,text='/',width='11').grid(row=5,column=2)) #2
signs.append(Button(window,text='C',width='35').grid(row=6,columnspan=5)) #3
window.mainloop()
