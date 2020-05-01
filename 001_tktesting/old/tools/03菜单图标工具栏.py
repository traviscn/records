import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog, colorchooser
from tkinter import ttk
from PIL import Image, ImageTk

import time
import threading

def showdialog():
    '''各种窗口'''
    #res = messagebox.askokcancel(title='标题', message='提示信息。。。', default=messagebox.CANCEL) # default=messagebox.CANCEL，指定默认焦点位置，另 ABORT/RETRY/IGNORE/OK/CANCEL/YES/NO
    #res = messagebox.showinfo(title='标题', message='提示信息。。。')
    #res = messagebox.showwarning(title='标题', message='提示信息。。。')
    #res = messagebox.showerror(title='标题', message='提示信息。。。')
    #res = messagebox.askquestion(title='标题', message='提示信息。。。') 
    #res = messagebox.askyesno(title='标题', message='提示信息。。。')
    #res = messagebox.askyesnocancel(title='标题', message='提示信息。。。')
    #res = messagebox.askretrycancel(title='标题', message='提示信息。。。')
    
    #res = filedialog.askdirectory()
    #res = filedialog.askopenfile(filetypes=[('xml', '*.xml')])
    #res = filedialog.askopenfiles()
    #res = filedialog.askopenfilename()
    #res = filedialog.askopenfilenames()
    #res = filedialog.asksaveasfile()
    #res = filedialog.asksaveasfilename()
   
    #res = simpledialog.askinteger(title='整数', prompt='输入一个整数', initialvalue=100)
    #res = simpledialog.askfloat(titlee='实数', prompt='输入一个实数', minvalue=0, maxvalue=11)
    res = simpledialog.askstring(title='字符串', prompt='输入一个字符串')
    
    #res = colorchooser.askcolor()
    print(res)
   



class Application(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.geometry('677x442')                  # 窗口大小
        #self.resizable(width=False, height=False) # 禁止改变窗口大小
        
        self.createUI()

    # 生成界面
    def createUI(self):
        self.createICO()
        self.createMenu()
        self.createToolbar()
        self.bindAll()
    
    # 创建菜单
    def createMenu(self):
        '''只支持两层嵌套'''
        menus = ['文件', '编辑', '帮助']
        items = [['新建', '打开', '保存', '另存为...', '关闭', '-', '退出'],
                 ['撤销', '-',  '剪切', '复制', '粘贴', '删除', '选择所有',['更多...','数据', '图表', '统计']],
                 ['索引', '关于']]
        callbacks = [[showdialog, showdialog, showdialog, showdialog, showdialog, None, showdialog],
                     [showdialog, None, showdialog, showdialog, showdialog, showdialog, showdialog, [showdialog, showdialog, showdialog]],
                     [showdialog, showdialog]]
        icos = [[self.img1, self.img2, self.img3, None, self.img4, None, None],
                [self.img1, None, self.img2, self.img3, None, self.img4, None, [self.img3, None, self.img4]],
                [self.img1, self.img2]]
        
        menubar = tk.Menu(self)
        for i,x in enumerate(menus):
            m = tk.Menu(menubar, tearoff=0)
            for item, callback, ico in zip(items[i], callbacks[i], icos[i]):
                if isinstance(item, list):
                    sm = tk.Menu(menubar, tearoff=0)
                    for subitem, subcallback, subico in zip(item[1:], callback, ico):
                        if subitem == '-':
                            sm.add_separator()
                        else:
                            sm.add_command(label=subitem, command=subcallback, image=subico, compound='left')
                    m.add_cascade(label=item[0], menu=sm)
                elif item == '-':
                    m.add_separator()
                else:
                    m.add_command(label=item, command=callback, image=ico, compound='left')
            menubar.add_cascade(label=x, menu=m)
        self.config(menu=menubar)
        
    # 生成所有需要的图标
    def createICO(self):
        self.img1 = ImageTk.PhotoImage(Image.open('..\images\jpg\IT.jpg'))
        self.img2 = ImageTk.PhotoImage(Image.open('..\images\jpg\IT.jpg'))
        self.img3 = ImageTk.PhotoImage(Image.open('..\images\jpg\IT.jpg'))
        self.img4 = ImageTk.PhotoImage(Image.open('..\images\jpg\IT.jpg'))
        #self.img5 = ImageTk.PhotoImage(Image.open('ico_new.jpg'))
        #self.img6 = ImageTk.PhotoImage(Image.open('ico_open.jpg'))
        
    # 生成工具条
    def createToolbar(self):
        toolframe = tk.Frame(self, height=20, bg='#F7EED6')#, relief=tk.RAISED)
        frame = tk.Frame(toolframe, bg='#F7EED6')
        ttk.Button(frame, width=20, image=self.img1, command=showdialog).grid(row=0, column=0, padx=1, pady=1, sticky=tk.E)
        ttk.Button(frame, width=20, image=self.img2, command=showdialog).grid(row=0, column=1, padx=1, pady=1, sticky=tk.E)
        ttk.Button(frame, width=20, image=self.img3, command=showdialog).grid(row=0, column=2, padx=1, pady=1, sticky=tk.E)
        frame.pack(side=tk.LEFT)
        toolframe.pack(fill=tk.X)
        
    #def createLayout(self):
        leftframe = tk.Frame(self, width=120, bg='#0000FF')
        ttk.Treeview()
        leftframe.pack(side=tk.LEFT, fill=tk.Y)
        mainframe = tk.Frame(self, bg='#00FFFF')
        tk.Text(mainframe).pack(side=tk.LEFT, fill=tk.X)
        ttk.Scrollbar(mainframe).pack(side=tk.LEFT,fill=tk.Y)
        mainframe.pack(side=tk.LEFT, fill=tk.BOTH)
        
    # 绑定快捷键
    def bindAll(self):
        self.bind_all('<Control-n>', lambda event:showdialog()) # 此处必须 lambda

    # 打包入线程（耗时的操作）
    @staticmethod
    def thread_it(func, *args):
        t = threading.Thread(target=func, args=args) 
        t.setDaemon(True)
        t.start()

        
        
app = Application()
app.mainloop()