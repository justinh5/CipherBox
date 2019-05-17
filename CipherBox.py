#!/usr/bin/env python3

from tkinter import Tk, Frame, Label, Button, OptionMenu, StringVar, TOP, LEFT, BOTH, N, E, S, W
from Crypt0 import *
from Strings import *
from Arithmetic import *
from Convert import *
from Other import *
import os


class MainController(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # The main container that contains the current frame
        self.container = Frame(self)
        self.container.pack(side=TOP, fill=BOTH, expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # for mapping the spelling of the listed items with class names
        self.pages = {'MainPage': MainPage, 'Caesar': Caesar, 'Vigenere': Vigenere, 'One-time pad': OTP,
                      'MD5 Hash': MD5, 'Base64 encode': Base64, 'ASCII chart': ASCIIChart, 'URL encode': URL,
                      'UTF-8 encode': UTF8, 'Unsigned Binary': Arithmetic, 'Sign and Magnitude': Arithmetic,
                      "One's Complement": Arithmetic, "Two's Complement": Arithmetic, 'Hexadecimal': Arithmetic,
                      'Modulus Calculator': Modulus, 'All Numbers': AllNumbers, 'All Numbers (alternate)': AllNumbersAlt,
                      'Binary Representation': BinRep, 'Data Storage Units': DUnits, 'String to Binary': StrToBin,
                      'Prime Number Checker': Prime, 'RSA': rsa, 'RSA Key Generator': RSAKeys, 'Hexdump': Hdump}

        self.current_frame = Frame()
        self.show_frame("MainPage")


    def show_frame(self, page_name):
        """Change current page
        Show a frame given the page name and communicate to the frames
        with an optional option parameter
        """
        self.current_frame.grid_forget()   # clear frame's widgets
        self.current_frame = self.pages[page_name](parent=self.container, controller=self)
        self.current_frame.grid(row=0, column=0, sticky=N + E + S + W)

        if self.pages[page_name].__name__ == 'Arithmetic':  # set an option when the frame is loaded
            self.current_frame.set_option(page_name)
        return


class MainPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        opFrame = Frame(self)

        opFrame.columnconfigure(0, pad=5)
        opFrame.columnconfigure(1, pad=5)
        opFrame.columnconfigure(2, pad=5)

        opFrame.rowconfigure(0, pad=5)
        opFrame.rowconfigure(1, pad=5)
        opFrame.rowconfigure(2, pad=5)
        opFrame.rowconfigure(3, pad=5)
        opFrame.rowconfigure(4, pad=5)
        opFrame.rowconfigure(5, pad=5)

        title = Label(opFrame, text="CipherBox")
        title.grid(row=0, columnspan=3)

        # Cryptography options
        cylabel = Label(opFrame, text="Crypto")
        cylabel.grid(row=1, column=0, padx=5, pady=20)

        CYOPTIONS = ["Caesar", "Vigenere", "One-time pad", "MD5 Hash", "RSA", "RSA Key Generator"]

        cyselect = StringVar(opFrame)
        cyselect.set(CYOPTIONS[0])  # default value

        cyoption = OptionMenu(opFrame, cyselect, *CYOPTIONS)
        cyoption.grid(row=1, column=1, padx=5, pady=5)
        cyoption.configure(width=30)

        cybutton = Button(opFrame, text="Go", command=lambda: controller.show_frame(cyselect.get()))
        cybutton.grid(row=1, column=2)
        cybutton.configure(width=3, height=2)

        # String options
        slabel = Label(opFrame, text="Strings")
        slabel.grid(row=2, column=0, padx=5, pady=5)

        SOPTIONS = ["ASCII chart", "Base64 encode", "URL encode", "UTF-8 encode"]

        sselect = StringVar(opFrame)
        sselect.set(SOPTIONS[0])  # default value

        soption = OptionMenu(opFrame, sselect, *SOPTIONS)
        soption.grid(row=2, column=1, padx=5, pady=5)
        soption.configure(width=30)

        sbutton = Button(opFrame, text="Go", command=lambda: controller.show_frame(sselect.get()))
        sbutton.grid(row=2, column=2, padx=5, pady=5)
        sbutton.configure(width=3, height=2)

        # Arithmetic options
        alabel = Label(opFrame, text="Arithmetic")
        alabel.grid(row=3, column=0)

        AOPTIONS = ["Unsigned Binary", "Sign and Magnitude", "One's Complement",
                    "Two's Complement", "Hexadecimal", "Modulus Calculator", "Prime Number Checker"]

        aselect = StringVar(opFrame)
        aselect.set(AOPTIONS[0])  # default value

        aoption = OptionMenu(opFrame, aselect, *AOPTIONS)
        aoption.grid(row=3, column=1, padx=5, pady=5)
        aoption.configure(width=30)

        abutton = Button(opFrame, text="Go", command=lambda: controller.show_frame(aselect.get()))
        abutton.grid(row=3, column=2, padx=5, pady=5)
        abutton.configure(width=3, height=2)

        # Converter options
        clabel = Label(opFrame, text="Converter")
        clabel.grid(row=4, column=0)

        COPTIONS = ["All Numbers", "All Numbers (alternate)", "Binary Representation", "Data Storage Units",
                    'String to Binary']

        cselect = StringVar(opFrame)
        cselect.set(COPTIONS[0])  # default value

        coption = OptionMenu(opFrame, cselect, *COPTIONS)
        coption.grid(row=4, column=1, padx=5, pady=5)
        coption.configure(width=30)

        cbutton = Button(opFrame, text="Go", command=lambda: controller.show_frame(cselect.get()))
        cbutton.grid(row=4, column=2, padx=5, pady=5)
        cbutton.configure(width=3, height=2)

        # Other options
        olabel = Label(opFrame, text="Other")
        olabel.grid(row=5, column=0)

        OOPTIONS = ["Hexdump"]

        oselect = StringVar(opFrame)
        oselect.set(OOPTIONS[0])  # default value

        ooption = OptionMenu(opFrame, oselect, *OOPTIONS)
        ooption.grid(row=5, column=1, padx=5, pady=5)
        ooption.configure(width=30)

        obutton = Button(opFrame, text="Go", command=lambda: controller.show_frame(oselect.get()))
        obutton.grid(row=5, column=2, padx=5, pady=5)
        obutton.configure(width=3, height=2)

        opFrame.pack(pady=50)


if __name__ == "__main__":
    root = MainController()
    root.title("CipherBox")
    root.geometry("800x600+600+100")
    # used for setting the window on top of all others in MacOS
    os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
    root.lift()
    root.mainloop()
