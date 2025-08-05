import os
import pymupdf

path=r"/home/sriram/doc"
file=os.listdir(path)
for i in file:
    data1=os.path.join(path,i)
    pdf=pymupdf.open(data1)
    for j in pdf:
        data=j.get_text().strip().splitlines()
        print(data)
