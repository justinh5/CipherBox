from tkinter import Frame, Button, Label, Listbox, Entry, StringVar, N, E, S, W
from Convert.Numbers.Convert import convert_dunits
import sys


class DUnits(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.left_value = StringVar()        # the input on the left
        self.right_value = StringVar()       # the input on the right

        self.columnconfigure(0, weight=1, pad=5)
        self.columnconfigure(1, weight=1, pad=5)

        self.rowconfigure(0, pad=5)
        self.rowconfigure(1, pad=5)
        self.rowconfigure(2, pad=5)
        self.rowconfigure(3, weight=1, pad=5)

        # Title
        bbutton = Button(self, text="<", command=lambda: controller.show_frame("MainPage"))
        bbutton.grid(row=0, column=0, padx=10, sticky=W)
        title = Label(self, text="Digital Storage")
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
        self.roptions.bind('<<ListboxSelect>>', lambda a: self.update_outputs(0))

        # Insert all keys in the dictionary in the listboxes
        units = ['bit', 'kilobit', 'kibibit', 'megabit', 'mebibit', 'gigabit', 'gibibit', 'terabit', 'tebibit',
                 'petabit', 'pebibit', 'byte', 'kilobyte', 'kibibyte', 'megabyte', 'mebibyte', 'gigabyte', 'gibibyte',
                 'terabyte', 'tebibyte', 'petabyte', 'pebibyte']
        for x in units:
            self.loptions.insert('end', x)
            self.roptions.insert('end', x)

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
            left_units = self.loptions.get(lselection[0])
            rselection = self.roptions.curselection()
            right_units = self.roptions.get(rselection[0])

            if args[0] == 0:
                self.right_value.set(convert_dunits(float(temp_left), left_units, right_units))
            else:
                self.left_value.set(convert_dunits(float(temp_right), right_units, left_units))

        except ValueError:
            if args[0] == 0:
                self.right_value.set("Invalid input!")
            else:
                self.left_value.set("Invalid input!")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        self.update_in_progress = False
