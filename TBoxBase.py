from tkinter import SEL, END, INSERT

def display(message, output):
    """Display message in textbox
    Displays any message in the tkinter textbox widget.
    Used for printing errors and displaying results.
    """
    output.configure(state="normal")
    output.delete(1.0, END)
    output.insert(1.0, message)
    output.configure(state="disabled")


def select_all(event):
    """Select all text event in textbox
    An event that is bound to the select-all key press.
    Selects all text within a text widget.
    """
    event.widget.tag_add(SEL, "1.0", END)
    event.widget.mark_set(INSERT, "1.0")
    event.widget.see(INSERT)
    return 'break'


def select_all_entry(event):
    event.widget.select_range(0, 'end')
    #event.widget.icursor('end')
    return 'break'
