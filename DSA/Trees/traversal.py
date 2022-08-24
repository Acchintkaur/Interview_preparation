class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
def insert(node,data):
    if node is None:
        node = Node(data)
        return node
    if data<node.data:
        node.left = insert(node.left,data)
    else:
        node.right = insert(node.right,data)
    return node
def preorder_traversal(node,preorder):
    if node:
        preorder.append(node.data)
        preorder_traversal(node.left,preorder)
        preorder_traversal(node.right,preorder)
    return preorder
def inorder_traversal(node,inorder):
    if node:
        inorder_traversal(node.left,inorder)
        inorder.append(node.data)
        inorder_traversal(node.right,inorder)
    return inorder
def postorder_traversal(node,postorder):
    if node:
        postorder_traversal(node.left,postorder)
        postorder_traversal(node.right,postorder)
        postorder.append(node.data)
    return postorder
def levelorder_traversal(node,levelorder):
    queue = []
    if node:
        queue.append(node)
        while queue:
            levelorder.append(queue[0].data)
            x=queue.pop(0)
            if x.left:
                queue.append(x.left)
            if x.right:
                queue.append(x.right)
    return levelorder

def delete_node(node, element):
    if node is None:
        return 
    if element<node.data:
        if node.left:
            node.left = delete_node(node.left,element)
        else:
            return
    elif element>node.data:
        if node.right:
            node.right = delete_node(node.right,element)
        else:
            return
    else:
        if node.left is None:
            temp =  node.right
            node = None
            return temp
        if node.right is None:
            temp = node.left
            node=None
            return temp
        node = node.right
        while node.left:
            node = node.left
        element = node.data
        node.right = delete_node(node.right, node.data)
    return node


node= insert(None,15)
insert(node,10)
insert(node,25)
insert(node,6)
insert(node,14)
insert(node,20)
insert(node,60)
preorder,inorder,postorder,levelorder =[],[],[],[]
print("preorder",preorder_traversal(node,preorder))
print("inorder",inorder_traversal(node,inorder))
print("postorder",postorder_traversal(node,postorder))
print("levelorder",levelorder_traversal(node,levelorder))
element= int(input("Enter the element you want to delete: "))
deleted = delete_node(node,element)
inorder=[]
print("after deletion",inorder_traversal(node,inorder))