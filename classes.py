from tkinter import *
from gfunctions import chooseroom

class Character(object):
    def __init__(self, loc, health, inventory = []):
        self.loc = loc
        self.inventory = inventory
        self.health = health
        chooseroom(self)


class Output(object):
	def write(textbox, string):
		textbox.delete('1.0', END)
		textbox.insert('end', string)
	def noreplace_write(textbox, string):
		textbox.insert('end', string)