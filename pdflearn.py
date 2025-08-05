import os
import pymupdf

path = r"/home/sriram/doc"
file = os.listdir(path)

sql_keywords = ('SELECT', 'INSERT', 'UPDATE', 'DELETE', 'CREATE', 'ALTER', 'DROP', 'TRUNCATE')

for i in file:
    data1 = os.path.join(path, i)
    pdf = pymupdf.open(data1)
    for j in pdf:
        data = j.get_text().strip().splitlines()
        # print(data)
        for k in data:
            line = k.strip()
            if any(line.upper().startswith(keyword) for keyword in sql_keywords):
                sql_query = line
                print(sql_query)
