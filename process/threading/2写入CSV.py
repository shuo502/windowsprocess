import csv
#with open("1.csv","w",newline="") as  datacsv:


csvw=csv.writer(open("1.csv","w",newline=""),dialect=("excel"))#最常用excel格式
csvw.writerow(["1","2","3","4","5"]    )
csvw.writerow(["1", "2", "3", "4", "5"])
