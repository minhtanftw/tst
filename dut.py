from collections import deque

line = deque()

#Enqueue

line.append("user1")
line.append("user2")

print(line.popleft())


stack = []

stack.append("tan")
stack.append("nhung")

print(stack.pop())


#Graph(network structure)

network = {
    "X":["Y", "Z"],
    "Y": ["Z"],
    "Z" : []
}
print(network["X"])