import sys
import os
import tkinter
import re
import tkinter.messagebox
import math
import random
import time
from functools import reduce

Calculate_Times=0
Calculate_Times_Save=0
Calculator = tkinter.Tk()
Calculator.title("Calculator")
#The size of the window
Calculator.geometry("420x500+0+0")
#Do not let the user to change the size of the page
Calculator.resizable(False,False)

#Creating a menu
menubar = tkinter.Menu(Calculator) #Create the menubar for the root

#Adding menu on menubar
fmenu1 = tkinter.Menu(Calculator)
fmenu2 = tkinter.Menu(Calculator)

#Adding buttons for different menu
fmenu1.add_command(label='Standard',command=lambda:standardcolor_on())
fmenu1.add_command(label='Random',command=lambda:randomcolor_on())
fmenu1.add_command(label='G.Fan',command=lambda:G_Fancolor_on())
fmenu2.add_command(label='What you need to know',command=lambda:Help())

#Add the menu to the menubar
menubar.add_cascade(label='Color',menu=fmenu1)
menubar.add_cascade(label='Help',menu=fmenu2)
Calculator.config(menu=menubar) 

#Help button
def Help():
    tkinter.messagebox.showinfo(title='Help', message='Hi there, this calculator is a muti-function calculater, but it is important that I should tell you, the operators: +, -, *, /, ** , //, Sin, Cos, Tan can bring into the function, but Square root and ! can only calculater the number (not the equation) that input in the Entry, it can not bring into the function ')

#Random Color
def randomcolor_a():
    global color
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = ''
    '''
    if sta == 'on':
    '''
    for i in range(6):
        color += colorArr[random.randint(0,14)]
    return'#'+color


def randomcolor_b():
    global color
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = ''
    for i in range(6):
        color += colorArr[random.randint(0,14)]
    return'#'+color


def randomcolor_c():
    global color
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = ''
    for i in range(6):
        color += colorArr[random.randint(0,14)]
    return'#'+color

def randomcolor_d():
    global color
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = ''
    for i in range(6):
        color += colorArr[random.randint(0,14)]
    return'#'+color


def randomcolor_e():
    global color
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = ''
    for i in range(6):
        color += colorArr[random.randint(0,14)]
    return'#'+color


def randomcolor_f():
    global color
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = ''
    '''
    if sta == 'on':
    '''
    for i in range(6):
        color += colorArr[random.randint(0,14)]
    return'#'+color


def randomcolor_g():
    global color
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = ''
    '''
    if sta == 'on':
    '''
    for i in range(6):
        color += colorArr[random.randint(0,14)]
    return'#'+color


def randomcolor_h():
    global color
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = ''
    '''
    if sta == 'on':
    '''
    for i in range(6):
        color += colorArr[random.randint(0,14)]
    return'#'+color


def randomcolor_i():
    global color
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = ''
    '''
    if sta == 'on':
    '''
    for i in range(6):
        color += colorArr[random.randint(0,14)]
    return'#'+color


def randomcolor_j():
    global color
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = ''
    '''
    if sta == 'on':
    '''
    for i in range(6):
        color += colorArr[random.randint(0,14)]
    return'#'+color


def randomcolor_k():
    global color
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = ''
    '''
    if sta == 'on':
    '''
    for i in range(6):
        color += colorArr[random.randint(0,14)]
    return'#'+color

def randomcolor_on():
    global rca,rcb,rcc,rcd,rce,rcf,rcg,rch,rci,rcj,rck #Global value for color
    #Set the color    
    rca=randomcolor_a()
    rcb=randomcolor_b()
    rcc=randomcolor_c()
    rcd=randomcolor_d()
    rce=randomcolor_e()
    rcf=randomcolor_f()
    rcg=randomcolor_g()
    rch=randomcolor_h()
    rci=randomcolor_i()
    rcj=randomcolor_j()
    rck=randomcolor_k()
    #Configure the color for every button
    btnAllClear.configure(bg = rcc)
    btnEqual.configure(bg = rcc)
    btnBackspace.configure(bg = rcc)
    btn1.configure(bg = rca)
    btn2.configure(bg = rca)
    btn3.configure(bg = rca)
    btn4.configure(bg = rca)
    btn5.configure(bg = rca)
    btn6.configure(bg = rca)
    btn7.configure(bg = rca)
    btn8.configure(bg = rca)
    btn9.configure(bg = rca)
    btn0.configure(bg = rca)
    btnDP.configure(bg = rca)
    btnSqrt.configure(bg = rca)
    btnPlus.configure(bg = rcb)
    btnMinus.configure(bg = rcb)
    btnTime.configure(bg = rcb)
    btnDivide.configure(bg = rcb)
    btnDTime.configure(bg = rcb)
    btnDDivide.configure(bg = rcb)
    btnAns.configure(bg = rce)
    btnPi.configure(bg = rca)
    btnEE.configure(bg = rca)
    btnParenthesisLeft.configure(bg = rcd)    
    btnParenthesisRight.configure(bg = rcd)
    btnSin.configure(bg = rcd)
    btnCos.configure(bg = rcd)
    btnTan.configure(bg = rcd)
    btnE.configure(bg = rcd)

