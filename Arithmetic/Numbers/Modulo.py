from tkinter import Frame, Button, Label, Entry, END, N, E, W
import sys


class Modulus(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.columnconfigure(0, weight=5, pad=5)
        self.columnconfigure(1, pad=5)
        self.columnconfigure(2, weight=5, pad=5)

        self.rowconfigure(0, pad=5)
        self.rowconfigure(1, pad=5)
        self.rowconfigure(2, pad=5)
        self.rowconfigure(3, weight=1, pad=5)

        # Title
        bbutton = Button(self, text="<", command=lambda: controller.show_frame("MainPage"))
        bbutton.grid(row=0, column=0, padx=10, sticky=W)
        title = Label(self, text="Modulus Calculator")
        title.grid(row=0, columnspan=4, padx=10, pady=20)

        # Operand 1
        op1 = Entry(self)
        op1.grid(row=1, column=0, padx=10, pady=10, sticky=E+W)
        op1.insert(0, "Operand 1")

        # Mod label
        label = Label(self, text="mod")
        label.grid(row=1, column=1)

        # Operand 2
        op2 = Entry(self)
        op2.grid(row=1, column=2, padx=10, pady=10, sticky=E+W)
        op2.insert(0, "Operand 2")

        # Result box
        self.output = Entry(self, text="Output")
        self.output.grid(row=2, columnspan=3, padx=10, sticky=E+W)

        # Calculate button
        ebutton = Button(self, text="Calculate", width=10)
        ebutton.grid(row=3, column=1, padx=10, sticky=N)
        ebutton.configure(command=lambda: self.mod_prep(op1.get(), op2.get()))

    # Check both operands for decimal numbers.
    def mod_prep(self, op1, op2):

        try:
            left = int(op1)
            right = int(op2)
            mod = left % right
            self.display(mod)
            return mod
        except ValueError:
            self.display("Invalid operands!")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        return

    def display(self, message):
        self.output.delete(0, END)
        self.output.insert(0, message)



