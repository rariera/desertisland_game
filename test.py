from PIL import ImageTk
from tkinter import *

_root = Tk()
_root.configure(bg = 'green')
_root.geometry('765x700')

def animation():
    _frames = [ PhotoImage(file='guy_horse.gif', format = 'gif -index %i' % i) for i in range(0,4) ]
    if animation.index == -1:
        return
    imagecanvas = canvas.create_image(0, 0, anchor = NW, image = _frames[animation.index])
    animation.index = animation.index + 1
    if animation.index > 3:
        animation.index = 0
    _root.after(300, animation)

def showimg():
    _root.photo = _photo
    imagecanvas = canvas.create_image(0,0, anchor = NW, image = _photo)
    cont.configure(text = 'let\'s go!!', command = showoimg)
    animation.index = -1

def showoimg():
    animation.index = 0
    animation()
    _root.photo = _photo
    cont.configure(text = 'let\'s not?', command = showimg)


text = Text(width = 70, height = 15)
_photo = ImageTk.PhotoImage(file = 'desert.png')
canvas = Canvas(width = 533, height = 535)

cont = Button(text = 'lol!', command = showimg)

def tkintermake():
    welcome = Label(text = '''Welcome to the desert island game!\nType something in the entry\n\nbox to begin!''', bg = 'blue4', fg = 'white')
    welcome.grid(row = 0, column = 0)
    cont.grid(row = 1, column = 1)
    text.grid(columnspan = 3, row = 3, column = 0)
    canvas.grid(rowspan = 3, columnspan = 3, row = 0, column = 2)

animation()

tkintermake()

_root.mainloop()
