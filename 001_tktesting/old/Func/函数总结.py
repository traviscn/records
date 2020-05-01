function 函数作用
    封装了一个功能 别人关心使用方法



def myfunc(): 函数定义
    注释
    关键字
    函数名
    参数
    函数体代码块
    返回值
    # function definition
    def funcname(parameter_list):
        pass

    # abstract class method 抽象类方法
    def funcname(self, parameter_list):
        raise NotImplementedError

    # class method
    def funcname(self, parameter_list):
        pass

    # static class method
    @staticmethod
    def funcname(parameter_list):
        pass

    # async statement  异步
    async def funcname(parameter_list):
        pass

myfunc 函数对象

myfunc 函数名

myfunc() 函数调用 
    返回值=函数名（参数）
    调用接收的只有返回值
    传入参数是实参

return 函数返回值
    #return的作用：
        #1.能够返回值
        #2.结束一个函数的执行 后面语句不执行
    #返回None：
        # 如果函数里什么都不写
        # return
        # return None
    #返回一个值：return 可以返回任意内容
    def my_max():
        a = 111
        b = 222
        if a > b:
            return a
        else:
            return b

    python 独有
    #多返回值：多个返回值以逗号隔开以元组的形式被返回
    #return 1,2,3  #===(1,2,3)
    #return [1,2,3]  #===[1,2,3]
    涉及到 拆包 解包操作

    #接受返回值：
    #1.一个值接受
    #2.多个变量接受：返回多少个值就用几个变量去接受，必须不多不少
    
    只返回一个 就终止
    # def find():
    #     l = [1,2,3,4,5,6]
    #     for i in l:
    #         if i % 3 == 0:
    #             return i

    返回一个列表
    # def find2():
    #     l = [1, 2, 3, 4, 5, 6]
    #     new_l = []
    #     for i in l:
    #         if i%3 == 0:
    #             new_l.append(i)
    #     return new_l

def myfunc(a,b,c=32,*args,**kargs):函数参数 
    五种参数   
        函数定义角度：形式参数，形参 函数调用角度：传入的得是实际参数，实参
        参数可以是任意的数据类型
        1.位置参数必须一一对应 
        2.关键字参数 必须在位置参数后面
        3.默认参数（通常是不可变类型）只在定义是赋值一次
        4.可位置参数（*args）
        5.可变关键字参数（ **kargs）