import tkinter as tk
from tkinter import ttk
from tkinter import Menu

class GuiRoot:
    def __init__(self, master,**kwargs):
        self.master = master
        self.master.title("PythonGUI")
        self.master.iconbitmap('images\ico\q.ico')
        self.master.config(**kwargs)
        self.setupUI()

    def setupUI(self,gui_title):
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

        
        
        tab = ttk.Frame(note)
        note.add(tab, text=self.gui_title)



def main():
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()