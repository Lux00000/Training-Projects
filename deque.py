from collections import deque

dq = deque([1, 2, 3, 7,-1])

#FIFO

dq.appendleft(10)
value = dq.pop()

dq.append(10)
value = dq.popleft()

#LIFO

dq.append(5)
value = dq.pop()

dq.appendleft(3)
value = dq.popleft()