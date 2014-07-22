quick_find = """considered an eager algorithm. Why?"""

array = list(range(10))
print(array)
for p, q in array:
	if array[p] == array[q]:
		print('true')
	else:
		print('false')

p_id = array[p]
q_id = array[q]

for i in array:
	if array[i] == p_id:
		array[i] = q_id



#for i in range(10):
#	n[i] = i

#x = list()
#[(x[i]) for i in range 10]

print(array)

assert(array[p] == array[q])