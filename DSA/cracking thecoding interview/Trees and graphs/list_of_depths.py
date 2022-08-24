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
    return node

def levelorder_traversal(node,levelorder):
    if node is None:
        return []
    queue =[node]
    next_queue = []
    level = []
    result = [] 
    while queue:
        for node in queue:
            level.append(node.data) 
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        result.append(level)
        level=[]
        queue =next_queue
        next_queue=[]
    return result

root = insert(None,15)
insert(root,10)
insert(root,25)
insert(root,6)
insert(root,14)
insert(root,20)
insert(root,60)
levelorder=[]
print(levelorder_traversal(root,levelorder))