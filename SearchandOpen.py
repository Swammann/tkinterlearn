#
# - learning how to use tkinter
#



import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []       # This is used to store file name directories


def addApp():

    # destroys all file names so it doesnt reprint. Not sure details
    for widget in frame.winfo_children():
        widget.destroy()

    # 'initialdir=' is asking where you want to start looking for a file
    # '/' I think is referring to the root directory
    # 'executables' is the name and '*' is all of the '.exe' type(executables)
    # '*.*' is all files of all types, 'all files' is what its called in the file type selector
    filename = filedialog.askopenfilename(initialdir='/ThisPC', title='Select File',
                                          filetypes=(('all files', '*.*'), ('executables', '*.exe')))
    apps.append(filename)
    print(filename)
    # Loop to assign labels to each of the file name directories in the apps list
    # Problem is it needs 'widget.destroy()' or it repeats the whole list every time
    for app in apps:
        label = tk.Label(frame, text=app, bg='gray')
        label.pack()


def runApp():

    # Runs the apps currently 'loaded', does it work onlly for apps?
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=700, width=700, bg='#00563f')
canvas.pack()  # actually 'sends' the canvas to the root

frame = tk.Frame(root, bg='#FFFFFF')
frame.place(relwidth=.8, relheight=0.8,
            relx=0.1, rely=0.1)  # use parameters to decide size and then centering

openFile = tk.Button(root, text='open file', padx=20, pady=5,
                     fg='#FFFFFF', bg='#00555f', command=addApp)
openFile.pack()

runApps = tk.Button(root, text='run apps', padx=20, pady=5,
                    fg='#FFFFFF', bg='#00555f', command=runApp)
runApps.pack()

root.mainloop()

