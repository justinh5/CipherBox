from tkinter import Frame, Button, Label, Entry, Text, Scrollbar, StringVar, WORD, N, E, S, W
from Crypt0.OTP.OTPencrypt import encrypt, decrypt
from TBoxBase import *
import sys


class OTP(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        key = StringVar()

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
        title = Label(self, text="One-Time Pad")
        title.grid(row=0, columnspan=2, padx=10)

        # Key
        sentry = Entry(self, textvariable=key)
        sentry.grid(row=1, column=0, columnspan=2, padx=10, sticky=W+E)
        sentry.insert(0, "Key")

        # Plaintext input
        tinput = Text(self, wrap=WORD)
        tinput.grid(row=2, columnspan=2, padx=10, pady=10, sticky=N+E+S+W)
        scrolli = Scrollbar(self, command=tinput.yview)
        tinput.configure(yscrollcommand=scrolli.set)
        scrolli.grid(row=2, column=1, pady=10, sticky=N+S+E)
        tinput.insert(1.0, "Input")
        tinput.bind("<Control-Key-a>", select_all)  # select-all Windows/Linux
        tinput.bind("<Command-Key-a>", select_all)  # select-all Mac

        # Encrypt/Decrypt buttons
        ebutton = Button(self, text="Encrypt", width=15)
        ebutton.grid(row=3, column=0, padx=10, sticky=E)
        ebutton.configure(command=lambda: self.encrypt_prep(tinput.get(1.0, 'end-1c'), key.get()))
        dbutton = Button(self, text="Decrypt", width=15)
        dbutton.grid(row=3, column=1, padx=10, sticky=W)
        dbutton.configure(command=lambda: self.decrypt_prep(tinput.get(1.0, 'end-1c'), key.get()))

        # Output box
        self.output = Text(self, wrap=WORD)
        self.output.grid(row=4, columnspan=2, padx=10, pady=10, sticky=N+E+S+W)
        self.output.bind("<1>", lambda event: self.output.focus_set())
        scrollo = Scrollbar(self, command=self.output.yview)
        scrollo.grid(row=4, column=1, pady=10, sticky=N+S+E)
        self.output.configure(yscrollcommand=scrollo.set)
        self.output.insert(1.0, "Output")
        self.output.configure(state="disabled")
        self.output.bind("<Control-Key-a>", select_all)  # select-all Windows/Linux
        self.output.bind("<Command-Key-a>", select_all)  # select-all Mac

    def encrypt_prep(self, plaintext, key):

        try:
            ciphertext = encrypt(plaintext, key)
            display(ciphertext, self.output)
        except ValueError:
            display("Invalid key!", self.output)
        except IndexError:
            display("Invalid key!", self.output)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        return

    def decrypt_prep(self, ciphertext, key):

        try:
            plaintext = decrypt(ciphertext, key)
            display(plaintext, self.output)
        except ValueError:
            display("Invalid key!", self.output)
        except IndexError:
            display("Invalid key!", self.output)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        return
