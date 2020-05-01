# -*- encoding: utf-8 -*-

from tkinter import *
import tkinter.messagebox as messagebox  #可以看帮助文档 tkinter文件架下面由messagebox.py文件
from tkinter import filedialog  # 从文件夹里面导入子文件
import os



filename=""

def author():
    messagebox.showinfo("作者信息", "本软件由麦子学院完成")

def about():
    messagebox.showinfo("版权信息.Copyright", "本软件版权归属麦子学院")

def openfile():
    global filename
    filename = filedialog.askopenfilename(defaultextension = ".txt")
    if filename == "":
        filename = None
    else:
        root.title("FileName: " +  os.path.basename(filename))
        textPad.delete(1.0,END)
        f= open(filename,'r')
        textPad.insert(1.0,f.read())
        f.close()
    # 涉及到编码问题 gbk 的读取不了

def ctrlo(event):
    openfile()


root = Tk()
root.title('Sundy Note')
root.geometry("800x800+100+100")
root.iconbitmap("q.ico")

# Create Menu
menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar,tearoff = False)
filemenu.add_command(label = "新建", accelerator = 'Ctrl + N')
# 如何实现具体的绑定？？此时，只有显示
filemenu.add_command(label = "打开", accelerator = 'Ctrl + O',command = openfile)
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
aboutmenu.add_command(label = "作者", command = author)
aboutmenu.add_command(label = "版权", command = about)
menubar.add_cascade(label = '关于', menu=aboutmenu)

# Create Toolbar
toolbar = Frame(root, height = 25, bg='#10a8a4')
# 事件1 command 回调
shortButton = Button(toolbar, text="open", command = openfile, padx=100, pady=5)
# widget.config 配置外观
shortButton.config(cursor = "gumby", fg="yellow", bg="dark green", font = ("times","28","bold"), relief= RAISED)
shortButton.pack(side=LEFT, padx=10)

shortButton = Button(toolbar, text="保存")
shortButton.pack( side=LEFT)
toolbar.pack(expand=NO,fill=X)


top = Toplevel(bg = "yellow")

# Create statusbar
status = Label(root, text="Ln20", bd=1, fg="RED",relief = SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

#linenumber&text
lnlabel = Label(root, width=2, bg="antique white")
lnlabel.pack(side=LEFT,fill=Y)

textPad =Text(root,undo=True)
textPad.pack(expand=YES,fill=BOTH)

scroll = Scrollbar(textPad)
textPad.config(yscrollcommand=scroll.set)
scroll.config(command = textPad.yview)
scroll.pack(side=RIGHT,fill=Y)
# 事件2绑定
textPad.bind_all("<Control-o>",ctrlo)

def closedWindow():
    if messagebox.askokcancel("Quit", "退出吗?"):
        root.destroy()

# 事件3 窗口系统级
root.protocol("WM_DELETE_WINDOW",closedWindow)


root.mainloop()