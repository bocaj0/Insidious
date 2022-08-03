from tkinter import *

current_page = 0


def dashboard_setup():
    # setting up the app's basic window settings
    root.title("Insidious 1.0")
    root.geometry("1280x720")

    # Specify Grid
    # row specifications
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=3)

    # column specifications
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=8)

    # Create Buttons
    dashboard_btn = Button(root, text="Dashboard")
    tasks_btn = Button(root, text="Tasks")
    settings_btn = Button(root, text="Settings")

    # Set grid
    dashboard_btn.grid(row=0, column=0, sticky="NSEW")
    tasks_btn.grid(row=1, column=0, sticky="NSEW")
    settings_btn.grid(row=2, column=0, sticky="NSEW")


# MAIN LOOP
if __name__ == "__main__":
    root = Tk()
    # Sets up the home page GUI
    home_page_setup()

    root.mainloop()


