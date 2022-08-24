# # using bfs
# def bfs(graph,visited,distance,start,end):
#     queue = []
#     queue.append(start)
#     visited[start]=True
#     distance[start]=0
#     while queue:
#         temp = queue.pop(0)
#         for item in graph[temp]:
#             if not visited[item]:
#                 queue.append(item)
#                 visited[item]=True
#                 distance[item] = distance[temp]+1
#     # return distance,distance[end]
#     return (distance[end]!=0 and distance[end]!=None)

# # values = [[0,5],[0,4],[0,1],[1,4],[2,1],[3,2],[3,4]]
# values= [[0,1],[0,2],[1,2],[2,0],[2,3],[3,3]]
# n=6
# graph = {}
# visited = {}
# distance = {}
# for i in range(n):
#     graph[i] = []
#     visited[i] =False
#     distance[i] =None
# for (u,v) in values:
#     graph[u].append(v)
# start,end=int(input("Enter from node")),int(input("Enter to node"))
# # print(graph)
# print(bfs(graph,visited,distance,start,end))


# using dfs-cycle detection
def dfs(graph,visited,start,end):
    if start ==end:
        return True
    visited.add(start)
    for child in graph[start]:
        if child not in visited:
            if dfs(graph,visited,child,end):
                return True
    return False

        

values = [[0,5],[0,4],[0,1],[1,4],[2,1],[3,2],[3,4]]
n=6
start,end =int(input("Enter from node")),int(input("Enter to node"))
graph ={}
visited = set()
for i in range(6):
    graph[i]=[]
for (u,v) in values:
    graph[u].append(v)
print(graph)
print(dfs(graph,visited,start,end))