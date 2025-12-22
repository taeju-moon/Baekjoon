import sys

input = sys.stdin.readline


class Node:
    def __init__(self, data, left=".", right="."):
        self.data = data
        self.left = left
        self.right = right

    def has_left(self):
        return self.left != "."

    def has_right(self):
        return self.right != "."


N = int(input())


root, child1, child2 = input().split()
tree = {}

tree[root] = Node(root, child1, child2)
tree[child1] = Node(child1)
tree[child2] = Node(child2)


for _ in range(N-1):
    parent, child1, child2 = input().split()
    if parent in tree:
        tree[parent].left = child1
        tree[parent].right = child2
    if child1 != ".":
        tree[child1] = Node(child1)
    if child2 != ".":
        tree[child2] = Node(child2)


def pre_order(node):
    if node in tree:
        child1 = tree[node].left
        child2 = tree[node].right
        print(tree[node].data, end="")
        if tree[node].has_left():
            pre_order(child1)
        if tree[node].has_right():
            pre_order(child2)


def in_order(node):
    if node in tree:
        child1 = tree[node].left
        child2 = tree[node].right
        if tree[node].has_left():
            in_order(child1)
        print(tree[node].data, end="")
        if tree[node].has_right():
            in_order(child2)


def post_order(node):
    if node in tree:
        child1 = tree[node].left
        child2 = tree[node].right
        if tree[node].has_left():
            post_order(child1)
        if tree[node].has_right():
            post_order(child2)
        print(tree[node].data, end="")


pre_order(root)
print()
in_order(root)
print()
post_order(root)
