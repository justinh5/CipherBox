from tkinter import Frame, Button, Label, Text, Scrollbar, WORD, N, E, S, W
from TBoxBase import *
import urllib.parse
import sys


class URL(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.columnconfigure(0, weight=1, pad=5)
        self.columnconfigure(1, weight=1, pad=5)

        self.rowconfigure(0, pad=5)
        self.rowconfigure(1, weight=1, pad=5)
        self.rowconfigure(2, pad=5)
        self.rowconfigure(3, weight=1, pad=5)

        # Title
        bbutton = Button(self, text="<", command=lambda: controller.show_frame("MainPage"))
        bbutton.grid(row=0, column=0, padx=10, sticky=W)
        title = Label(self, text="URL Encode")
        title.grid(row=0, columnspan=2, padx=10)

        # Message input
        tinput = Text(self, wrap=WORD)
        tinput.grid(row=1, columnspan=2, padx=10, pady=10, sticky=N+E+S+W)
        scrolli = Scrollbar(self, command=tinput.yview)
        tinput.configure(yscrollcommand=scrolli.set)
        scrolli.grid(row=1, column=1, pady=10, sticky=N+S+E)
        tinput.insert(1.0, "Input")
        tinput.bind("<Control-Key-a>", select_all)  # select-all Windows/Linux
        tinput.bind("<Command-Key-a>", select_all)  # select-all Mac

        # Encode/Decode buttons
        ebutton = Button(self, text="Encode", width=15)
        ebutton.grid(row=2, column=0, padx=10, sticky=E)
        ebutton.configure(command=lambda: self.encode_prep(tinput.get(1.0, 'end-1c')))
        dbutton = Button(self, text="Decode", width=15)
        dbutton.grid(row=2, column=1, padx=10, sticky=W)
        dbutton.configure(command=lambda: self.decode_prep(tinput.get(1.0, 'end-1c')))

        # Output box
        self.output = Text(self, wrap=WORD)
        self.output.grid(row=3, columnspan=2, padx=10, pady=10, sticky=N+E+S+W)
        self.output.bind("<1>", lambda event: self.output.focus_set())
        scrollo = Scrollbar(self, command=self.output.yview)
        scrollo.grid(row=3, column=1, pady=10, sticky=N+S+E)
        self.output.configure(yscrollcommand=scrollo.set)
        self.output.insert(1.0, "Output")
        self.output.configure(state="disabled")
        self.output.bind("<Control-Key-a>", select_all)  # select-all Windows/Linux
        self.output.bind("<Command-Key-a>", select_all)  # select-all Mac

    def encode_prep(self, string):

        try:
            encoded= urllib.parse.quote(string)
            display(encoded, self.output)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        return

    def decode_prep(self, string):

        try:
            decoded = urllib.parse.unquote(string)
            display(decoded, self.output)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        return
