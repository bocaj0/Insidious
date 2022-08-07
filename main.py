from tkinter import *


class MainGui:
    def __init__(self, app, title, geometry):
        self.root = app
        self.root.title(title)
        self.root.geometry(geometry)
        self.show_page = LoginPage(self, self.root)

    def change_page(self, page):
        self.page = page

        if self.page == 0:
            self.show_page = LoginPage(self, self.root)

        if self.page == 1:
            self.show_page = BasePage(self, self.root)


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

        # Login button
        self.login = Button(self.frame, text='Login', command=self.clicked)
        self.login.grid(row=3, column=1)

    def clicked(self):
        self.frame.destroy()
        self.parent.change_page(1)


class BasePage:
    def __init__(self, parent, window):
        self.parent = parent
        self.window = window
        self.frame = Frame(window)
        self.frame.pack()

        # self.header = Label(self.frame, text="")
        # self.header.grid(row=0, column=1)

        # Create Buttons
        self.dashboard_btn = Button(self.frame, text="Dashboard", command=self.change_dash_page)
        self.tasks_btn = Button(self.frame, text="Tasks", command=self.change_task_page)
        self.settings_btn = Button(self.frame, text="Settings", command=self.change_sett_page)

        # Set grid
        self.dashboard_btn.grid(row=0, column=0, sticky="NW")
        self.tasks_btn.grid(row=1, column=0, sticky="NW")
        self.settings_btn.grid(row=2, column=0, sticky="NW")

        # self.show_page = DashboardPage(self, self.window)

    def change_dash_page(self):
        self.frame.destroy()
        self.show_page = DashboardPage(self, self.window)

    def change_task_page(self):
        self.frame.destroy()
        self.show_page = DashboardPage(self, self.window)

    def change_sett_page(self):
        self.frame.destroy()
        self.show_page = DashboardPage(self, self.window)


class DashboardPage:
    def __init__(self, parent, window):
        self.parent = parent
        self.window = window
        self.frame = Frame(window)
        self.frame.pack()

        # Welcome button
        self.welcome_lbl = Label(self.frame, text='IT WORKED!')
        self.welcome_lbl.grid(row=0, column=1)

        # Login button
        self.login = Button(self.frame, text='TEST', command=self.test)
        self.login.grid(row=3, column=1)

    def test(self):
        self.frame.destroy()
        self.parent.parent.change_page(1)


    # def tasks_clicked(self):
        # self.parent.change_page(2)
        # creates tasks page header
        # self.header.grid_forget()
        # self.header = Label(self.frame, text="Tasks")
        # self.header.grid(row=0, column=1)

    # def settings_clicked(self):
        # self.frame.destroy()
        # self.parent.change_page(3)
        # creates settings page header
        # self.header.grid_forget()
        # self.header = Label(self.frame, text="Settings")
        # self.header.grid(row=0, column=1)


if __name__ == '__main__':
    root = Tk()
    MainGui(root, "Insidious 1.0", "1280x720")
    root.mainloop()