#Standard color
def standardcolor_on():
    global rca,rcb,rcc,rcd,rce,rcf,rcg,rch,rci,rcj,rck #Global value for color
    #Set the color     
    rca=rcb=rcc=rcd=rce='#e6e6e6' # #e6e6e6 and #FFA500 is color code for white and orange
    rcf=rcg=rch=rci=rcj=rck='#FFA500'
    #Configure the color for every button
    btnAllClear.configure(bg = rcc)
    btnEqual.configure(bg = rcc)
    btnBackspace.configure(bg = rcc)
    btn1.configure(bg = rca)
    btn2.configure(bg = rca)
    btn3.configure(bg = rca)
    btn4.configure(bg = rca)
    btn5.configure(bg = rca)
    btn6.configure(bg = rca)
    btn7.configure(bg = rca)
    btn8.configure(bg = rca)
    btn9.configure(bg = rca)
    btn0.configure(bg = rca)
    btnDP.configure(bg = rca)
    btnSqrt.configure(bg = rca)
    btnPlus.configure(bg = rcb)
    btnMinus.configure(bg = rcb)
    btnTime.configure(bg = rcb)
    btnDivide.configure(bg = rcb)
    btnDTime.configure(bg = rcb)
    btnDDivide.configure(bg = rcb)
    btnAns.configure(bg = rce)
    btnPi.configure(bg = rca)
    btnEE.configure(bg = rca)
    btnParenthesisLeft.configure(bg = rcd)    
    btnParenthesisRight.configure(bg = rcd)
    btnSin.configure(bg = rcd)
    btnCos.configure(bg = rcd)
    btnTan.configure(bg = rcd)
    btnE.configure(bg = rcd)

def G_Fancolor_on():
    global rca,rcb,rcc,rcd,rce,rcf,rcg,rch,rci,rcj,rck #Global value for color
    #Set the color 
    rca=rcb=rcc=rcd=rce='#e6e6e6' 
    rcf=randomcolor_f()
    rcg=randomcolor_g()
    rch=randomcolor_h()
    rci=randomcolor_i()
    rcj=randomcolor_j()
    rck=randomcolor_k()
    #Configure the color for every button
    btnAllClear.configure(bg = rcc)
    btnEqual.configure(bg = rcc)
    btnBackspace.configure(bg = rcc)
    btn1.configure(bg = rca)
    btn2.configure(bg = rca)
    btn3.configure(bg = rca)
    btn4.configure(bg = rca)
    btn5.configure(bg = rca)
    btn6.configure(bg = rca)
    btn7.configure(bg = rca)
    btn8.configure(bg = rca)
    btn9.configure(bg = rca)
    btn0.configure(bg = rca)
    btnDP.configure(bg = rca)
    btnSqrt.configure(bg = rca)
    btnPlus.configure(bg = rcb)
    btnMinus.configure(bg = rcb)
    btnTime.configure(bg = rcb)
    btnDivide.configure(bg = rcb)
    btnDTime.configure(bg = rcb)
    btnDDivide.configure(bg = rcb)
    btnAns.configure(bg = rce)
    btnPi.configure(bg = rca)
    btnEE.configure(bg = rca)
    btnParenthesisLeft.configure(bg = rcd)    
    btnParenthesisRight.configure(bg = rcd)
    btnSin.configure(bg = rcd)
    btnCos.configure(bg = rcd)
    btnTan.configure(bg = rcd)
    btnE.configure(bg = rcd)

