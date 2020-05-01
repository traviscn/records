# from tkinter import *
import tkinter as tk
import math
from tkinter  import ttk
import tkinter.messagebox as tkm
import tkinter.filedialog as tkf
import tkinter.colorchooser as tkc

from tkinter.tix import Tk, Control, ComboBox  #升级的组合控件包
# from tkinter.messagebox import showinfo, showwarning, showerror #各种类型的提示框
# from .tkinter.Part.Tooltips_copy_2 import ToolTip as ttip
from tools.Tooltips_copy_2 import ToolTip as ttip

# 相对位置如何引用 part 下面子包






root = tk.Tk()
root.iconbitmap("images\ico\QQ.ico")
root.title("tkinter GUI")

#root.geometry("800x500")    # 设置窗口大小 注意：是x 不是*
root.resizable(width=False, height=False) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
root.tk.eval('package require Tix')  #引入升级包，这样才能使用升级的组合控件


def sayHi():
    var.set("Button command\n used,so \ntextvariable\n changed\n 动态标签")
    print(vvar.get())
    # colorc = colorchooser.askcolor()
    # print(colorc)


def cal():
    result = 3.65*float(sss[2].get())*math.sqrt(float(sss[0].get())
                                                )/math.pow(float(sss[1].get()), 0.75)
    ee5.insert(0, result)
    rr.set(result)


def test(content):
    if content.isdigit():
        return True
    else:
        return False
tabControl=ttk.Notebook(root) #创建Notebook

frame1 = tk.LabelFrame(tabControl, text="Label-Label") #新建选项卡 tab1 
# frame1.pack(side=tk.LEFT)
frame2 = tk.LabelFrame(tabControl, text="Label-BUtton")
# frame2.pack(side=tk.LEFT)
frame3 = tk.LabelFrame(tabControl, text="Label-=Entry")
# frame3.pack(side=tk.LEFT)
tabC5 = tk.LabelFrame(tabControl, text="Tix")
tabC = ttk.Notebook(tabControl)

tabC2=tk.LabelFrame(tabC,text="No2")
tabC1=tk.LabelFrame(tabC,text="No1")
tabC3=tk.LabelFrame(tabC,text="No3")

tabC.add(tabC1,text="标准对话框")   #相当于pack()
tabC.add(tabC2,text="事件绑定")
tabC.add(tabC3,text="tkinter类继承主要方式")


tabControl.add(frame1,text="空间布局") #把选项卡加到Notebook中
tabControl.add(frame2,text="常见按钮")
tabControl.add(frame3,text="交互")
tabControl.add(tabC,text="绑定对话框")
tabControl.add(tabC5,text="tkinter.Tix")



tabControl.pack(side=tk.LEFT)

tabC.select(tabC3)
tabControl.select(frame2)

v = tk.IntVar()
var = tk.StringVar()

menubar = tk.Menu(root)
# 下拉菜单添加到顶级菜单中,默认tearoff=True
openVar = tk.IntVar()
saveVar = tk.IntVar()
editVar = tk.IntVar()
filemenu = tk.Menu(menubar)
filemenu.add_checkbutton(label="Open", command=sayHi, variable=openVar)
filemenu.add_checkbutton(label="Save", command=sayHi, variable=saveVar)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
# 下拉菜单添加到顶级菜单中
editmenu = tk.Menu(menubar, tearoff=False)
editmenu.add_radiobutton(label="Copy", command=sayHi,
                         variable=editVar, value=1)
editmenu.add_command(label="Copy2", command=sayHi)
editmenu.add_separator()
editmenu.add_radiobutton(label="Cut", command=sayHi, variable=editVar, value=2)
menubar.add_cascade(label="Edit", menu=editmenu)
# command = sayHi mistake
menubar.add_command(label="Quit22", command=root.quit)
menubar.add_command(label="Help", command=sayHi)
# 显示菜单
root.config(menu=menubar)
# 用于菜单按钮出现在其他位置
mb = tk.Menubutton(frame1, text="Menubutton", relief=tk.RAISED)
mb.pack()
filemenu2 = tk.Menu(mb)
filemenu2.add_command(label="打开", command=sayHi)
filemenu2.add_separator()
filemenu2.add_command(label="保存", command=sayHi)
mb.config(menu=filemenu2)


