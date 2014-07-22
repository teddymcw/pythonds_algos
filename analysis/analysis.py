"""Write two Python functions to find the minimum number in a list. 
The first function should compare each number to every other number on the list. O(n2). 
The second function should be linear O(n)"""

import time
from random import randrange

def findmin_linear(ls):
	minimum = ls[0]
	for i in ls:
		if i < minimum:
			minimum = i 
	return minimum

def findmin_quad(ls):
	minimum = ls[0]
	for i in ls: #began copying code, note double iterator
		issmallest = True
		for j in ls:
			if i > j:
				issmallest = False
		if issmallest:
			minimum = i 
		return minimum

first_test_ls = range(10, 100)
second_test_ls = range(20,40)

print(findmin_quad(first_test_ls))
print(findmin_quad(second_test_ls))
print(findmin_linear(first_test_ls))
print(findmin_linear(second_test_ls))

for ls in range(1000, 10001, 1000):
	rand_ls = [randrange(100000) for x in range(ls)]
	start = time.time()
	print(findmin_linear(rand_ls))
	end = time.time()
	print("size: {0} time: {1}".format(ls, end-start))
