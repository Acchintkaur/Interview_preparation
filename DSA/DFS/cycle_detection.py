# https://favtutor.com/blogs/detect-cycle-in-undirected-graph
def dfs(graph, node, visited, par):
    # assign current node as
    visited[node] = True
    # loop for every edge
    for child in graph[node]:
        # if child is not visited
        if not visited[child]:
            return dfs(graph,child,visited, node)
        else:
            # if child is visited, and child is not a parent_node
            if child !=par:
                return True
    return False


values = [[1,2], [1,5], [2,3], [2,4], [2,5], [3,4], [3,6], [4,5], [4,6], [5,6]]
graph = {}
n=6
visited = {}
for i in range(1,n+1):
    graph[i] = []
    visited[i] = False

for u,v in values:
    graph[u].append(v)
    graph[v].append(u)

print(dfs(graph, 1, visited, -1))