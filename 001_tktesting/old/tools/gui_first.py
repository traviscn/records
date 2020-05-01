import tkinter as tk
from myApp import GuiRoot

class GuiFirst():
    def __init__(self,master):
        self.master= master
        self.master.title("PythonGUI")
        self.setupUI()

    def ui(self):
        frame1 = tk.Frame(self.master)
        frame1.pack()
        theLabel1 = tk.Label(frame1, text="CC")
        theLabel1.pack()

        frame2 = tk.Frame(self.master)
        frame2.pack()
        theLabel2 = tk.Label(frame2, text="CCC")
        theLabel2.pack()



if __name__ == "__main__":
    app = GuiFirst(GuiRoot)
    main()