#The color for button which will be set when user run the calculator
rca=randomcolor_a()
rcb=randomcolor_b()
rcc=randomcolor_c()
rcd=randomcolor_d()
rce=randomcolor_e()
rcf=randomcolor_f()
rcg=randomcolor_g()
rch=randomcolor_h()
rci=randomcolor_i()
rcj=randomcolor_j()
rck=randomcolor_k()
   
'''Label'''

#Add a entry to our window and set it to Read only

#This give a way for user to change the text in the entry
Var = tkinter.StringVar(Calculator,'')
#Create the entry
Entry = tkinter.Entry(Calculator,textvariable=Var)
#Set the entry to Read only
Entry['state'] = 'readonly'
#Place our entry
Entry.place(x=10, y=10, width=400, height=50)

#Give the certain number/operator a meaning
π = math.pi
sin = math.sin
cos = math.cos
tan = math.tan
e = math.e
    
'''Button'''
'''
for __name__ = '__main__':
    while True:
        for i in '0123456789+-*/':
            Calculator.bind(str(i),ButtonClick(str(i))
'''

def ButtonClick(btn): #btn stands for button
    global Calculate_Times
    global Calculate_Times_Save
    global Ans
    global π
    #Get the text in the Entry
    Content = Var.get()
    '''
    btn = sys.stdin.readline(1).strip()
    '''
    #Check the length of input
    for i in range(len(Content)+1):
        if i == 55:
            tkinter.messagebox.showerror('Error','You input too many numbers and/or operators')
            Content=Content[:len(Content)-len(Content)+55]
    #Check the times that user calculate if user did the calculate, then clean the entry
    if Calculate_Times>=1:
        Content=''
        Calculate_Times=0
    #If the user click on the decimal point button, add a ) before it
    if Content.startswith('.'):
        Content = '0'+Content   
    #If user click on normal number button
    if btn in '123456789':
        Calculate_Times_Save=0
        if Content.endswith('0'):
            try:
                Content_save = eval(str(Content)) #Calculate the result in the content
            except:
                Content = Content[:len(Content)-1] #If the calculation in the calculator can't get result take away last chapter
            if Content_save.startswith('-'):
                Content_save = Content[:0]
                return Content_save
            if int(Content_save) < 10:
                if '.' in Content:
                    Content += btn
                else:
                    Content = Content[:len(Content)-1]
                    Content += btn
            elif int(Content_save) >= 10:
                Content += btn
            '''
            Content=Content[:len(Content)-1]
            Content+=btn
            '''
        else:
            Content+=btn #add the number that user click to the content
    if btn == '0':
        Calculate_Times_Save=0
        if Content.endswith(Operators):#Check whelther the end of the content is operator or not
            return
        if Content.endswith('0'):
            try:
                Content_save = str(eval(str(Content)))
            except:
                Content = Content[:len(Content)-1]
            if Content_save.startswith('-'):
                Content_save = Content[:0]
                return Content_save
            if int(Content_save) < 10:
                if '.' in Content:
                    Content+= btn
                else:
                    Content = Content[:len(Content)-1]
                    Content += btn
            elif int(Content_save) >= 10:
                Content += btn
        else:
            Content+=btn
    #If user click ondecimal point
    elif btn == '.':
        Calculate_Times_Save=0
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
        Calculate_Times_Save=0
        Content=Content[:len(Content)-1]
    #If user click on button
    elif btn == '=':
        Content_save=0
        Calculate_Times_Save=0
        Calculate_Times=Calculate_Times+1
        Calculate_Times_Save=Calculate_Times_Save+1
        try: #Find the result in the content
            Content = str(eval(str(Content)))
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
        if Calculate_Times_Save!=0:
            Content+=Ans
        if Content.endswith(""):
            return
        Content+=btn
    elif btn == '-':
        if Content.endswith(Operators):
            tkinter.messagebox.showerror('Error','Continous operators not exist')
            return
        if Calculate_Times_Save!=0:
            Content+=Ans
        Content+=btn
    elif btn == '*':
        if Content.endswith(Operators):
            tkinter.messagebox.showerror('Error','Continous operators not exist')
            return
        if Calculate_Times_Save!=0:
            Content+=Ans
        Content+=btn
    elif btn == '/':
        if Content.endswith(Operators):
            tkinter.messagebox.showerror('Error','Continous operators not exist')
            return
        if Calculate_Times_Save!=0:
            Content+=Ans
        Content+=btn
    elif btn == '**':
        if Content.endswith(Operators):
            tkinter.messagebox.showerror('Error','Continous operators not exist')
            return
        if Calculate_Times_Save!=0:
            Content+=Ans
        Content+=btn
    elif btn == '//':
        if Content.endswith(Operators):
            tkinter.messagebox.showerror('Error','Continous operators not exist')
            return
        if Calculate_Times_Save!=0:
            Content+=Ans
        Content+=btn
    #if the user click on answer button
    elif btn == 'Ans':
        Calculate_Times_Save=0
        btn=Ans
        Content+=btn
    #If the user click on pi button
    elif btn == 'π':
        Calculate_Times_Save=0
        Content+=btn
    #If the user click on parenthsis
    elif btn == '(':
        Calculate_Times_Save=0
        if Content.endswith(Number):
            time = ('*')
            Content+=time
            Content+=btn
        else:
            Content+=btn
    elif btn == ')':
        Calculate_Times_Save=0
        Content+=btn
    #If the user click on square root
    elif btn == '√':
        Calculate_Times_Save=0
        b = Content.split('.')
        if all(map(lambda x:x.isdigit(),b)):
            Content = eval(Content)**0.5 #Square root the content
        else:
            tkinter.messagebox.showerror('Error','Expression is incorrect (If you want to use square root in the expression, try using **0.5)')
    #If the user click on sin/cos/tan
    elif btn == 'sin(':
        Calculate_Times_Save=0
        Content+=btn #Beacuse we give the sin a meaning, when we click on '=', 'math.sin' will exchange the sin in the equation
        '''
        c = Content.split('.')
        if all(map(lambda x:x.isdigit(),c)):
            Content = math.sin(math.radians(int(Content))) #Sin the content
        else:
            tkinter.messagebox.showerror('Error','Expression is incorrect')
        '''
    elif btn == 'cos(':
        Calculate_Times_Save=0
        Content+=btn #Same as sin, when we click on '=', 'math.cos' will exchange the cos in the equation 
        '''
        d = Content.split('.')
        if all(map(lambda x:x.isdigit(),d)):
            Content = math.cos(math.radians(int(Content))) #Cos the content
        else:
            tkinter.messagebox.showerror('Error','Expression is incorrect')
        '''
    elif btn == 'tan(':
        Calculate_Times_Save=0
        Content+=btn #Same as sin and cos, when we click on '=', 'math.tan' will exchange the cos in the equation 
        '''
        e = Content.split('.')
        if all(map(lambda x:x.isdigit(),e)):
            Content = math.tan(math.radians(int(Content))) #Tan the content
        else:
            tkinter.messagebox.showerror('Error','Expression is incorrect')
        '''
    #When you click on factorial number
    elif btn == '!':
        Calculate_Times_Save=0
        if Content == '':
            tkinter.messagebox.showerror('Error','Expression is empty')
        elif '.' in Content:
            tkinter.messagebox.showerror('Error','You can only have integer')
        else:
            c = int(Content)
            for i in range(int(Content),1,-1):
                c = c*(i-1)
                Content = str(c)
    elif btn == 'e':
        Content+=btn

    Var.set(Content)

