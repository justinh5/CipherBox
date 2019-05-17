from tkinter import Frame, Button, Label, Text, Scrollbar, messagebox, WORD, N, E, S, W
from TBoxBase import *
from Crypto.PublicKey import RSA
import binascii
import sys


class rsa(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.columnconfigure(0, weight=1, pad=5)
        self.columnconfigure(1, weight=1, pad=5)

        self.rowconfigure(0, pad=5)
        self.rowconfigure(1, weight=1, pad=5)
        self.rowconfigure(2, weight=1, pad=5)
        self.rowconfigure(3, pad=5)
        self.rowconfigure(4, weight=1, pad=5)

        # Title
        bbutton = Button(self, text="<", command=lambda: controller.show_frame("MainPage"))
        bbutton.grid(row=0, padx=10, sticky=W)
        bbutton = Button(self, text="Help", command=lambda: self.help())
        bbutton.grid(row=0, column=1, padx=10, sticky=E)
        title = Label(self, text="RSA")
        title.grid(row=0, columnspan=2, padx=10)

        # Public/private key input
        keyinput = Text(self, wrap=WORD)
        keyinput.grid(row=1, columnspan=2, padx=10, pady=10, sticky=N+E+S+W)
        scrolli = Scrollbar(self, command=keyinput.yview)
        keyinput.configure(yscrollcommand=scrolli.set)
        scrolli.grid(row=1, column=1, pady=10, sticky=N+S+E)
        keyinput.insert(1.0, "Public/Private key")
        keyinput.bind("<Control-Key-a>", select_all)  # select-all Windows/Linux
        keyinput.bind("<Command-Key-a>", select_all)  # select-all Mac

        # Plain/ciphertext input
        tinput = Text(self, wrap=WORD)
        tinput.grid(row=2, columnspan=2, padx=10, pady=10, sticky=N + E + S + W)
        scrolli = Scrollbar(self, command=tinput.yview)
        tinput.configure(yscrollcommand=scrolli.set)
        scrolli.grid(row=2, column=1, pady=10, sticky=N + S + E)
        tinput.insert(1.0, "Plain/Ciphertext")
        tinput.bind("<Control-Key-a>", select_all)  # select-all Windows/Linux
        tinput.bind("<Command-Key-a>", select_all)  # select-all Mac

        # Encode/Decode buttons
        ebutton = Button(self, text="Encrypt", width=15)
        ebutton.grid(row=3, column=0, padx=10, sticky=E)
        ebutton.configure(command=lambda: self.encrypt(keyinput.get(1.0, 'end-1c'), tinput.get(1.0, 'end-1c')))
        dbutton = Button(self, text="Decrypt", width=15)
        dbutton.grid(row=3, column=1, padx=10, sticky=W)
        dbutton.configure(command=lambda: self.decrypt(keyinput.get(1.0, 'end-1c'), tinput.get(1.0, 'end-1c')))

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

    def encrypt(self, public_key, plaintext):

        try:
            pub = RSA.importKey(public_key)
            ciphertext = pub.encrypt(plaintext.encode('utf-8'), 32)
            display(binascii.hexlify(ciphertext[0]), self.output)
        except ValueError:
            display("Invalid key!", self.output)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        return

    def decrypt(self, private_key, ciphertext):

        try:
            priv = RSA.importKey(private_key)
            plaintext = priv.decrypt(binascii.unhexlify(ciphertext))
            display(plaintext, self.output)
        except ValueError:
            display("Invalid key!", self.output)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        return

    def help(self):
        messagebox.showinfo("RSA help", "- The RSA public key is used to encrypt messages,"
                            " and only the private key can decrypt them\n\n"
                            "- For security, real applications use padding schemes with the encryption, such as "
                            "OAEP or PKCS1 v2\n\n"
                            "- All keys are expected to be in PEM format\n\n"
                            "- Ciphertext is expected to be in hex format for decryption")
