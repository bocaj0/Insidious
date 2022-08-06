from tkinter import *


class MainGui:
    def __init__(self, app, title, geometry):

        self.root = app
        self.root.title(title)
        self.root.geometry(geometry)
        self.pageshow = LoginPage(self, self.root)

    def change_page(self, page):
        self.page = page

        if self.page == 0:
            self.pageshow = LoginPage(self, self.root)

        if self.page == 1:
            self.pageshow = BasePage(self, self.root)


class LoginPage:
    def __init__(self, parent, window):
        self.parent = parent
        self.frame = Frame(window)
        self.frame.pack()

        # Welcome button
        self.welcome_lbl = Label(self.frame, text='Welcome!')
        self.welcome_lbl.grid(row=0, column=1)

        # Username
        self.username_lbl = Label(self.frame, text='Username: ')
        self.username_lbl.grid(row=1, column=0)
        self.username_entry = Entry(self.frame)
        self.username_entry.grid(row=1, column=1)

        # Password
        self.password_lbl = Label(self.frame, text='Password: ')
        self.password_lbl.grid(row=2, column=0)
        self.password_entry = Entry(self.frame)
        self.password_entry.grid(row=2, column=1)

        # login button
        self.login = Button(self.frame, text='Login', command=self.clicked)
        self.login.grid(row=3, column=1)

    def clicked(self):
        self.frame.destroy()
        self.parent.change_page(1)


class BasePage:
    def __init__(self, parent, window):
        self.parent = parent
        self.frame = Frame(window)
        self.frame.pack()

        self.header = Label(self.frame, text="")
        self.header.grid(row=0, column=1)

        # Create Buttons
        self.dashboard_btn = Button(self.frame, text="Dashboard", command=self.dashboard_setup)
        self.tasks_btn = Button(self.frame, text="Tasks", command=self.tasks_setup)
        self.settings_btn = Button(self.frame, text="Settings", command=self.settings_setup)

        # Set grid
        self.dashboard_btn.grid(row=0, column=0, sticky="NW")
        self.tasks_btn.grid(row=1, column=0, sticky="NW")
        self.settings_btn.grid(row=2, column=0, sticky="NW")

    def dashboard_setup(self):
        # creates dashboard page header
        self.header.grid_forget()
        self.header = Label(self.frame, text="Dashboard")
        self.header.grid(row=0, column=1)

    def tasks_setup(self):
        # creates tasks page header
        self.header.grid_forget()
        self.header = Label(self.frame, text="Tasks")
        self.header.grid(row=0, column=1)

    def settings_setup(self):
        # creates settings page header
        self.header.grid_forget()
        self.header = Label(self.frame, text="Settings")
        self.header.grid(row=0, column=1)

    def clicked(self):
        self.frame.destroy()
        self.parent.change_page(0)


if __name__ == '__main__':
    root = Tk()
    MainGui(root, "Insidious 1.0", "1280x720")
    root.mainloop()
