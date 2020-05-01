import numpy as np

def print_attr(*args):
    '''数组对象常用属性的打印'''
    for arg in args:
        print('='*25)

        print("data:\n{}\ndtype:{}\nshape: {} \nsize:{}\nndim:{}\nnbytes:{}".format(
            arg, arg.dtype, arg.shape, arg.size, arg.ndim, arg.nbytes))

'''数组创建 array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)
数组的元素类型 可以是内置的 int float unit bool string_ unicode_ 但是数组元素类型要一致'''
    # data = np.array([1, 2, 3, 4, 5])  # [1 2 3 4 5]  shape: (5,)
    # # data1 = np.array([1, 2, 3, 4, 5],ndmin=2) # [[1 2 3 4 5]]  ndim:2

    # # print (np.__version__) #1.16.2
    # # print ('='*20,data,type(data)) #[1 2 3 4 5] <class 'numpy.ndarray'>

    # # print(dir(data))
    # # dir(data) # dir(np) # help(np.array) 在终端可以直接显示

    # # new_data = data.astype(np.float) #[1. 2. 3. 4. 5.] float64
    # # new_data = data.astype(np.unicode_) #['1' '2' '3' '4' '5'] <U11
    # # new_data = data.astype(np.bool) #[ True  True  True  True  True] bool
    # # new_data = data.astype(np.string_) #[b'1' b'2' b'3' b'4' b'5'] |S11
    # # print('='*20,new_data,new_data.dtype)

    # da = np.array([[1, 2, ], [5, 6, 7, 8], [9.0, 10, 11, 12]])  # dtype:object 元素不齐
    # # 嵌套列表 dtype:float64
    # da1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9.0, 10, 11, 12]])
    # # 嵌套元组 dtype:float64
    # da2 = np.array([(1, 2, 3, 4), (5, 6, 7, 8), (9.0, 10, 11, 12)])
    # da3 = np.array([[[1, 2], [10, 20], [100, 200]], [
    #                [3, 4], [30, 40], [300, 400]], [[5, 6], [50, 60], [500, 600]]])

    # # print_attr(data,data1,da,da1,da2,da3)

    # da4 = np.array([[ [ [1,1000],[2,2000] ], [ [10,1000], [20,2000] ], [ [100,1000] , [200,2000] ] ], [
    #                [[3,1000], [4,2000]], [[30,1000], [40,2000]], [[300,1000], [400,2000]]]] )

    # derange = np.arange(1, 10).reshape((3, 3))
    # delin = np.linspace(1, 100, 16).reshape((4, 4))
    # delog = np.logspace(2, 10, num=4).reshape((2, 2))

    # dediag = np.diag([1, 2, 33, 55, 22], k=1)
    # # np.fromfunction(function,shape,**kwargs)
    # defunc = np.fromfunction(lambda i, j: (i+1)*(j+1), (9, 9), dtype=np.int)

    # # print_attr(derange,delin,delog,dediag,defunc)
    # # print_attr(da4)

'''索引 和 筛选''''''下表分别是 数组 列表 整数'''

    # a = np.arange(24).reshape(2,3,4)
    # # a.ndim
    # #np.ndim(a)
    # # 都是维度 区分维度跟形状    数组的轴与层数的理解

    # # print_attr(a)
    # print("--"*20)
    # print("--"*20)
    # print(a)
    # a[1,0]=100
    # a[1,0,0]=50
    # print("--"*20)
    # print(a[1],a[1][0],a[1,0,2])  # a[1][0] == a[(1,0)] == a[1,0]
    # print("--"*20)

    # print(a[[1,0]])
    # print("--"*20)
    # print(a[[1,0],[0,1]])
    # print("--"*20)
    # print(a[a>22])

