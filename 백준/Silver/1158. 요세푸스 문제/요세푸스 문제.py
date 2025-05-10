N, K = map(int, input().split(" "))

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

head = Node(1)
cursor = head
for i in range(2,N+1,1):
    new_node = Node(i)
    new_node.prev = cursor
    
    cursor.next = new_node
    cursor = new_node

cursor.next = head
head.prev = cursor
cursor = head

result = []


while len(result) != N:
    for i in range(K-1):
        cursor = cursor.next

    result.append(cursor.data)

    prev = cursor.prev
    next = cursor.next
    

    if prev != None: prev.next = next
    if next != None: next.prev = prev

    cursor = next

    

print(str(result).replace("[", "<").replace("]", ">"))