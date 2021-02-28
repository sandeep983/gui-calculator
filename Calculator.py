from tkinter import Tk, PhotoImage, Button, Entry, END, TRUE, BOTH, Frame, GROOVE, LEFT
import tkinter.messagebox



#gui
ui = Tk()
ui.iconbitmap(True, "cal3.ico")
ui.title("Calculator")
ui.geometry("329x320+500+125")
                                    


#when the button is pressed
def btn1():
    if disp.get() == "0":
        disp.delete(0, END)
    current = len(disp.get())
    disp.insert(current, '1')

def btn2():
    if disp.get() == "0":
        disp.delete(0, END)
    current = len(disp.get())
    disp.insert(current, '2')

def btn3():
    if disp.get() == "0":
        disp.delete(0, END)
    current = len(disp.get())
    disp.insert(current, '3')

def btn4():
    if disp.get() == "0":
        disp.delete(0, END)
    current = len(disp.get())
    disp.insert(current, '4')

def btn5():
    if disp.get() == "0":
        disp.delete(0, END)
    current = len(disp.get())
    disp.insert(current, '5')

def btn6():
    if disp.get() == "0":
        disp.delete(0, END)
    current = len(disp.get())
    disp.insert(current, '6')

def btn7():
    if disp.get() == "0":
        disp.delete(0, END)
    current = len(disp.get())
    disp.insert(current, '7')

def btn8():
    if disp.get() == "0":
        disp.delete(0, END)
    current = len(disp.get())
    disp.insert(current, '8')

def btn9():
    if disp.get() == "0":
        disp.delete(0, END)
    current = len(disp.get())
    disp.insert(current, '9')

def btn0():
    if disp.get() == "0":
        disp.delete(0, END)
    current = len(disp.get())
    disp.insert(current, '0')

def key_event(*args):
    if disp.get() == "0":
        disp.delete(0, END)

def btn_plus():
    current = len(disp.get())
    disp.insert(current, "+")


def btn_minus():
    current = len(disp.get())
    disp.insert(current, "-")

def btn_multi():
    current = len(disp.get())
    disp.insert(current, "*")

def btn_divide():
    current = len(disp.get())
    disp.insert(current, "/")

def btn_dot():
    current = len(disp.get())
    disp.insert(current, ".")

def btn_clear(*args):
    disp.delete(0, END)
    disp.insert(0, "0")

def btn_delete():
    current = len(disp.get())
    display = str(disp.get())
    if display == '':
        disp.insert(0, '0')
    elif display == ' ':
        disp.insert(0, '0')
    elif display == '0':
        pass
    else:
        disp.delete(0, END)
        disp.insert(0, display[0:current-1])

def btn_equal(*args):
    try:
        ans = disp.get()
        ans = eval(ans)
        disp.delete(0, END)
        disp.insert(0, ans)
    except:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")



#display screen
disp = Entry(ui, font="Verdana 28", fg="black", bg="#abbab1", bd="0", justify="right", cursor="arrow")
disp.bind("<Return>", btn_equal)
disp.bind("<Escape>", btn_clear)
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



#buttons of Row 1
btnrow1 = Frame(ui, bg="#000000")
btnrow1.pack(expand=TRUE, fill=BOTH)

btn1 = Button(btnrow1, text="1", font="Segoe 20", relief=GROOVE, bd=0, command=btn1, fg="white", bg="#333333")
btn1.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn2 = Button(btnrow1, text="2", font="Segoe 20", relief=GROOVE, bd=0,  command=btn2, fg="white", bg="#333333")
btn2.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn3 = Button(btnrow1, text="3", font="Segoe 20", relief=GROOVE, bd=0, command=btn3, fg="white", bg="#333333")
btn3.pack(side=LEFT, expand=TRUE, fill=BOTH)

btndivide = Button(btnrow1, text="/", font="Segoe 20", relief=GROOVE, bd=0, command=btn_divide, fg="white", bg="#333333")
btndivide.pack(side=LEFT, expand=TRUE, fill=BOTH)



#buttons of Row 2
btnrow2 = Frame(ui)
btnrow2.pack(expand=TRUE, fill=BOTH)

btn4 = Button(btnrow2, text="4", font="Segoe 20", relief=GROOVE, bd=0, command=btn4, fg="white", bg="#333333")
btn4.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn5 = Button(btnrow2, text="5", font="Segoe 20", relief=GROOVE, bd=0, command=btn5, fg="white", bg="#333333")
btn5.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn6 = Button(btnrow2, text="6", font="Segoe 20", relief=GROOVE, bd=0, command=btn6, fg="white", bg="#333333")
btn6.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnmulti = Button(btnrow2, text="×", font="Segoe 20", relief=GROOVE, bd=0, command=btn_multi, fg="white", bg="#333333")
btnmulti.pack(side=LEFT, expand=TRUE, fill=BOTH)



#buttons of Row 3
btnrow3 = Frame(ui)
btnrow3.pack(expand=TRUE, fill=BOTH)

btn7 = Button(btnrow3, text="7", font="Segoe 20", relief=GROOVE, bd=0, command=btn7, fg="white", bg="#333333")
btn7.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn8 = Button(btnrow3, text="8", font="Segoe 20", relief=GROOVE, bd=0, command=btn8, fg="white", bg="#333333")
btn8.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn9 = Button(btnrow3, text="9", font="Segoe 20", relief=GROOVE, bd=0, command=btn9, fg="white", bg="#333333")
btn9.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnminus = Button(btnrow3, text="−", font="Segoe 20", relief=GROOVE, bd=0, command=btn_minus, fg="white", bg="#333333")
btnminus.pack(side=LEFT, expand=TRUE, fill=BOTH)



#buttons of Row 4
btnrow4 = Frame(ui)
btnrow4.pack(expand=TRUE, fill=BOTH)

btnclear = Button(btnrow4, text="C", font="Segoe 20", relief=GROOVE, bd=0, command=btn_clear, fg="white", bg="#333333")
btnclear.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn0 = Button(btnrow4, text="0", font="Segoe 20", relief=GROOVE, bd=0, command=btn0, fg="white", bg="#333333")
btn0.pack(side=LEFT, expand=TRUE, fill=BOTH)

btndot = Button(btnrow4, text="•", font="Segoe 20", relief=GROOVE, bd=0, command=btn_dot, fg="white", bg="#333333")
btndot.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnplus = Button(btnrow4, text="+", font="Segoe 20", relief=GROOVE, bd=0, command=btn_plus, fg="white", bg="#333333")
btnplus.pack(side=LEFT, expand=TRUE, fill=BOTH)



#buttons of Row 5
btnrow5 = Frame(ui)
btnrow5.pack(expand=TRUE, fill=BOTH)

btndelete = Button(btnrow5, text="del", font="Segoe 20", relief=GROOVE, bd=0, command=btn_delete, fg="white", bg="#333333")
btndelete.pack(side=LEFT, expand=TRUE, fill=BOTH)

btneq = Button(btnrow5, text="=", font="Segoe 20", relief=GROOVE, bd=0, command=btn_equal, fg="white", bg="#333333")
btneq.pack(side=LEFT, expand=TRUE, fill=BOTH)

ui.mainloop()