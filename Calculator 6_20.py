import tkinter
import re
import tkinter.messagebox
import math

Calculate_Times=0
Calculator = tkinter.Tk()
Calculator.title("Calculator")
#The size of the window
Calculator.geometry("420x450+0+0")
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
    global Calculate_Times
    global Ans
    #Get the text in the Entry
    Content = Var.get()
    #Check the times that user calculate if user did the calculate, then clean the entry
    if Calculate_Times>=1:
        Content=''
        Calculate_Times=0
    #If the user click on the decimal point button, add a ) before it
    if Content.startswith('.'):
        Content = '0'+Content   
    #If user click on normal number button
    if btn in '0123456789':
        Content+=btn #add the number that user click to the content
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
        Calculate_Times=0
        Content=''
    #If user click on DEL button(DEL=Delete)
    elif btn == 'DEL':
        Content=Content[:len(Content)-1]
    #If user click on button
    elif btn == '=':
        Calculate_Times=Calculate_Times+1
        try: #Find the result in the content
            Content = str(eval(Content))
            Ans=Content
            btnAns['state'] = 'active'
        except: #If the content can't find the result
            tkinter.messagebox.showerror('Error','Expression is incorrect')
            return
    #If the user click on operators
    elif btn == '+':
        if Content.endswith(Operators):
            tkinter.messagebox.showerror('Error','Continous operators not exist')
            return
        Content+=btn
    elif btn == '-':
        if Content.endswith(Operators):
            tkinter.messagebox.showerror('Error','Continous operators not exist')
            return
        Content+=btn
    elif btn == '*':
        if Content.endswith(Operators):
            tkinter.messagebox.showerror('Error','Continous operators not exist')
            return
        Content+=btn
    elif btn == '/':
        if Content.endswith(Operators):
            tkinter.messagebox.showerror('Error','Continous operators not exist')
            return
        Content+=btn
    elif btn == '**':
        if Content.endswith(Operators):
            tkinter.messagebox.showerror('Error','Continous operators not exist')
            return
        Content+=btn
    elif btn == '//':
        if Content.endswith(Operators):
            tkinter.messagebox.showerror('Error','Continous operators not exist')
            return
        Content+=btn
    #if the user click on answer button
    elif btn == 'Ans':
        btn=Ans
        Content+=btn
    #If the user click on pi button
    elif btn == 'math.pi':
        Content+=btn
    #If the user click on parenthsis
    elif btn == '(':
        Content+=btn
    elif btn == ')':
        Content+=btn
    #If the user click on square root(Sqrt=Square Root)
    elif btn == '√':
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
digits = list('1234567890.')+['√']
index = 0
for row in range(4):
    for col in range(3):
        d = digits[index]
        index += 1
        btnDigit=tkinter.Button(Calculator,text=d,command=lambda x=d:ButtonClick(x))
        btnDigit.place(x=10+col*100,y=115+row*50,width=100,height=50)

#operators
Operators = ('+','-','*','/','**','//') #** is number to the power of number, // is take the divisible

btnPlus = tkinter.Button(Calculator,text='+',command=lambda:ButtonClick('+'))
btnPlus.place(x=310,y=65,width=100,height=50)

btnMinus = tkinter.Button(Calculator,text='-',command=lambda:ButtonClick('-'))
btnMinus.place(x=310,y=115,width=100,height=50)

btnTime = tkinter.Button(Calculator,text='*',command=lambda:ButtonClick('*'))
btnTime.place(x=310,y=165,width=100,height=50)

btnDivide = tkinter.Button(Calculator,text='/',command=lambda x=Operators:ButtonClick('/'))
btnDivide.place(x=310,y=215,width=100,height=50)

btnDTime = tkinter.Button(Calculator,text='**',command=lambda:ButtonClick('**'))
btnDTime.place(x=310,y=265,width=100,height=50)

btnDDivide = tkinter.Button(Calculator,text='//',command=lambda x=Operators:ButtonClick('//'))
btnDDivide.place(x=310,y=315,width=100,height=50)

btnAns = tkinter.Button(Calculator,text='Ans',command=lambda:ButtonClick('Ans'))
btnAns.place(x=210,y=65,width=100,height=50)
btnAns['state'] = 'disable'

btnPi = tkinter.Button(Calculator,text='π',command=lambda:ButtonClick('math.pi'))
btnPi.place(x=210,y=315,width=100,height=50)

btnParenthesisLeft = tkinter.Button(Calculator,text='(',command=lambda:ButtonClick('('))
btnParenthesisLeft.place(x=10,y=315,width=100,height=50)

btnParenthesisRight = tkinter.Button(Calculator,text=')',command=lambda:ButtonClick(')'))
btnParenthesisRight.place(x=110,y=315,width=100,height=50)

btnBackspace = tkinter.Button(Calculator,text='DEL',command=lambda:ButtonClick('DEL'))
btnBackspace.place(x=210,y=365,width=100,height=50)

Calculator.mainloop
