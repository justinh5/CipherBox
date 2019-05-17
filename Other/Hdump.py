from tkinter import Frame, Button, Label, Text, Entry, Scrollbar, \
                    filedialog, StringVar, WORD, N, E, S, W
from TBoxBase import *
import hexdump


class Hdump(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        path = StringVar()

        self.columnconfigure(0, weight=1, pad=5)
        self.columnconfigure(1, weight=1, pad=5)

        self.rowconfigure(0, pad=5)
        self.rowconfigure(1, pad=5)
        self.rowconfigure(2, pad=5)
        self.rowconfigure(3, weight=1, pad=5)

        # Title
        bbutton = Button(self, text="<", command=lambda: controller.show_frame("MainPage"))
        bbutton.grid(row=0, column=0, padx=10, sticky=W)
        title = Label(self, text="Hexdump")
        title.grid(row=0, columnspan=2, padx=10)

        button_browse = Button(self, text="Browse", command=self.browse)
        button_browse.grid(row=1, column=0, padx=5, pady=5, sticky=E)

        self.entry = Entry(self, width=50, textvariable=path)
        self.entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        dbutton = Button(self, text="Dump", command=lambda: self.hexdump(path.get()))
        dbutton.grid(row=2, columnspan=2, pady=2)

        # Output box
        self.output = Text(self, wrap=WORD)
        self.output.grid(row=3, columnspan=2, padx=5, pady=5, sticky=N+E+S+W)
        self.output.bind("<1>", lambda event: self.output.focus_set())
        scrollo = Scrollbar(self, command=self.output.yview)
        scrollo.grid(row=3, column=1, pady=10, sticky=N + S + E)
        self.output.configure(yscrollcommand=scrollo.set)
        self.output.configure(state="disabled")
        self.output.bind("<Control-Key-a>", select_all)  # select-all Windows/Linux
        self.output.bind("<Command-Key-a>", select_all)  # select-all Mac

    def browse(self):
        filename = filedialog.askopenfilename()
        self.entry.delete(0, END)
        self.entry.insert(0, filename)

    def hexdump(self, filepath):
        string = hexdump.hexdump(open(filepath, 'rb'), result='return')
        display(string, self.output)
