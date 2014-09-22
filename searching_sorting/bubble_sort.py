def bubbleSort(alist):
    print("bubblesorting list: {}".format(alist))
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            print("assessing {0} and {1}".format(alist[i], alist[i+1]))
            if alist[i]>alist[i+1]:
                print("switching {0} and {1}".format(alist[i], alist[i+1]))
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp 
                print("now alist is: {}".format(alist))
            else: 
                print("skipping {0} and {1}".format(alist[i], alist[i+1]))
#print section below shortbubblesort

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)

print(len(alist))
range_play = range(8, 0, -1)
print(range_play)
