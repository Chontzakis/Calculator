from tkinter import *

window = Tk()
window.configure(background = 'black')
top_label = Entry(window).grid(row=0,columnspan=3)
def button_click(number):
    top_label.insert(0,number)

n1 = Button(window,text='1',width='11',padx = 12 , pady = 10,command = lambda: button_click(1))
n2 = Button(window,text='2',width='11',padx = 12 , pady = 10,command = lambda: button_click(2))
n3 = Button(window,text='3',width='11',padx = 12 , pady = 10,command = lambda: button_click(3))
n4 = Button(window,text='4',width='11',padx = 12 , pady = 10,command = lambda: button_click(4))
n5 = Button(window,text='5',width='11',padx = 12 , pady = 10,command = lambda: button_click(5))
n6 = Button(window,text='6',width='11',padx = 12 , pady = 10,command = lambda: button_click(6))
n7 = Button(window,text='7',width='11',padx = 12 , pady = 10,command = lambda: button_click(7))
n8 = Button(window,text='8',width='11',padx = 12 , pady = 10,command = lambda: button_click(8))
n9 = Button(window,text='9',width='11',padx = 12 , pady = 10,command = lambda: button_click(9))
n1.grid(row=4,column=2)
n2.grid(row=4,column=1)
n3.grid(row=4,column=0)
n4.grid(row=3,column=2)
n5.grid(row=3,column=1)
n6.grid(row=3,column=0)
n7.grid(row=2,column=2)
n8.grid(row=2,column=1)
n9.grid(row=2,column=0)

s1 = Button(window,text='+',width='11',padx = 12 , pady = 10)
s2 = Button(window,text='*',width='11',padx = 12 , pady = 10)
s3 = Button(window,text='/',width='11',padx = 12 , pady = 10)
s4 = Button(window,text='C',width='40',padx = 10 , pady = 10)
s1.grid(row=5,column=0) #0
s2.grid(row=5,column=1) #1
s3.grid(row=5,column=2) #2
s4.grid(row=6,columnspan=3)


window.mainloop()
