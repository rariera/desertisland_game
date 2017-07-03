#Coconut make a class!!! then can make instances of class (see ex.41, Learn python the hard way)

from items import *
from tkintermaker import *
from initalisation import *
from loop import entry, loop

entry.bind('<Return>', loop)



toolslist = [axe]
#root = tkintermake()

#Calling initialisation...  
it = initialisation()
#character = it.character
turn_no = it.turn_no



print('the test is complete')
root = tkintermake()
root.mainloop()


