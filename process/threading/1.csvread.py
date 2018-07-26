import csv
path=r"C:\Users\Tsinghua-yincheng\Desktop\day23down\csv\000001.csv"
reader=csv.reader(open(path,"r")) #读取文件
for  item  in reader:#读取每一行
    #print(item)  list  itten[13]
    for data in item: #读取每一列
        print(data)
