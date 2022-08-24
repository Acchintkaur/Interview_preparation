# https://www.pythonpool.com/adjacency-list-python/
# Which is better – adjacency matrix or adjacency list?
# Adjacency list has the upper hand over the adjacency matrix because of its efficiency. 
# An adjacency list occupies less memory space than an adjacency matrix. 
# In addition, it is easier to iterate over the edges in the adjacency list because 
# the neighboring nodes for a given node can be accessed easily. 
# Also, creating edges and nodes in a list is efficient compared to creating edges and nodes in a matrix.
adj_list = {}
mylist = []
def add_node(node):
  if node not in mylist:
    mylist.append(node)
  else:
    print("Node ",node," already exists!")
 
def add_edge(node1, node2):
  temp = []
  if node1 in mylist and node2 in mylist:
    if node1 not in adj_list:
      temp.append(node2)
      adj_list[node1] = temp
   
    elif node1 in adj_list:
      temp.extend(adj_list[node1])
      temp.append(node2)
      adj_list[node1] = temp

       
  else:
    print("Nodes don't exist!")

 
def graph():
  for node in adj_list:
    print(node, " ---> ", [i for i in adj_list[node]])
 
#Adding nodes
add_node(0)
add_node(1)
add_node(2)
add_node(3)
add_node(4)
#Adding edges
add_edge(0,1)
add_edge(1,2)
add_edge(2,3)
add_edge(3,0)
add_edge(3,4)
add_edge(4,0)
 
#Printing the graph
graph()
 
#Printing the adjacency list
print(adj_list)