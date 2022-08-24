# values,graph=[],{}
# n = int(input())
# for i in range(n):
#     values.append([int(input("u")),int(input("v")),int(input("d"))])
values = [[1,2,3] , [2,5,1] , [3,4,4] , [4,5,8] , [3,7,4] , [6,9,1] , [1,3,2] , [4,7,5] , [5,6,6] , [7,6,2] , [7,9,2] , [7,8,1]]
n=9
graph = {}
for i in range(1,n+1):
    graph[i]=[]
for u,v,d in values:
    graph[u].append([d,v])
    graph[v].append([d,u])
print(graph)