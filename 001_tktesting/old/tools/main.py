import tkinter as tk
from tkinter import ttk
from tkinter import Menu

class GUI:
    def __init__(self, master,**kargs):
        self.master = master
        self.master.title("PythonGUI")
        self.master.iconbitmap('images\ico\q.ico')
        self.master.config()
        # self.ui_menu()
        self.ui_tab()

    def ui(self):
        pass

    
    def _quit(self):
        self.master.quit()
        self.master.destroy()
        exit() 


    def ui_menu(self):
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


    def ui_tab(self,master=None):
        tabControl = ttk.Notebook(self.master)          # Create Tab Control

        tab1 = ttk.Frame(tabControl)            # Create a tab 
        tabControl.add(tab1, text='第一页')      # Add the tab
        tab2 = ttk.Frame(tabControl)            # Add a second tab
        tabControl.add(tab2, text='第二页')      # Make second tab visible

        tabControl.config()
        tabControl.pack(expand=1, fill="both")  # Pack to make visible

        # LabelFrame using tab1 as the parent
        mighty = ttk.LabelFrame(tab1, text=' Mighty Python ')
        mighty.grid(column=0, row=0, padx=8, pady=4)

        # Modify adding a Label using mighty as the parent instead of self.master
        a_label = ttk.Label(mighty, text="Enter a name:")
        a_label.grid(column=0, row=0, sticky='W')





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









def main():
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
