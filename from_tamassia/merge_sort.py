from random import randint

def merge(S1, S2, S):
	i = j = 0
	while i + j < len(S):
		if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
			S[i+j] = S1[i]  # copy ith element of S1 as next item of S
			i += 1
		else:
			S[i+j] = S2[j]  # copy jth element of S2 as next item of S
			j += 1
	print("This is S: {}".format(S))
	

def merge_sort(S):
	n = len(S)
	print("this is n: {}".format(n))
	if n < 2: 
		return
	mid = n // 2
	S1 = S[0:mid]
	S2 = S[mid:n]
	merge_sort(S1)
	merge_sort(S2)
	merge(S1, S2, S)
	

x = range(30)
test_list = [(num * randint(1,20)) for num in x]



if __name__ == "__main__":
	print(test_list)
	print(merge_sort(test_list))