def binarySearch(alist, item):
	    if len(alist) == 0:
	        return False
	    else:
	        midpoint = len(alist)//2
	        if alist[midpoint]==item:
	          return True
	        else:
	          if item<alist[midpoint]:
	            return binarySearch(alist[:midpoint],item)
	          else:
	            return binarySearch(alist[midpoint+1:],item)
	
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print("binary search 1")
print(binarySearch(testlist, 3))
print("binary search 2")
print(binarySearch(testlist, 2))

def bubbleSort(alist):
	    for passnum in range(len(alist)-1,0,-1):
	        for i in range(passnum):
	            if alist[i]>alist[i+1]:
	                temp = alist[i]
	                alist[i] = alist[i+1]
	                alist[i+1] = temp
#print section below shortbubblesort

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1

alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)

	
alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)
print(len(alist))

alist = range(7)

def analyze_bubble_sort1(list):
	n = len(list) - 1
	print("bub1")
	print(n)

#the notebook calls this 'bubble trace'
def analyze_bubble_sort(list):
	n = len(list) - 1
	print(n)
	bubble_comparisons = .5 * n ** 2 - (.5 * n)
	return bubble_comparisons



print(analyze_bubble_sort(alist))

def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)

print("insertion sort")
def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)

print("why use this range stuff")
def rangeStuff(alist):
   print(range(1,len(alist)))

rangeStuff(alist)


print("merge sort")
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)

