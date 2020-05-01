# -*- coding:utf-8 -*-
import os
my_dir= r'C:\Users\Administrator\pyprojects\PyInstallerUse\pyinstxtractor\PICS'
for i in os.listdir(my_dir):
    file_name = i.split('.')[-1]
    if file_name == 'jpg' or file_name == 'PNG' or file_name =='gif' :
        os.remove(os.path.join(my_dir,i))
with open (r"C:\Users\Administrator\pyprojects\PyInstallerUse\pyinstxtractor\PICS\t.txt","a") as f:
    f.write("Delete PICS Done")