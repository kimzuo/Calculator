import tkinter
import re
import tkinter.messagebox

Calculator=tkinter.Tk()
Calculator.title("Calculator")
#The size of the window
Calculator.geometry("400x400+0+0")
#Do not let the user to change the size of the page
Calculator.resizable(False,False)

'''Label'''

#Add a entry to our window and set it to Read only

#This give a way for user to change the text in the entry
Var=tkinter.StringVar(Calculator,'')
#Create the entry
Entry=tkinter.Entry(Calculator,textvariable=Var)
#Set the entry to Read only
Entry['state']='readonly'
#place our entry
Entry.place(x=10, y=10, width=390, height=30)
