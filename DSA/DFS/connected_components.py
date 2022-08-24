def dfs(graph,node,visited):
    print(node)
    sm=0
    visited.add(node)
    for child in graph[node]:
        if child not in visited:
            sm+=dfs(graph,child,visited)
    
    return sm+1
  
values=[['A','C'],['A','D'],['A','B'],['B','E'],['D','E'],['F','H'],['F','G'],['I','J']]
nodes = ['A','B','C','D','E','F','G','H','I','J','K']
graph = {}
for vert in nodes:
    graph[vert] = []
for u,v in values:
    graph[u].append(v)
    graph[v].append(u)
visited = set()
answer= []
for item in nodes:
    if item not in visited:
        print("\n")
        temp= dfs(graph,item,visited)
        answer.append(temp)
print(answer)