'''Button interface'''

def test_enter(event = None):
    global color_list_binds
    for i in range (len(color_list_binds)):
        color_list_binds[i]['background']=rcf

def test_leave(event = None):
    global color_list_binds
    for i in range (len(color_list_binds)):     
        color_list_binds[i]['background']=rcb

#MouseOver
def EnterPlus(btn):
    btnPlus['background']=rcf
def LeavePlus(btn):
    btnPlus['background']=rcb

def EnterMinus(btn):
    btnMinus['background']=rcf
def LeaveMinus(btn):
    btnMinus['background']=rcb

def EnterTime(btn):
    btnTime['background']=rcf
def LeaveTime(btn):
    btnTime['background']=rcb

def EnterDivide(btn):
    btnDivide['background']=rcf
def LeaveDivide(btn):
    btnDivide['background']=rcb

def EnterDTime(btn):
    btnDTime['background']=rcf
def LeaveDTime(btn):
    btnDTime['background']=rcb

def EnterDDivide(btn):
    btnDDivide['background']=rcf   
def LeaveDDivide(btn):
    btnDDivide['background']=rcb

def EnterAns(btn):
    btnAns['background']=rcg   
def LeaveAns(btn):
    btnAns['background']=rce

def EnterPi(btn):
    btnPi['background']=rch   
