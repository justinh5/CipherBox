from tkinter import Frame, Button, Label, Text, Scrollbar, WORD, N, E, S, W
from TBoxBase import *
import sys


class StrToBin(Frame):

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
        title = Label(self, text="String to Binary")
        title.grid(row=0, padx=10)

        # Text input
        tinput = Text(self, wrap=WORD)
        tinput.grid(row=1, padx=10, pady=10, sticky=N+E+S+W)
        scrolli = Scrollbar(self, command=tinput.yview)
        tinput.configure(yscrollcommand=scrolli.set)
        scrolli.grid(row=1, pady=10, sticky=N+S+E)
        tinput.insert(1.0, "String")
        tinput.bind("<Control-Key-a>", select_all)  # select-all Windows/Linux
        tinput.bind("<Command-Key-a>", select_all)  # select-all Mac

        # Encode/Decode buttons
        ebutton = Button(self, text="Convert", width=15)
        ebutton.grid(row=2)
        ebutton.configure(command=lambda: self.convert(tinput.get(1.0, 'end-1c')))

        # Output box
        self.output = Text(self, wrap=WORD)
        self.output.grid(row=3, padx=10, pady=10, sticky=N+E+S+W)
        self.output.bind("<1>", lambda event: self.output.focus_set())
        scrollo = Scrollbar(self, command=self.output.yview)
        scrollo.grid(row=3, pady=10, sticky=N+S+E)
        self.output.configure(yscrollcommand=scrollo.set)
        self.output.insert(1.0, "Binary")
        self.output.configure(state="disabled")
        self.output.bind("<Control-Key-a>", select_all)  # select-all Windows/Linux
        self.output.bind("<Command-Key-a>", select_all)  # select-all Mac

    def convert(self, string):

        try:
            binary = ' '.join(format(ord(x), 'b') for x in string)
            display(binary, self.output)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        return
