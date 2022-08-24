class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
# # using dfs
# def isbst(node,left,right):
#     if node is None:
#         return True 
#     if not (node.data>left and node.data<right):
#         return False
#     return (isbst(node.left,left,node.data) and isbst(node.right,node.data,right))

# using inorder traversal
import math
prev=-math.inf
def isbst(node):
    global prev
    if node :
        if not isbst(node.left):
            return False
        if prev>node.data:
            return False
        prev = node.data
        return (isbst(node.right))
    return True

def insert(node,data):
    if node is None:
        node = Node(data)
        return node
    if data<node.data:
        node.left = insert(node.left,data)
    else:
        node.right = insert(node.right,data)
    return node

node = insert(None,15)
insert(node,10)
insert(node,25)
insert(node,6)
insert(node,14)
insert(node,20)
insert(node,60)
# print(isbst(node,float("-inf"),float("inf")))
print(isbst(node))