def LeavePi(btn):
    btnPi['background']=rca

def EnterParenthesisLeft(btn):
    btnParenthesisLeft['background']=rci  
def LeaveParenthesisLeft(btn):
    btnParenthesisLeft['background']=rcd

def EnterParenthesisRight(btn):
    btnParenthesisRight['background']=rci  
def LeaveParenthesisRight(btn):
    btnParenthesisRight['background']=rcd

def EnterSin(btn):
    btnSin['background']=rci  
def LeaveSin(btn):
    btnSin['background']=rcd

def EnterCos(btn):
    btnCos['background']=rci  
def LeaveCos(btn):
    btnCos['background']=rcd

def EnterTan(btn):
    btnTan['background']=rci  
def LeaveTan(btn):
    btnTan['background']=rcd

def EnterE(btn):
    btnE['background']=rci  
def LeaveE(btn):
    btnE['background']=rcd

def EnterAllClear(btn):
    btnAllClear['background']=rcj  
def LeaveAllClear(btn):
    btnAllClear['background']=rcc

def EnterEqual(btn):
    btnEqual['background']=rcj  
def LeaveEqual(btn):
    btnEqual['background']=rcc

def EnterBackspace(btn):
    btnBackspace['background']=rcj
def LeaveBackspace(btn):
    btnBackspace['background']=rcc

def EnterDigit(btn):
    btnd['background']=rck  
def LeaveDigit(btn):
    btnd['background']=rca

def EnterEE(btn):
    btnEE['background']=rch   
def LeaveEE(btn):
    btnEE['background']=rca

def Enter1(btn):
    btn1['background']=rch   
def Leave1(btn):
    btn1['background']=rca

def Enter2(btn):
    btn2['background']=rch   
def Leave2(btn):
    btn2['background']=rca

def Enter3(btn):
    btn3['background']=rch   
def Leave3(btn):
    btn3['background']=rca
    
def Enter4(btn):
    btn4['background']=rch   
def Leave4(btn):
    btn4['background']=rca

def Enter5(btn):
    btn5['background']=rch   
def Leave5(btn):
    btn5['background']=rca

def Enter6(btn):
    btn6['background']=rch   
def Leave6(btn):
    btn6['background']=rca

def Enter7(btn):
    btn7['background']=rch   
def Leave7(btn):
    btn7['background']=rca

def Enter8(btn):
    btn8['background']=rch   
def Leave8(btn):
    btn8['background']=rca

def Enter9(btn):
    btn9['background']=rch   
def Leave9(btn):
    btn9['background']=rca

def Enter0(btn):
    btn0['background']=rch   
def Leave0(btn):
    btn0['background']=rca

def EnterDP(btn):
    btnDP['background']=rch   
def LeaveDP(btn):
    btnDP['background']=rca

def EnterSqrt(btn):
    btnSqrt['background']=rch   
def LeaveSqrt(btn):
    btnSqrt['background']=rca

# = ,AC and DEL
btnAllClear = tkinter.Button(Calculator,text='AC',command=lambda:ButtonClick('AC'),bg=rcc)
btnAllClear.place(x=10,y=65,width=100,height=50)
btnAllClear.bind('<Enter>',EnterAllClear)
btnAllClear.bind('<Leave>',LeaveAllClear)

btnEqual = tkinter.Button(Calculator,text='=',command=lambda:ButtonClick('='),bg=rcc)
btnEqual.place(x=310,y=365,width=100,height=50)
btnEqual.bind('<Enter>',EnterEqual)
btnEqual.bind('<Leave>',LeaveEqual)

btnBackspace = tkinter.Button(Calculator,text='DEL',command=lambda:ButtonClick('DEL'),bg=rcc)
btnBackspace.place(x=110,y=65,width=100,height=50)
btnBackspace.bind('<Enter>',EnterBackspace)
btnBackspace.bind('<Leave>',LeaveBackspace)

