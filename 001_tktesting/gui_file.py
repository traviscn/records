from tkinter import *

class GuiFile:
    def __init__(self,master,**kwrags):

        self.master = master
        self.create_widget()

    def create_widget(self):
        btn=Button(self.master, text="测试")
        btn.pack()