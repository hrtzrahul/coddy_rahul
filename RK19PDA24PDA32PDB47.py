from tkinter import *
import tkinter.messagebox
import math
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator")
root.geometry("650x400+300+300")



switch = None

# Button on press

# button "1" :- to enter 1
def btn1_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '1')


# button "2" :- to enter 2
def btn2_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '2')


# button "3" :- to enter 3
def btn3_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '3')


# button "4" :- to enter 4
def btn4_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '4')


# button "5" :- to enter 5
def btn5_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '5')


# button "6" :- to enter 6
def btn6_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '6')


# button "7" :- to enter 7
def btn7_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '7')


# button "8" :- to enter 8
def btn8_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '8')


# button "9" :- to enter 9
def btn9_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '9')

# button "0" :- to enter 0
def btn0_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '0')


# function for entering the numeric characters and point(.)
def key_event(*args):
    if disp.get() == '0':
        disp.delete(0, END)


# button "+" :- to perform add operation
def btnp_clicked():
    pos = len(disp.get())
    disp.insert(pos, '+')


# button "-" :- to perform subtraction operation
def btnm_clicked():
    pos = len(disp.get())
    disp.insert(pos, '-')


# button "*" :- to perform multiplication operation
def btnml_clicked():
    pos = len(disp.get())
    disp.insert(pos, '*')


# button "/" :- to perform division operation
def btnd_clicked():
    pos = len(disp.get())
    disp.insert(pos, '/')


# button "C" :- to clean the screen
def btnc_clicked(*args):
    disp.delete(0, END)
    disp.insert(0, '0')


# button "sin" :- to perform sin() function on the entered number
def sin_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.sin(math.radians(ans))
        else:
            ans = math.sin(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


# button "cos" :- to perform cos() function on the entered number
def cos_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.cos(math.radians(ans))
        else:
            ans = math.cos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


# button "tan" :- to perform tan() function on the entered number
def tan_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.tan(math.radians(ans))
        else:
            ans = math.tan(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


# button "sin-1" :- to perform asin() function on the entered number
def arcsin_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.asin(ans))
        else:
            ans = math.asin(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


# button "cos-1" :- to perform acos() function on the entered number
def arccos_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.acos(ans))
        else:
            ans = math.acos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


# button "tan-1" :- to perform atan() function on the entered number
def arctan_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.atan(ans))
        else:
            ans = math.atan(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


# button "x^y" :- to perform y times x operation on the entered number x(say)
def pow_clicked():
    pos = len(disp.get())
    disp.insert(pos, '**')


# button "round" :- to roundoff the entered number
def round_clicked():
    try:
        ans = float(disp.get())
        ans = round(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


# button "log" :- to perform log() function on the entered number
def logarithm_clicked():
    try:
        ans = float(disp.get())
        ans = math.log10(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

# button "x!" :- to perform factorial operation on the entered number x(say)
def fact_clicked():
    try:
        ans = float(disp.get())
        ans = math.factorial(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


# button "√x" :- to perform sqare root operation on the entered number x(say)
def sqr_clicked():
    try:
        ans = float(disp.get())
        ans = math.sqrt(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


# button "dot(.)" :- to enter point(.)
def dot_clicked():
    pos = len(disp.get())
    disp.insert(pos, '.')


# button "π(pi)" :- to enter pi(π)
def pi_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.pi))


# button "e" :- to enter the value of "e=2.718281828459045"
def e_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.e))


# button "(" :- to enter "("
def bl_clicked():
    pos = len(disp.get())
    disp.insert(pos, '(')


# button ")" :- to enter ")"
def br_clicked():
    pos = len(disp.get())
    disp.insert(pos, ')')


# button "⌫" :- to delete the last entered character
def del_clicked():
    pos = len(disp.get())
    display = str(disp.get())
    if display == '':
        disp.insert(0, '0')
    elif display == ' ':
        disp.insert(0, '0')
    elif display == '0':
        pass
    else:
        disp.delete(0, END)
        disp.insert(0, display[0:pos-1])


# button "rad/deg" :- to convert from radians to degree and vice-versa
def conv_clicked():
    global switch
    if switch is None:
        switch = True
        conv_btn['text'] = "Deg"
        ans = float(disp.get())
        ans = math.radians(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))

    else:
        switch = None
        conv_btn['text'] = "Rad"
        ans = float(disp.get())
        ans = math.degrees(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))


