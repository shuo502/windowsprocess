import multiprocessing

def func(mydict,mylist):
    mydict["高清华"]="睡觉帮帮主"
    mydict["何丰成"]="睡觉帮大护法"
    mylist.append(11)
    mylist.append(22)
    mylist.append(33)

if __name__=="__main__":
    #with multiprocessing.Manager() as MG:
        mydict=multiprocessing.Manager().dict()
        mylist=multiprocessing.Manager().list(range(5))

        p=multiprocessing.Process(target=func,args=(mydict,mylist))
        p.start()
        p.join()

        print(mylist)
        print(mydict)
