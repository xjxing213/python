##from tkinter import *

#demo1
##btn = Button()
##btn.pack()
##btn['text'] = 'Click me!'
##
##def clickme():
##    print("don't click me!you fig man")
####
####btn['command'] = clickme
##

##demo2
##Button(text='Click me too!',command=clickme).pack()

##demo3
##Label(text="I'm in the first window!").pack()
##second = Toplevel()
##Label(second, text="I'm in the second window!").pack()

##demo4
##for i in range(10):
##    Button(text=i).pack()

##demo5
##top = Tk()
##def callback(event):
##    print(event.x, event.y)
##
##top.bind('<Button-1>', callback)

##demo6文本编辑器
from tkinter import *
from tkinter.scrolledtext import ScrolledText
def load():
    with open(filename.get()) as file:
        contents.delete('1.0', END)
        contents.insert(INSERT, file.read())
def save():
    with open(filename.get(), 'w') as file:
        file.write(contents.get('1.0', END))
top = Tk()
top.title("Simple Editor")

contents = ScrolledText()
contents.pack(side=BOTTOM, expand=True, fill=BOTH)

filename = Entry()
filename.pack(side=LEFT, expand=True, fill=X)

Button(text='Open', command=load).pack(side=LEFT)
Button(text='Save', command=save).pack(side=LEFT)

mainloop()


    
    
