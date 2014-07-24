from unordered_list import Node, UnorderedList 

class TestNode:

	def test_initialize():
		first_node = Node("initial string")
		assert(first_node.data == "initial string")
		assert(first_node.next == None)

	#def test_getData():

