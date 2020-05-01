import tkinter as tk
# 由于tkinter中没有ToolTip功能，所以自定义这个功能如下


class ToolTip():
    def __init__(self, widget, text):
        self.widget = widget
        self.text=text
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
        self.widget.bind('<Enter>', self.showtip)
        self.widget.bind('<Leave>', self.hidetip)
        print(self.widget,self.text)
        print(bool(self.text))

    def showtip(self, text):
        "Display text in tooltip window" 
        if self.tipwindow or not self.text:#??????????
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))

        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                         background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self,event):  #######为什么一定要加上event?
        # tw = self.tipwindow
        # if tw:
        #     tw.destroy()
        # self.tipwindow = None
        self.tipwindow.destroy()
        self.tipwindow = None


    # def enter(self,event):
    #     self.showtip(self.text)

    # def leave(self,event):
    #     self.hidetip()

# ===================================================================

if __name__=="__main__":

    def change():
        b.configure(text='Hello\n ')
        b.configure(state='disabled')    # Disable the Button Widget


    root = tk.Tk()

    b = tk.Button(root, text="点击一次", command=change)
    c = tk.Label(root, text="点击")


    b.pack()
    c.pack()


    # Add Tooltip
    ToolTip(b,       '这是一个Button.')
    # ToolTip(c,       '')
    ToolTip(c,       '这是一个Label.')

    root.mainloop()
