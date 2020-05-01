import tkinter as tk
from tkinter import ttk
from tkinter import Menu

class GUI:
    def __init__(self, master,**kargs):
        self.master = master
        self.master.title("PythonGUI")
        self.master.iconbitmap('images\ico\q.ico')
        self.master.config()
        self.ui_menu()
        self.ui_tab()


        tabControl = ttk.Notebook(self.master)          # Create Tab Control




    def ui_menu():
        menu_bar = Menu(self.master)
        self.master.config(menu=menu_bar)

        # Add menu items
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=_quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Add another Menu to the Menu Bar and an item
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About")
        menu_bar.add_cascade(label="Help", menu=help_menu)


    def ui_tab():
        passS




    def ui(self):
        frame1 = tk.Frame(self.master)
        frame1.pack()
        theLabel1 = tk.Label(frame1, text="CC")
        theLabel1.pack()

        frame2 = tk.Frame(self.master)
        frame2.pack()
        theLabel2 = tk.Label(frame2, text="CCC")
        theLabel2.pack()

        frame3 = tk.Frame(self.master)
        frame3.pack()
        note = ttk.Notebook(frame3)
        note.pack()

        tab_name = ["File", "Edit", "Modify",
                    "Generate", "Analysis", "Setting", "About"]
        for i in range(len(tab_name)):
            tab = ttk.Frame(note)
            note.add(tab, text=tab_name[i])

class GlobalVar():
    def __init__(self):
        pass

    def log(self, text):
        pass



