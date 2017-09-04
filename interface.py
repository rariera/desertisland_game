import tkintermaker

class Interface(object):
    def print():
        raise Exception
        
class InterfaceTK(Interface):
    def print(self, string):
        tkintermaker.text.delete('1.0', END)
		tkintermaker.text.insert('end', string)
