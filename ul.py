from tkinter import *
import os
from tkinter import messagebox
from tkinter import filedialog

#start
window=Tk()
window.geometry("200x50")

filedir = "temp.txt"

#fuctions
def Lower():
	global filedir
	with open(filedir, 'r') as theCore:
		theContents = theCore.read()
		with open(filedir, 'w') as theProcess:
			theProcess.seek(0)
			theProcess.write(theContents.lower())
	with open(filedir, 'r') as theCore:
		print(theCore.read())
def Upper():
	global filedir
	with open(filedir, 'r') as theCore:
		theContents = theCore.read()
		with open(filedir, 'w') as theProcess:
			theProcess.seek(0)
			theProcess.write(theContents.upper())			
	with open(filedir, 'r') as theCore:
		print(theCore.read())

# def donothing():
	# filewin = Toplevel(window)
	# button = Button(filewin, text="Do nothing button")
	# button.pack()

def fileget():
	global filedir
	filedir = filedialog.askopenfilename()
	print(filedir)

#config
window.title("V")
#buttons
Fitten = Button (window, text="File", command=fileget)
Fitten.pack(side=TOP)
Uptton = Button (window, text="Upper", command=Upper)
Uptton.pack(side=LEFT)
Lowtten = Button (window, text="Lower", command=Lower)
Lowtten.pack(side=RIGHT)
#end
window.mainloop()
