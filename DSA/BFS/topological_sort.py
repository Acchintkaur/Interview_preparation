def bfs(graph, visited, indegree):
    queue = []
    for key in visited:
        if indegree[key] == 0:
            queue.append(key)
            visited[key] = True
    while queue:
        temp = queue.pop(0)
        print(temp, end = " ")
        for child in graph[temp]:
            if not visited[child]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
                    visited[child]=True
values=[[1,2] , [2,3] , [ 1,3] , [4,1] , [6,1] , [6,3] , [4,3] , [5,3] , [8,1] , [1,7] , [9,8] , [9,7]]
graph = {}
visited = {}
indegree = {}
for i in range(1,len(values)+1):
    graph[i] = []
    visited[i] = False
    indegree[i] = 0

for (u,v) in values:
    graph[u].append(v)  
    indegree[v] +=1

bfs(graph,visited, indegree)