from deque import Deque

def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print("begin testing print statments")
print(palchecker("lsdkjfskf"))
print(palchecker("radar"))



d = Deque()
d.isEmpty()
print('begin printing d in script here')
print(d.isEmpty())
d.addRear("l")
d.addRear("l")
d.addFront("l")
d.addFront("l")
d.size()
print(d.size())
d.addRear(9.9)
d.addFront(9.9)

print(d.items)
#print(palchecker(d)) won't work
print(palchecker("can't make deque twice!"))
