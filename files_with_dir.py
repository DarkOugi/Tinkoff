import os
files = os.listdir('files')
res = ''
for i in range(len(files)):
    res+=f'files/{files[i]} plagiat1/{files[i]}\n'
f = open('files.txt','w')
f.write(res)
f.close()