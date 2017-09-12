from tkinter import *
from PIL import ImageTk
import tkinter.scrolledtext as ScrolledText
import sys
from winsound import PlaySound
import winsound
import os

_root = Tk()
_root.configure(bg = 'blue4')
_root.geometry('765x800')

_bc = False

def animation(): 		 		  	
    if animation.index == -1:
        return
    imagecanvas = canvas.create_image(0, 0, anchor = NW, image = _frames[animation.index])
    animation.index = animation.index + 1
    if animation.index >= 29:
        imagecanvas = canvas.create_image(0,0, anchor = NW, image = ImageTk.PhotoImage(file = 'beach.png'))
        return
    _root.after(200, animation)



def showimg():
    imagecanvas = canvas.create_image(0,0, anchor = NW, image = _image)
    animation.index = -1

def showoimg():
    animation.index = 0
    animation()
    _root.photo = _photo
    
def much(character):
    if character != 'beach1':
        musicfile = character.room['music']
    else:
        musicfile = 'ocean.wav'
    print(musicfile)
    if os.path.isfile(musicfile):
        PlaySound(musicfile, winsound.SND_ASYNC|winsound.SND_LOOP)
    else:
        print('error: musicfile %s is nonexistent' % musicfile)


canvas = Canvas(width = 533, height = 535)
text = ScrolledText.ScrolledText(width = 70, height = 15)
_frames = [ PhotoImage(file='beginning.gif', format = 'gif -index %i' % i) for i in range(0,31) ]
_photo = ImageTk.PhotoImage(file = 'desert.png')

showoimg()

def bach(character):
    _bc = ImageTk.PhotoImage(file = character.room['background'])
    _image = _bc
    _root._image = _image
    imagecanvas = canvas.create_image(0,0, anchor = NW, image = _image)
    animation.index = -1


def tkintermake():
    welcome = Label(text = '''Welcome to the desert island game!\nType something in the entry\n\nbox to begin!''', bg = 'blue4', fg = 'white')
    welcome.grid(row = 0, column = 0)
    text.grid(columnspan = 3, rowspan = 10, row = 3, column = 0)
    canvas.grid(rowspan = 3, columnspan = 3, row = 0, column = 2)
    return _root

def exit():
    PlaySound(None, winsound.SND_ASYNC)
    _root.destroy()
    sys.exit()
	
if __name__ == "__main__":
    root = tkintermake()
    root.mainloop()