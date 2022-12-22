import os
import sys

dir_one, dir_two,file_name = sys.argv[1:]
files = os.listdir(dir_one)
res = ''
for i in range(len(files)):
    res+=f'{dir_one}/{files[i]} {dir_two}/{files[i]}\n'
f = open(file_name,'w')
f.write(res)
f.close()