import tkinter
import re
import tkinter.messagebox

Calculator = tkinter.Tk()
Calculator.title("Calculator")
#The size of the window
Calculator.geometry("420x400+0+0")
#Do not let the user to change the size of the page
Calculator.resizable(False,False)

'''Label'''

#Add a entry to our window and set it to Read only

#This give a way for user to change the text in the entry
Var = tkinter.StringVar(Calculator,'')
#Create the entry
Entry = tkinter.Entry(Calculator,textvariable=Var)
#Set the entry to Read only
Entry['state'] = 'readonly'
#place our entry
Entry.place(x=10, y=10, width=400, height=50)


'''Button'''
def ButtonClick(btn): #btn stands for button
    #Get the text in the Entry
    Content = Var.get()
    #If the user click on the decimal point button, add a ) before it
    if Content.startswith('.'):
        Content = '0'+Content
    
    #If user click on normal number button
    if btn in '0123456789':
        Content += btn #add the number that user click to the content
    #If user click ondecimal point
    elif btn == '.':
        LastPart = re.split(r'\+|-|\*|/]',Content)[-1] #split each word
        if '.' in LastPart:
            tkinter.messagebox.showerror('Error','Too many decimal points')
            return
        else:
            Content += btn #add the decimal points that user click to the content
    #If user click on AC button(AC=All Clear)
    elif btn == 'AC':
        Content=''
    #If user click on button
    elif btn == '=':
        try: #Find the result in the content
            Content = str(eval(Content))
        except: #If the content can't find the result
            tkinter.messagebox.showerror('Error','Expression is incorrect')
            return
    #If the user click on operators
    elif btn in Operators:
        if Content.endswith(Operators):
            tkinter.messagebox.showerror('Error','Continous operators not exist')
            return
        Content+=btn
    #If the user click on square root(Sqrt=Square Root)
    elif btn == 'Sqrt':
        a = Content.split('.')
        if all(map(lambda x:x.isdigit(),a)):
            Content = eval(Content)**0.5 #Square root the content
        else:
            tkinter.messagebox.showerror('Error','Expression is incorrect')
    Var.set(Content)
    

'''Button interface'''
# = and AC
btnAllClear = tkinter.Button(Calculator,text='AC',command=lambda:ButtonClick('AC'))
btnAllClear.place(x=10,y=65,width=100,height=50)
btnEqual = tkinter.Button(Calculator,text='=',command=lambda:ButtonClick('='))
btnEqual.place(x=110,y=65,width=100,height=50)

#digits or numbers and square root
digits = list('1234567890.')+['Sqrt']
index = 0
for row in range(4):
    for col in range(3):
        d = digits[index]
        index += 1
        btnDigit=tkinter.Button(Calculator,text=d,command=lambda x=d:ButtonClick(x))
        btnDigit.place(x=10+col*100,y=115+row*50,width=100,height=50)

#operators
Operators = ('+','-','*','/','**','//') #** is number to the power of number, // is take the divisible
for index, Operators in enumerate(Operators):
    btnOperators = tkinter.Button(Calculator,text=Operators,command=lambda x=Operators:ButtonClick(x))
    btnOperators.place(x=310,y=65+index*50,width=100,height=50)    

Calculator.mainloop
