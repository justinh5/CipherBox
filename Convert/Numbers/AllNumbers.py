from tkinter import Frame, Button, Label, Listbox, Entry, Scrollbar, StringVar, N, E, S, W
from Convert.Numbers.Convert import convert_numbers


class AllNumbers(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.left_value = StringVar()        # the input on the left
        self.right_value = StringVar()       # the input on the right

        self.OPTIONS = {'binary': 2, 'octal': 8, 'decimal': 10, 'hexadecimal': 16, 'base-2': 2, 'base-3': 3,
                        'base-4': 4, 'base-5': 5, 'base-6': 6, 'base-7': 7, 'base-8': 8, 'base-9': 9, 'base-10': 10,
                        'base-11': 11, 'base-12': 12, 'base-13': 13, 'base-14': 14, 'base-15': 15, 'base-16': 16,
                        'base-17': 17, 'base-18': 18, 'base-19': 19, 'base-20': 20, 'base-21': 21, 'base-22': 22,
                        'base-23': 23, 'base-24': 24, 'base-25': 25, 'base-26': 26, 'base-27': 27, 'base-28': 28,
                        'base-29': 29, 'base-30': 30, 'base-31': 31, 'base-32': 32, 'base-33': 33, 'base-34': 34,
                        'base-35': 35, 'base-36': 36}

        self.columnconfigure(0, weight=1, pad=5)
        self.columnconfigure(1, weight=1, pad=5)

        self.rowconfigure(0, pad=5)
        self.rowconfigure(1, pad=5)
        self.rowconfigure(2, pad=5)
        self.rowconfigure(3, weight=1, pad=5)

        # Title
        bbutton = Button(self, text="<", command=lambda: controller.show_frame("MainPage"))
        bbutton.grid(row=0, column=0, padx=10, sticky=W)
        title = Label(self, text="All Numbers")
        title.grid(row=0, columnspan=4, padx=10)

        # Labels
        flabel = Label(self, text="From:")
        flabel.grid(row=1, column=0, padx=10, sticky=W)

        tlabel = Label(self, text="To:")
        tlabel.grid(row=1, column=1, padx=10, sticky=W)

        # In/Outputs
        self.left = Entry(self, textvariable=self.left_value)
        self.left.grid(row=2, column=0, padx=10, sticky=E+W)

        self.right = Entry(self, textvariable=self.right_value)
        self.right.grid(row=2, column=1, padx=10, sticky=E+W)

        # Options
        self.loptions = Listbox(self, exportselection=0)
        self.loptions.grid(row=3, column=0, padx=12, pady=8, sticky=N+E+S+W)
        self.roptions = Listbox(self, exportselection=0)
        self.roptions.grid(row=3, column=1, padx=12, pady=8, sticky=N+E+S+W)

        self.loptions.bind('<<ListboxSelect>>', lambda a: self.update_outputs(1))
        lscroll = Scrollbar(self, command=self.loptions.yview)
        lscroll.grid(row=3, column=0, pady=8, sticky=N+S+E)
        self.loptions.configure(yscrollcommand=lscroll.set)

        self.roptions.bind('<<ListboxSelect>>', lambda a: self.update_outputs(0))
        rscroll = Scrollbar(self, command=self.roptions.yview)
        rscroll.grid(row=3, column=1, pady=8, sticky=N+S+E)
        self.roptions.configure(yscrollcommand=rscroll.set)

        # Insert all keys in the dictionary in the listboxes
        l = ['binary', 'octal', 'decimal', 'hexadecimal']
        for i in range(0, 4):
            self.loptions.insert('end', l[i])
            self.roptions.insert('end', l[i])

        for i in range(2, 37):
            self.loptions.insert('end', "base-" + str(i))
            self.roptions.insert('end', "base-" + str(i))

        self.loptions.select_set(0)  # select first item on the left
        self.roptions.select_set(0)  # select first item on the right

        # If the contents of an entry box change, update each box
        self.update_in_progress = False
        self.left_value.trace("w", lambda a,b,c: self.update_outputs(0))
        self.right_value.trace("w", lambda a,b,c: self.update_outputs(1))

    def update_outputs(self, *args):
        if self.update_in_progress:
            return
        try:
            self.update_in_progress = True
            temp_left = self.left_value.get()
            temp_right = self.right_value.get()

            lselection = self.loptions.curselection()
            left_type = self.loptions.get(lselection[0])
            rselection = self.roptions.curselection()
            right_type = self.roptions.get(rselection[0])

            x = self.OPTIONS[left_type]
            y = self.OPTIONS[right_type]

            if args[0] == 0:
                self.right_value.set(convert_numbers(temp_left, x, y))
            else:
                self.left_value.set(convert_numbers(temp_right, y, x))

        except ValueError:
            if args[0] == 0:
                self.right_value.set("Invalid input!")
            else:
                self.left_value.set("Invalid input!")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        self.update_in_progress = False
