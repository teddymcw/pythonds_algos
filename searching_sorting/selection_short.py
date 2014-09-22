def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           print("comparing: {0} and {1}".format(alist[location],alist[positionOfMax]))
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location
               print("switching: {0} and {1}".format(alist[location],alist[positionOfMax]))
               print("list is now: {}".format(alist))
               print("positionOfMax: {}".format(positionOfMax))
               print("value of max: {}".format(alist[positionOfMax]))
           else:
                print("skipping: {0} and {1}".format(alist[location],alist[positionOfMax]))

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp


alist = [54,26,93,17,77,31,44,55,20]
print(alist)
selectionSort(alist)
print(alist)