from collections import deque
# deque stands for double ended queue

d = deque()
d.append(1)
d.append(2)
print(d)

d.appendleft(3)
d.appendleft(4)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.extend([1, 2, 3])
d.extend([3, 4, 5, 6])
print(d)

d.rotate(1) # it will rotate all elements to the right by one place. to rotate left, give a negative number