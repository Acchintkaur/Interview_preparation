class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(node,data):
    if node is None:
        node=Node(data)
        return node
    if data<node.data:
        node.left = insert(node.left,data)
    else:
        node.right = insert(node.right,data)
def height(node):
    if node is None:
        return 0
    else:
        return max(height(node.left),height(node.right))+1
def isbalanced(node):
    if node is None:
        return True
    if abs(height(node.left)-height(node.right))<=1 and isbalanced(node.left) and isbalanced(node.right):
        return True
    else:
        return False

node = insert(None,15)
insert(node,10)
insert(node,25)
insert(node,6)
insert(node,14)
insert(node,20)
insert(node,60)
print(isbalanced(node))