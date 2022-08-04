from tkinter import *

# page tracker
current_page = 0


# dashboard labels
dashboard_header = ''


# tasks labels
tasks_header = ''


# settings labels
settings_header = ''


def tab_setup():
    # setting up the app's basic window settings
    global current_page
    current_page = 0

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
    dashboard_btn = Button(root, text="Dashboard", command=dashboard_setup())
    tasks_btn = Button(root, text="Tasks", command=tasks_setup())
    settings_btn = Button(root, text="Settings", command=settings_setup())

    # Set grid
    dashboard_btn.grid(row=0, column=0, sticky="NSEW")
    tasks_btn.grid(row=1, column=0, sticky="NSEW")
    settings_btn.grid(row=2, column=0, sticky="NSEW")


def create_labels():
    global dashboard_header, tasks_header, settings_header
    dashboard_header = Label(root, text="Dashboard")
    dashboard_header.grid(row=0, column=1, sticky="NSEW")

    tasks_header = Label(root, text="Tasks")
    tasks_header.grid(row=0, column=1, sticky="NSEW")

    settings_header = Label(root, text="Settings")
    settings_header.grid(row=0, column=1, sticky="NSEW")


def forget_buttons():
    global dashboard_header, tasks_header, settings_header
    dashboard_header.pack_forget()
    tasks_header.pack_forget()
    settings_header.pack_forget()


def dashboard_setup():
    forget_buttons()
    # creates dashboard page header
    global dashboard_header
    dashboard_header.pack


def tasks_setup():
    forget_buttons()
    # creates tasks page header
    global tasks_header
    tasks_header.pack


def settings_setup():
    forget_buttons()
    # creates settings page header
    global settings_header
    settings_header.pack


# MAIN LOOP
if __name__ == "__main__":
    root = Tk()
    root.title("Insidious 1.0")
    root.geometry("1280x720")

    # Sets up the home page GUI
    create_labels()
    tab_setup()

    root.mainloop()


