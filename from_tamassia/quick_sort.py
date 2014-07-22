def quick_sort(S):
	n = len(S)
	if n < 2:
		return
	p = S.first()
	L = LinkedQueue()
	E = LinkedQueue()
	G = LinkedQueue()
	while not S.is_empty():
		if S.first() < p:
			L.enqueue(S.dequeue())
		elif p < S.first():
			G.enqueue(S.dequeue())


class LinkedQueue(object):
	"""FIFO queue implementation using a singly linked list for storage."""
	class _Node:
	"""Lightweight, nonpublic class for storing a singly linked node.""" 
	"""(omitted here; identical to that of LinkedStack. Node)"""
	￼￼def __init__(self):
	"""Create an empty queue.""" 
		self._head = None
		self._tail = None
		self._size = 0
	￼￼￼￼￼￼# number of queue elements ”””Return the number of elements in the queue.”””
	￼def __len__(self):
	￼￼￼￼return self._size
	def is_empty(self):
	"""Return True if the queue is empty.""" 
		return self._size == 0
	def first(self):
	"""Return (but do not remove) the element at the front of the queue."""
	    if self.is empty():
			raise Empty('Queue is empty')
		return self._head._element # front aligned with head of list


	def dequeue(self):
		"""Remove and return the first element of the queue (i.e., FIFO).
		Raise Empty exception if the queue is empty."""
		if self.is empty():
		    raise Empty("Queue is empty") answer = self._head._element
		self._head = self._head._next
		self._size −= 1
		if self.is empty(): 
			self._tail = None
		return answer
		# special case as queue is empty # removed head had been the tail
	def enqueue(self, e):
		"""Add an element to the back of queue."""
		newest = self._Node(e, None) 
		if self.is_empty():
			self._head = newest 
		else:
			self._tail._next = newest 
		self._tail = newest
		self. size += 1