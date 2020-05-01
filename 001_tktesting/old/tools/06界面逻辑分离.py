import tkinter as tk
from tkinter import ttk


class Application(tk.Tk): # 继承自 tk.Tk
    '''界面、逻辑分离示例'''
    
    def __init__(self):
        '''初始化'''
        super().__init__() # 有点相当于tk.Tk()
        
        self.createWidgets()

    def createWidgets(self):
        '''界面'''
        self.mainframe = ttk.Frame(self, padding="3 3 12 12") # 注意ttk.Frame()的第一个参数为self，因为这个类继承自tk.Tk类
        self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        # 定义了两个变量（下面会将它们绑定到输入部件 Entry 和标签部件 Label 上）
        # self.feet = StringVar()
        self.feet = tk.DoubleVar()
        self.meters = tk.StringVar()

        # 定义Entry部件，并把它赋给一个变量，方便在别处引用它。
        self.feet_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.feet)
        self.feet_entry.grid(row=1, column=2, sticky=(tk.W, tk.E))
        self.feet_entry.focus()

        # 定义Label部件
        ttk.Label(self.mainframe, textvariable=self.meters).grid(row=2, column=2, sticky=(tk.W, tk.E))
        
        # 定义Button部件
        ttk.Button(self.mainframe, text="Calculate", command=self.calculate).grid(row=3, column=3, sticky=tk.W)

        # 定义三个Label部件
        ttk.Label(self.mainframe, text="feet").grid(row=1, column=3, sticky=tk.W)
        ttk.Label(self.mainframe, text="is equivalent to").grid(row=2, column=1, sticky=tk.E)
        ttk.Label(self.mainframe, text="meters").grid(row=2, column=3, sticky=tk.W)
        
        # 设置每格的 padding
        for child in self.mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
            
        
        # 给窗口绑定回车键事件
        self.bind('<Return>', self.calculate)

    
    def calculate(self, *args): # 注意：参数必须是带!星!号!的 *args. 否则无论如何都会报类型错误：TypeError
        '''逻辑'''
        try:
            #value = float(self.feet.get()) # 如果前面定义为stringVar: self.feet = StringVar()
            value = self.feet.get()
            self.meters.set('{:.4f}'.format((0.3048 * value * 10000.0 + 0.5)/10000.0))
        except ValueError:
            pass


if __name__ == '__main__':
    # 实例化Application
    app = Application()
    
    # 设置窗口标题
    app.title("Feet to Meters")
    
    # 主消息循环:
    app.mainloop()