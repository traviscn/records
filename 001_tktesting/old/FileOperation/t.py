
try:
    with open("FileOperation/文件操作总结.txt",encoding="utf-8",mode='r') as f:
        with open("FileOperation/文件操作总结back.txt",encoding="utf-8",mode='w') as fb:
            #content=f.read()
            # content=f.readline()
            # content=f.readlines()
            # content=f.readlines()
            for line in f:
                if not line ==  True:
                    a=line.strip()
                    fb.write (a+"\n")
            # print(content)
except ValueError as e:
    print ("mistake",e)
else:
    print("*"*10,"Else","*"*10)
finally:
    print("*"*10,"Finally","*"*10)