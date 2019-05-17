from tkinter import Frame, Button, Label, Entry, Text, OptionMenu, Scrollbar, StringVar, WORD, N, E, S, W
from Arithmetic.Numbers.Evaluate import evaluate
from TBoxBase import *
import re
import sys


class Arithmetic(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.columnconfigure(0, weight=1, pad=5)

        self.rowconfigure(0, pad=5)
        self.rowconfigure(1, pad=5)
        self.rowconfigure(2, pad=5)
        self.rowconfigure(3, pad=5)
        self.rowconfigure(4, pad=5)
        self.rowconfigure(5, pad=5)
        self.rowconfigure(6, weight=1, pad=5)

        # Title
        bbutton = Button(self, text="<", command=lambda: controller.show_frame("MainPage"))
        bbutton.grid(row=0, padx=10, sticky=W)
        title = Label(self, text="Number Arithmetic")
        title.grid(row=0)

        # Type options
        TOPTIONS = ["Unsigned Binary", "Sign and Magnitude", "One's Complement", "Two's Complement", "Hexadecimal"]

        self.tselect = StringVar(self)
        toption = OptionMenu(self, self.tselect, *TOPTIONS)
        toption.grid(row=1, padx=8, sticky=W+E)

        # Operand 1
        op1 = Entry(self)
        op1.grid(row=2, padx=10, pady=10, sticky=E+W)
        op1.insert(0, "Operand 1")

        # Operator option
        OOPTIONS = ["+", "-", "*", "/ (will round)"]

        operator = StringVar(self)
        operator.set(OOPTIONS[0])  # default value

        ooption = OptionMenu(self, operator, *OOPTIONS)
        ooption.grid(row=3, padx=8, sticky=W)
        ooption.configure(width=8)

        # Operand 2
        op2 = Entry(self)
        op2.grid(row=4, padx=10, pady=10, sticky=E+W)
        op2.insert(0, "Operand 2")

        # Evaluate button
        ebutton = Button(self, text="=", width=10)
        ebutton.grid(row=5)
        ebutton.configure(command=lambda: self.calc_prep(op1.get(), op2.get(), operator.get(), self.tselect.get()))

        # Output box
        self.output = Text(self, wrap=WORD)
        self.output.grid(row=6, padx=11, pady=10, sticky=N+E+S+W)
        self.output.bind("<1>", lambda event: self.output.focus_set())
        scrollo = Scrollbar(self, command=self.output.yview)
        scrollo.grid(row=6, pady=10, sticky=N+S+E)
        self.output.configure(yscrollcommand=scrollo.set)
        self.output.insert(1.0, "Output")
        self.output.configure(state="disabled")
        self.output.bind("<Control-Key-a>", select_all)  # select-all Windows/Linux
        self.output.bind("<Command-Key-a>", select_all)  # select-all Mac

    def set_option(self, option):
        self.tselect.set(option)
        return

    # Check for valid operands and overflow
    def calc_prep(self, op1, op2, op, kind):

        try:
            if kind in ["Unsigned Binary", "Sign and Magnitude", "One's Complement", "Two's Complement"]:
                int(op1, 2)
                int(op2, 2)
                if kind in ["Sign and Magnitude", "One's Complement", "Two's Complement"]:
                    if (op1[0] == "1" and len(op1) == 1) or (op2[0] == "1" and len(op2) == 1):
                        display("Must have two or more bits!", self.output)
                        return
                else:
                    if int(op2, 2) > int(op1, 2) and op == "-":
                        display("Overflow!", self.output)
                        return
            else:
                if not (re.fullmatch("(0x)?[A-F0-9]*", op1, re.I) and re.fullmatch("(0x)?[A-F0-9]*", op2, re.I)):
                    display("Invalid hex operands!", self.output)
                    return
            result = evaluate(op1, op2, op, kind)
            display(result, self.output)
        except ValueError:
            display("Invalid binary operands!", self.output)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
