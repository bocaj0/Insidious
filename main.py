from tkinter import *
from pathlib import Path

# Tracks the page of the app GUI
website_file_location = ''
curr_page = 0
prev_page = 0


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


# changes the pages/creates new pages for dashboard/tasks/settings
def page_change(current, num):
    global curr_page, prev_page
    curr_page = num
    if curr_page != prev_page:
        current.show_page.frame.destroy()

    if curr_page == 0:
        if prev_page != 0:
            current.show_page = DashboardPage(current, current.window)
    if curr_page == 1:
        if prev_page != 1:
            current.show_page = TasksPage(current, current.window)
    if curr_page == 2:
        if prev_page != 2:
            current.show_page = WebsitesPage(current, current.window)
    if curr_page == 3:
        if prev_page != 3:
            current.show_page = PaymentPage(current, current.window)
    if curr_page == 4:
        if prev_page != 4:
            current.show_page = ProxiesPage(current, current.window)
    if curr_page == 5:
        if prev_page != 5:
            current.show_page = CaptchaPage(current, current.window)

    prev_page = num


# creates the side labels of dashboard/tasks/settings
class BasePage:
    def __init__(self, parent, window):
        self.parent = parent
        self.window = window
        self.frame = Frame(window, width=400, height=720, bg="red")
        self.frame.pack(side=LEFT, anchor='nw', fill='both')

        # Create Buttons
        self.dashboard_btn = Button(self.frame, text="\tDashboard\t", command=lambda: page_change(self, 0))
        self.tasks_btn = Button(self.frame, text="\t   Tasks\t\t", command=lambda: page_change(self, 1))
        self.accounts_btn = Button(self.frame, text="\tWebsites\t\t", command=lambda: page_change(self, 2))
        self.payment_btn = Button(self.frame, text="        Payment/Shipping\t", command=lambda: page_change(self, 3))
        self.proxies_btn = Button(self.frame, text="\t  Proxies\t\t", command=lambda: page_change(self, 4))
        self.captcha_btn = Button(self.frame, text="\t Captcha\t\t", command=lambda: page_change(self, 5))
        self.logout_btn = Button(self.frame, text="\t  Logout\t\t", command=self.clicked)

        # Set grid
        self.dashboard_btn.grid(row=0, column=0)
        self.tasks_btn.grid(row=1, column=0)
        self.accounts_btn.grid(row=2, column=0)
        self.payment_btn.grid(row=3, column=0)
        self.proxies_btn.grid(row=4, column=0)
        self.captcha_btn.grid(row=5, column=0)
        self.logout_btn.grid(row=6, column=0)

        self.show_page = DashboardPage(self, self.window)

    def clicked(self):
        page_change(self, 10)  # random number that are not equal and do not represent a page
        self.frame.destroy()
        self.parent.change_page(0)


class DashboardPage:
    def __init__(self, parent, window):
        self.frame = Frame(window, bg="green")
        self.frame.pack(side=LEFT, anchor='nw', fill='both', expand=TRUE)

        # Welcome button
        self.welcome_lbl = Label(self.frame, text='DASHBOARD PAGE')
        self.welcome_lbl.grid(row=0, column=1)

        # Login button
        self.login = Button(self.frame, text='TEST1')
        self.login.grid(row=3, column=1)


class TasksPage:
    def __init__(self, parent, window):
        self.frame = Frame(window, bg="yellow")
        self.frame.pack(side=LEFT, anchor='nw', fill='both', expand=TRUE)

        # Welcome button
        self.welcome_lbl = Label(self.frame, text='TASKS PAGE')
        self.welcome_lbl.grid(row=0, column=1)

        # Login button
        self.login = Button(self.frame, text='TEST2')
        self.login.grid(row=3, column=1)


# destroys the popup window for adding a website
def add_website(window, entry):
    global website_file_location
    website_file_location = str(Path.cwd()) + "\\websites.txt"

    path = Path(website_file_location)

    if path.is_file():
        with open(website_file_location, 'a') as f:
            f.write('\n' + entry.get())
    else:
        with open(website_file_location, 'w') as f:
            f.write(entry.get())

    window.destroy()


class WebsitesPage:
    def __init__(self, parent, window):
        self.window = window
        self.frame = Frame(window, bg="blue")
        self.frame.pack(side=LEFT, anchor='nw', fill='both', expand=TRUE)

        # Welcome button
        self.welcome_lbl = Label(self.frame, text='WEBSITES PAGE')
        self.welcome_lbl.grid(row=0, column=1)

        # Login button
        self.login = Button(self.frame, text='ADD WEBSITE', bg="purple", fg='white', command=self.add_website_popup)
        self.login.grid(row=0, column=2)

    def add_website_popup(self):
        # Create a Toplevel window
        self.website_popup = Toplevel(self.window)
        self.website_popup.geometry('400x400')

        # Create an Entry Widget in the Toplevel window
        entry = Entry(self.website_popup, width=25)
        entry.pack()

        # Create a Button Widget in the Toplevel Window
        add_btn = Button(self.website_popup, text="Add Website", command=lambda: add_website(self.website_popup, entry))
        add_btn.pack(pady=5, side=TOP)


class PaymentPage:
    def __init__(self, parent, window):
        self.frame = Frame(window, bg="yellow")
        self.frame.pack(side=LEFT, anchor='nw', fill='both', expand=TRUE)

        # Welcome button
        self.welcome_lbl = Label(self.frame, text='PAYMENT PAGE')
        self.welcome_lbl.grid(row=0, column=1)

        # Login button
        self.login = Button(self.frame, text='TEST2')
        self.login.grid(row=3, column=1)


class ProxiesPage:
    def __init__(self, parent, window):
        self.frame = Frame(window, bg="blue")
        self.frame.pack(side=LEFT, anchor='nw', fill='both', expand=TRUE)

        # Welcome button
        self.welcome_lbl = Label(self.frame, text='Proxies PAGE')
        self.welcome_lbl.grid(row=0, column=1)

        # Login button
        self.login = Button(self.frame, text='TEST3')
        self.login.grid(row=3, column=1)


class CaptchaPage:
    def __init__(self, parent, window):
        self.frame = Frame(window, bg="yellow")
        self.frame.pack(side=LEFT, anchor='nw', fill='both', expand=TRUE)

        # Welcome button
        self.welcome_lbl = Label(self.frame, text='CAPTCHA PAGE')
        self.welcome_lbl.grid(row=0, column=1)

        # Login button
        self.login = Button(self.frame, text='TEST2')
        self.login.grid(row=3, column=1)


if __name__ == '__main__':
    root = Tk()
    MainGui(root, "Insidious 1.0", "1280x720")
    root.mainloop()
