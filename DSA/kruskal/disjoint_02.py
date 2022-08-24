def find(graph, node):
    if graph[node] < 0:
        return node
    else:
        temp = find(graph,graph[node])
        graph[node] = temp
        return temp

def union(graph, a, b):
    org_a = a
    org_b = b
    a = find(graph, a)
    b = find(graph, b)
    if a == b:
        print("Cannot connect because it is a part of family", org_a, org_b)
    else:
        if graph[a]<graph[b]:
            graph[a] = graph[a] + graph[b]
            graph[b] = a
        else:
            graph[b] = graph[b] + graph[a]
            graph[a] = b

n = 7
graph = {}
for i in range(n):
    graph[i] = -1
values = [[0,1] , [1,2] , [2,3] , [4,5]]
for u,v in values:
    union(graph,u,v)
print(graph)