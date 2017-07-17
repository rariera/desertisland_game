from tkinter import *
from PIL import ImageTk
import tkinter.scrolledtext as ScrolledText


#import check_command
#import health
_root = Tk()
_root.configure(bg = 'green')
_root.geometry('765x800')

def animation(): 		 		  	
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
	
cont = Button(text = 'Continue?', command = showimg)
canvas = Canvas(width = 533, height = 535)
text = ScrolledText.ScrolledText(width = 70, height = 15)
_frames = [ PhotoImage(file='guy_horse.gif', format = 'gif -index %i' % i) for i in range(0,4) ]
_photo = ImageTk.PhotoImage(file = 'beginning_animation.gif')

showimg()

def tkintermake():
    welcome = Label(text = '''Welcome to the desert island game!\nType something in the entry\n\nbox to begin!''', bg = 'blue4', fg = 'white')
    welcome.grid(row = 0, column = 0)
    cont.grid(row = 0, column = 1)
    text.grid(columnspan = 3, row = 3, column = 0)
    canvas.grid(rowspan = 3, columnspan = 3, row = 0, column = 2)
	
    return _root
	
if __name__ == "__main__":
    root = tkintermake()
    root.mainloop()
	
	
	

