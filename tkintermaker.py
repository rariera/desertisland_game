import rooms
import items
import tools
import gfunctions
import cfunctions

from tkinter import *
from PIL import ImageTk

from loop import loop
import check_command
import health

class Output(object):
	def write(self, textbox, string):
		textbox.delete('1.0', END)
		textbox.insert('end', string)

def animation(): 		 		  	
    if animation.index == -1:
        return
    imagecanvas = canvas.create_image(0, 0, anchor = NW, image = frames[animation.index])
    animation.index = animation.index + 1
    if animation.index > 3:
        animation.index = 0
    root.after(300, animation)

def delete(widget):
    widget.grid_forget()

def showimg():
    root.photo = photo
    imagecanvas = canvas.create_image(0,0, anchor = NW, image = photo)
    cont.configure(text = 'let\'s go!!', command = showoimg)
    animation.index = -1

def showoimg():
    animation.index = 0
    animation()
    root.photo = photo
    cont.configure(text = 'let\'s not?', command = showimg)




def entryget(Event = None):
    userinput = input.get()
    print(userinput)
    if userinput == 'yay':
        write(text, 'Yeah, that\'s it!')
    elif userinput == '':
        write(text, 'No, you need to type something in!')


welcome = Label(text = '''Welcome to Steve\'s game!\n
Type something in the entry\n
box to begin!''', bg = 'blue4', fg = 'white')
	
cont = Button(text = 'Continue?', command = showimg)
text = Text(width = 70, height = 15)
canvas = Canvas(width = 533, height = 535)
input = Entry()
confirm = Button(text = 'Enter', command = loop)
frames = [ PhotoImage(file='guy_horse.gif', format = 'gif -index %i' % i) for i in range(0,4) ]
photo = ImageTk.PhotoImage(file = 'desert.png')
root = Tk()
root.geometry('765x700')
root.configure(background = 'blue4')
confirm = Button(text = 'Enter', command = loop)

def tkintermake():
    welcome.grid(row = 0, column = 0)
    cont.grid(row = 0, column = 1)
    text.grid(columnspan = 3, row = 3, column = 0)
    canvas.grid(rowspan = 3, columnspan = 3, row = 0, column = 2)
    input.grid(row = 1, column = 0)
    userinput = ''
    confirm.grid(row = 1, column = 1)
    input.bind('<Return>', loop)

    animation.index = 0
    animation()

