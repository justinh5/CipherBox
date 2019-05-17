from tkinter import Frame, Button, Label, Entry, Checkbutton, Text, Scrollbar, \
                    StringVar, BooleanVar, RIGHT, LEFT, WORD, N, E, S, W
from TBoxBase import *
from Crypt0.Caesar.CEnDecode import encode, decode
import sys


class Caesar(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        shift = StringVar()
        known = BooleanVar()   # true -> shift key known

        self.columnconfigure(0, weight=1, pad=5)
        self.columnconfigure(1, weight=1, pad=5)

        self.rowconfigure(0, pad=5)
        self.rowconfigure(1, pad=5)
        self.rowconfigure(2, weight=1, pad=5)
        self.rowconfigure(3, pad=5)
        self.rowconfigure(4, weight=1, pad=5)

        # Title
        bbutton = Button(self, text="<", command=lambda: controller.show_frame("MainPage"))
        bbutton.grid(row=0, column=0, padx=10, sticky=W)
        title = Label(self, text="Caesar Cipher")
        title.grid(row=0, columnspan=2, padx=10)

        # Shift Key
        sframe = Frame(self)
        sentry = Entry(sframe, textvariable=shift, width=55)
        sentry.pack(side=LEFT)
        sentry.insert(0, "Shift key")
        cb = Checkbutton(sframe, text="Unknown key", variable=known)
        cb.select()
        cb.pack(side=RIGHT, padx=10)
        sframe.grid(row=1, columnspan=2, padx=10, sticky=W+E)

        # Text input
        tinput = Text(self, wrap=WORD)
        tinput.grid(row=2, columnspan=2, padx=10, pady=10, sticky=N+E+S+W)
        scrolli = Scrollbar(self, command=tinput.yview)
        tinput.configure(yscrollcommand=scrolli.set)
        scrolli.grid(row=2, column=1, pady=10, sticky=N+S+E)
        tinput.insert(1.0, "Input")
        tinput.bind("<Control-Key-a>", select_all)  # select-all Windows/Linux
        tinput.bind("<Command-Key-a>", select_all)  # select-all Mac

        # Encode/Decode buttons
        ebutton = Button(self, text="Encode", width=15)
        ebutton.grid(row=3, column=0, padx=10, sticky=E)
        ebutton.configure(command=lambda: self.encode_prep(tinput.get(1.0, 'end-1c'), shift.get()))
        dbutton = Button(self, text="Decode", width=15)
        dbutton.grid(row=3, column=1, padx=10, sticky=W)
        dbutton.configure(command=lambda: self.decode_prep(tinput.get(1.0, 'end-1c'), shift.get(), not known.get()))

        # Output box
        self.output = Text(self, wrap=WORD)
        self.output.grid(row=4, columnspan=2, padx=10, pady=10, sticky=N+E+S+W)
        self.output.bind("<1>", lambda event: self.output.focus_set())
        scrollo = Scrollbar(self, command=self.output.yview)
        scrollo.grid(row=4, column=1, pady=10, sticky=N+S+E)
        self.output.configure(yscrollcommand=scrollo.set)
        self.output.insert(1.0, "Output")
        self.output.configure(state="disabled")
        self.output.bind("<Control-Key-a>", select_all)    # select-all Windows/Linux
        self.output.bind("<Command-Key-a>", select_all)    # select-all Mac

    def encode_prep(self, plaintext, shift):

        try:
            shift2 = int(shift)
            ciphertext = encode(plaintext, shift2)
            display(ciphertext, self.output)
        except ValueError:
            display("Invalid shift key!", self.output)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

        return

    def decode_prep(self, ciphertext, shift, known):

        try:
            shift = int(shift) if known else 0
            plaintext = decode(ciphertext, shift, known)
            display(plaintext, self.output)
        except ValueError:
            display("Invalid shift key!", self.output)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