# button "ln" :- to perform ln operation on the entered number
def ln_clicked():
    try:
        ans = float(disp.get())
        ans = math.log(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


# button "%" :- to get the remainder (x%y)
def mod_clicked():
    pos = len(disp.get())
    disp.insert(pos, '%')


# button "=" :- to get the output of the performed operation
def btneq_clicked(*args):
    try:
        ans = disp.get()
        ans = eval(ans)
        disp.delete(0, END)
        disp.insert(0, ans)

    except:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


# Label

data = StringVar()

disp = Entry(root, font="Times 20", fg="#43FFF6", bg="black", bd=0, justify=RIGHT, insertbackground="#abbab1", cursor="arrow")
disp.bind("<Return>", btneq_clicked)
disp.bind("<Escape>", btnc_clicked)
disp.bind("<Key-1>", key_event)
disp.bind("<Key-2>", key_event)
disp.bind("<Key-3>", key_event)
disp.bind("<Key-4>", key_event)
disp.bind("<Key-5>", key_event)
disp.bind("<Key-6>", key_event)
disp.bind("<Key-7>", key_event)
disp.bind("<Key-8>", key_event)
disp.bind("<Key-9>", key_event)
disp.bind("<Key-0>", key_event)
disp.bind("<Key-.>", key_event)
disp.insert(0, '0')
disp.focus_set()
disp.pack(expand=TRUE, fill=BOTH)

# Row 1 Buttons

btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=TRUE, fill=BOTH)

pi_btn = Button(btnrow1, text="π", font="Times 18", relief=GROOVE, bd=0, command=pi_clicked, fg="#43FFF6", bg="black")
pi_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

fact_btn = Button(btnrow1, text=" x! ", font="Times 18", relief=GROOVE, bd=0, command=fact_clicked, fg="#43FFF6", bg="black")
fact_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sin_btn = Button(btnrow1, text="sin", font="Times 18", relief=GROOVE, bd=0, command=sin_clicked, fg="#43FFF6", bg="black")
sin_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

cos_btn = Button(btnrow1, text="cos", font="Times 18", relief=GROOVE, bd=0, command=cos_clicked, fg="#43FFF6", bg="black")
cos_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

tan_btn = Button(btnrow1, text="tan", font="Times 18", relief=GROOVE, bd=0, command=tan_clicked, fg="#43FFF6", bg="black")
tan_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn1 = Button(btnrow1, text="1", font="Times 23", relief=GROOVE, bd=0, command=btn1_clicked, fg="#43FFF6", bg="black")
btn1.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn2 = Button(btnrow1, text="2", font="Times 23", relief=GROOVE, bd=0,  command=btn2_clicked, fg="#43FFF6", bg="black")
btn2.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn3 = Button(btnrow1, text="3", font="Times 23", relief=GROOVE, bd=0, command=btn3_clicked, fg="#43FFF6", bg="black")
btn3.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnp = Button(btnrow1, text="+", font="Times 23", relief=GROOVE, bd=0, command=btnp_clicked, fg="#43FFF6", bg="black")
btnp.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 2 Buttons

btnrow2 = Frame(root)
btnrow2.pack(expand=TRUE, fill=BOTH)

e_btn = Button(btnrow2, text="e", font="Times 18", relief=GROOVE, bd=0, command=e_clicked, fg="#43FFF6", bg="black")
e_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sqr_btn = Button(btnrow2, text=" √x ", font="Times 18", relief=GROOVE, bd=0, command=sqr_clicked, fg="#43FFF6", bg="black")
sqr_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sinh_btn = Button(btnrow2, text="sin−1", font="Times 11 bold", relief=GROOVE, bd=0, command=arcsin_clicked, fg="#43FFF6", bg="black")
sinh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

cosh_btn = Button(btnrow2, text="cos-1", font="Times 11 bold", relief=GROOVE, bd=0, command=arccos_clicked, fg="#43FFF6", bg="black")
cosh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

