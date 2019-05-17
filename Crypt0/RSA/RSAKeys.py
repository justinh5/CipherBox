from tkinter import Frame, Button, Label, Entry, OptionMenu, Text, Scrollbar, \
                    StringVar, LEFT, WORD, N, E, S, W
from TBoxBase import *
from Crypto.PublicKey import RSA
import sys


class RSAKeys(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        KOPTIONS = ["1024 bits", "2048 bits", "4096 bits"]

        self.columnconfigure(0)
        self.columnconfigure(1, weight=1)

        self.rowconfigure(0, pad=5)
        self.rowconfigure(1, pad=5)
        self.rowconfigure(2, weight=1, pad=5)
        self.rowconfigure(3, pad=5)
        self.rowconfigure(4, pad=5)
        self.rowconfigure(5, pad=5)
        self.rowconfigure(6, pad=5)
        self.rowconfigure(7, pad=5)


        # Title
        bbutton = Button(self, text="<", command=lambda: controller.show_frame("MainPage"))
        bbutton.grid(row=0, column=0, padx=10, sticky=W)
        title = Label(self, text="RSA Key Generator")
        title.grid(row=0, columnspan=2, padx=10)

        # Key length
        kframe = Frame(self)
        klength_label = Label(kframe, text="Key Length")
        klength_label.pack(side=LEFT)
        kselect = StringVar(self)
        kselect.set(KOPTIONS[0])  # default value

        koption = OptionMenu(kframe, kselect, *KOPTIONS)
        koption.pack(side=LEFT, padx=10)
        koption.configure(width=40)

        gbutton = Button(kframe, text="Generate", width=15)
        gbutton.pack(side=LEFT, padx=10)
        gbutton.configure(command=lambda: self.generate(kselect.get()))

        kframe.grid(row=1, columnspan=2, padx=10, pady=5, sticky=E+W+N)

        # Result key frame
        keyframe = Frame(self)

        keyframe.columnconfigure(0, weight=1, pad=5)
        keyframe.columnconfigure(1, pad=5)
        keyframe.columnconfigure(2, weight=1, pad=5)

        keyframe.rowconfigure(0, pad=5)
        keyframe.rowconfigure(1, weight=1, pad=5)

        # Box labels
        pub_label = Label(keyframe, text="Public Key")
        pub_label.grid(row=0, column=0, padx=10, sticky=W)

        priv_label = Label(keyframe, text="Private Key")
        priv_label.grid(row=0, column=2, sticky=W)

        # Public key box
        self.pub_output = Text(keyframe, wrap=WORD)
        self.pub_output.grid(row=1, column=0, padx=10, pady=10, sticky=N+E+S+W)
        self.pub_output.bind("<1>", lambda event: self.pub_output.focus_set())
        scrolli = Scrollbar(keyframe, command=self.pub_output.yview)
        self.pub_output.configure(yscrollcommand=scrolli.set)
        scrolli.grid(row=1, column=0, pady=10, sticky=N+S+E)
        self.pub_output.configure(state="disabled")
        self.pub_output.bind("<Control-Key-a>", select_all)  # select-all Windows/Linux
        self.pub_output.bind("<Command-Key-a>", select_all)  # select-all Mac

        # Private key box
        self.priv_output = Text(keyframe, wrap=WORD)
        self.priv_output.grid(row=1, column=2, padx=10, pady=10, sticky=N+E+S+W)
        self.priv_output.bind("<1>", lambda event: self.priv_output.focus_set())
        scrolli = Scrollbar(keyframe, command=self.priv_output.yview)
        self.priv_output.configure(yscrollcommand=scrolli.set)
        scrolli.grid(row=1, column=2, pady=10, sticky=N+S+E)
        self.priv_output.configure(state="disabled")
        self.priv_output.bind("<Control-Key-a>", select_all)  # select-all Windows/Linux
        self.priv_output.bind("<Command-Key-a>", select_all)  # select-all Mac

        keyframe.grid(row=2, columnspan=2, pady=5, sticky=E+W+N+S)


        plabel = Label(self, text="p")
        plabel.grid(row=3, column=0, padx=3, pady=3)
        self.p = Entry(self)
        self.p.grid(row=3, column=1, padx=10, pady=3, sticky=E+W)
        self.p.bind("<Control-Key-a>", select_all_entry)  # select-all Windows/Linux
        self.p.bind("<Command-Key-a>", select_all_entry)  # select-all Mac

        # q
        qlabel = Label(self, text="q")
        qlabel.grid(row=4, column=0, padx=3, pady=3)
        self.q = Entry(self)
        self.q.grid(row=4, column=1, padx=10, pady=3, sticky=E + W)
        self.q.bind("<Control-Key-a>", select_all_entry)  # select-all Windows/Linux
        self.q.bind("<Command-Key-a>", select_all_entry)  # select-all Mac

        # N
        Nlabel = Label(self, text="N")
        Nlabel.grid(row=5, column=0, padx=3, pady=3)
        self.N = Entry(self)
        self.N.grid(row=5, column=1, padx=10, pady=3, sticky=E + W)
        self.N.bind("<Control-Key-a>", select_all_entry)  # select-all Windows/Linux
        self.N.bind("<Command-Key-a>", select_all_entry)  # select-all Mac

        # e
        elabel = Label(self, text="e")
        elabel.grid(row=6, column=0, padx=3, pady=3)
        self.e = Entry(self)
        self.e.grid(row=6, column=1, padx=10, pady=3, sticky=E + W)
        self.e.bind("<Control-Key-a>", select_all_entry)  # select-all Windows/Linux
        self.e.bind("<Command-Key-a>", select_all_entry)  # select-all Mac

        # d
        dlabel = Label(self, text="d")
        dlabel.grid(row=7, column=0, padx=3, pady=3)
        self.d = Entry(self)
        self.d.grid(row=7, column=1, padx=10, pady=3, sticky=E + W)
        self.d.bind("<Control-Key-a>", select_all_entry)  # select-all Windows/Linux
        self.d.bind("<Command-Key-a>", select_all_entry)  # select-all Mac

    # Clear all variable boxes
    def clear(self):
        self.p.delete(0, 'end')
        self.q.delete(0, 'end')
        self.N.delete(0, 'end')
        self.e.delete(0, 'end')
        self.d.delete(0, 'end')

    def generate(self, keysize):

        try:
            RSAkey = RSA.generate(int(keysize[0:4]))

            display(RSAkey.publickey().exportKey(), self.pub_output)
            display(RSAkey.exportKey(), self.priv_output)

            self.clear()
            self.p.insert(0, str(getattr(RSAkey.key, 'p')))
            self.q.insert(0, str(getattr(RSAkey.key, 'q')))
            self.N.insert(0, str(getattr(RSAkey.key, 'n')))
            self.e.insert(0, str(getattr(RSAkey.key, 'e')))
            self.d.insert(0, str(getattr(RSAkey.key, 'd')))
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

        return
