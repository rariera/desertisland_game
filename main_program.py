from tkintermaker import *
from initialisation import *
from loop import entry, loop

entry.bind('<Return>', loop)

#Calling initialisation...
it = initialisation()
turn_no = it.turn_no


root = tkintermake()
root.mainloop()