#digits or numbers and square root
'''
digits = list('1234567890.')+['√']
index = 0
for row in range(4):
    for col in range(3):
        global d
        d = digits[index]
        index += 1
        btnDigit=tkinter.Button(Calculator,text=d,command=lambda x=d:ButtonClick(x),bg=rca)
        btnDigit.place(x=10+col*100,y=115+row*50,width=100,height=50)
'''
Number = ('0','1','2','3','4','5','6','7','8','9')

btn1 = tkinter.Button(Calculator,text='1',command=lambda:ButtonClick('1'),bg=rca)
btn1.place(x=10,y=115,width=100,height=50)
btn1.bind('<Enter>',Enter1)
btn1.bind('<Leave>',Leave1)

btn2 = tkinter.Button(Calculator,text='2',command=lambda:ButtonClick('2'),bg=rca)
btn2.place(x=110,y=115,width=100,height=50)
btn2.bind('<Enter>',Enter2)
btn2.bind('<Leave>',Leave2)

btn3 = tkinter.Button(Calculator,text='3',command=lambda:ButtonClick('3'),bg=rca)
btn3.place(x=210,y=115,width=100,height=50)
btn3.bind('<Enter>',Enter3)
btn3.bind('<Leave>',Leave3)

btn4 = tkinter.Button(Calculator,text='4',command=lambda:ButtonClick('4'),bg=rca)
btn4.place(x=10,y=165,width=100,height=50)
btn4.bind('<Enter>',Enter4)
btn4.bind('<Leave>',Leave4)

btn5 = tkinter.Button(Calculator,text='5',command=lambda:ButtonClick('5'),bg=rca)
btn5.place(x=110,y=165,width=100,height=50)
btn5.bind('<Enter>',Enter5)
btn5.bind('<Leave>',Leave5)

btn6 = tkinter.Button(Calculator,text='6',command=lambda:ButtonClick('6'),bg=rca)
btn6.place(x=210,y=165,width=100,height=50)
btn6.bind('<Enter>',Enter6)
btn6.bind('<Leave>',Leave6)

btn7 = tkinter.Button(Calculator,text='7',command=lambda:ButtonClick('7'),bg=rca)
btn7.place(x=10,y=215,width=100,height=50)
btn7.bind('<Enter>',Enter7)
btn7.bind('<Leave>',Leave7)

btn8 = tkinter.Button(Calculator,text='8',command=lambda:ButtonClick('8'),bg=rca)
btn8.place(x=110,y=215,width=100,height=50)
btn8.bind('<Enter>',Enter8)
btn8.bind('<Leave>',Leave8)

btn9 = tkinter.Button(Calculator,text='9',command=lambda:ButtonClick('9'),bg=rca)
btn9.place(x=210,y=215,width=100,height=50)
btn9.bind('<Enter>',Enter9)
btn9.bind('<Leave>',Leave9)

btn0 = tkinter.Button(Calculator,text='0',command=lambda:ButtonClick('0'),bg=rca)
btn0.place(x=10,y=265,width=100,height=50)
btn0.bind('<Enter>',Enter0)
btn0.bind('<Leave>',Leave0)

btnDP = tkinter.Button(Calculator,text='.',command=lambda:ButtonClick('.'),bg=rca)
btnDP.place(x=110,y=265,width=100,height=50)
btnDP.bind('<Enter>',EnterDP)
btnDP.bind('<Leave>',LeaveDP)

btnSqrt = tkinter.Button(Calculator,text='√',command=lambda:ButtonClick('√'),bg=rca)
btnSqrt.place(x=210,y=265,width=100,height=50)
btnSqrt.bind('<Enter>',EnterSqrt)
btnSqrt.bind('<Leave>',LeaveSqrt)

#operators
Operators = ('+','-','*','/','**','//','sin(','cos(','tan(') #** is number to the power of number, // is take the divisible
btnPlus = tkinter.Button(Calculator,text='+',command=lambda:ButtonClick('+'),bg=rcb)
btnPlus.place(x=310,y=65,width=100,height=50)
btnPlus.bind('<Enter>',EnterPlus)
btnPlus.bind('<Leave>',LeavePlus)

