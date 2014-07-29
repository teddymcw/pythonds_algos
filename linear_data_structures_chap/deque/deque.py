class Deque: 
	def __init__(self):
		self.items = []

	def getItems(self):
		return self.items 

	def isEmpty(self):
		return self.items == []

	def addFront(self, item):
		self.items.append(item)

	def addRear(self, item):
		self.items.insert(0,item)

	def removeFront(self):
		return self.items.pop()

	def removeRear(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)

"""d = Deque()
d.isEmpty()
print(d.isEmpty())
d.addRear("l")
d.addRear("l")
d.addFront("l")
d.addFront("l")
d.size()
print(d.size())
d.addRear(9.9)
d.addFront(9.9)
"""