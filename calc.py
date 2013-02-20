from Tkinter import *
import math
import tkMessageBox
from random import randrange
#fn for frame creation
def frame(root, side): 
    w = Frame(root,relief=FLAT,bg="black")
    w.pack(side=side, expand=YES, fill=BOTH)
    return w
#fn for button creation
def button(root, side, text, command=None): 
    w = Button(root, text=text, command=command, width=4, height=3,bg="black",fg="white")
    w.pack(side=side, expand=YES, fill=BOTH)
    return w
def alert():
   tkMessageBox.showinfo("Credits", "Smjrifle ;)")

class Calculator(Frame):
	#pass paramerter to methods defined on an object
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'AERIAL 12 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Smjrifle Calculator')
        display = StringVar()
        quote = StringVar()
        msg1=["With the new day comes new strength and new thoughts","Dont complain just work harder","If you think you made it, your at the wrong place, never stop","The grass is greener where you water it","Life doesnt have to suc, DO something about it","You are never too old to set another goal or to dream a new dream","Act as if what you do makes a difference. It does","If you can dream it, you can do it","Always desire to learn something useful","If youve got a talent, protect it"]
        irand = randrange(0, 9)
        quote.set(msg1[irand])
        #set random quotes in calculator top, why? well doesn't hurt to be motivated everytime ;)
        Message( self, textvariable=quote, relief=SUNKEN, font=('times', 12),width=500,bg="black",fg="white").pack(side=TOP,expand=YES,fill=BOTH)
        #frame for trigonometric fn down left
        trig = frame(self,LEFT)
        #extra contents 
        extra = frame(self,RIGHT)
        #operators
        opsF = frame(self,RIGHT)
        Entry(self, relief=SUNKEN, textvariable=display).pack(side=TOP, expand=YES, fill=BOTH)
		#keys
        for key in ("123", "456", "789", "0."):
			keyF = frame(self, TOP)
			for char in key:	
				button(keyF, LEFT, char,
                       lambda w=display, c=char: w.set(w.get()+c))
        #backspace
        button(opsF, TOP, "<-",
                       lambda w=display, c=char: w.set(w.get()[:-1]))
        #extra
        button(extra, TOP, "sq",
                       lambda w=display, c=char: w.set(pow(float(w.get()),2))) 
        button(extra, TOP, "sqrt",
                       lambda w=display, c=char: w.set(math.sqrt(float(w.get()))))               
        button(extra, TOP, "e",
                       lambda w=display, c=char: w.set(math.exp(float(w.get()))))   
        button(extra, TOP, "log10",
                       lambda w=display, c=char: w.set(math.log10(float(w.get())))) 
                     #trig
        button(trig, TOP, "Sin",
                       lambda w=display, c=char: w.set(math.sin(math.radians(float(w.get())))))   
        button(trig, TOP, "Cos",
                       lambda w=display, c=char: w.set(math.cos(math.radians(float(w.get())))))   
        button(trig, TOP, "Tan",
                       lambda w=display, c=char: w.set(math.tan(math.radians(float(w.get())))))  
        button(trig, TOP, "n!",
                       lambda w=display, c=char: w.set(math.factorial(float(w.get()))))
        button(trig, TOP, "Credits",command=alert)
        button(extra, TOP, 'Clr', lambda w=display: w.set(''))
        #operators
        
        for char in "+-*/=":
            if char == '=':
                btn = button(keyF, LEFT, char)
                btn.bind('<ButtonRelease-1>',
                         lambda e, s=self, w=display: s.calc(w), '+')
            else:
                btn = button(opsF, TOP, char,
                   lambda w=display, s=' %s '%char: w.set(w.get()+s))

        clearF = frame(self, BOTTOM)
        
#fn to calculate answer
    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")

if __name__ == '__main__':
    Calculator().mainloop()
