# -*- encoding: utf-8 -*-

import os
from tkinter import *
# import tkinter.messagebox as messagebox  #可以看帮助文档 tkinter文件架下面由messagebox.py文件
from tkinter import filedialog  # 从文件夹里面导入子文件
from tkinter import messagebox  # 可以看帮助文档 tkinter文件架下面由messagebox.py文件


class GuiMaster:
    """FirstGui"""
    def __init__(self,master=None):
        self.master = master
        #变量定义？？
        filename=""
        self.menu_ui()
        self.toolbar_ui()
        self.status_ui()
        self.textpad_ui()


        # 事件3 窗口系统级
        self.master.protocol("WM_DELETE_WINDOW",self.closedWindow)
        # 事件2绑定
        self.master.bind_all("<Control-o>",self.ctrlo)


    def menu_ui(self):
        # Create Menupython 
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        filemenu = Menu(menubar,tearoff = False)
        filemenu.add_command(label = "新建", accelerator = 'Ctrl + N')
        # 如何实现具体的绑定？？此时，只有显示
        filemenu.add_command(label = "打开", accelerator = 'Ctrl + O',command = self.openfile) #ruhe diaoyongwaibu?、?
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
        aboutmenu.add_command(label = "版权", command = self.about)
        menubar.add_cascade(label = '关于', menu=aboutmenu)
    def toolbar_ui(self):
        # Create Toolbar
        toolbar = Frame(self.master, height = 25, bg='#10a8a4')
        # 事件1 command 回调
        shortButton = Button(toolbar, text="open", command = self.openfile, padx=100, pady=5)
        # widget.config 配置外观
        shortButton.config(cursor = "gumby", fg="yellow", bg="dark green", font = ("times","28","bold"), relief= RAISED)
        shortButton.pack(side=LEFT, padx=10)

        shortButton = Button(toolbar, text="保存")
        shortButton.pack( side=LEFT)
        toolbar.pack(expand=NO,fill=X)


        #top = Toplevel(bg = "yellow")
    def status_ui(self):
        # Create statusbar
        status = Label(self.master, text="Ln20", bd=1, fg="RED",relief = SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)

        #linenumber&text
        lnlabel = Label(self.master, width=2, bg="antique white")
        lnlabel.pack(side=LEFT,fill=Y)
    def textpad_ui(self):
        textPad =Text(self.master,undo=True)
        textPad.pack(expand=YES,fill=BOTH)

        scroll = Scrollbar(textPad)
        textPad.config(yscrollcommand=scroll.set)
        scroll.config(command = textPad.yview)
        scroll.pack(side=RIGHT,fill=Y)

    ###什么时候卸载外面 什么时候卸载里面
    def author(self):
        messagebox.showinfo("作者信息", "本软件由麦子学院完成")

    def about(self):
        messagebox.showinfo("版权信息.Copyright", "本软件版权归属麦子学院")
    ## 函数内怎么调用组件？？？
    ##函数内调用其他函数的变量
    def openfile(self):
        global filename
        filename = filedialog.askopenfilename(defaultextension = ".txt")
        if filename == "":
            filename = None
        else:
            self.master.title("FileName: " +  os.path.basename(filename))
            self.master.textPad.delete(1.0,END)
            f= open(filename,'r')
            self.master.textPad.insert(1.0,f.read())
            f.close()
        # 涉及到编码问题 gbk 的读取不了

    def ctrlo(self, event):
        self.openfile()

    def closedWindow(self):
        if messagebox.askokcancel("Quit", "退出吗?"):
            self.master.destroy()



def test():
    root = Tk() 
    # root.config()   
    root.title('Sundy Note')
    root.geometry("800x800+100+100")
    root.iconbitmap("q.ico")
    GuiMaster(master = root)
    root.mainloop()

if __name__ == "__main__":
    test()