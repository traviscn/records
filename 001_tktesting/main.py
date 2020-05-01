# -*- encoding: utf-8 -*-

from tkinter import *
from gui_master import GuiMaster

def main():
    root = Tk() 
    # root.config()   
    GuiMaster(master = root)
    root.mainloop()

if __name__ == "__main__":
    main()