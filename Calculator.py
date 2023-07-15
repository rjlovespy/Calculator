from tkinter import *
from numpy import * 
from scipy.special import *
import tkinter.messagebox as tmsg


"""  
1. event.widget["text/image"] function helps in retriving text/image from a widget
2. eval(<str>) is a bulit in function of python that evaluates <str> if 
   it is a mathematical expression scripted perfectly in python 3
"""
def click(event):
    global screenval
    text = event.widget["text"]
    
    if text == "+":
        operation["text"] = "Current Operation: Addition"
    if text == "-":
        operation["text"] = "Current Operation: Subtraction"
    elif text == "x":
        text = "*"
        operation["text"] = "Current Operation: Multiplication"
    elif text == "÷":
        text = "/"
        operation["text"] = "Current Operation: Division"
    elif text == "eˣ":
        text = "exp( )"
        operation["text"]="Current Operation: Exponentiation"
    elif text == "|x|":
        text = "abs( )"
        operation["text"]="Current Operation: Absolute Value or Modulus"
    elif text == "⌈x⌉":
        text = "ceil( )"
        operation["text"]="Current Operation: Integer Ceiling Function or Smallest Integer Function"
    elif text == "⌊x⌋":
        text = "floor( )"
        operation["text"]="Current Operation: Integer Floor Function or Greatest Integer Function"
    elif text == "log":
        text = "log10( )"
        operation["text"]="Current Operation: Common Logarithm"
    elif text == "ln":
        text = "log( )"
        operation["text"]="Current Operation: Natural Logarithm"
    elif text == "1/x":
        text = "1/( )"
        operation["text"]="Current Operation: Multiplicative Inverse or Reciprocal"
    elif text == "√x":
        text = "sqrt( )"
        operation["text"]="Current Operation: Square Root"
    elif text == "∛x":
        text = "cbrt( )"
        operation["text"]="Current Operation: Cube Root"
    elif text == "ⁿ√x":
        text = "( )**(1/( ))"
        operation["text"]="Current Operation: nth Root"
    elif text == "x²":
        text = "( )**2"
        operation["text"]="Current Operation: Square"
    elif text == "x³":
        text = "( )**3"
        operation["text"]="Current Operation: Cube"
    elif text == "xⁿ":
        text = "( )**( )"
        operation["text"]="Current Operation: Exponentiation"
    elif text=="n!":
        text = "factorial( )"
        operation["text"]="Current Operation: Factorial"
    elif text == "sin":
        if mode["text"]=="Current unit of angle: Radians":
            text = "sin( )"
        else:
            text = "sin(deg2rad( ))"
        operation["text"]="Current Operation: sine"
    elif text == "cos":
        if mode["text"]=="Current unit of angle: Radians":
            text = "cos( )"
        else:
            text = "cos(deg2rad( ))"
        operation["text"]="Current Operation: cosine"
    elif text == "tan":
        if mode["text"]=="Current unit of angle: Radians":
            text = "tan( )"
        else:
            text = "tan(deg2rad( ))"
        operation["text"]="Current Operation: tangent"
    elif text == "asin":
        if mode["text"]=="Current unit of angle: Radians":
            text = "arcsin( )"
        else:
            text = "rad2deg(arcsin( ))"
        operation["text"]="Current Operation: arcsine"
    elif text == "acos":
        if mode["text"]=="Current unit of angle: Radians":
            text = "arccos( )"
        else:
            text = "rad2deg(arccos( ))"
        operation["text"]="Current Operation: arccosine"
    elif text == "atan":
        if mode["text"]=="Current unit of angle: Radians":
            text = "arctan( )"
        else:
            text = "rad2deg(arctan( ))"
        operation["text"]="Current Operation: arctangent"
    else:
        pass
    
    if text == "=":
        try:
            if screenval.get().isdecimal():
                screenval.set(screenval.get())
            else:
                screenval.set(eval(screenval.get()))
            screen.update()
        except Exception:
            screenval.set("Invalid Input")
            screen.update()
    elif text == "C":
        screenval.set("")
        screen.update()
    elif text == "⎌":
        l = len(screenval.get())
        screenval.set(screenval.get()[:l-1])
        screen.update()
    elif ((text == "deg") and ((mode["text"]=="Current unit of angle: Radians") or (mode["text"]=="Current unit of angle: Degrees"))):
        mode["text"] = "Current unit of angle: Degrees"
    elif ((text == "rad") and ((mode["text"]=="Current unit of angle: Degrees") or (mode["text"]=="Current unit of angle: Radians"))):
        mode["text"] = "Current unit of angle: Radians"
    else:
        screenval.set(screenval.get()+text)
        screen.update()
    
            
