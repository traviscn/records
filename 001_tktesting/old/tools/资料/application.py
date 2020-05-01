import tkinter as tk


class App:

    def __init__(self, root):

        self.root = root
        self.root.title("TestTile")
        #self.testMenu()
        self.testEntry()

        # self.testFrame()
        # self.testLabel()
        # self.testButton()

    def testMenu(self):
        print("Hi*Menu****************************")
        # 顶级菜单
        menubar = tk.Menu(self.root)

        # 下拉菜单添加到顶级菜单中,默认tearoff=True
        filemenu = tk.Menu(menubar)
        filemenu.add_command(label="Open", command=self.sayHi)
        filemenu.add_command(label="Save", command=self.sayHi)
        filemenu.add_separator()
        filemenu.add_command(label="Quit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        # 下拉菜单添加到顶级菜单中
        editmenu = tk.Menu(menubar, tearoff=False)
        editmenu.add_command(label="Copy", command=self.sayHi)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=self.sayHi)
        menubar.add_cascade(label="Edit", menu=editmenu)

        # command = sayHi mistake
        menubar.add_command(label="Quit", command=self.root.quit)
        menubar.add_command(label="Help", command=self.sayHi)
        # 显示菜单
        self.root.config(menu=menubar)

    def testFrame(self):
        print("Hi*Frame****************************")
        frame1 = tk.Frame(self.root)
        frame2 = tk.Frame(self.root)

        frame1.pack(side=tk.LEFT, padx=20, pady=50)
        frame2.pack(side=tk.LEFT, padx=20, pady=50)
        # hits 用于复杂布局中组件分组

    def testLabel(self):
        print("Hi*Label****************************")
        textLabel = tk.Label(self.root, text="Label\n00001",
                             bg="yellow", justify=tk.RIGHT)
        textLabel.pack(side=tk.LEFT, fill=tk.X, expand=True)

        var = tk.StringVar()
        var.set("HHHHHHHHHHH")
        vartextLabel = tk.Label(
            self.root, textvariable=var, bg="green", justify=tk.RIGHT)
        vartextLabel.pack(side=tk.LEFT, fill=tk.X, expand=True)
        # pack()  默认按顺序纵向排列 通过side设置成横向排列
        # Label 描述标签 可以文字图片 还可以compound图文混排
        # var 改变现实文字涉及定义域
        photo = tk.PhotoImage(
            file="C:\\Users\Administrator\\pyprojects\\pic\\IT.gif")
        imgLabel = tk.Label(self.root, image=photo, bg="blue")
        imgLabel.pack(side=tk.RIGHT)

    def testButton(self):
        print("Hi*Button****************************")
        hiButton = tk.Button(self.root, bg="red", fg="blue",
                             text="打招呼", command=self.sayHi)
        # misktake: command=self.say_hi()
        hiButton.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # side=tkinter.TOP BOTTOM LEFTRIGHT

    def sayHi(self):
        print("Hi*小胖子****************************")
        w1 = tk.Message(self.root, text="请问你是小胖子吗？", width=600)
        w1.pack()
    def why(self,content):
        if content.isdigit():
            return True
        else:
            return False
    def cal(self):
        return 3

    def testEntry(self):
        print("Hi*Entry****************************")
        ll1=tk.Label(self.root,text="流量Q m3/s")
        ll1.grid(row=0,column=0,sticky=tk.W)
        ll2=tk.Label(self.root,text="扬程H m")
        ll2.grid(row=1,column=0,sticky=tk.W)
        ll3=tk.Label(self.root,text="转速n r/min")
        ll3.grid(row=2,column=0,sticky=tk.W)

        ss1=tk.StringVar()
        ss2=tk.StringVar()
        ss3=tk.StringVar()



        ee1=tk.Entry(self.root,textvariable=ss1)
        ee1.grid(row=0,column=1,sticky=tk.E)


        tk.Button(self.root,text="计算",command=print("YYYY"),bg="yellow").grid(row=5,column=0)
        tk.Button(self.root,text="清空",command=print("XXX"),bg="red").grid(row=5,column=1)

        # tk.Label(self.root,text="流量Q m3/s").grid(row=0,column=0)
        # tk.Entry(self.root,textvariable=tk.StringVar(),validate="focusout",validatecommand=sayHi,invalidate=sayHi).grid(row=0.column=1)

        # w1 = tk.Message(self.root, text="请问你是小胖子吗？", width=600)
        # w1.pack()


def main():
    root = tk.Tk()
    # 根窗口 作为参数实例化App对象
    app = App(root)
    root.mainloop()
    # mistake: root.mianloop


if __name__ == "__main__":
    main()
