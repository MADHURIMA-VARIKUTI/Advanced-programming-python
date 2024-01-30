from tkinter import *

calc = Tk()
calc.geometry("400x420")
calc.title("Calculator")
calcLabel = Label(calc, text="Calculator", bg='grey',font=("times new roman", 30, 'bold'))
calcLabel.pack(side=TOP)
calc.config(background='grey')

textin = StringVar()
operator = ""


def clickbut(number):  # lambda:clickbut(1)
    global operator
    operator = operator+str(number)
    textin.set(operator)


def equlbut():
    global operator
    add = str(eval(operator))
    textin.set(add)
    operator = ''


def clrbut():
    textin.set('')


metext = Entry(calc, font=("times new roman", 20, 'bold'),
               textvar=textin, width=60, bd=10, bg='light blue')
metext.pack()

but1 = Button(calc, bg='white', font =("times new roman", 20, 'bold'), command=lambda: clickbut(1), text="1")
but1.place(x=15, y=120)

but2 = Button(calc, bg='white', font =("times new roman", 20, 'bold'), command=lambda: clickbut(2), text="2")
but2.place(x=15, y=190)

but3 = Button(calc, bg='white', font =("times new roman", 20, 'bold'), command=lambda: clickbut(3), text="3")
but3.place(x=15, y=260)

but4 = Button(calc, bg='white', font =("times new roman", 20, 'bold'), command=lambda: clickbut(4), text="4")
but4.place(x=80, y=120)

but5 = Button(calc, bg='white', font =("times new roman", 20, 'bold'), command=lambda: clickbut(5), text="5")
but5.place(x=80, y=190)

but6 = Button(calc, bg='white', font =("times new roman", 20, 'bold'), command=lambda: clickbut(6), text="6")
but6.place(x=80, y=260)

but7 = Button(calc, bg='white', font =("times new roman", 20, 'bold'), command=lambda: clickbut(7), text="7")
but7.place(x=145, y=120)

but8 = Button(calc, bg='white', font =("times new roman", 20, 'bold'), command=lambda: clickbut(8), text="8")
but8.place(x=145, y=190)

but9 = Button(calc, bg='white', font =("times new roman", 20, 'bold'), command=lambda: clickbut(9), text="9")
but9.place(x=145, y=260)

but0 = Button(calc, bg='white', font =("times new roman", 20, 'bold'), command=lambda: clickbut(0), text="0")
but0.place(x=15, y=330)

butdot = Button(calc, bg='white', font =("times new roman", 20, 'bold'), command=lambda: clickbut("."), text=".")
butdot.place(x=85, y=330)

butpl = Button(calc, bg='white', text="+", font =("times new roman", 20, 'bold'), command=lambda: clickbut("+"))
butpl.place(x=210, y=120)

butsub = Button(calc, bg='white', text="-", font =("times new roman", 20, 'bold'), command=lambda: clickbut("-"))
butsub.place(x=210, y=190)

butml = Button(calc, bg='white', text="*", font =("times new roman", 20, 'bold'), command=lambda: clickbut("*"))
butml.place(x=210, y=260)

butdiv = Button(calc, bg='white', text="/", font =("times new roman", 20, 'bold'), command=lambda: clickbut("/"))
butdiv.place(x=210, y=330)

butmod = Button(calc, bg='white', font =("times new roman", 20, 'bold'), command=lambda: clickbut("%"), text="%")
butmod.place(x=145, y=330)

butclear = Button(calc, bg='yellow', font =("times new roman", 20, 'bold'), text="CE", command=clrbut)
butclear.place(x=275, y=120)

butequal = Button(calc, bg='yellow', font =("times new roman", 20, 'bold'), command=equlbut, text="=")
butequal.place(x=275, y=220)
calc.mainloop()