def callArithmeticCalculator():
    global root, screenval, screen, b, operation
    root.destroy()
    
    root = Tk()
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    root.configure(background="#8F8FBC")
    root.overrideredirect(True)
    
    def openToggleMenu():
        f = Frame(root, bg="#8F8FBC", highlightbackground="white", highlightthickness=1)
        f.place(x=60, y=45, width=200, height=140)
        def closeToggleMenu():
            f.destroy() 
        Button(f, text="X",command= closeToggleMenu, bg="crimson", font="lucida 12 bold", width=4, bd=3, relief=RAISED).grid(row=0, column=0, sticky=W, ipady=5)
        Button(f, text= "Arithemtic Calculator", command=callArithmeticCalculator, bg="#8F8FBC", font="lucida 12 bold", relief=FLAT).grid(row=1, column=0, sticky=W, ipady=5)
        Button(f, text= "Scientific Calculator", command=callScientificCalculator, bg="#8F8FBC", font="lucida 12 bold", relief=FLAT).grid(row=2, column=0, sticky=W, ipady=5)
    
    def giveHelp():
        fo = open("E:\\GUI Development\\News\\Calculator_help.txt","r")
        tmsg.showinfo(title="Instructions", message=f"{fo.read()}")
        
    def tellAbout():
        fo = open("E:\\GUI Development\\News\\Calculator_about.txt","r")
        tmsg.showinfo(title="Details", message=f"{fo.read()}")
        
    def Exit():
        root.destroy()
        
    # Titlebar and Menubar
    f0 = Frame(root, bg="#8F8FBC", highlightbackground="white", highlightthickness=1)
    f0.pack(fill=X)
    calculator = PhotoImage(file="E:\\GUI Development\\News\\Calculator.png")
    Label(f0, image=calculator, bg="#8F8FBC").pack(side=LEFT, padx=15, pady=5)
    Button(f0, text= "Category", command=openToggleMenu,  bg="#8F8FBC", font="lucida 12 bold", relief=FLAT).pack(side=LEFT, pady=5)
    Button(f0, text= "Help", command=giveHelp,  bg="#8F8FBC", font="lucida 12 bold", relief=FLAT).pack(side=LEFT, padx=15, pady=5)
    Button(f0, text= "About", command=tellAbout,  bg="#8F8FBC", font="lucida 12 bold", relief=FLAT).pack(side=LEFT, pady=5)
    Label(f0, text= "Calculator [Version 0.1]", bg="#8F8FBC", font="lucida 12 bold").pack(side=LEFT, padx=410, pady=5)
    Button(f0, text="x", command=Exit, bg="crimson", font="lucida 12 bold", width=4, bd=3, relief=SUNKEN).pack(side=RIGHT, padx=15, pady=5)
    
    # Display Screen of Arithmetic Calculator
    f1 = Frame(root, bg="#8F8FBC")
    f1.pack(fill=X, padx=105, pady=50)
    screenval = StringVar()
    screenval.set("")
    screen = Entry(f1, textvariable=screenval, font="lucida 50 bold", bg="#FFFFD3", relief=FLAT)
    screen.pack(fill=X, ipady=25)

    # Buttons of Arithmetic Calculator
    f2 = Frame(root, bg="#8F8FBC")
    f2.pack(fill=X, padx=80, pady=25)
    character = [["(",")","⎌","C"],["7","8","9","÷"],["4","5","6","x"],["1","2","3","-"],[".","0","=","+"]]
    for i in range(5):
        for j in range(4):
            if ((i==0) and (j==2)) or ((i==0) and (j==3)):
                b = Button(f2, text=character[i][j], bg="crimson", font="lucida 30 bold",width=11, height=1, bd=5, relief=SUNKEN)
                b.grid(row=i, column=j, padx=30, pady=5)      
                b.bind("<Button-1>",click)   
            else:
                b = Button(f2, text=character[i][j], bg="lime", font="lucida 30 bold",width=11, height=1, bd=5, relief=SUNKEN)
                b.grid(row=i, column=j, padx=30, pady=5)      
                b.bind("<Button-1>",click)              
                
    # Statusbar of Arithmetic Calculator  
    f3 = Frame(root, bg="#8F8FBC", highlightbackground="white", highlightthickness=1)
    f3.pack(fill=X, side=BOTTOM)
    Label(f3,text="Arithmetic Calculator", font="lucida 12 bold", bg="#8F8FBC").grid(row=0, column=0, padx=15, ipady=5) 
    operation = Label(f3,text="Current Operation: None", font="lucida 12 bold", bg="#8F8FBC")
    operation.grid(row=0, column=2, padx=15, ipady=5)
    root.mainloop()

    
