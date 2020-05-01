
# w 模式 不存在创建 存在清空重写
obj= open('FileOperation/log.txt',encoding="utf-8",mode='w')
obj.write("12\n34\n58")
obj.close()

obj1= open('FileOperation/log.txt',mode='wb')
obj1.write("12\n34\n58\nkhjj".encode("utf-8"))
obj1.close()

# a 模式 不存在创建 存在清空重写
obja= open('FileOperation/loga.txt',encoding="utf-8",mode='a')
obja.write("12\n34\n58")
obja.close()

objaa= open('FileOperation/logaaa.txt',mode='ab')
objaa.write("12\n34\n58\nkhjj".encode("utf-8"))
objaa.close()