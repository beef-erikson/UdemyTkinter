from tkinter import *
from tkinter import messagebox

# Create and hide window
root = Tk()
root.withdraw()

# Various message boxes
messagebox.showinfo('Tkinter info', 'Hello World')
messagebox.showerror('Tkinter error', 'error window')
messagebox.showwarning('Tkinter warning', 'warning window')

# User input message boxes
result = messagebox.askquestion('Delete', 'Are you sure?', icon='warning')
if result == 'yes':
    print('deleted')
else:
    print('cancelled')

result = messagebox.askokcancel('Delete', 'Delete all files?', icon='warning')
if result:
    print('deleted')
else:
    print('cancelled')

result = messagebox.askretrycancel('Warning', 'Failed, try again?')
if result:
    print('trying')
else:
    print('gave up')
