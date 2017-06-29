import rooms
import items
import gfunctions


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



def write(textbox, string):
    textbox.delete('1.0', END)
    textbox.insert('end', string)
    

def entryget(Event = None):
    userinput = input.get()
    print(userinput)
    if userinput == 'yay':
        write(text, 'Yeah, that\'s it!')
    elif userinput == '':
        write(text, 'No, you need to type something in!')
