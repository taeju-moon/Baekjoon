count = int(input())
datas = []
for i in range(count):
    datas.append(input())

class Node:
    data = ""
    prev = None
    next = None
    def __init__(self, d):
        self.data = d



def get_password(keys):
    node = Node("root")
    for key in keys:
        if key == "<":
            if node.data == "root":
                continue
            else:
                node = node.prev
        elif key == ">":
            if  node.next == None:
                continue
            else:
                node = node.next
        elif key == "-":
            if node.data == "root": continue
            prev = node.prev
            next = node.next
            
            prev.next = next
            if next != None: next.prev = prev
            node = prev
        else:
            new_node = Node(key)
            new_node.prev = node
            new_node.next = node.next
            
            if node.next != None: node.next.prev = new_node
            node.next = new_node
            node = new_node

    while node.data != "root":
        node = node.prev

    node = node.next
    
    result = ""
    while node:
        result += node.data
        node = node.next
    print(result)
                
    

for data in datas:
    get_password(data)