btnMinus = tkinter.Button(Calculator,text='-',command=lambda:ButtonClick('-'),bg=rcb)
btnMinus.place(x=310,y=115,width=100,height=50)
btnMinus.bind('<Enter>',EnterMinus)
btnMinus.bind('<Leave>',LeaveMinus)

btnTime = tkinter.Button(Calculator,text='*',command=lambda:ButtonClick('*'),bg=rcb)
btnTime.place(x=310,y=165,width=100,height=50)
btnTime.bind('<Enter>',EnterTime)
btnTime.bind('<Leave>',LeaveTime)

btnDivide = tkinter.Button(Calculator,text='/',command=lambda x=Operators:ButtonClick('/'),bg=rcb)
btnDivide.place(x=310,y=215,width=100,height=50)
btnDivide.bind('<Enter>',EnterDivide)
btnDivide.bind('<Leave>',LeaveDivide)

btnDTime = tkinter.Button(Calculator,text='**',command=lambda:ButtonClick('**'),bg=rcb)
btnDTime.place(x=310,y=265,width=100,height=50)
btnDTime.bind('<Enter>',EnterDTime)
btnDTime.bind('<Leave>',LeaveDTime)

btnDDivide = tkinter.Button(Calculator,text='//',command=lambda x=Operators:ButtonClick('//'),bg=rcb)
btnDDivide.place(x=310,y=315,width=100,height=50)
btnDDivide.bind('<Enter>',EnterDDivide)
btnDDivide.bind('<Leave>',LeaveDDivide)

btnAns = tkinter.Button(Calculator,text='Ans',command=lambda:ButtonClick('Ans'),bg=rce)
btnAns.place(x=210,y=65,width=100,height=50)
btnAns['state'] = 'disable'
btnAns.bind('<Enter>',EnterAns)
btnAns.bind('<Leave>',LeaveAns)

btnPi = tkinter.Button(Calculator,text='π',command=lambda:ButtonClick('π'),bg=rca)
btnPi.place(x=210,y=315,width=100,height=50)
btnPi.bind('<Enter>',EnterPi)
btnPi.bind('<Leave>',LeavePi)

btnEE = tkinter.Button(Calculator,text='e',command=lambda:ButtonClick('e'),bg=rca)
btnEE.place(x=110,y=315,width=100,height=50)
btnEE.bind('<Enter>',EnterEE)
btnEE.bind('<Leave>',LeaveEE)

btnParenthesisLeft = tkinter.Button(Calculator,text='(',command=lambda:ButtonClick('(') ,bg=rcd)
btnParenthesisLeft.place(x=10,y=415,width=100,height=50)
btnParenthesisLeft.bind('<Enter>',EnterParenthesisLeft)
btnParenthesisLeft.bind('<Leave>',LeaveParenthesisLeft)

btnParenthesisRight = tkinter.Button(Calculator,text=')',command=lambda:ButtonClick(')'),bg=rcd)
btnParenthesisRight.place(x=110,y=415,width=100,height=50)
btnParenthesisRight.bind('<Enter>',EnterParenthesisRight)
btnParenthesisRight.bind('<Leave>',LeaveParenthesisRight)

btnSin = tkinter.Button(Calculator,text='Sin(Rad)',command=lambda:ButtonClick('sin('),bg=rcd)
btnSin.place(x=10,y=365,width=100,height=50)
btnSin.bind('<Enter>',EnterSin)
btnSin.bind('<Leave>',LeaveSin)

btnCos = tkinter.Button(Calculator,text='Cos(Rad)',command=lambda:ButtonClick('cos('),bg=rcd)
btnCos.place(x=110,y=365,width=100,height=50)
btnCos.bind('<Enter>',EnterCos)
btnCos.bind('<Leave>',LeaveCos)

btnTan = tkinter.Button(Calculator,text='Tan(Rad)',command=lambda:ButtonClick('tan('),bg=rcd)
btnTan.place(x=210,y=365,width=100,height=50)
btnTan.bind('<Enter>',EnterTan)
btnTan.bind('<Leave>',LeaveTan)

btnE = tkinter.Button(Calculator,text='!',command=lambda:ButtonClick('!'),bg=rcd)
btnE.place(x=10,y=315,width=100,height=50)
btnE.bind('<Enter>',EnterE)
btnE.bind('<Leave>',LeaveE)


Calculator.mainloop

