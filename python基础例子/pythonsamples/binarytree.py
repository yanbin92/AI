#coding=utf-8
# binarytree.py
# def inorder(t):
#     if t:
#         for x in inorder(t.left):
#             yield x
#         yield t.label
#         for x in inorder(t.right):
#             yield x

def inorder(node):
    stack = []
    while node:
        while node.left:
            stack.append(node)
            node = node.left
        yield node.label
        while not node.right:
            try:
                node = stack.pop()
            except IndexError:
                return
            yield node.label
        node = node.right

class Tree:

    def __init__(self, label, left=None, right=None):
        self.label = label
        self.left = left
        self.right = right
    #类似java 的toString
    def __repr__(self, level=0, indent="    "):
        s = level*indent + self.label
        if self.left:
            s = s + "\n" + self.left.__repr__(level+1, indent)
        if self.right:
            s = s + "\n" + self.right.__repr__(level+1, indent)
        return s

    def __iter__(self):
        return inorder(self)

# Create a Tree from a list.
def tree(list):
    n = len(list)
    # print(n)
    if n == 0:
        return []
    i = int(n / 2)
    # print(i)
    return Tree(list[i], tree(list[:i]), tree(list[i+1:]))




t = tree("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# Print the nodes of the tree in in-order.
for x in t:
    print(x)

print(t)


# # A non-recursive generator.
# def inorder(node):
#     stack = []
#     while node:
#         while node.left:
#             stack.append(node)
#             node = node.left
#         yield node.label
#         while not node.right:
#             try:
#                 node = stack.pop()
#             except IndexError:
#                 return
#             yield node.label
#         node = node.right