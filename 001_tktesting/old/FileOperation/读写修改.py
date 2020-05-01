#r+ 必须现有这个文件 用的比较多
# 先读 后写是追加写 
# 先写会从第一行开始覆盖 与光标有关 读写相当于两个光标
# 可以定位 seek（）
#  W+ 先清空 在写 在读 新写入的 a+ 

# 写文件要注意：确认是否存在 否则存在清空隐患


# obj= open('FileOperation/aaa.txt',encoding="utf-8",mode='r+')
# obj.read(2)
# obj.seek(6)
# obj.write("12\n34\n58")
# obj.close()

#不要同时读写操作一个文件，读写，修改文件。不要对当前文件直接修改，分两步先读取到内存，修改

# f = open('FileOPeration/test/file.txt',encoding='utf-8')
# f2 = open('FileOPeration/test/file_bak','w',encoding='utf-8')
# for line in f:
#     content = line.split(' ')
#     content[0] = content[0]+'Helloooo'
#     user_str = '|'.join(content)
#     f2.write(user_str)
# f.close()
# f2.close()

# import os   #模块- 用来和操作系统交互的模块
# os.remove('FileOPeration/test/file.txt')  #删除一个文件
# os.rename('FileOPeration/test/file_bak','FileOPeration/test/file.txt')  #重命名一个文件

with open('FileOPeration/test/file.txt',encoding='utf-8') as f:
    with open('FileOPeration/test/file_bak','w',encoding='utf-8') as f2:
        for line in f:
            content = line.split(' ')
            content[0] = content[0]+'Helloooo'
            user_str = '|'.join(content)
            f2.write(user_str)
