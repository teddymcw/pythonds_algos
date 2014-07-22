def combos(iter_list):
    result = list()
    for i in iter_list:
           for j in iter_list:
                   for k in iter_list:
                       result.append([i,j,k])
    return result

ten_list = [1, 2, 4, 6, 7, 8, 9, 11, 14, 17]
twelve_list = [1, 2, 4, 6, 7, 8, 9, 11, 14, 17, 19, 21]

def count_combos(result):
	count = 0
	new = combos(result)
	for i in new:
		count += 1
	print(count)

if __name__ == "__main__":
	print(len(ten_list))
	count_combos(ten_list)
	print(len(twelve_list))
	count_combos(twelve_list)