#
# - learning how to use tkinter
#

import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

# To get rid of empty spaces in 'save.txt'
# Checks if there is a file named 'save.txt', opens and reads it
# Splits the directory names into separate elements of an list
# Moves each element of the 'tempApps' list into 'apps' array, stripping it
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        print(tempApps)
        print(apps)
        apps = [x for x in tempApps if x.strip()]
        print(tempApps)
        print(apps)




def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir='/Program Files', title='Select File',
                                          filetypes=(('all files', '*.*'), ('executables', '*.exe')))
    apps.append(filename)
    print(filename)

    for app in apps:
        label = tk.Label(frame, text=app, bg='gray')
        label.pack()


def runApp():

    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=700, width=700, bg='#00563f')
canvas.pack()  # actually 'sends' the canvas to the root

frame = tk.Frame(root, bg='#FFFFFF')
frame.place(relwidth=.8, relheight=0.8,
            relx=0.1, rely=0.1)

openFile = tk.Button(root, text='open file', padx=20, pady=5,
                     fg='#FFFFFF', bg='#00555f', command=addApp)
openFile.pack()

runApps = tk.Button(root, text='run apps', padx=20, pady=5,
                    fg='#FFFFFF', bg='#00555f', command=runApp)
runApps.pack()

# Make the directory names into labels to see what is currently saved
for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

# Creates a 'save.txt' file and loops the directories to save to it
# If you open it and close it will just add ',' which is a problem
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')

