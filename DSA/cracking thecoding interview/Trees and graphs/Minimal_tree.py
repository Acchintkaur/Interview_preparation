class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def arr_to_bst(values):
    if not values:
        return None
    mid = len(values)//2
    root = Node(values[mid])
    root.left=arr_to_bst(values[:mid])
    root.right=arr_to_bst(values[mid+1:])
    return root

def preorder_traversal(node,preorder):
    if node:
        preorder.append(node.data)
        preorder_traversal(node.left,preorder)
        preorder_traversal(node.right,preorder)
    return preorder

values= [7,6,5,4,3,2,1]
preorder = []
values.sort()
root = arr_to_bst(values)
print(preorder_traversal(root,preorder))
