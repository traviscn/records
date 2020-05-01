# from tkinter import *
import tkinter as tk
import tkinter.messagebox as tkm
import tkinter.filedialog as tkf
import tkinter.colorchooser as tkc




root=tk.Tk()
root.iconbitmap(r"C:\Users\Administrator\pyprojects\pic\QQ.ico")


# frame=tk.Frame(root,width=300,height=300,bg="pink")
# frame.pack()
def calltkm():
    filename=tkm.askyesno(title="ask标题", message="你确定吗？",icon=tkm.QUESTION)
    filename1=tkm.showwarning(title="show标题", message="内容",icon=tkm.WARNING)
    print(filename,filename1)

def calltkf():
    filename=tkf.askopenfilename(initialdir="D:/test/",filetypes=[("所有文件","*.*"),("TXT","txt"),("Word",".docx"),("ZIP",".zip")])
    print(filename)
    filename1=tkf.asksaveasfilename(initialdir="D:/test/",filetypes=[("所有文件","*.*"),("TXT","txt"),("Word",".docx"),("ZIP",".zip")])
    print(filename1)

def calltkc():
    filename=tkc.askcolor()
    print(filename)


tk.Button(root, text="标准消息对话框",width=10,height=5,relief=tk.RAISED,command=calltkm,bg="red",fg="green",justify=tk.RIGHT,padx=5,pady=5,anchor=tk.E).pack(fill=tk.X)
tk.Button(root,text="选择文件",command=calltkf).pack(side=tk.BOTTOM,fill=tk.BOTH,expand=tk.YES)
tk.Button(root,text="选择颜色",command=calltkc).pack()


tk.mainloop()
