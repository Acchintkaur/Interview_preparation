def find(graph, node):
    if graph[node] < 0:
        return node
    else:
        temp = find(graph,graph[node])
        graph[node] = temp
        return temp

def union(graph, a, b, answer):
    org_a = a
    org_b = b
    a = find(graph, a)
    b = find(graph, b)
    if a == b:
        pass
    else:
        answer.append([org_a,org_b])
        if graph[a]<graph[b]:
            graph[a] = graph[a] + graph[b]
            graph[b] = a
        else:
            graph[b] = graph[b] + graph[a]
            graph[a] = b

n = 7
graph = [-1] * (n+1)
answer = []
values = [[1,2,1] , [1,3,3] , [3,4,1] , [2,6,4] , [6,5,6] , [6,7,2] , [7,5,7] , [3,6,2] , [4,5,5]]
values = sorted(values, key = lambda values: values[2])
print(values)
for u,v,d in values:
    union(graph,u,v,answer)
print(answer)