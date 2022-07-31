from tkinter import *

#setting up the app's basic window settings
root = Tk()
root.title("Insidious 1.0")
root.geometry("1280x720")

# Specify Grid
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

Grid.rowconfigure(root, 1, weight=1)

# Create Buttons
button_1 = Button(root, text="Button 1")
button_2 = Button(root, text="Button 2")

# Set grid
button_1.grid(row=0, column=0, sticky="NSEW")
button_2.grid(row=1, column=0, sticky="NSEW")

root.mainloop()

