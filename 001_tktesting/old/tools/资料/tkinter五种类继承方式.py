import tkinter as tk

# 继承object 方式一 引用tk.Frame给parent self.rootframe = tk.Frame(parent) tk.Label(self.rootframe)


# class MyApp(object):
#     def __init__(self, parent):
#         self.rootframe = tk.Frame(parent)
#         self.rootframe.pack()

#         self.setupUI()

#     def setupUI(self):
#         tk.Label(self.rootframe, text="标签").pack()


# if __name__ == "__main__":
#     root = tk.Tk()
#     MyApp(root)
#     root.mainloop()

#继承object 方式二 #self.root = parent  tk.Label(self.root)

class MyApp(object):
    def __init__(self,parent,**kwargs):
        self.root = parent
        self.root.config(**kwargs)

        self.setupUI()

    def setupUI(self):
        tk.Label(self.root, text="标签").pack()

def main():
    root = tk.Tk()
    app=MyApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

# 继承 tk.Tk

# class MyApp(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.setupUI()

#     def setupUI(self):
#         tk.Label(self, text="标签").pack()


# if __name__ == "__main__":
#     MyApp().mainloop()

# # 继承 tk.Frame 方式一 有 parent

# class MyApp(tk.Frame):
#     def __init__(self,parent=tk.NONE):
#         super().__init__(parent)
#         self.pack()

#         self.setupUI()

#     def setupUI(self):
#         tk.Label(self, text="标签").pack()


# if __name__ == "__main__":
#     MyApp(tk.Tk()).mainloop()

# # 继承 tk.Frame 方式二 沒有 parent

# class MyApp(tk.Frame):
#     def __init__(self):
#         super().__init__()
#         self.pack()

#         self.setupUI()

#     def setupUI(self):
#         tk.Label(self, text="标签").pack()


# if __name__ == "__main__":
#     MyApp().mainloop()
