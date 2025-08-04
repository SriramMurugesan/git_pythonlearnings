import os
import pymupdf

sqldata=r"D:\doc"
file=os.listdir(sqldata)
for i in file:
    data_ex=os.path.join(sqldata,i)
    full_data=pymupdf.open(data_ex)
    print(full_data)
