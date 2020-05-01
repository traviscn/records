#这是系统的登录界面  
import tkinter 

#from tkinter import messagebox
import tkinter.messagebox as messagebox
class Login(object):  
    def __init__(self):  
        # 创建主窗口,用于容纳其它组件  
        self.root = tkinter.Tk()  
        # 给主窗口设置标题内容  
        self.root.title("影视资源管理系统(离线版)")  
        self.root.geometry('450x300')  
        #运行代码时记得添加一个gif图片文件，不然是会出错的
        self.canvas = tkinter.Canvas(self.root, height=200, width=500)#创建画布  
        self.image_file = tkinter.PhotoImage(file='..\images\gif\IT.gif')#加载图片文件  
        self.image = self.canvas.create_image(0,0, anchor='nw', image=self.image_file)#将图片置于画布上  
        self.canvas.pack(side='top')#放置画布（为上端）  
  
        #创建一个`label`名为`Account: `  
        self.label_account = tkinter.Label(self.root, text='Account: ')  
        #创建一个`label`名为`Password: `  
        self.label_password = tkinter.Label(self.root, text='Password: ')  
          
  
        # 创建一个账号输入框,并设置尺寸  
        self.input_account = tkinter.Entry(self.root, width=30)  
        # 创建一个密码输入框,并设置尺寸  
        self.input_password = tkinter.Entry(self.root, show='*',  width=30)  
  
        # 创建一个登录系统的按钮  
        self.login_button = tkinter.Button(self.root, command = self.backstage_interface, text = "Login", width=10)  
        # 创建一个注册系统的按钮  
        self.siginUp_button = tkinter.Button(self.root, command = self.siginUp_interface, text = "Sign up", width=10)  
  
    # 完成布局  
    def gui_arrang(self):  
        self.label_account.place(x=60, y= 170)  
        self.label_password.place(x=60, y= 195)  
        self.input_account.place(x=135, y=170)  
        self.input_password.place(x=135, y=195)  
        self.login_button.place(x=140, y=235)  
        self.siginUp_button.place(x=240, y=235)  
  
    # 进入注册界面  
    def siginUp_interface(self):  
        # self.root.destroy()  
        tkinter.messagebox.showinfo(title='影视资源管理系统', message='进入注册界面')  
          
    # 进行登录信息验证  
    def backstage_interface(self):  
        account = self.input_account.get().ljust(10," ")  
        password = self.input_password.get().ljust(10," ")  
        #对账户信息进行验证，普通用户返回user，管理员返回master，账户错误返回noAccount，密码错误返回noPassword  
        verifyResult = verifyAccount.verifyAccountData(account,password)  
  
        if verifyResult=='master':  
            self.root.destroy()  
            tkinter.messagebox.showinfo(title='影视资源管理系统', message='进入管理界面')  
        elif verifyResult=='user':  
            self.root.destroy()  
            tkinter.messagebox.showinfo(title='影视资源管理系统', message='进入用户界面')   
        elif verifyResult=='noAccount':  
            tkinter.messagebox.showinfo(title='影视资源管理系统', message='该账号不存在请重新输入!')  
        elif verifyResult=='noPassword':  
            tkinter.messagebox.showinfo(title='影视资源管理系统', message='账号/密码错误请重新输入!')  
  
def main():  
    # 初始化对象  
    L = Login()  
    # 进行布局  
    L.gui_arrang()  
    # 主程序执行  
    tkinter.mainloop()  
  
  
if __name__ == '__main__':  
    main()  
