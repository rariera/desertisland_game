#Coconut make a class!!! then can make instances of class (see ex.41, Learn python the hard way)

from items import *
from tkintermaker import *
from initalisation import *
from loop import entry, loop

entry.bind('<Return>', loop)



#Calling initialisation...
it = initialisation()
turn_no = it.turn_no


root = tkintermake()
root.mainloop()