tanh_btn = Button(btnrow2, text="tan-1", font="Times 11 bold", relief=GROOVE, bd=0, command=arctan_clicked, fg="#43FFF6", bg="black")
tanh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn4 = Button(btnrow2, text="4", font="Times 23", relief=GROOVE, bd=0, command=btn4_clicked, fg="#43FFF6", bg="black")
btn4.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn5 = Button(btnrow2, text="5", font="Times 23", relief=GROOVE, bd=0, command=btn5_clicked, fg="#43FFF6", bg="black")
btn5.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn6 = Button(btnrow2, text="6", font="Times 23", relief=GROOVE, bd=0, command=btn6_clicked, fg="#43FFF6", bg="black")
btn6.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnm = Button(btnrow2, text="-", font="Times 23", relief=GROOVE, bd=0, command=btnm_clicked, fg="#43FFF6", bg="black")
btnm.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 3 Buttons

btnrow3 = Frame(root)
btnrow3.pack(expand=TRUE, fill=BOTH)

conv_btn = Button(btnrow3, text="Rad", font="Times 12 bold", relief=GROOVE, bd=0, command=conv_clicked, fg="#43FFF6", bg="black")
conv_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

round_btn = Button(btnrow3, text="round", font="Times 10 bold", relief=GROOVE, bd=0, command=round_clicked, fg="#43FFF6", bg="black")
round_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

ln_btn = Button(btnrow3, text="ln", font="Times 18", relief=GROOVE, bd=0, command=ln_clicked, fg="#43FFF6", bg="black")
ln_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

logarithm_btn = Button(btnrow3, text="log", font="Times 17", relief=GROOVE, bd=0, command=logarithm_clicked, fg="#43FFF6", bg="black")
logarithm_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

pow_btn = Button(btnrow3, text="x^y", font="Times 17", relief=GROOVE, bd=0, command=pow_clicked, fg="#43FFF6", bg="black")
pow_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn7 = Button(btnrow3, text="7", font="Times 23", relief=GROOVE, bd=0, command=btn7_clicked, fg="#43FFF6", bg="black")
btn7.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn8 = Button(btnrow3, text="8", font="Times 23", relief=GROOVE, bd=0, command=btn8_clicked, fg="#43FFF6", bg="black")
btn8.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn9 = Button(btnrow3, text="9", font="Times 23", relief=GROOVE, bd=0, command=btn9_clicked, fg="#43FFF6", bg="black")
btn9.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnml = Button(btnrow3, text="*", font="Times 23", relief=GROOVE, bd=0, command=btnml_clicked, fg="#43FFF6", bg="black")
btnml.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 4 Buttons

btnrow4 = Frame(root)
btnrow4.pack(expand=TRUE, fill=BOTH)

mod_btn = Button(btnrow4, text="%", font="Times 21", relief=GROOVE, bd=0, command=mod_clicked, fg="#43FFF6", bg="black")
mod_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

bl_btn = Button(btnrow4, text=" ( ", font="Times 21", relief=GROOVE, bd=0, command=bl_clicked, fg="#43FFF6", bg="black")
bl_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

br_btn = Button(btnrow4, text=" ) ", font="Times 21", relief=GROOVE, bd=0, command=br_clicked, fg="#43FFF6", bg="black")
br_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

dot_btn = Button(btnrow4, text=" • ", font="Times 21", relief=GROOVE, bd=0, command=dot_clicked, fg="#43FFF6", bg="black")
dot_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnc = Button(btnrow4, text="C", font="Times 23", relief=GROOVE, bd=0, command=btnc_clicked, fg="#43FFF6", bg="black")
btnc.pack(side=LEFT, expand=TRUE, fill=BOTH)

del_btn = Button(btnrow4, text="⌫", font="Times 20", relief=GROOVE, bd=0, command=del_clicked, fg="#43FFF6", bg="black")
del_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn0 = Button(btnrow4, text="0", font="Times 23", relief=GROOVE, bd=0, command=btn0_clicked, fg="#43FFF6", bg="black")
btn0.pack(side=LEFT, expand=TRUE, fill=BOTH)

btneq = Button(btnrow4, text="=", font="Times 23", relief=GROOVE, bd=0, command=btneq_clicked, fg="#43FFF6", bg="black")
btneq.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnd = Button(btnrow4, text="/", font="Times 23", relief=GROOVE, bd=0, command=btnd_clicked, fg="#43FFF6", bg="black")
btnd.pack(side=LEFT, expand=TRUE, fill=BOTH)


root.mainloop()