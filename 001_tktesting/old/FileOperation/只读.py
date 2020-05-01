# --*-- coding: utf-8 --*--
'''
内存里面存储的是bytes 是编码 utf-8  显示的时候涉及到转换成显示的
b 字节
''''

# 文件打开三要素 1.路径 文件存在（都是以0 1 存在）2.  编码 指定特定编码（utf-8 gbk） 3.模式 只读 只写 读写。。。

# r w 模式 需要将编码格式转换成 Unicode模式 需要指定 encoding='utf-8'/'gbk' 没指定是因为默认设置

file1 = open(r"C:\Users\Administrator\pyprojects\FileOperation\test.txt",
             encoding='utf-8', mode='r')
# 读取utf-8 gbk等 内存里面 bytes  文件在内存上面都是 编码数据    转换成 Unicode（str）编码数据 content是字符串数据类型
content1 = file1.read()  # 字符串类型
file1.close()
print(content1, type(content1))

# rb 模式 无需转换 无需encoding
#file = open(r"C:\Users\Administrator\pyprojects\FileOperation\test.txt",encoding='utf-8',mode='rb')
# 报错，因为rb模式，不能指定编码格式，他是直接读取bytes content shi bytes 类型

file = open(
    r"C:\Users\Administrator\pyprojects\FileOperation\test.txt", mode='rb')
content = file.read()  # bytes类型  一般用于读取网络传输
file.close()
print(content, type(content))


#相对路径 给予当前工作文件夹
obj = open('FileOperation/log', encoding='utf-8', mode='r')
c = obj.read()
obj.close()
print(c, type(c))
