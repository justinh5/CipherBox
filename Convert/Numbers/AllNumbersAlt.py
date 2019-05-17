from tkinter import Frame, Button, Label, Text, OptionMenu, Scrollbar, StringVar, WORD, END, N, E, S, W
from Convert.Numbers.Convert import convert_numbers
from TBoxBase import *
import sys


class AllNumbersAlt(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.OPTIONS = {'binary': 2, 'octal': 8, 'decimal': 10, 'hexadecimal': 16, 'base-2': 2, 'base-3': 3,
                        'base-4': 4, 'base-5': 5, 'base-6': 6, 'base-7': 7, 'base-8': 8, 'base-9': 9, 'base-10': 10,
                        'base-11': 11, 'base-12': 12, 'base-13': 13, 'base-14': 14, 'base-15': 15, 'base-16': 16,
                        'base-17': 17, 'base-18': 18, 'base-19': 19, 'base-20': 20, 'base-21': 21, 'base-22': 22,
                        'base-23': 23, 'base-24': 24, 'base-25': 25, 'base-26': 26, 'base-27': 27, 'base-28': 28,
                        'base-29': 29, 'base-30': 30, 'base-31': 31, 'base-32': 32, 'base-33': 33, 'base-34': 34,
                        'base-35': 35, 'base-36': 36}

        self.columnconfigure(0, weight=1, pad=5)
        self.columnconfigure(1, pad=5)
        self.columnconfigure(2, weight=1, pad=5)

        self.rowconfigure(0, pad=5)
        self.rowconfigure(1, pad=5)
        self.rowconfigure(2, weight=1, pad=5)
        self.rowconfigure(3, pad=5)
        self.rowconfigure(4, weight=1, pad=5)

        # Title
        bbutton = Button(self, text="<", command=lambda: controller.show_frame("MainPage"))
        bbutton.grid(row=0, column=0, padx=10, sticky=W)
        title = Label(self, text="All Numbers")
        title.grid(row=0, columnspan=3, padx=10)

        # Option boxes
        self.lselect = StringVar(self)
        self.loption = OptionMenu(self, self.lselect, ())
        self.loption.grid(row=1, column=0, padx=10, sticky=W + E)
        self.lselect.set("binary")

        tolabel = Label(self, text="to")
        tolabel.grid(row=1, column=1, padx=10)

        self.rselect = StringVar(self)
        self.roption = OptionMenu(self, self.rselect, ())
        self.roption.grid(row=1, column=2, padx=10, sticky=W + E)
        self.rselect.set("binary")

        # Insert all keys in the dictionary in the dropdown menus
        l = ['binary', 'octal', 'decimal', 'hexadecimal']
        for i in range(0, 4):
            self.loption['menu'].add_command(label=l[i], command=lambda value=l[i]: self.lselect.set(value))
            self.roption['menu'].add_command(label=l[i], command=lambda value=l[i]: self.rselect.set(value))

        for i in range(2, 37):
            self.loption['menu'].add_command(label="base-"+str(i), command=lambda value="base-"+str(i): self.lselect.set(value))
            self.roption['menu'].add_command(label="base-"+str(i), command=lambda value="base-"+str(i): self.rselect.set(value))

        # Value input
        self.vinput = Text(self, wrap=WORD)
        self.vinput.grid(row=2, columnspan=3, padx=10, pady=10, sticky=N+E+S+W)
        scrolli = Scrollbar(self, command=self.vinput.yview)
        self.vinput.configure(yscrollcommand=scrolli.set)
        scrolli.grid(row=2, column=2, pady=10, sticky=N+S+E)
        self.vinput.insert(1.0, "Input")
        self.vinput.bind("<Control-Key-a>", select_all)  # select-all Windows/Linux
        self.vinput.bind("<Command-Key-a>", select_all)  # select-all Mac

        # Encode/Decode buttons
        ebutton = Button(self, text="Convert", command=self.click)
        ebutton.grid(row=3, column=1, sticky=E+W)

        # Output box
        self.output = Text(self, wrap=WORD)
        self.output.grid(row=4, columnspan=3, padx=10, pady=10, sticky=N+E+S+W)
        self.output.bind("<1>", lambda event: self.output.focus_set())
        scrollo = Scrollbar(self, command=self.output.yview)
        scrollo.grid(row=4, column=2, pady=10, sticky=N+S+E)
        self.output.configure(yscrollcommand=scrollo.set)
        self.output.insert(1.0, "Output")
        self.output.configure(state="disabled")

    def click(self):
        """Process the inputs before encoding
        The key must be alphabetic with no numbers.
        """

        try:
            x = self.lselect.get()
            y = self.rselect.get()
            value = self.vinput.get(1.0, 'end-1c')
            result = convert_numbers(value, self.OPTIONS[x], self.OPTIONS[y])
            display(result, self.output)
        except ValueError:
            display("Invalid input!", self.output)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
