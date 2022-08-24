def bfs(graph, visited):
    queue = []
    queue.append(1)
    visited[1] = True
    while queue:
        temp = queue.pop(0)
        print(temp, end = " --> ")
        for child in graph[temp]:
            if not visited[child]:
                queue.append(child)
                visited[child]=True
values=[[1,2] , [1,6] , [1,7] , [1,8] , [2,3] , [3,4] , [3,5] , [7,8] , [8,9]]
graph = {}
visited = {}
for i in range(1,len(values)+1):
    graph[i] = []
    visited[i] = False

for (u,v) in values:
    graph[u].append(v)
    graph[v].append(u)   

bfs(graph,visited)