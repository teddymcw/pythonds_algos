#best way to go if list is already somewhat sorted
#optimization of bubble sort
#will stop at certain operations because we already know

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       steps = 0
       print("now alist is: {}, {}".format(alist, steps))
       exchanges = False
       for i in range(passnum):
           print("assessing {0} and {1}".format(alist[i], alist[i+1]))
           if alist[i]>alist[i+1]:
               print("switching {0} and {1}".format(alist[i], alist[i+1]))
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
               print("now alist is: {}".format(alist))
               steps += 1
           else: 
                print("skipping {0} and {1}".format(alist[i], alist[i+1]))
                steps += 1
       passnum = passnum-1

alist = [54,26,93,17,77,31,44,55,20]
shortBubbleSort(alist)
print(alist)
