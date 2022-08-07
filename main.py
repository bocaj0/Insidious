from tkinter import *

# Tracks the page of the app GUI
base_page = 0


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
        self.frame = Frame(window, width=400, height=720, bg="red")
        self.frame.pack(side=LEFT, anchor='nw', fill='both')

        # Create Buttons
        self.dashboard_btn = Button(self.frame, text="\tDashboard\t", command=self.change_dash_page)
        self.tasks_btn = Button(self.frame, text="\t    Tasks\t\t", command=self.change_task_page)
        self.settings_btn = Button(self.frame, text="\t  Settings\t", command=self.change_sett_page)

        # Set grid
        self.dashboard_btn.grid(row=0, column=0)
        self.tasks_btn.grid(row=1, column=0)
        self.settings_btn.grid(row=2, column=0)

        self.show_page = DashboardPage(self, self.window)

    def change_dash_page(self):
        global base_page
        if base_page != 0:
            base_page = 0
            self.show_page = DashboardPage(self, self.window)

    def change_task_page(self):
        global base_page
        if base_page != 1:
            base_page = 1
            self.show_page = TasksPage(self, self.window)

    def change_sett_page(self):
        global base_page
        if base_page != 2:
            base_page = 2
            self.show_page = SettingsPage(self, self.window)


class DashboardPage:
    def __init__(self, parent, window):
        global base_page
        self.frame = Frame(window, bg="blue")
        self.frame.pack()

        # Welcome button
        self.welcome_lbl = Label(self.frame, text='dash!')
        self.welcome_lbl.grid(row=0, column=1)

        # Login button
        self.login = Button(self.frame, text='TEST1')
        self.login.grid(row=3, column=1)

        if base_page != 0:
            self.frame.destroy()
            # self.parent.parent.change_page(0)


class TasksPage:
    def __init__(self, parent, window):
        global base_page
        self.frame = Frame(window, bg="blue")
        self.frame.pack()

        # Welcome button
        self.welcome_lbl = Label(self.frame, text='TASKS!')
        self.welcome_lbl.grid(row=0, column=1)

        # Login button
        self.login = Button(self.frame, text='TEST2')
        self.login.grid(row=3, column=1)

        if base_page != 1:
            self.frame.destroy()


class SettingsPage:
    def __init__(self, parent, window):
        global base_page
        self.frame = Frame(window, bg="blue")
        self.frame.pack()

        # Welcome button
        self.welcome_lbl = Label(self.frame, text='Settings!')
        self.welcome_lbl.grid(row=0, column=1)

        # Login button
        self.login = Button(self.frame, text='TEST3')
        self.login.grid(row=3, column=1)

        if base_page != 2:
            self.frame.destroy()


if __name__ == '__main__':
    root = Tk()
    MainGui(root, "Insidious 1.0", "1280x720")
    root.mainloop()
