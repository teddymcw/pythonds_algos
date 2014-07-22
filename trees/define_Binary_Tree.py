#If each node in the tree has a maximum of two children, 
#we say that the tree is a binary tree

#below you will see that we are defining a bt as being recursive. 
#You see this when we are referring tot eh parent as the root

#two ways of implementing them in python
#The first technique we will call “list of lists,” this requires no classes just methods
#the second technique we will call “nodes and references.”

#BinaryTree() creates a new instance of a binary tree.
#getLeftChild() returns the binary tree corresponding to the left child of the current node.
#getRightChild() returns the binary tree corresponding to the right child of the current node.
#setRootVal(val) stores the object in parameter val in the current node.
#getRootVal() returns the object stored in the current node.
#insertLeft(val) creates a new binary tree and installs it as the left child of the current node.
#insertRight(val) creates a new binary tree and installs it as the right child of the current node.

#now look in Binary Tree for first implementation and
#BT_by_class for second