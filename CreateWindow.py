#
# - learning how to use tkinter
#

import tkinter as tk
from tkinter import filedialog, Text
import os  # allows us to run the apps that we add to our app

root = tk.Tk()  # This holds the whole app, whenever you make something like a button et you attach it to the root


# creates and alters the GUI,
canvas = tk.Canvas(root, height=700, width=700, bg='#00563f')
canvas.pack()  # actually 'sends' the canvas to the root

# like making a 'container', scales with the window
frame = tk.Frame(root, bg='#FFFFFF')
frame.place(relwidth=.8, relheight=0.8,
            relx=0.1, rely=0.1)  # use parameters to decide size and then centering

# creates a button, needs a function added through 'command='
openFile = tk.Button(root, text='open file', padx=20, pady=5,
                     fg='#FFFFFF', bg='#00555f')
openFile.pack()

# create another button
runApps = tk.Button(root, text='run apps', padx=20, pady=5,
                    fg='#FFFFFF', bg='#00555f')
runApps.pack()

# creates the GUI and allows it to run
root.mainloop()