def callScientificCalculator():
    global root, screenval, screen, b, mode, operation
    root.destroy()    
    
    root = Tk()
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    root.configure(background="#8F8FBC")
    root.overrideredirect(True)
    
    def openToggleMenu():
        f = Frame(root, bg="#8F8FBC", highlightbackground="white", highlightthickness=1)
        f.place(x=60, y=45, width=200, height=140)
        def closeToggleMenu():
            f.destroy() 
        Button(f, text="X",command= closeToggleMenu, bg="crimson", font="lucida 12 bold", width=4, bd=3, relief=RAISED).grid(row=0, column=0, sticky=W, ipady=5)
        Button(f, text= "Arithemtic Calculator", command=callArithmeticCalculator, bg="#8F8FBC", font="lucida 12 bold", relief=FLAT).grid(row=1, column=0, sticky=W, ipady=5)
        Button(f, text= "Scientific Calculator", command=callScientificCalculator, bg="#8F8FBC", font="lucida 12 bold", relief=FLAT).grid(row=2, column=0, sticky=W, ipady=5)
    
    def giveHelp():
        fo = open("E:\\GUI Development\\News\\Calculator_help.txt","r")
        tmsg.showinfo(title="Instructions", message=f"{fo.read()}")
        
    def tellAbout():
        fo = open("E:\\GUI Development\\News\\Calculator_about.txt","r")
        tmsg.showinfo(title="Details", message=f"{fo.read()}")
    
    def Exit():
        root.destroy()
           
    # Titlebar and Menubar
    f0 = Frame(root, bg="#8F8FBC", highlightbackground="white", highlightthickness=1)
    f0.pack(fill=X)
    calculator = PhotoImage(file="E:\\GUI Development\\News\\Calculator.png")
    Label(f0, image=calculator, bg="#8F8FBC").pack(side=LEFT, padx=15, pady=5)
    Button(f0, text= "Category", command=openToggleMenu,  bg="#8F8FBC", font="lucida 12 bold", relief=FLAT).pack(side=LEFT, pady=5)
    Button(f0, text= "Help", command=giveHelp,  bg="#8F8FBC", font="lucida 12 bold", relief=FLAT).pack(side=LEFT, padx=15, pady=5)
    Button(f0, text= "About", command=tellAbout,  bg="#8F8FBC", font="lucida 12 bold", relief=FLAT).pack(side=LEFT, pady=5)
    Label(f0, text= "Calculator [Version 0.1]", bg="#8F8FBC", font="lucida 12 bold").pack(side=LEFT, padx=410, pady=5)
    Button(f0, text="x", command=Exit, bg="crimson", font="lucida 12 bold", width=4, bd=3, relief=SUNKEN).pack(side=RIGHT, padx=15, pady=5)
    
    # Display Screen of Scientific Calculator
    f1 = Frame(root, bg="#8F8FBC")
    f1.pack(fill=X, padx=80, pady=20)
    screenval = StringVar()
    screenval.set("")
    screen = Entry(f1, textvariable=screenval, font="lucida 50 bold", bg="#FFFFD3", relief=FLAT) 
    screen.pack(fill=X, ipady=25)             

    # Buttons of Scientific Calculator
    f2 = Frame(root, bg="#8F8FBC")
    f2.pack(fill=X, padx=75, pady=10)
    character = [["(",")","deg","rad","|x|","⎌","C"],["n!","1/x","log","ln","⌈x⌉","⌊x⌋","÷"],
                ["√x","∛x","ⁿ√x","7","8","9","x"],["x²","x³","xⁿ","4","5","6","-"],
                ["sin","cos","tan","1","2","3","+"],["asin","acos","atan","eˣ","0",".","="]]
    for i in range(6):
        for j in range(7):
            if ((i==0) and (j==5)) or ((i==0) and (j==6)):
                b = Button(f2, text=character[i][j], bg="crimson", font="lucida 30 bold",width=7, height=1, bd=5, relief=SUNKEN)
                b.grid(row=i, column=j, padx=7, pady=5)      
                b.bind("<Button-1>",click)
            else:
                b = Button(f2, text=character[i][j], bg="lime", font="lucida 30 bold",width=7, height=1, bd=5, relief=SUNKEN)
                b.grid(row=i, column=j, padx=7, pady=5)      
                b.bind("<Button-1>",click) 
              
    # Statusbar of Scientific Calculator
    f3 = Frame(root, bg="#8F8FBC", highlightbackground="white", highlightthickness=1)
    f3.pack(fill=X, side=BOTTOM)
    Label(f3,text="Scientific Calculator", font="lucida 12 bold", bg="#8F8FBC").grid(row=0, column=0, padx=15, ipady=5)
    mode = Label(f3,text="Current unit of angle: Radians", font="lucida 12 bold", bg="#8F8FBC")
    mode.grid(row=0, column=1, padx=15, ipady=5)
    operation = Label(f3,text="Current Operation: None", font="lucida 12 bold", bg="#8F8FBC")
    operation.grid(row=0, column=2, padx=15, ipady=5)
    root.mainloop()
 
 
root = Tk()
callArithmeticCalculator()