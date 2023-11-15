from collections import deque
from datetime import datetime
my_deque = deque()
my_list = []

for i in range(1_000_000):
    my_list.append(i)
    my_deque.append(i)

start = datetime.now()
for i in range(10_000):
    my_list.pop(0)
end = datetime.now()
list_time = end - start

start = datetime.now()
for i in range(10_000):
    my_deque.pop()
end = datetime.now()
que_time = end - start

print(list_time)
print()
print(que_time)