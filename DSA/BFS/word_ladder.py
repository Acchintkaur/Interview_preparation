def onediff(a,b):
    count = 0
    if a!=b:
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
    return count == 1
def bfs(graph, visited, distance, start,end):
    queue = []
    queue.append(start)
    visited[start] = True
    distance[start] = 1
    while queue:
        temp = queue.pop(0)
        print(temp, end = " ")
        for child in graph[temp]:
            if not visited[child]:
                queue.append(child)
                visited[child]=True
                distance[child] = distance[temp] + 1
    print("\n",distance)
    print("answer = ", distance[end] )
values=["poon" , "plee" , "same" , "poie" , "plie" , "poin", "plea" ,"plea"]
start = "toon"
values.append(start)
end = "plea"
graph = {}
visited = {}
distance = {}
if start != end and end in values:
    for i in values:
        graph[i] = []
        visited[i] = False
        distance[i] = None
    
    for i in range(len(values)):
        for j in range(i,len(values)):
            if onediff(values[i],values[j]):
                graph[values[i]].append(values[j])
                graph[values[j]].append(values[i])   
    
    bfs(graph, visited, distance, start,end)
else :
    print("word not present")