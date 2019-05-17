from tkinter import ttk, Frame, Button, Label, NO, CENTER, N, E, S, W


class ASCIIChart(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.columnconfigure(0, weight=1, pad=5)

        self.rowconfigure(0, pad=5)
        self.rowconfigure(1, weight=1, pad=5)

        # Title
        bbutton = Button(self, text="<", command=lambda: controller.show_frame("MainPage"))
        bbutton.grid(row=0, sticky=W)
        title = Label(self, text="ASCII Chart")
        title.grid(row=0)

        controls = {0: 'NUL', 1: 'SOH', 2: 'STX', 3: 'ETX', 4: 'EOT', 5: 'ENQ', 6: 'ACK', 7: 'BEL', 8: 'BS',
                   9: 'HT', 10: 'LF', 11: 'VT', 12: 'FF', 13: 'CR', 14: 'SO', 15: 'SI', 16: 'DLE', 17: 'DC1',
                   18: 'DC2', 19: 'DC3', 20: 'DC4', 21: 'NAK', 22: 'SYN', 23: 'ETB', 24: 'CAN', 25: 'EM', 26: '1A',
                   27: 'ESC', 28: 'FS', 29: 'GS', 30: 'RS', 31: 'US'}

        descriptions = {0: 'Null char', 1: 'Start of heading', 2: 'Start of text', 3: 'End of text',
                        4: 'End of transmission', 5: 'Enquiry', 6: 'Acknowledgment', 7: 'Bell', 8: 'Back space',
                        9: 'Horizontal Tab', 10: 'Line feed', 11: 'Vertical Tab', 12: 'Form Feed',
                        13: 'Carriage return', 14: 'Shift Out / X-On', 15: 'Shift In / X-Off', 16: 'Data line escape',
                        17: 'Device control 1', 18: 'Device control 2', 19: 'Device control 3', 20: 'Device control 4',
                        21: 'Negative Acknowledgement', 22: 'Synchronize idle', 23: 'End of transmit block',
                        24: 'Cancel', 25: 'End of medium', 26: 'Substitute', 27: 'Escape', 28: 'File separator',
                        29: 'Group separator', 30: 'Record separator', 31: 'Unit separator', 32: 'Space',
                        33: 'Exclamation mark', 34: 'Double quotes', 35: 'Number', 36: 'Dollar', 37: 'Percent',
                        38: 'Ampersand', 39: 'Single quote', 40: 'Open parenthesis', 41: 'Close parenthesis',
                        42: 'Asterisk', 43: 'Plus', 44: 'Comma', 45: 'Hyphen', 46: 'Period', 47: 'Forward slash',
                        48: 'Zero', 49: 'One', 50: 'Two', 51: 'Three', 52: 'Four', 53: 'Five', 54: 'Six', 55: 'Seven',
                        56: 'Eight', 57: 'Nine', 58: 'Colon', 59: 'Semicolon', 60: 'Less than', 61: 'Equals',
                        62: 'Greater Than', 63: 'Question mark', 64: 'At symbol', 91: 'Opening bracket', 92: 'Backslash',
                        93: 'Closing bracket', 94: 'Caret', 95: 'Underscore', 96: 'Grave accent', 123: 'Opening brace',
                        124: 'Vertical bar', 125: 'Closing brace', 126: 'Tilde', 127: 'Delete'}

        chart = ttk.Treeview(self)
        chart['columns'] = ('DEC', 'OCT', 'HEX', 'BIN', 'Symbol', 'HTML Number', 'Description')
        chart.grid(row=1, sticky=N + E + S + W)

        # scrollbar
        yscroll = ttk.Scrollbar(self, command=chart.yview)
        chart['yscroll'] = yscroll.set
        yscroll.grid(row=1, sticky=N+S+E)

        # column headings and options
        chart.heading("DEC", text="DEC")
        chart.heading("OCT", text="OCT")
        chart.heading("HEX", text="HEX")
        chart.heading("BIN", text="BIN")
        chart.heading("Symbol", text="Symbol")
        chart.heading("HTML Number", text="HTML Number")
        chart.heading("Description", text="Description")

        chart.column("#0", stretch=NO, width=0)
        chart.column("DEC", width=1, anchor=CENTER)
        chart.column("OCT", width=1, anchor=CENTER)
        chart.column("HEX", width=1, anchor=CENTER)
        chart.column("BIN", width=1, anchor=CENTER)
        chart.column("Symbol", width=1, anchor=CENTER)
        chart.column("HTML Number", width=1, anchor=CENTER)
        chart.column("Description", width=100, anchor=W)

        # fill the chart with ASCII data
        for i in range(0, 128):

            # control characters
            if i < 32:
                chart.insert("", "end", values=(i, oct(i)[2:], hex(i)[2:], bin(i)[2:], controls[i], "&#0" + str(i), descriptions[i]))
            # uppercase characters
            elif 64 < i < 91:
                desc = "Uppercase " + chr(i)
                chart.insert("", "end", values=(i, oct(i)[2:], hex(i)[2:], bin(i)[2:], chr(i), "&#" + str(i), desc))
            # lowercase characters
            elif 96 < i < 123:
                desc = "Lowercase " + chr(i)
                chart.insert("", "end", values=(i, oct(i)[2:], hex(i)[2:], bin(i)[2:], chr(i), "&#" + str(i), desc))
            # other
            else:
                chart.insert("", "end", values=(i, oct(i)[2:], hex(i)[2:], bin(i)[2:], chr(i), "&#" + str(i), descriptions[i]))