#TopLevel 顶级窗口组件蕾丝Frame 但是他哟偶一个独立的出口有自己的标题边框等等
def sayTop():
    top = tk.Toplevel()
    top.title("顶级窗口")
    tk.Button(top,text="Button in\n Top",command=sayHi).pack()
    top.attributes("-alpha",0.8) #设置和获取窗口属性
    msg=tk.Message(top,text="topopoppop")
    msg.pack()

# 可以出现多个Top如何控制只出现一个
tk.Button(frame1,text="弹出顶级窗口",command=sayTop).pack()
# pack()  默认按顺序纵向排列 通过side设置成横向排列
# Label 描述标签 可以文字图片 还可以compound图文混排
# var 改变现实文字涉及定义域
OPTIONS=["Python", "C++", "Ruby", "Java"]
vvar=tk.StringVar()
vvar.set(OPTIONS[0])

# 菜单选项 蕾丝下拉列表框
w=tk.OptionMenu(frame1,vvar,*OPTIONS)
w.pack()

tk.Button(frame1,text="选了啥？",command=sayHi).pack()


tk.Message(frame1,text="Message跟Label差不多，用于显示多行文本信息",width=200).pack()

textLabel = tk.Label(frame1, text="text\nLabel组件\n文字",
                     bg="yellow", justify=tk.RIGHT, padx=1)
textLabel.pack(side=tk.LEFT, fill=tk.X)
var.set("textvariable\nStringSta()动态标签")
vartextLabel = tk.Label(frame1, textvariable=var,
                        bg="green", fg="red", justify=tk.LEFT, padx=20)
vartextLabel.pack(side=tk.RIGHT, fill=tk.Y)
frame11 = tk.LabelFrame(frame1, text="二级Label")
frame11.pack(side=tk.LEFT, fill=tk.Y)
photo = tk.PhotoImage(file="images\png\IT.PNG")
imgLabel = tk.Label(frame11, image=photo, bg="blue")
imgLabel.pack()
photo1 = tk.PhotoImage(file="images\png\DO.PNG")

imgLabel1 = tk.Label(frame11, text="compound\n图文混排", image=photo1,compound=tk.CENTER, fg="black", bg="blue", font=("Arial", 20))
imgLabel1.pack()
theButton = tk.Button(frame1, text="Button\ncommand", command=sayHi)
theButton.pack(anchor=tk.S)

grp = tk.LabelFrame(frame2, text="Radiobutton", padx=5, pady=5)
grp.pack(side=tk.LEFT)

LANGS = [("Python", 1), ("C++", 2), ("Ruby", 3),
         ("Java", 4), ("one", 1), ("Two", 2), ("Five", 5)]
# 单选共享同一个variable选项，且需要设置不同的value,用于表示选中,相同的value会被同时选中！value值覆盖intVar（）1
for lang, num in LANGS:
    # b=tk.Radiobutton(grp,text=lang,value=num)
    b = tk.Radiobutton(grp, text=lang, variable=v, value=num)
    # b=tk.Radiobutton(grp,text=lang,variable=v,value=num)
    b.pack(anchor=tk.W)


# tk.Radiobutton(grp,text="one",variable=v,value=1).pack(anchor=tk.W)
# tk.Radiobutton(grp,text="one_again",variable=v,value=1).pack(anchor=tk.W)
# tk.Radiobutton(grp,text="two",variable=v,value=2).pack(anchor=tk.W)
# 单选 同一个tkinter变量IntVar（）


grp1 = tk.LabelFrame(frame2, text="Checkbutton", padx=5, pady=5)
grp1.pack(side=tk.RIGHT)

l = tk.Label(frame2, textvariable=v, bg="red")
l.pack(side=tk.LEFT, fill=tk.X, anchor=tk.N)