'''切片'''
    # a= np.arange(10,20)

    # # b= np.arange(0,60,10)
    # # b=np.arange(0,6)
    # b= np.arange(0,60,10).reshape(-1,1) + np.arange(0,6)
    # print("--"*20)
    # print(b)
    # print("--"*20)
    # c=b[1:4,2:5]

    # print(c)
    # print("--"*20)
    # c[1]=1000
    # print(c)
    # print("--"*20)
    # print(b)
    # d=b[:3,[0,3]]
    # print(d)
    # print("--"*20)
    # print(b)
    # print("--"*20)
    # print("--"*20)
    # d[1]=100
    # print(d)
    # print(b)

'''数组的基本操作'''
'''变形'''
        # a = np.arange(10)

        # b= np.reshape(a,(2,5))   #c= a.reshape((2,5)) 

        # c= np.reshape(b,(-1,2))
        # c[1,1]=100
        # print_attr(b,c)
        # print_attr(a)

        # d = b.flatten()
        # d[5]=600
        # ne= b.ravel() # np.ravel(b)
        # ne[9]=900

        # print_attr(b,d,ne)

        # data = np.arange(5)
        # c= data[:,np.newaxis]
        # d=data[np.newaxis,:]
        # print_attr(data,c,d)

        # data2=np.expand_dims(data,axis=0)
        # data3 = np.expand_dims(data,axis=1)
        # print_attr(data2,data3)
'''组合 分割'''
    # a = np.arange(9).reshape(3,3)
    # b = np.arange(12).reshape(3,4)
    # c = np.arange(15).reshape(3,5)
    # aa =a*3
    # print_attr(a,b,c)
    # print_attr(aa)

    # d=np.hstack((a,b,c))
    # print_attr(d)
    # bb=b.T
    # d=np.vstack((a,b))
    # print_attr(d)

    # d = np.column_stack((a,b))
    # print_attr(d)
    # e = np.row_stack((a,b.T))
    # print_attr(e)
    # a = np.arange(24).reshape(4,6)
    # b= np.hsplit(a,2)  #b=np.split(a,2,axis=1)
    # print(b)
    # print_attr(b[0],b[1])

    # c= np.split(a,2,axis=0) #c=np.vsplit(a,2)
    # print(c)
    # print_attr(c[0],c[1])
'''改编元素'''
    # a = np.array([[1,2,3],[4,5,6]])
    # b = np.array([[7,8,9]])
    # print_attr(a,b)
    # r = np.append(a,b)
    # rr = np.append(a,b,axis=0)
    # print_attr(r,rr)

'''通用函数'''
    # alpha=np.linspace(-1,1,11)
    # y= np.sin(np.pi*alpha)
    # out=np.round(y,decimals=3)
    # print(alpha)
    # print(y)
    # print(out)
    # print(np.add(alpha,out))
    # print(np.sin(30/180*np.pi))
    # print(np.arcsin(0.5)/np.pi*180)
    # print(np.sqrt(4))
    # print(np.exp(1))
    # print(np.log(np.exp(1)))
    # print(np.log2(3)+np.log10(5))

    # print(np.power(2,3),np.remainder(5,2),np.round(3.545))

    # a = np.arange(10,100,2,dtype=float)
    # # print(a.shape)
    # b = np.logspace(2,4,a.shape[0])
    # m = np.empty_like(b)
    # print(a.dtype)
    # print(b.dtype)
    # print(m)
    # print(np.remainder(b,a))

    # np.remainder(b,a,out=m)
    # print(m)

    # pow_ufunc = np.frompyfunc(pow,2,1)
    # a = np.arange(10)

    # b=pow_ufunc(a,a)
    # print(b)

    # pow_ufunc2 = np.vectorize(pow,otypes=[np.int])
    # c=pow_ufunc2(a,a)
    # print(c)

    # d = pow(a,a) 
    # print(d)

# c = np.random.randint(2,size=(2,3,5))
# d = np.random.randint(2,size=(3,2,4))
# print_attr(c,d)
# e = np.tensordot(c,d,axes=((0,1),(1,0)))
# print_attr(e)

r = np.array([1,-1])
fr = np.poly(r)
print_attr(fr)
