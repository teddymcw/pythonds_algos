def test_anagram(word1, word2):
	if sorted(word1) == sorted(word2):
		return True
	return False 

"""As we will see in a later chapter, sorting is typically either O(n2) or O(nlogn), 
so the sorting operations dominate the iteration. In the end, 
this algorithm will have the same order of magnitude as that of the sorting process."""

"""to make anagram calls we would need a list of somewhat sorted english words and
then compare this word to the words of that length or something, only returning
the sorted matches"""