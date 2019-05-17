from tkinter import Frame, Text, Button, Label, Scrollbar, WORD, N, E, W, S
from TBoxBase import *
from Arithmetic.Numbers.Primality.PrimeTest import is_prime, next_prime
import sys


class Prime(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.columnconfigure(0, weight=1, pad=5)

        self.rowconfigure(0, pad=5)
        self.rowconfigure(1, weight=1, pad=5)
        self.rowconfigure(2, pad=5)
        self.rowconfigure(3, weight=1, pad=5)

        # Title
        bbutton = Button(self, text="<", command=lambda: controller.show_frame("MainPage"))
        bbutton.grid(row=0, padx=10, sticky=W)
        title = Label(self, text="Primality Test")
        title.grid(row=0, padx=10)

        # Number input
        tinput = Text(self, wrap=WORD)
        tinput.grid(row=1, padx=10, pady=10, sticky=N + E + S + W)
        scrolli = Scrollbar(self, command=tinput.yview)
        tinput.configure(yscrollcommand=scrolli.set)
        scrolli.grid(row=1, pady=10, sticky=N + S + E)
        tinput.insert(1.0, "Integer")
        tinput.bind("<Control-Key-a>", select_all)  # select-all Windows/Linux
        tinput.bind("<Command-Key-a>", select_all)  # select-all Mac

        # Check button
        ebutton = Button(self, text="Check", width=15)
        ebutton.grid(row=2)
        ebutton.configure(command=lambda: self.check(tinput.get(1.0, 'end-1c')))

        # Output box
        self.output = Text(self, wrap=WORD)
        self.output.grid(row=3, padx=10, pady=10, sticky=N + E + S + W)
        self.output.bind("<1>", lambda event: self.output.focus_set())
        scrollo = Scrollbar(self, command=self.output.yview)
        scrollo.grid(row=3, pady=10, sticky=N + S + E)
        self.output.configure(yscrollcommand=scrollo.set)
        self.output.insert(1.0, "Output")
        self.output.configure(state="disabled")
        self.output.bind("<Control-Key-a>", select_all)  # select-all Windows/Linux
        self.output.bind("<Command-Key-a>", select_all)  # select-all Mac

    def check(self, number):
        try:
            number = int(number)
            if is_prime(number):
                display("Number is prime", self.output)
            else:
                next = next_prime(number)
                display("Not prime. Next prime is " + str(next), self.output)
        except ValueError:
            display("Invalid number!", self.output)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        return
