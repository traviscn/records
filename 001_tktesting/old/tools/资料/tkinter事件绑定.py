import tkinter as tk

root=tk.Tk()


frame=tk.Frame(root,width=200,height=200,bg="blue")
frame.pack()
frame1=tk.Frame(root,width=200,height=200,bg="yellow")
frame1.pack()
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

frame.bind("<Button-1>",callbackbutton)

# frame.bind("<Motion>",callback)
frame1.bind("<Control-Shift-KeyPress-O>",callbackkey)
# frame1.bind("<Control-Shift-KeyPress-F>",callbackkey)
frame1.focus_set()


tk.mainloop()