LANGSS = ["Python", "C++", "Ruby", "Java"]
vvv = []
# IntVar（） 是tkinter变量，用于按钮是否被选中，没有variable也是可以的，不能动态显示按钮是否被选中
# 多选 选中则是不同，单独拥有tkinter变量IntVar（）
for i in LANGSS:
    vvv.append(tk.IntVar())
    # b=tk.Checkbutton(grp1,text=i)
    b = tk.Checkbutton(grp1, text=i, variable=vvv[-1])
    b.pack(anchor=tk.W)

for i in range(4):
    ll = tk.Label(frame2, textvariable=vvv[i], bg="green")
    ll.pack(fill=tk.X)

sb=tk.Scrollbar(frame2)
# sb.pack()
sb.pack(side=tk.RIGHT,fill=tk.Y)

theLB=tk.Listbox(frame2,setgrid=True,height=12,yscrollcommand=sb.set)
# STEP1 yscrollcommand=sb.set
# theLB=tk.Listbox(frame2,setgrid=True,height=12,selectmode=tk.MULTIPLE)
theLB.pack(side=tk.RIGHT)
for i in range(30):
    theLB.insert(tk.END,i)

ttw=tk.Button(frame2,text="删除所有",command= lambda x=theLB:x.delete(0,tk.END))
# ttw=tk.Button(frame2,text="删除所有",command= theLB.delete(0,tk.END))
# 如果不用lambda函数直接用相当于直接调用了，一次性的
ttw.pack()
Bactive=tk.Button(frame2,text="删除所选",command= lambda x=theLB:x.delete(tk.ACTIVE))
Bactive.pack()


sb.config(command=theLB.yview)
#Step2 listbox.yview



# 奖函数包装起来可以带参数返回 %P最新输入内容
testCMD = root.register(test)

namelist = ["流量Q m3/s", "扬程H m", "转速n r/min", "效率", "NPSH"]
sss = []
for i in range(len(namelist)):
    tk.Label(frame3, text=namelist[i]).grid(row=i, column=0, sticky=tk.W)
    sss.append(tk.StringVar())
    ee = tk.Entry(frame3, textvariable=sss[-1], validate="focusout",
                  validatecommand=(testCMD, "%P"), invalidcommand=sayHi)
    ee.grid(row=i, column=1, sticky=tk.E)
    ee.delete(0, tk.END)

tk.Label(frame3,image=photo).grid(row=0,column=2,columnspan=6,sticky=tk.S)

tk.Button(frame3, text="计算", command=cal, bg="yellow").grid(
    row=len(namelist), column=0)
tk.Button(frame3, text="清空", command=sayHi, bg="red").grid(
    row=len(namelist), column=1)

rr = tk.StringVar()
ll5 = tk.Label(frame3, textvariable=rr)

ll5.grid(row=len(namelist)+1, column=1, sticky=tk.E)

ee5 = tk.Spinbox(frame3, values=("m","mm","cm"))
ee5.grid(row=len(namelist)+1, column=1, sticky=tk.E,rowspan=3)
ee6=tk.Entry(frame3, textvariable=tk.StringVar(), show="*",validate="focusout",
                  validatecommand=(testCMD, "%P"), invalidcommand=sayHi)
ee6.grid(row=len(namelist)+2, column=0, sticky=tk.E,rowspan=2)
ee6.insert(0,"加密显示")
# tk.Message(frame3,text=ee6.get()).grid(row=len(namelist)+3, column=0, sticky=tk.E)
# 如何动态显示加密内容
tk.Label(frame3,text=ee6.get()).grid(row=len(namelist)+3, column=0, sticky=tk.E)


# PanedWindow组件蕾丝Frame 空间管理组件,创建了三窗格

mm1= tk.PanedWindow(frame1, showhandle=True,sashrelief=tk.SUNKEN)
mm1.pack(side=tk.LEFT)
left=tk.Button(mm1,text="Left Pane",command=sayHi,bg="green")
left.pack()
mm1.add(left)
mm2= tk.PanedWindow(frame1, orient=tk.VERTICAL)
mm1.add(mm2)

