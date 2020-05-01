# -*- encoding: utf-8 -*-

from tkinter import *
import tkinter.messagebox as messagebox  
from tkinter import filedialog 
import os

class SunnyNote:
    def __init__(self,master=None):
        self.master = master
        self.menu_ui()
        self.toolbar_ui()
        self.status_ui()
        self.textpad_ui()
    def menu_ui(self):
        # Create Menupython 
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        filemenu = Menu(menubar,tearoff = False)
        filemenu.add_command(label = "新建", accelerator = 'Ctrl + N')
        filemenu.add_command(label = "打开", accelerator = 'Ctrl + O',command = self.openfile)
        filemenu.add_command(label = "保存", accelerator = 'Ctrl + S')
        filemenu.add_command(label = "另存为", accelerator = 'Ctrl + Shift+ S')
        menubar.add_cascade(label = '文件', menu=filemenu)

        editmenu = Menu(menubar)
        editmenu.add_command(label = "撤销", accelerator = 'Ctrl + Z')
        editmenu.add_command(label = "重做", accelerator = 'Ctrl + Y')
        editmenu.add_separator()
        editmenu.add_command(label = "剪切", accelerator = 'Ctrl + X')
        editmenu.add_command(label = "复制", accelerator = 'Ctrl + C')
        editmenu.add_command(label = "粘贴", accelerator = 'Ctrl + V')
        editmenu.add_separator()
        editmenu.add_command(label = "查找", accelerator = 'Ctrl + F')
        editmenu.add_command(label = "全选", accelerator = 'Ctrl + A')
        menubar.add_cascade(label = "编辑", menu = editmenu)

        aboutmenu = Menu(menubar)
        aboutmenu.add_command(label = "作者", command = self.author)
        menubar.add_cascade(label = '关于', menu=aboutmenu)
    def toolbar_ui(self):
        # Create Toolbar
        toolbar = Frame(self.master, height = 25, bg='#10a8a4')
        shortButton = Button(toolbar, text="open", command = self.openfile, padx=100, pady=5)
        shortButton.config(fg="yellow", bg="dark green", font = ("times","28","bold"), relief= RAISED)
        shortButton.pack(side=LEFT, padx=10)

        shortButton = Button(toolbar, text="保存")
        shortButton.pack( side=LEFT)
        toolbar.pack(expand=NO,fill=X)
    def status_ui(self):
        # Create statusbar
        status = Label(self.master, text="Ln20", bd=1, fg="RED",relief = SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)

        #linenumber&text
        lnlabel = Label(self.master, width=2, bg="antique white")
        lnlabel.pack(side=LEFT,fill=Y)
    def author(self):
        messagebox.showinfo("作者信息", "本软件由麦子学院完成")
    def textpad_ui(self):
        textPad =Text(self.master,undo=True)
        textPad.pack(expand=YES,fill=BOTH)

        scroll = Scrollbar(textPad)
        textPad.config(yscrollcommand=scroll.set)
        scroll.config(command = textPad.yview)
        scroll.pack(side=RIGHT,fill=Y)

    filename = ""
    def openfile(self):
        global filename
        filename = filedialog.askopenfilename(defaultextension = ".txt")
        if filename == "":
            filename = None
        else:
            self.master.title("FileName: " +  os.path.basename(filename))
            textPad.delete(1.0,END)
            f= open(filename,'r')
            textPad.insert(1.0,f.read())
            f.close()

def test():
    root = Tk() 
    SunnyNote(master = root)
    root.mainloop()

if __name__ == "__main__":
    test()