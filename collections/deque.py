from collections import deque
d = deque()
d.append(1)
d.append(2)
d.append(3)

print(d)

d.pop()

print(d)
d.extendleft([4,5,6])

d.popleft()
print(d)

d.rotate(1)

print(d)