def getText():
    print(text.get(1.2,2.6))
    print(text.get(1.0,line.end))



top=tk.Button(mm2,text="top Pane",command=sayHi,bg="red")
top.pack()
mm2.add(top)
bottom=tk.Button(mm2,text="bottom Pane",command=sayHi,bg="blue")
bottom.pack()
mm2.add(bottom)
# Text显示和处理多行文本 同意支持插入image对象跟Windows组件
# indexes marks tags事件绑定 字体颜色等等
text=tk.Text(root,width=30,height=20)
text.pack()
text.insert(tk.INSERT,"I LOVE\n")
text.insert(tk.END,"XXHXHXH\n")
bbb=tk.Button(text,text="内嵌按钮",command= getText)
bbb.pack()
text.window_create(tk.INSERT,window=bbb)
text.image_create(tk.END,image=photo)

# Canvas 显示和编辑图形
# arc bitmap image polygon line rectangle text window oval..

ww=tk.Canvas(root,width=200,height=200,bg="green")
ww.pack()
ww.create_line(0,0,200,200,fill="red",dash=(4,4))
ww.create_rectangle(0,0,100,100,fill="pink")
ww.create_text(50,50,text="文本")
ww.create_oval(50,100,200,200,fill="blue")

tk.Button(root,text="删除所有Canvas对象",command=lambda x=tk.ALL:ww.delete(x)).pack()

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

tk.Button(tabC1, text="标准消息对话框",width=10,height=5,relief=tk.RAISED,command=calltkm,bg="red",fg="green",justify=tk.RIGHT,padx=5,pady=5,anchor=tk.E).pack(fill=tk.X)
tk.Button(tabC1,text="选择文件",command=calltkf).pack(side=tk.BOTTOM,fill=tk.BOTH,expand=tk.YES)
tk.Button(tabC1,text="选择颜色",command=calltkc).pack()

frame_tabC=tk.Frame(tabC2,width=200,height=200,bg="blue")
frame_tabC.pack(side=tk.LEFT,anchor=tk.N)
frame1_tabC=tk.Frame(tabC2,width=200,height=200,bg="yellow")
frame1_tabC.pack()
def callbackbutton(event):
    print("组件：{}".format(event.widget))
    print("坐标位置：{},{}".format(event.x,event.y))
    print("相对位置：{},{}".format(event.x_root,event.y_root))
    print("事件类型：{}".format(event.type))
def callbackkey(event):
    print("按键是：{},{},{}".format(event.char,event.keysym,event.keycode))
    print("坐标位置：{},{}".format(event.x,event.y))
    print("相对位置：{},{}".format(event.x_root,event.y_root))
    print("事件类型：{}".format(event.type))

frame_tabC.bind("<Button-1>",callbackbutton)

# frame.bind("<Motion>",callback)
frame1_tabC.bind("<Control-Shift-KeyPress-O>",callbackkey)
# frame1.bind("<Control-Shift-KeyPress-F>",callbackkey)
frame1_tabC.focus_set()

text_tabC3=tk.Text(tabC3,width=50,height=25)
text_tabC3.pack()
text_tabC3.insert(tk.INSERT,
'''
class MyApp(object):
    def __init__(self,root,**kwargs):
        self.root = root
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
    '''
    )

bbb=tk.Button(tabC3,text="五种继承方式代码查看",command= sayHi)
bbb.pack()

ct=Control(tabC5,label='Number:',integer=True,max=12,min=2,value=2,step=2)
ct.label.config(font='Helvetica 14 bold')
ct.pack()

cb=ComboBox(tabC5,label='Type:',editable=True)
for animal in ('dog','cat','hamster','python'):
    cb.insert(tk.END,animal)
cb.pack()

ttip(ttw,"这是一个 Button")
ttip(Bactive,"这是一个啥？")

tk.mainloop()
